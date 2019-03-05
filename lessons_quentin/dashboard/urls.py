from django.conf.urls import url
from django.contrib import admin

from rest_framework.generics import CreateAPIView
from dashboard.models import Subscription
from dashboard.serializers import SubSerializer
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
        url(r'^create_sub$', CreateAPIView.as_view(queryset=Subscription.objects.all(), serializer_class=SubSerializer), name='post_sub'),
        url(r'^update_status$', views.UpdateStatusSubView.as_view(), name='update_status')
]
