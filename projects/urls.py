from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('new/',views.new_project,name='new'),
    path('<int:project_id>/detail',views.project_detail,name='detail')
]