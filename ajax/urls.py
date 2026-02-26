from django.urls import path

from .views import HomeView, ButtonDemoView, FormDemoView, FibonacciPost

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("button/", ButtonDemoView.as_view(), name="btn_demo"),
    path("form/", FormDemoView.as_view(), name="form_demo"),
    path("fibonacci/", FibonacciPost.as_view(), name="fibonacci"),
]
