from django.contrib import admin
from library.models import *


admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(BookRequest)