from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import Person


class CarterUser(Person):
    GENDER_CHOICES = (
        ('m', _('male')),
        ('f', _('female')),
        ('o', _('other'))
    )

    CARTER_USER_TYPES = (
        ('COMPANY', 'company')
        ('ADMIN', _('adminstrator')),
        ('SELLER', _('seller'))
    )

    class Meta:
        verbose_name = _('Carter User')
        verbose_name_plural = _('Carter Users')

    user = models.OneToOneField(
        'auth.User',
        related_name='carter_user',
        null=True,
        on_delete=models.SET_NULL,
        blank=True
    )

    gender = models.CharField(
        _('gender'),
        choices=GENDER_CHOICES,
        max_length=1,
        null=True,
        blank=True
    )

    user_type = models.CharField(
        _('user type'),
        choices=CARTER_USER_TYPES,
        max_length=10
    )

    def __str__(self):
        return f'{self.name}'
