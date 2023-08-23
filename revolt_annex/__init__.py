from django.template import Library
import pymysql

register = Library()
from .custom_filters import filter_by_date


pymysql.install_as_MySQLdb()
