# questions/admin.py
from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    inlines = [AnswerInline]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created_at', 'like_count')
    search_fields = ('content',)
    list_filter = ('created_at',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)