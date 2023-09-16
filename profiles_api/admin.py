from django.contrib import admin
from profiles_api import models

# Register your models here.
admin.site.register(models.UserProfile)
        # This tells the Django  admin to register the UserProfile modelo with the admin site.  This allows us to use the Admin site to work with our users.
