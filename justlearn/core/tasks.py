from datetime import datetime, timedelta

from justlearn.celery import app as celery_app

from .models import Lesson


@celery_app.task
def remove_old_lessons_from_db():
    for el in Lesson.objects.all():
        if datetime.today().date - el.lesson_date > timedelta(days=10):
            el.delete()

