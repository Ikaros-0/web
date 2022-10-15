from django.contrib import admin

# Register your models here.
from .models import Question, Choice

"""
# 注册Question对象的后台
# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)

# 注册Choice对象的后台
# admin.site.register(Choice)
"""

# 同时注册Question和Choice对象的后台
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Data information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', "pub_date", "was_published_recently")
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)