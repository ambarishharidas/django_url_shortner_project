from django.contrib import admin
from .models import LongToShort, ShortUrlDetails
# Register your models here.

admin.site.register(LongToShort)
admin.site.register(ShortUrlDetails)