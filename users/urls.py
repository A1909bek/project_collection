from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('profile/<str:username>/',views.ProfileView.as_view(),name='profile'),
    path('update/',views.UpdateProfileView.as_view(),name='update')
]
