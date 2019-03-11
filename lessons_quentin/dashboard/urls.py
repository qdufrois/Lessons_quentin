from django.conf.urls import url
from django.contrib import admin

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from account.models import Account
from dashboard.models import Subscription, Lesson
from dashboard.serializers import (
    SubSerializer,
    LessonSerializer,
    SubLessonSerializer,
    LessonStudentSerializer,
    LockedLessonSerializer,
    AccountSubSerializer,
)
from dashboard import views


app_name = "dashboard"

urlpatterns = [
    url(
        r"^create_sub$",
        CreateAPIView.as_view(
            queryset=Subscription.objects.all(), serializer_class=SubSerializer
        ),
        name="post_sub",
    ),
    url(r"^update_status$", views.UpdateStatusSubView.as_view(), name="update_status"),
    url(
        r"^create_lesson$",
        CreateAPIView.as_view(
            queryset=Lesson.objects.all(), serializer_class=LessonSerializer
        ),
        name="post_lesson",
    ),
    url(
        r"^subscription_lessons/(?P<pk>\d+)/$",
        RetrieveAPIView.as_view(
            queryset=Subscription.objects.all(), serializer_class=SubLessonSerializer
        ),
        name="get_sub",
    ),
    url(r"^enrol_student$", views.EnrolStudentView.as_view(), name="enrol_student"),
    url(
        r"^lesson/(?P<pk>\d+)/$",
        RetrieveAPIView.as_view(
            queryset=Lesson.objects.all(), serializer_class=LessonStudentSerializer
        ),
        name="get_lesson",
    ),
    url(
        r"^lock_lesson/(?P<pk>\d+)/$",
        UpdateAPIView.as_view(
            queryset=Lesson.objects.all(), serializer_class=LockedLessonSerializer
        ),
        name="lock_lesson",
    ),
    url(
        r"^subscriptions/(?P<pk>\d+)/$",
        ListAPIView.as_view(
            queryset=Account.objects.all(), serializer_class=AccountSubSerializer
        ),
        name="account_sub",
    
        
    )   
]
