# urls.py
from django.urls import path
from . import views 

app_name = 'personnel_mgn'

urlpatterns = [
    path('personnel/', views.PersonnelListView.as_view(), name='personnel_list'),
    path('personnel/<int:pk>/', views.PersonnelDetailView.as_view(), name='personnel_detail'),
    path('personnel/new/', views.PersonnelCreateView.as_view(), name='personnel_create'),
    path('personnel/<int:pk>/edit/', views.PersonnelUpdateView.as_view(), name='personnel_update'),
    path('personnel/<int:pk>/delete/', views.PersonnelDeleteView.as_view(), name='personnel_delete'),
]
