from django.urls import path
from .views import EditorChartView


urlpatterns = [
    path('', EditorChartView.as_view(), name='editorChart'),
]