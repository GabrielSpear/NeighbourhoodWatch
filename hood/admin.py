from django.contrib import admin
from . models import Hood, Business, Profile, Post

# Register your models here.
admin.site.register(Hood)
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(Post)
