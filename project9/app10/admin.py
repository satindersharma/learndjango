from django.contrib import admin
from .models import Reporter,Article,InstaUser, Profile
# Register your models here.


admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(InstaUser)
admin.site.register(Profile)