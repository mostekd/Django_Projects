from celery import shared_task

from .models import User, UserSubmission

from celery_once import QueueOnce

@shared_task(
    bind=False,
    soft_time_limit=60 * 60,
    time_limit=70 * 60,
    base=QueueOnce,
    once={"graceful": True},
)
def count_submissions():
    count = UserSubmission.objects.count()
    print(f"Total submissions: {count}")

@shared_task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()
