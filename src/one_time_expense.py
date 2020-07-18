from .impact import Impact


class OneTimeExpense(Impact):
    def __init__(self, when, amount) -> None:
        self.when = when
        self.amount = amount

    def events(self):
        return [(self.when, -self.amount)]
