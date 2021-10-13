from django.contrib import admin
from .models import Survey, Question, AnswerQuestion, Answer

# Register your models here.


admin.site.register(Question)
admin.site.register(AnswerQuestion)
admin.site.register(Answer)
@admin.register(Survey)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("name", "start", "stop")
    list_display_links = ("name", "start", "stop")
