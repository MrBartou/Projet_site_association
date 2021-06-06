from django.core import validators
from django.db.models import *
from django.core.validators import RegexValidator
# Create your models here.


class Event(Model):
    title = CharField(max_length=32)
    start = DateTimeField()
    end = DateTimeField()

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class PartnershipType(Model):
    title = CharField(max_length=32)

    def __str__(self):
        return self.title


class Partnership(Model):
    category = ForeignKey(PartnershipType,
                          on_delete=CASCADE,
                          null=False)
    img_abs_path = CharField(max_length=256)
    title = CharField(max_length=32)
    description = CharField(max_length=256)

    def __str__(self):
        return self.title


class Subscription(Model):
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    event = ForeignKey(Event, on_delete=CASCADE, null=False)

    email_address = EmailField()
    phone_number = CharField(max_length=32, validators=(RegexValidator(
        # Check if it's a valid french phone number <3
        regex="^(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)"
        "[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2})"
        "{4}|\d{2}(?:[\s.-]?\d{3}){2})$"
    ),))

    school_name = CharField(max_length=32)
    graduation_year = IntegerField()

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return "%s %s (%s)" % (self.first_name,
                               self.last_name,
                               self.email_address)
