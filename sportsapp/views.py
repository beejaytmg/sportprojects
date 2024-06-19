from django.shortcuts import render, get_object_or_404
from .models import League, Match, Team
import os
from django.http import HttpResponse, request
from django.conf import settings
def league_list(request):
    leagues = League.objects.all()
    return render(request, 'sports/league_list.html', {'leagues': leagues})

def league_matches(request, slug):
    league = get_object_or_404(League, slug=slug)
    matches = Match.objects.filter(league=league).order_by('-match_date')
    return render(request, 'sports/league_matches.html', {'league': league, 'matches': matches})

def match_detail(request, slug):
    match = get_object_or_404(Match, slug=slug)
    return render(request, 'sports/match_detail.html', {'match': match})
def robots_txt(request):
    ads_file_path = os.path.join(settings.BASE_DIR, 'robots.txt')
    try:
        with open(ads_file_path, 'r') as file:
            content = file.read()
        return HttpResponse(content, content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse('File not found.', status=404, content_type='text/plain')