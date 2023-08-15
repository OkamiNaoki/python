from django.urls import path
from .views import FibonacciView

urlpatterns = [
    path('fib/', FibonacciView.as_view(), name='fibonacci'),
]
