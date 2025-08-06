from django.urls import path 
from . import views
from .views import IndexView, ReportView
urlpatterns = [
    path('', IndexView.as_view(), name='index_url'),
    path('<str:links>', ReportView.as_view(), name='overview_url')
]
