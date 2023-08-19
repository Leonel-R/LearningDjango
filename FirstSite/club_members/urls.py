from django.urls import path
from . import views

urlpatterns = [
    path('club_members/', views.club_members, name='club_members'),
    path('club_members/details/<int:id>', views.details, name='details'),
]

