from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from .models import Result


# Create your views here.

overviews = {
    'results' : '試合結果',
    'about_team' : 'チームについて',
    'Instagram' : 'インスタ'
}


class IndexView(TemplateView):
    template_name = 'start_page/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team_name"] = '野路コレクション'
        context['overview_items'] = overviews.items()
        return context
    
    
class ReportView(View):
    def get(self, request, links):
        try:
            overview = overviews[links]
            results = Result.objects.all()
            return render(request, 'start_page/result.html', {
                'overviews': overview,
                'results': results
            })
        except KeyError:
            raise Http404('Page not found')
        
class AboutTeamView(View):
    def get(self, request):
        return render(request, 'start_page/about_team.html', {
            'team_name': '野路コレクション',
            'team_description': 
                '野路コレクションは、立命館大学びわこ・くさつキャンパスのサッカーサークルです。みたいな感じで文章入れれます。レイアウトも、詳しく指摘していただければ自由に変更できます。'
        })
