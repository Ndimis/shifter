from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client
from .forms import ClientForm

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'customer_mgn/customer_list.html'
    context_object_name = 'clients'

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'customer_mgn/customer_detail.html'
    context_object_name = 'client'
    success_url = reverse_lazy('customer_mgn:client_list')

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'customer_mgn/customer_form.html'
    success_url = reverse_lazy('customer_mgn:client_list')

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'customer_mgn/customer_form.html'
    success_url = reverse_lazy('customer_mgn:client_list')

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'customer_mgn/customer_confirm_delete.html'
    success_url = reverse_lazy('customer_mgn:client_list')

