from django.contrib import admin
from .models import Profile, Skill, Project, SocialLink, ContactInfo


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'is_available')
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'title', 'typewriter_roles', 'bio_short', 'bio_long')
        }),
        ('Media', {
            'fields': ('image', 'resume')
        }),
        ('Availability', {
            'fields': ('is_available', 'availability_text')
        }),
        ('About Stats', {
            'fields': ('languages', 'education', 'projects_count')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'icon_class', 'order')
    list_editable = ('order',)
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tags', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'order')
    list_editable = ('order',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'location')
