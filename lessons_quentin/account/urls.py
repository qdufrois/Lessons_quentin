from django.conf.urls import url
from rest_framework.generics import CreateAPIView, DestroyAPIView

from account import views
from account.models import Account, Student
from account.serializers import AccountSerializer, StudentSerializer


app_name = "account"

urlpatterns = [
    # Get url displaying the infos of all or a specific account
    url(
        r"^(?:(?P<account_id>[0-9]+)/)?$",
        views.ListAccountView.as_view(),
        name="get_account",
    ),
    # Post url to create an account instance
    url(
        r"^create$",
        CreateAPIView.as_view(
            queryset=Account.objects.all(), serializer_class=AccountSerializer
        ),
        name="post_account",
    ),
    # Post url to create a student instance
    url(
        r"^create_student$",
        CreateAPIView.as_view(
            queryset=Student.objects.all(), serializer_class=StudentSerializer
        ),
        name="post_student",
    ),
    # Delete url to delete student via its primary key
    url(
        r"^delete_student/(?P<pk>[0-9]+)$",
        DestroyAPIView.as_view(
            queryset=Student.objects.all(), serializer_class=StudentSerializer
        ),
        name="delete_student",
    ),
]
