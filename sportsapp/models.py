from django.db import models


class League(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo_url = models.URLField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True, max_length=200, null=True)  # Slug for the URL
    modified = models.DateTimeField(auto_now=True)  # Auto-updates to current time on save
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo_url = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    stadium = models.CharField(max_length=100, blank=True)
    founded_year = models.PositiveIntegerField(blank=True, null=True)
    league = models.ForeignKey(League, related_name='teams', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Match(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Live', 'Live'),
        ('Finished', 'Finished'),
    ]

    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    home_score = models.PositiveIntegerField(blank=True, null=True)
    away_score = models.PositiveIntegerField(blank=True, null=True)
    match_date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    league = models.ForeignKey(League, related_name='matches', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Scheduled')
    slug = models.SlugField(unique=True, max_length=200, null=True)  # Slug for the URL

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.match_date.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        unique_together = ('home_team', 'away_team', 'match_date')
        ordering = ['-match_date']


class MatchLink(models.Model):
    match = models.ForeignKey(Match, related_name='watch_links', on_delete=models.CASCADE)
    url = models.URLField()
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Link for {self.match}"


class MatchDescription(models.Model):
    match = models.OneToOneField(Match, related_name='description', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Description for {self.match}"

