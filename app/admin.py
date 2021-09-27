from django.contrib import admin
from .models import LandingPageDetails, Gift, Comment
# Register your models here.

admin.site.register(LandingPageDetails)
admin.site.register(Gift)
admin.site.register(Comment)