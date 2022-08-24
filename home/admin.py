from django.contrib import admin
from .models import *
# Register your models here.
class homeModels1(admin.ModelAdmin):
    prepopulated_fields= {'slug':('title',)}

admin.site.register(hero)
admin.site.register(heroSingle)
admin.site.register(firstSection)
admin.site.register(statSection)
admin.site.register(serviceSingle,homeModels1)
admin.site.register(Service)
admin.site.register(Sermons_main_section)
admin.site.register(Sermon,homeModels1)
admin.site.register(verset)
admin.site.register(verset_main_page)
admin.site.register(evenement,homeModels1)
admin.site.register(evenement_main_page)
admin.site.register(secteur,homeModels1)
admin.site.register(secteur_main)
admin.site.register(contact_page)
admin.site.register(about_page)
admin.site.register(wrapper_about_page)
admin.site.register(li_subtitle_about)
admin.site.register(live,homeModels1)
admin.site.register(bay)
admin.site.register(Img)
admin.site.register(Img2)
admin.site.register(fundRaiser,homeModels1)
admin.site.register(participation)
admin.site.register(tag)

