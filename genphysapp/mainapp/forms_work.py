from .models import Feedback


def post_feedback(author, feedtext):
     Feedback.objects.create(author=author, text=feedtext)