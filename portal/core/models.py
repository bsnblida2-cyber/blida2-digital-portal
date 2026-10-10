from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class PublishedQuerySet(models.QuerySet):
    def published(self): return self.filter(status="published", published_at__lte=timezone.now())

class ContentBase(models.Model):
    STATUS = [("draft", "مسودة"), ("review", "بانتظار المراجعة"), ("published", "منشور"), ("archived", "مؤرشف")]
    title = models.CharField("العنوان", max_length=220)
    slug = models.SlugField("الرابط المختصر", max_length=240, unique=True, blank=True)
    summary = models.CharField("ملخص", max_length=500, blank=True)
    body = models.TextField("المحتوى", blank=True)
    status = models.CharField("الحالة", max_length=12, choices=STATUS, default="draft", db_index=True)
    published_at = models.DateTimeField("تاريخ النشر", null=True, blank=True, db_index=True)
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    updated_at = models.DateTimeField("آخر تحديث", auto_now=True)
    objects = PublishedQuerySet.as_manager()
    class Meta:
        abstract = True
        ordering = ["-published_at", "-created_at"]
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.title, allow_unicode=True)[:230] or f"content-{int(timezone.now().timestamp())}"
        super().save(*args, **kwargs)

class Announcement(ContentBase):
    category = models.CharField("التصنيف", max_length=80, blank=True)
    important = models.BooleanField("إعلان مهم", default=False)
    expires_at = models.DateTimeField("انتهاء العرض", null=True, blank=True)
    class Meta(ContentBase.Meta):
        verbose_name = "إعلان"; verbose_name_plural = "الإعلانات"
    def __str__(self): return self.title

class News(ContentBase):
    category = models.CharField("التصنيف", max_length=80, blank=True)
    image_url = models.URLField("رابط صورة (اختياري)", blank=True)
    class Meta(ContentBase.Meta):
        verbose_name = "خبر"; verbose_name_plural = "الأخبار"
    def __str__(self): return self.title

class Service(models.Model):
    title = models.CharField("اسم الخدمة", max_length=180)
    description = models.CharField("وصف الخدمة", max_length=400, blank=True)
    url = models.URLField("الرابط", max_length=500)
    icon = models.CharField("رمز أو أيقونة", max_length=40, default="↗")
    category = models.CharField("الفئة", max_length=100, blank=True)
    sort_order = models.PositiveIntegerField("الترتيب", default=0)
    active = models.BooleanField("مفعلة", default=True)
    class Meta:
        ordering = ["sort_order", "title"]; verbose_name = "خدمة رقمية"; verbose_name_plural = "الخدمات الرقمية"
    def __str__(self): return self.title

class Faculty(models.Model):
    title = models.CharField("اسم الكلية/المعهد", max_length=220)
    description = models.CharField("وصف", max_length=400, blank=True)
    url = models.URLField("الرابط", max_length=500, blank=True)
    sort_order = models.PositiveIntegerField("الترتيب", default=0)
    active = models.BooleanField("مفعلة", default=True)
    class Meta:
        ordering = ["sort_order", "title"]; verbose_name = "كلية أو معهد"; verbose_name_plural = "الكليات والمعاهد"
    def __str__(self): return self.title
