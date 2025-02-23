from django.contrib import admin
from .models import TarotCard, Love, Career, Health, Finance

# Register your models here.

class TarotCardAdmin(admin.ModelAdmin):
    ordering = ['item']
    list_filter = ['item']

class LoveAdmin(admin.ModelAdmin):
    ordering = ['tarot_card__item', 'tarot_card__name']
    list_filter = ['tarot_card__item']

class CareerAdmin(admin.ModelAdmin):
    ordering = ['tarot_card__item', 'tarot_card__name']
    list_filter = ['tarot_card__item']

class HealthAdmin(admin.ModelAdmin):
    ordering = ['tarot_card__item', 'tarot_card__name']
    list_filter = ['tarot_card__item']

class FinanceAdmin(admin.ModelAdmin):
    ordering = ['tarot_card__item', 'tarot_card__name']
    list_filter = ['tarot_card__item']

admin.site.register(TarotCard, TarotCardAdmin)
admin.site.register(Love, LoveAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Health, HealthAdmin)
admin.site.register(Finance, FinanceAdmin)
