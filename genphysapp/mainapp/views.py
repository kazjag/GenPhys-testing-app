"""
View functions
"""
import random
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Feedback, Problem
from . import forms_work
# pylint: disable=no-member
# Create your views here.
def main_page(request):
    """
    rendering main_page
    :param request: request
    :return: render object
    """
    return render(request, 'mainapp/main_page.html')


def render_feedback(request):
    """
        rendering feedback list page
        :param request: request
        :return: render object
    """
    feedbacks = Feedback.objects.all().order_by("-created_date")
    return render(request, 'mainapp/feedback_list.html', {'feedbacks': feedbacks})

def render_feedbackform(request):
    """
            rendering feedback list page
            :param request: request
            :return: render object
    """
    return render(request, 'mainapp/feedback_form.html')


@csrf_exempt
def check_feedbackpost(request):
    """
                processing POST request from feedback page
                :param request: request
                :return: render object
    """
    if request.method == "POST":
        cache.clear()
        author = request.POST.get("author", "")
        feedtext = request.POST.get("feedtext", "")
        context = {"author_name": author}
        if len(author) == 0:
            context["success"] = False
            context["comment"] = "Имя автора должно быть не пустым. Введите имя автора"
        elif len(author) > 50:
            context["success"] = False
            context["comment"] = "Превышено допустимое число символов в имени автора"
        elif len(feedtext) < 5:
            context["success"] = False
            context["comment"] = "Слишком мало символов. Не стесняйтесь :)"
        else:
            context["success"] = True
            context["comment"] = "Отзыв принят. Спасибо!"
            forms_work.post_feedback(author, feedtext)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "mainapp/feedback_afteradd.html", context)

    return render_feedbackform(request)

def create_test(request):
    """
                creating test and rendering test page
                :param request: request
                :return: render object
    """
    indices = random.sample(range(1, Problem.objects.count()+1), 2)
    objects = Problem.objects.filter(pk__in=indices)
    context = {"objects": objects}
    return render(request, "mainapp/task_page.html", context)

@csrf_exempt
def check_test_answers(request):
    """
                    processing test answers and rendering results page
                    :param request: request
                    :return: render object
    """
    if request.method == "POST":
        answers = request.POST
        result,  correct_ans  = {}, {}
        keys = list(answers.keys())
        objects = Problem.objects.filter(pk__in=keys)
        for pk in answers:
            correct_ans[pk] = Problem.objects.get(pk=pk).answer
            try:
                answer = float(answers[pk])
                if (Problem.objects.get(pk=pk).left_border <=
                        answer <= Problem.objects.get(pk=pk).right_border):
                    result[pk] = True
                else:
                    result[pk] = False
            except ValueError:
                result[pk] = False
        return render(request, "mainapp/test_result.html",
                      {"objects": objects, "keys": keys,
                                "answers": answers.values, "result": result.values(),
                                "res_sum": sum(result.values()),
                                "task_sum": len(keys)})

    return main_page(request)
# pylint: enable=no-member
