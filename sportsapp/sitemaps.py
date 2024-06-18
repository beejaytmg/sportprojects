# sports/sitemaps.py

from django.contrib.sitemaps import Sitemap
from .models import League, Match

class LeagueSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return League.objects.all()

    def lastmod(self, obj):
        return obj.modified  # Ensure 'modified' field is added in the League model

    def location(self, obj):
        return f"/matches/{obj.slug}/"


class MatchSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Match.objects.all()

    def lastmod(self, obj):
        return obj.match_date

    def location(self, obj):
        return f"/match/{obj.slug}/"
