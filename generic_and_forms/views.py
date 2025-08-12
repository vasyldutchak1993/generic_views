from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Jacket
from .forms import JacketForm

class JacketListView(ListView):
    model = Jacket
    template_name = 'jackets/jacket_list.html'
    context_object_name = 'jackets'

class JacketCreateView(CreateView):
    model = Jacket
    form_class = JacketForm
    template_name = 'jackets/jacket_form.html'
    success_url = reverse_lazy('jacket_list')

class JacketDetailView(DetailView):
    model = Jacket
    template_name = 'jackets/jacket_detail.html'
    context_object_name = 'jacket'

class JacketUpdateView(UpdateView):
    model = Jacket
    form_class = JacketForm
    template_name = 'jackets/jacket_form.html'
    success_url = reverse_lazy('jacket_list')

class JacketDeleteView(DeleteView):
    model = Jacket
    template_name = 'jackets/jacket_confirm_delete.html'
    success_url = reverse_lazy('jacket_list')