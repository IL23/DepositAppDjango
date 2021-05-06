from django import forms
from deposits.models import Deposit


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = [
            'deposit',
            'term',
            'rate',
        ]

        labels = {
            'deposit': "Deposit (eur)",
            'term': "Term (years)",
            'rate': "Rate (decimal)",
        }
