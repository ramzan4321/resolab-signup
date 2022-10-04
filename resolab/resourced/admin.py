from django.contrib import admin
from .models import ResourceProvider,ResourceSeeker,ResourceSeekerServices

admin.site.register(ResourceProvider)
admin.site.register(ResourceSeeker)
admin.site.register(ResourceSeekerServices)