import random
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


def rand_code():
    return '{}.{}{}{}.{}{}{}.{}'.format(*str(int(random.uniform(10000001, 99999999))))


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=20, default=rand_code,
                            verbose_name='Código', editable=False)

    class Meta:
        abstract = True


class Person(Base):
    birthdate = models.DateTimeField(_('birthdate'))
    first_name = models.CharField(_('first name'), max_length=20)
    last_name = models.CharField(_('last name'), max_length=20)
    cpf = models.CharField('CPF', min_length=11, null=True, blank=True)
    rg = models.CharField('RG', min_length=10, null=True, blank=True)

    class Meta:
        abstract = True


class Contact(Base):
    phone = models.CharField(_('phone'), max_length=12)
    seccond_phone = models.CharField(_('phone'), max_length=12)
    email = models.EmailField(_('email'))
    linkedIn = models.URLField('LinkdIn', null=True, blank=True)
    site = models.URLField(_('site'), null=True, blank=True)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class Address(Base):
    ADDRESS_TYPES = (
        ('HOME', _('home address'))
        ('BUSINESS', _('business address')),
        ('TEMP', _('temporary address')),
    )
    address_type = models.CharField(
        _('address type'), choices=ADDRESS_TYPES, max_length=9)
    street = models.CharField(_('street'), max_length=50)
    neighborhood = models.CharField(_('neighborhood'), max_length=30)
    number = models.CharField(_('number'), max_length=6)
    zip_code = models.CharField(_('zip code'), max_length=7)
    city = models.CharField(_('city'), max_length=30)
    state = models.CharField(_('state'), max_length=30)
    country = models.CharField(_('country'), max_length=20)
    complement = models.CharField(
        _('complement'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
