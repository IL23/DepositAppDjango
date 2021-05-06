from django.db import models


class Deposit(models.Model):
    deposit = models.IntegerField(max_length=10)
    term = models.IntegerField(max_length=2)
    rate = models.FloatField()

    def interest_calc(self):
        interest_result = 0
        for year in range(self.term):
            interest_result += self.deposit * self.rate
            self.deposit += interest_result
        return interest_result

    interest = property(interest_calc)



