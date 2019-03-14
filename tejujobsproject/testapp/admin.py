from django.contrib import admin
from testapp.models import hydjobs,blorejobs,chennaijobs,punejobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['id','date','company','eligibility','title','address','email','phonenumber']
admin.site.register(hydjobs,hydjobsAdmin)
class blorejobsAdmin(admin.ModelAdmin):
    list_display=['id','date','company','eligibility','title','address','email','phonenumber']
admin.site.register(blorejobs,blorejobsAdmin)
class punejobsAdmin(admin.ModelAdmin):
    list_display=['id','date','company','eligibility','title','address','email','phonenumber']
admin.site.register(punejobs,punejobsAdmin)
class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['id','date','company','eligibility','title','address','email','phonenumber']
admin.site.register(chennaijobs,chennaijobsAdmin)
