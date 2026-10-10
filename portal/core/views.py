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

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

SPACE_NAMES = {
    "student": "الطالب",
    "teacher": "الأستاذ",
    "researcher": "الباحث",
    "staff": "الموظف",
    "international": "الزائر الدولي",
}

def sign_up(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect(request.GET.get("next") or "home")
    return render(request, "registration/signup.html", {"form": form})

def space_entry(request, space):
    if space not in SPACE_NAMES:
        from django.http import Http404
        raise Http404

    # International visitors can browse without an account.
    if space == "international":
        return render(request, "core/space.html", {
            "space_name": SPACE_NAMES[space],
            "space": space,
            "is_international": True,
        })

    # Send protected spaces straight to this portal's login page.
    # Preserve the intended destination so successful login returns here.
    if not request.user.is_authenticated:
        return redirect(f"{reverse('login')}?next={reverse('space_entry', kwargs={'space': space})}")

    return render(request, "core/space.html", {
        "space_name": SPACE_NAMES[space],
        "space": space,
        "is_international": False,
    })
