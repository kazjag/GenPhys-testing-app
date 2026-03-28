from django.shortcuts import render
from .models import Feedback


# Create your views here.
def main_page(request):
    return render(request, 'mainapp/main_page.html')


def render_feedback(request):
    feedbacks = Feedback.objects.all().order_by("-created_date")
    return render(request, 'mainapp/feedback_list.html', {'feedbacks': feedbacks})
