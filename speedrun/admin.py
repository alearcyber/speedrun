from django.contrib import admin

from .models import Run
from .models import User

admin.site.register(Run)
admin.site.register(User)
