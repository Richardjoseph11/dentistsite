from django.contrib import admin
from .models import Category, Service, Testimony, Ourdentist, Appointment

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Testimony)
admin.site.register(Ourdentist)

class FrontendAdmin(admin.ModelAdmin):
	list_display = ["name", "your_phone","email","address","time","date","status"]
	list_filter = ('date', 'time')
admin.site.register(Appointment, FrontendAdmin)