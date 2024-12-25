from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Appointment
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class AppointmentListView(ListView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'app/blog_list.html'

class AppointmentDetailView(DetailView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'app/blog_detail.html'

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['user', 'firstname', 'lastname', 'email', 'address', 'contact_number']
    template_name = 'app/blog_create.html'

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['user', 'firstname', 'lastname', 'email', 'address', 'contact_number']
    template_name = 'app/blog_update.html'

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'app/blog_delete.html'
    success_url = reverse_lazy('blog')