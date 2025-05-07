from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from todo.models import Task
from datetime import timedelta

class Command(BaseCommand):
    help = 'Wysyła przypomnienia o zadaniach bliskich deadline'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        upcoming = now + timedelta(hours=1)
        tasks = Task.objects.filter(deadline__lte=upcoming, deadline__gte=now, complete=False)

        for task in tasks:
            if task.user.email:
                send_mail(
                    subject=f'Przypomnienie: {task.title}',
                    message=f'Twoje zadanie "{task.title}" ma termin: {task.deadline.strftime("%Y-%m-%d %H:%M")}',
                    from_email='no-reply@todo.local',
                    recipient_list=[task.user.email],
                )
        self.stdout.write(self.style.SUCCESS('Wysłano przypomnienia.'))
