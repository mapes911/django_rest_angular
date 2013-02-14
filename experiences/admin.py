from django.contrib import admin
from experiences.models import Experience


class ExperienceAdmin(admin.ModelAdmin):
    fields = ('user', 'title', 'moral')
admin.site.register(Experience, ExperienceAdmin)
