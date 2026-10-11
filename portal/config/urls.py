from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from core import views
from core.sitemaps import StaticViewSitemap

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/signup/", views.sign_up, name="signup"),
    path("spaces/<slug:space>/", views.space_entry, name="space_entry"),
    path("health/", views.health, name="health"),
    path("sw.js", views.service_worker, name="service_worker"),
    path("api/news/", views.news_api, name="news_api"),
    path("api/services/", views.services_api, name="services_api"),
    path("robots.txt", views.robots, name="robots"),
    path("sitemap.xml", sitemap, {"sitemaps": {"static": StaticViewSitemap}}, name="sitemap"),
]
