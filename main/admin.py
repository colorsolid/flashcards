from django.contrib import admin
from .models import FlashCard


class FlashCardAdmin(admin.ModelAdmin):
    pass


admin.site.register(FlashCard, FlashCardAdmin)
