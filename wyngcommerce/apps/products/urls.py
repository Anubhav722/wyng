from django.urls import path
from apps.products import views

urlpatterns = [
    path('am/', views.blah, name="bam"),
]
