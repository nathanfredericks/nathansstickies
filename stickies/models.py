from django.db import models
from django.core.validators import MinValueValidator
from django.template.defaultfilters import truncatechars
from django.contrib import admin


class Sticky(models.Model):
    window = models.PositiveIntegerField(validators=[MinValueValidator(1)], unique=True)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return truncatechars(self.text, 100)

    @property
    def short_text(self):
        return truncatechars(self.text, 100)

    class Meta:
        verbose_name_plural = 'Stickies'


class StickyAdmin(admin.ModelAdmin):
    list_display = ('window', 'short_text', 'created_at')
