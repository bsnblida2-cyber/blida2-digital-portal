from django.utils import timezone
from .models import Announcement, News, Service, Faculty


def admin_dashboard(request):
    """Small, database-backed summary used by the custom Django admin home."""
    if not request.path.startswith("/admin/"):
        return {}

    announcement_total = Announcement.objects.count()
    announcement_published = Announcement.objects.filter(
        status="published", published_at__lte=timezone.now()
    ).count()
    news_total = News.objects.count()
    news_published = News.objects.filter(
        status="published", published_at__lte=timezone.now()
    ).count()
    service_total = Service.objects.count()
    service_active = Service.objects.filter(active=True).count()
    faculty_total = Faculty.objects.count()
    faculty_active = Faculty.objects.filter(active=True).count()

    def percent(part, total):
        return round(part * 100 / total) if total else 0

    return {
        "dashboard_stats": {
            "announcements": announcement_total,
            "announcements_published": announcement_published,
            "announcements_other": max(announcement_total - announcement_published, 0),
            "announcements_percent": percent(announcement_published, announcement_total),
            "news": news_total,
            "news_published": news_published,
            "news_other": max(news_total - news_published, 0),
            "news_percent": percent(news_published, news_total),
            "services": service_total,
            "services_active": service_active,
            "services_inactive": max(service_total - service_active, 0),
            "services_percent": percent(service_active, service_total),
            "faculties": faculty_total,
            "faculties_active": faculty_active,
            "faculties_inactive": max(faculty_total - faculty_active, 0),
            "faculties_percent": percent(faculty_active, faculty_total),
        }
    }
