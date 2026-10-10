from django.contrib import admin
from .models import Announcement, News, Service, Faculty
admin.site.site_header = "إدارة البوابة الرقمية — جامعة البليدة 2"
admin.site.site_title = "إدارة البوابة"
admin.site.index_title = "إدارة المحتوى المؤسسي"
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "important", "published_at", "updated_at")
    list_filter = ("status", "important", "category")
    search_fields = ("title", "summary", "body")
    prepopulated_fields = {"slug": ("title",)}
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "published_at", "updated_at")
    list_filter = ("status", "category")
    search_fields = ("title", "summary", "body")
    prepopulated_fields = {"slug": ("title",)}
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "active", "sort_order")
    list_filter = ("active", "category")
    search_fields = ("title", "description")
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("title", "active", "sort_order")
    list_filter = ("active",)
    search_fields = ("title", "description")
