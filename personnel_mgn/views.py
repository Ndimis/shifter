from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Personnel


@method_decorator(login_required, name='dispatch')
class PersonnelListView(ListView):
    model = Personnel
    template_name = 'personnel_mgn/personnel_list.html'
    context_object_name = 'personnels'

@method_decorator(login_required, name='dispatch')
class PersonnelDetailView(DetailView):
    model = Personnel
    template_name = 'personnel_mgn/personnel_detail.html'
    context_object_name = 'personnel'

@method_decorator(login_required, name='dispatch')
class PersonnelCreateView(CreateView):
    model = Personnel
    template_name = 'personnel_mgn/personnel_form.html'
    fields = '__all__' 
    success_url = reverse_lazy('personnel_mgn:personnel_list')

@method_decorator(login_required, name='dispatch')
class PersonnelUpdateView(UpdateView):
    model = Personnel
    template_name = 'personnel_mgn/personnel_form.html'
    fields = '__all__' 
    success_url = reverse_lazy('personnel_mgn:personnel_list')

@method_decorator(login_required, name='dispatch')
class PersonnelDeleteView(DeleteView):
    model = Personnel
    template_name = 'personnel_mgn/personnel_confirm_delete.html'
    success_url = reverse_lazy('personnel_mgn:personnel_list')

