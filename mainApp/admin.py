from django.contrib import admin
from .models import Owner, Education, Experience, Volunteering, Tool, SoftSkill, MainSkill, Language,\
    ProgrammingSkill, Testimonial, Project


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'last_name', 'nickname', 'birthday', 'age', 'phone')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('type', 'program', 'faculty', 'university')
    ordering = ('-year_start',)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'city', 'country', 'year_start', 'month_start', 'year_end', 'month_end',
                    'is_current_job', 'is_visible')
    ordering = ('-year_start', '-month_start',)

    class Media:
        js = ('static/vendor/jquery/jquery.min.js', '/static/admin/js/hide_fields.js',)


class VolunteeringAdmin(admin.ModelAdmin):
    list_display = ('position', 'organisation')
    ordering = ('-year_start', '-month_start',)


class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('name', )


class MainSkillAdmin(admin.ModelAdmin):
    list_display = ('name', )


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')


class ProgrammingSkillAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'company')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Volunteering, VolunteeringAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(SoftSkill, SoftSkillAdmin)
admin.site.register(MainSkill, MainSkillAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(ProgrammingSkill, ProgrammingSkillAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Project, ProjectAdmin)
