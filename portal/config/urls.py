from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from core import views
from core.sitemaps import StaticViewSitemap
urlpatterns = [path("admin/", admin.site.urls), path("", views.home, name="home"), path("health/", views.health, name="health"), path("api/news/", views.news_api, name="news_api"), path("api/services/", views.services_api, name="services_api"), path("robots.txt", views.robots, name="robots"), path("sitemap.xml", sitemap, {"sitemaps": {"static": StaticViewSitemap}}, name="sitemap")]
