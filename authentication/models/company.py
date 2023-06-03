from django.utils.translation import gettext_lazy as _
from django.db import models

from base.models import Base
from . import CarterUser


class Company(Base):
    # Car Store
    cnpj = models.CharField('CNPJ', max_length=16)
    fantasy_name = models.CharField(_('fantasy name'), max_length=50)
    corporate_name = models.CharField(_('corporate name'), max_length=50)
    company_logo = models.URLField(_('company logo'), null=True, blank=True)

    carter_user = models.OneToOneField(
        CarterUser, related_name='company_user', on_delete=models.SET_NULL, null=True, blank=True)
    contact = models.ForeignKey(
        'base.Contact', on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(
        'base.Address', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')
