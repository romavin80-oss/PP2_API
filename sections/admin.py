from django.contrib import admin

from sections.models import Section, Content, Question, Test


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_filter = ('title',)
    ordering = ('id',)
    search_fields = ('title',)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'title')
    list_filter = ('section',)
    ordering = ('id', 'section',)
    search_fields = ('title',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'question', 'answer')
    list_filter = ('section',)
    ordering = ('id', 'section',)
    search_fields = ('question',)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'title', 'is_active')
    list_filter = ('section', 'is_active')
    ordering = ('id',)
    search_fields = ('title', 'description')
    filter_horizontal = ('questions',)
