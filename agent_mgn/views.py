from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from agent_mgn.models import Agent
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class AgentListView(ListView):
    model = Agent
    template_name = 'agent_mgn/agent_list.html'
    context_object_name = 'agents'

@method_decorator(login_required, name='dispatch')
class AgentDetailView(DetailView):
    model = Agent
    template_name = 'agent_mgn/agent_detail.html'
    context_object_name = 'agent'

@method_decorator(login_required, name='dispatch')
class AgentCreateView(CreateView):
    model = Agent
    template_name = 'agent_mgn/agent_form.html'
    fields = '__all__'  # À ajuster en fonction de vos besoins
    success_url = reverse_lazy('agent_mgn:agent_list')

@method_decorator(login_required, name='dispatch')
class AgentUpdateView(UpdateView):
    model = Agent
    template_name = 'agent_mgn/agent_form.html'
    fields = '__all__'  # À ajuster en fonction de vos besoins
    success_url = reverse_lazy('agent_mgn:agent_list')

@method_decorator(login_required, name='dispatch')
class AgentDeleteView(DeleteView):
    model = Agent
    template_name = 'agent_mgn/agent_confirm_delete.html'
    success_url = reverse_lazy('agent_mgn:agent_list')

