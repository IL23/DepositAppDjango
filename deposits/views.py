from django.shortcuts import render

from django.views.generic import View, ListView, FormView, DetailView
from deposits.forms import DepositForm
from django.urls import reverse_lazy
from deposits.models import Deposit


class DepositListView(ListView):

    model = Deposit
    template_name = 'deposit_list.html'


class DepositDetailView(DetailView):

    model = Deposit
    template_name = 'deposit_detail.html'


class AddDeposit(FormView):
    form_class = DepositForm
    template_name = 'add_deposit.html'
    success_url = reverse_lazy('deposit-list')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)

        return response
