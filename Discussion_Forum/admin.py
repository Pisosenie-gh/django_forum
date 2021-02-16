from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(forum)
admin.site.register(Reviews)
admin.site.register(Category)
admin.site.register(PodCategory)
admin.site.register(Like)
admin.site.register(Call)
admin.site.register(ForumPopular)
