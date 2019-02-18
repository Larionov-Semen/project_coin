
from django.contrib import admin

from coin_ul.models import Choice, Money


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class ChoiceAdmin (admin.ModelAdmin):
    list_display = ('user', 'lot', 'choice_sum', )
    fieldsets = [
        (None, {'fields': ('user', 'lot', 'choice_sum', 'num', 'time')}),
    ]


class MoneyAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture', 'status', 'pub_date', )
    fieldsets = [
        (None,               {'fields': ('name', 'status')}),
        ('Информация', {'fields': ['pub_date', 'year', 'type_money',
                                   ('num', 'price',),
                                   ('description', 'picture', 'url'),

                                   ]}
         )
    ]

    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['name']


admin.site.register(Money, MoneyAdmin)
admin.site.register(Choice, ChoiceAdmin)

# Register your models here.
