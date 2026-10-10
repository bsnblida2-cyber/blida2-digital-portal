from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_GET
from django.db.models import Q
from .models import Announcement, News, Service, Faculty

def home(request):
    context = {"announcements": Announcement.objects.published().filter(Q(expires_at__isnull=True) | Q(expires_at__gt=timezone.now()))[:5], "news": News.objects.published()[:4], "services": Service.objects.filter(active=True)[:8], "faculties": Faculty.objects.filter(active=True)[:8]}
    return render(request, "core/home.html", context)

@require_GET
def news_api(request):
    return JsonResponse({"results": [{"title": x.title, "slug": x.slug, "summary": x.summary, "category": x.category, "published_at": x.published_at.isoformat() if x.published_at else None} for x in News.objects.published()[:50]]})

@require_GET
def services_api(request):
    return JsonResponse({"results": [{"title": x.title, "description": x.description, "url": x.url, "category": x.category, "icon": x.icon} for x in Service.objects.filter(active=True)]})

@require_GET
def health(request): return JsonResponse({"status": "ok", "service": "blida2-portal"})

@require_GET
def robots(request):
    from django.conf import settings
    return HttpResponse(f"User-agent: *\nAllow: /\nSitemap: {settings.SITE_URL}/sitemap.xml\n", content_type="text/plain")
