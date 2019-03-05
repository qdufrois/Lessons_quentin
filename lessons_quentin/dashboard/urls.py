from django.conf.urls import url
from django.contrib import admin

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from dashboard.models import Subscription, Lesson
from dashboard.serializers import SubSerializer, LessonSerializer, SubLessonSerializer, LessonStudentSerializer
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
        url(r'^create_sub$', CreateAPIView.as_view(queryset=Subscription.objects.all(), serializer_class=SubSerializer), name='post_sub'),
        url(r'^update_status$', views.UpdateStatusSubView.as_view(), name='update_status'),
        url(r'^create_lesson$', CreateAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='post_lesson'),
        url(r'^subscription/(?P<pk>\d+)/$', RetrieveAPIView.as_view(queryset=Subscription.objects.all(), serializer_class=SubLessonSerializer), name='get_sub'),
        url(r'^enrol_student$', views.EnrolStudentView.as_view(), name='enrol_student'),
        url(r'^lesson/(?P<pk>\d+)/$', RetrieveAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonStudentSerializer), name='get_lesson'),
]
