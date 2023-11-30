from django.contrib import admin
from .models import CV


class CVAdmin(admin.ModelAdmin):
    list_display = ["cv", "user", "created_date"]

    class Meta:
        model = CV

admin.site.register(CV, CVAdmin)

