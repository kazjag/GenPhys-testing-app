from django.shortcuts import render
from .models import Feedback
from django.core.cache import cache
from . import forms_work
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def main_page(request):
    return render(request, 'mainapp/main_page.html')


def render_feedback(request):
    feedbacks = Feedback.objects.all().order_by("-created_date")
    return render(request, 'mainapp/feedback_list.html', {'feedbacks': feedbacks})

def render_feedbackform(request):
    return render(request, 'mainapp/feedback_form.html')


@csrf_exempt
def check_feedbackpost(request):
    print(request.method)
    if request.method == "POST":
        cache.clear()
        author = request.POST.get("author", "")
        feedtext = request.POST.get("feedtext", "")
        print('a ', author, ' a', 'b ', feedtext, ' b')
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
    else:
        return render_feedbackform(request)

