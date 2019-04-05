from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django import forms
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.auth.admin import UserAdmin as django_UserAdmin
from django.db.models.fields import TextField

from khetha import models

# Tweaked InlineModelAdmin defaults:


class _InlineModelAdmin(InlineModelAdmin):
    extra = 0
    show_change_link = True


class _TabularInline(admin.TabularInline, _InlineModelAdmin):
    pass


@admin.register(models.User)
class UserAdmin(django_UserAdmin):
    """
    Re-use Django's `UserAdmin`.
    """


class QuestionInline(SortableInlineAdminMixin, _TabularInline):
    model = models.Question
    exclude = ["description"]
    raw_id_fields = ["task"]


class AnswerOptionInline(SortableInlineAdminMixin, _TabularInline):
    model = models.AnswerOption
    raw_id_fields = ["question"]


class AnswerInline(_TabularInline):
    model = models.Answer
    ordering = ["question__order"]
    raw_id_fields = ["tasksubmission", "question"]
    formfield_overrides = {TextField: {"widget": forms.TextInput}}


@admin.register(models.Task)
class TaskAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["slug", "title", "description", "points", "is_published"]
    search_fields = ["slug", "title", "description"]
    list_editable = ["is_published"]
    list_filter = ["is_published"]

    inlines = [QuestionInline]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["text", "task"]
    raw_id_fields = ["task"]

    inlines = [AnswerOptionInline]


@admin.register(models.AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ["text", "question"]
    raw_id_fields = ["question"]


@admin.register(models.TaskSubmission)
class TaskSubmissionAdmin(admin.ModelAdmin):
    date_hierarchy = "modified_at"
    ordering = ["-modified_at"]
    list_display_links = ["task", "user_key"]
    list_display = ["task", "user_key", "modified_at"]
    search_fields = ["task__title", "user_key"]
    list_filter = [("task", admin.RelatedOnlyFieldListFilter)]

    raw_id_fields = ["task"]
    readonly_fields = ["created_at", "modified_at"]

    inlines = [AnswerInline]
