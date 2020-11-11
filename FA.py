from Transition import Transition


class FA:
    def __init__(self):
        self.__states = []
        self.__alphabet = []
        self.__initial_state = ""
        self.__final_states = []
        self.__transitions = []

    def is_deterministic(self):
        for t in self.__transitions:
            if len(t.to_states) > 1:
                return False
        return True

    @staticmethod
    def parse_line(sett, line, element):
        items = line.split(',')
        for i in items:
            if i in sett:
                raise ValueError(f'Fa {element} must be unique')
            sett.append(i)

        return sett

    @staticmethod
    def parse_transition_line(line):
        items = line.split(',')
        return Transition(items[0], items[1], items[2:])

    def is_accepted(self, sequence):
        state = self.__initial_state
        for character in sequence:
            transition_exists = False
            for t in self.__transitions:
                if t.from_state == state and t.symbol == character:
                    transition_exists = True
                    state = t.to_states[0]

            if not transition_exists:
                return False

        return state in self.__final_states

    def read_from_file(self, file_name):
        file = open(file_name, "r")
        self.__states = self.parse_line(self.__states, file.readline().strip('\n'), "states")
        self.__alphabet = self.parse_line(self.__alphabet, file.readline().strip('\n'), "alphabet")
        self.__initial_state = file.readline().strip('\n')
        self.__final_states = self.parse_line(self.__final_states, file.readline().strip('\n'), "alphabet")

        for line in file:
            new_transition = self.parse_transition_line(line.strip('\n'))

            for transition in self.__transitions:
                if transition.from_state == new_transition.from_state and transition.symbol == new_transition.symbol:
                    transition.to_states.append(new_transition.from_state)
            self.__transitions.append(new_transition)

    def __str__(self):
        return f"FA: \n" \
               f"alphabet: {self.__alphabet}\n" \
               f"initial state: {self.__initial_state}\n" \
               f"final state: {self.__final_states}\n" \
               f"transitions: {self.__transitions}\n"
