import random


class DnaSequence:
    _allowed_letters = ['A', 'T', 'C', 'G', 'N']

    def __init__(self, sequence=None, file=None):
        if sequence and file:
            raise TypeError("Wrong input data - define one input source")

        if file:
            with open(file, 'r') as reader:
                self.sequence = reader.read()
        elif sequence:
            self.sequence = sequence
        self.print_sequence()

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        for letter in value.upper():
            if letter not in self._allowed_letters:
                raise ValueError(f"{letter} not allowed in sequence")
        self._sequence = value.upper()

    def print_sequence(self):
        print(self.sequence)

    def print_sequence_reverse(self):
        print(self.sequence[::-1])

    def extend_sequence(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Wrong input data")

        for _ in range(value):
            self.sequence += random.choice(self._allowed_letters)

    def trim_sequence(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong input data")

        if value > len(self.sequence):
            raise ValueError(f"{value} bigger than sequence len {len(self.sequence)}")

        self.sequence = self.sequence[:-value]
