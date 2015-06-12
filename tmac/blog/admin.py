from django.contrib import admin
from blog.models import User, Employee, Blog, Entry

admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Blog)
admin.site.register(Entry)
