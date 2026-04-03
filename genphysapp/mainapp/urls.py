"""
URLS -> view funcs
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('feedback', views.render_feedback),
    path('feedback_form', views.render_feedbackform),
    path('send_feedback', views.check_feedbackpost),
    path('testing_page', views.create_test),
    path('send_answers', views.check_test_answers),
    path('register', views.register),
    path('login', views.login),
    path('login_page', views.login_page),
    path('logout', views.logout),
]
