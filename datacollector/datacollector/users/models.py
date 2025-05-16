from django.contrib.auth.models import AbstractUser
from datetime import date
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for DataCollector.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class Voivodeship(models.Model):
    name = models.CharField(max_length=100)

class City(models.Model):
    name = models.CharField(max_length=100)
    voivodeship = models.ForeignKey(Voivodeship, on_delete=models.CASCADE, related_name="cities")

class UserSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name="submissions")
    birthdate = models.DateField()
    
    def age(self):
        today = date.today()
        return today.year - self.birthdate.year - (
            (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
        )
    
    def __str__(self):
        return f"{self.name} ({self.email})"

