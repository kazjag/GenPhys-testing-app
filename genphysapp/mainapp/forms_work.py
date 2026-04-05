"""
 Functions to work with forms
"""
from .models import Feedback

def post_feedback(author, feedtext):
    """

    :param author: author of the feedback
    :param feedtext: text of feedback
    :return: None
    """
    Feedback.objects.create(author=author, text=feedtext)
