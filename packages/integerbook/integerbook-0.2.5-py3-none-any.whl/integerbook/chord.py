class Chord:
    def __init__(self, offset, numeral, accidental, kind, modifications, bass=None,
                 secondary_numeral_function=None, secondary_numeral_key=None):
        self.offset = offset
        self.numeral = numeral
        self.accidental = accidental
        self.kind = kind
        self.modifications = modifications
        self.bass = bass
        self.secondary_numeral_function = secondary_numeral_function
        self.secondary_numeral_key = secondary_numeral_key

