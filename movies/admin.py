from django.contrib import admin

from movies.models import Movie
from .models import *
# Register your models here.
admin.site.register(Movie)