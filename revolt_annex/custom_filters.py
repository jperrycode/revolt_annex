from datetime import datetime
from django import template

register = template.Library()

@register.filter
def filter_by_date(queryset):
    now = datetime.now()
    return queryset.filter(date_field__gte=now)
