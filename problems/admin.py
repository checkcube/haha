from django.contrib import admin
from .models import Problem

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'approved', 'difficulty', 'created_at')
    list_filter = ('approved', 'difficulty', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'author__username')
    ordering = ('-created_at',)
