from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name ='main_page'),
    path('feedback', views.render_feedback),
    path('feedback_form', views.render_feedbackform),
    path('send_feedback', views.check_feedbackpost),
]