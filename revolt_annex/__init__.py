from django.template import Library

register = Library()
from .custom_filters import filter_by_date
