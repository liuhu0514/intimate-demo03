from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'poll', 'que']
    list_filter = ['cname']
    search_fields = ['cname']
    list_per_page = 5


class QuestionAdmin(admin.ModelAdmin):
    # 后台管理显示字段
    list_display = ['id', 'name', 'poll']
    # 过滤字段
    list_filter = ['qname']
    # 搜索字段
    search_fields = ['qname']
    # 分页数量
    list_per_page = 5
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
