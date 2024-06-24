from django.urls import path
from . import views

app_name = 'agent_mgn'

urlpatterns = [
    path('agents/', views.AgentListView.as_view(), name='agent_list'),
    path('agents/<int:pk>/', views.AgentDetailView.as_view(), name='agent_detail'),
    path('agents/create/', views.AgentCreateView.as_view(), name='agent_create'),
    path('agents/<int:pk>/update/', views.AgentUpdateView.as_view(), name='agent_update'),
    path('agents/<int:pk>/delete/', views.AgentDeleteView.as_view(), name='agent_delete'),
]