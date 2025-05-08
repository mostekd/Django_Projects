from django.core.management.base import BaseCommand
from django.utils import timezone
from crudapp.models import Todo
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Wysyła przypomnienia o zadaniach zbliżających się do deadline'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        upcoming = now + timezone.timedelta(hours=12)

        todos = Todo.objects.filter(deadline__lte=upcoming, deadline__gte=now)
        for todo in todos:
            user = todo.user
            if user.email:
                send_mail(
                    subject='Przypomnienie o zadaniu!',
                    message=f'Cześć {user.username}, zadanie \"{todo.name}\" ma deadline o {todo.deadline}.',
                    from_email='noreply@twojaapp.pl',
                    recipient_list=[user.email],
                )
                self.stdout.write(f'Wysłano przypomnienie do {user.email}')
