from django.contrib import admin
from .models import Summary, MindMap, StudyPlan, Reminder


@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'text', 'user__username')
    list_filter = ('created_at',)


@admin.register(MindMap)
class MindMapAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'content', 'user__username')
    list_filter = ('created_at',)


@admin.register(StudyPlan)
class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'deadline', 'created_at')
    search_fields = ('subject', 'goal', 'user__username')
    list_filter = ('deadline', 'created_at')


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'created_at')
    search_fields = ('title', 'note', 'user__username')
    list_filter = ('date', 'created_at')