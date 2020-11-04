class Transition:
    def __init__(self, from_state, symbol, to_states):
        self.from_state = from_state
        self.symbol = symbol
        self.to_states = to_states[:]

    def __str__(self):
        return f"Transition: fromstate {self.from_state} symbol {self.symbol}  tostates {self.to_states}\n"

    __repr__ = __str__
