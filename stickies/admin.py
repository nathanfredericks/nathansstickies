from django.contrib import admin
from .models import Sticky, StickyAdmin

admin.site.register(Sticky, StickyAdmin)
