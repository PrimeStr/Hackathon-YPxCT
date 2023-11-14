from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.views import (StudentViewSet, VacancyViewSet,
                          MatchingStudentsViewSet, FavoriteStudentViewSet,
                          CompareStudentViewSet, LocationView,
                          EducationLevelView, CourseView, ScheduleView,
                          SkillView, SpecializationView)
from users.views import CustomUserViewSet

router = DefaultRouter()

router.register(r'users', CustomUserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'vacancies', VacancyViewSet, basename='vacancies')
router.register(r'locations', LocationView, basename='location'),
router.register(r'courses', CourseView, basename='course'),
router.register(r'education_levels', EducationLevelView,
                basename='education_levels'),
router.register(r'schedules', ScheduleView, basename='schedule'),
router.register(r'skills', SkillView, basename='skills'),
router.register(r'specializations', SpecializationView,
                basename='specialization'),

urlpatterns = [
    path('', include(router.urls)),
    path(
        'activation_user/<str:uid>/<str:token>/',
        CustomUserViewSet.as_view({'get': 'activate'}), name='activate'
    ),
    path('auth/', include('djoser.urls.jwt')),
    path(
        'matching/<int:vacancy_id>/',
        MatchingStudentsViewSet.as_view({'get': 'list'}),
        name='matching-students-list'
    ),
    path('favorite/<int:student_id>/', FavoriteStudentViewSet.as_view(
        {'post': 'post', 'delete': 'delete'})
         ),
    path('favorite/', FavoriteStudentViewSet.as_view(
        {'get': 'get_favorites'})
         ),
    path('compare/<int:student_id>/', CompareStudentViewSet.as_view(
        {'post': 'post', 'delete': 'delete'})
         ),
    path('compare/', CompareStudentViewSet.as_view({'get': 'get_compare'})),
]
