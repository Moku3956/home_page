from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


# Create your views here.

overviews = {
    'results' : '試合結果',
    'about_team' : 'チームについて'    
}

def index(request):
    index_list = list(overviews.keys())
    # index_urls = " "
    # for index in index_list:
    #     index_path = reverse('overview_url', args=[index])
    #     index_urls += f'<li><a href="{index_path}">{index}</a></li>'
    
    # response_data = index_urls
    return render(request, 'start_page/index.html', {
        'team_name': '野路コレクション', 
        'response_data': index_list
    })
    


def report(request, links):
    try:
        overview = overviews[links]
        return render(request, 'start_page/start_page.html', {
            'team_name': '野路コレクション', 
            'overviews': overview
        })
    except:
        return HttpResponseNotFound('こちらのページは見つかりませんでした')