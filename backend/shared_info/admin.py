from django.contrib import admin

from shared_info.models import (Skill, EducationLevel, Specialization,
                                Schedule, Course)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Schedule.

    Параметры:
        - list_display: Поля, которые будут отображаться в списке
        графиков работы.

    Модель:
        - Schedule.
    """
    list_display = ('name',)


@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели EducationLevel.

    Параметры:
        - list_display: Поля, которые будут отображаться в списке
        уровней образования.

    Модель:
        - EducationLevel.
    """
    list_display = ('name',)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Specialization.

    Параметры:
        - list_display: Поля, которые будут отображаться в
        списке специализаций.

    Модель:
        - Specialization.
    """
    list_display = ('name',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Skill.

    Параметры:
        - list_display: Поля, которые будут отображаться в списке
        ключевых навыков.

    Модель:
        - Skill.
    """
    list_display = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Course.

    Параметры:
        - list_display: Поля, которые будут отображаться в списке курсов.

    Модель:
        - Course.
    """
    list_display = ('name',)
