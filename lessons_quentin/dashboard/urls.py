from django.conf.urls import url
from django.contrib import admin
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from account.models import Account
from dashboard import views
from dashboard.models import Subscription, Lesson
from dashboard.serializers import (
    SubSerializer,
    LessonSerializer,
    SubLessonSerializer,
    LessonStudentSerializer,
    LockedLessonSerializer,
    AccountSubSerializer,
)


app_name = "dashboard"

urlpatterns = [
    # Post url to create an subscription instance
    url(
        r"^create_sub$",
        CreateAPIView.as_view(
            queryset=Subscription.objects.all(), serializer_class=SubSerializer
        ),
        name="post_sub",
    ),
    # Post url to update the status of a subscription
    url(r"^update_status$", views.UpdateStatusSubView.as_view(), name="update_status"),
    # Post url to create a lesson instance
    url(
        r"^create_lesson$",
        CreateAPIView.as_view(
            queryset=Lesson.objects.all(), serializer_class=LessonSerializer
        ),
        name="post_lesson",
    ),
    # Get url to retrieve a subscription and all its lessons
    url(
        r"^subscription_lessons/(?P<pk>\d+)/$",
        RetrieveAPIView.as_view(
            queryset=Subscription.objects.all(), serializer_class=SubLessonSerializer
        ),
        name="get_sub",
    ),
    # Post url to create a link between a student and a lesson
    url(r"^enrol_student$", views.EnrolStudentView.as_view(), name="enrol_student"),
    # Get url to retrieve a lesson and all its students
    url(
        r"^lesson/(?P<pk>\d+)/$",
        RetrieveAPIView.as_view(
            queryset=Lesson.objects.all(), serializer_class=LessonStudentSerializer
        ),
        name="get_lesson",
    ),
    # Patch url to lock or unlock a lesson
    url(
        r"^lock_lesson/(?P<pk>\d+)/$",
        UpdateAPIView.as_view(
            queryset=Lesson.objects.all(), serializer_class=LockedLessonSerializer
        ),
        name="lock_lesson",
    ),
    # Get url to retrieve an account and all its subscriptions (including their statuses)
    url(
        r"^subscriptions/(?P<pk>\d+)/$",
        RetrieveAPIView.as_view(
            queryset=Account.objects.all(), serializer_class=AccountSubSerializer
        ),
        name="account_sub",
    ),
]
