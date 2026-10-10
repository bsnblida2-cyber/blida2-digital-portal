# بوابة جامعة البليدة 2

بوابة رقمية تجريبية مبنية باستخدام Django، قابلة للنشر على Render وربطها بقاعدة PostgreSQL.

## تشغيل محلي

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

متغيرات البيئة موضحة في `.env.example`. لا تضع كلمات المرور أو `SECRET_KEY` داخل المستودع.
