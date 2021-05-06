class DepositClass:
    def __init__(self, deposit, term, rate):
        self.deposit = deposit
        self.term = term
        self.rate = rate

    def interest(self):
        interest_result = 0
        for year in range(self.term):
            interest_result += self.deposit * self.rate
            self.deposit += interest_result
        return interest_result


deposit = DepositClass(deposit=1000,
                  term=2,
                  rate=0.05,)

interest = deposit.interest()
print(interest)
