from django.urls import path

from home.views import IndexListView, BaseView

urlpatterns = [

    path("", IndexListView.as_view(), name="index"),
    path("base", BaseView.as_view(), name="base"),
    ]