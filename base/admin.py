from django.contrib import admin

from .models import Address, Contact

# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Address, AddressAdmin)
admin.site.register(Contact, ContactAdmin)
