FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
WORKDIR /app
RUN addgroup --system app && adduser --system --ingroup app app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /app/media /app/staticfiles && chown -R app:app /app
USER app
EXPOSE 10000
CMD ["sh", "-c", "python manage.py makemigrations core --noinput && python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-10000} --workers 2 --timeout 60"]
