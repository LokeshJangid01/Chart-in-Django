from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Editor

# Create your views here.
class EditorChartView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Editor.objects.all()
        return context