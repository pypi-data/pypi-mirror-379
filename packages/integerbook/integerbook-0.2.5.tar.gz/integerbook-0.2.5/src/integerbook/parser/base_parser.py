import music21
from typing import Type
from integerbook.parser.parse_settings import ParseSettings

class BaseParser:
    def __init__(self, stream_obj, settings):
        self.stream_obj = stream_obj
        self.ParseSettings = settings
        self.lowest_midi = self._get_lowest_midi()

    def _get_number_and_accidental_from_pitch(self, pitch, key):
        if key.mode == 'major':
            number, m21_accidental = key.getScaleDegreeAndAccidentalFromPitch(pitch)
        else:
            if self.ParseSettings.minor_perspective == "parallel":
                number, m21_accidental = self._get_scale_degree_and_accidental_parallel_major(key, pitch)
            elif self.ParseSettings.minor_perspective == "relative":
                number, m21_accidental = key.relative.getScaleDegreeAndAccidentalFromPitch(pitch)
            elif self.ParseSettings.minor_perspective == "minor":
                number, m21_accidental = key.getScaleDegreeAndAccidentalFromPitch(pitch)
            else:
                raise ValueError(
                    f"Invalid minor_perspective '{self.ParseSettings.minor_perspective}'. "
                    "Allowed values: 'parallel', 'relative', 'minor'."
                )

        if m21_accidental:
            accidental = m21_accidental.unicode
        else:
            accidental = ''
        return str(number), accidental

    def _get_scale_degree_and_accidental_parallel_major(self, key, pitch):
        number, accidental = key.getScaleDegreeAndAccidentalFromPitch(pitch)

        if number in {3, 6, 7}:
            if accidental and accidental.name == 'flat':
                number -= 1
                accidental = None
            if not accidental:
                accidental = music21.pitch.Accidental('flat')
            if accidental and accidental.name == 'sharp':
                accidental = None

        return number, accidental

    def _get_current_key(self, offset):
        key = music21.key.Key('C')
        for key_i in self.stream_obj[music21.key.Key]:
            if self._get_offset(key_i) <= offset:
                key = key_i
        return key

    def _get_lowest_midi(self):
        lowest_midi = 127
        for m21_note in self.stream_obj[music21.note.Note]:
            if m21_note.pitch.midi < lowest_midi:
                lowest_midi = m21_note.pitch.midi
        if self.ParseSettings.chord_progression:
            lowest_midi = self.stream_obj[music21.key.Key][0].getTonic().ps
        return lowest_midi

    def _get_highest_midi(self):
        highest_midi = 0
        for m21_note in self.stream_obj[music21.note.Note]:
            if m21_note.pitch.midi > highest_midi:
                highest_midi = m21_note.pitch.midi
        if self.ParseSettings.chord_progression:
            highest_midi = self._get_lowest_midi() + 12
        return highest_midi

    def _get_offset(self, m21_el):
        return float(m21_el.getOffsetInHierarchy(self.stream_obj))

    @staticmethod
    def get_voice_number(m21_note):
        """ returns maximum 2"""
        if m21_note.containerHierarchy():
            container = m21_note.containerHierarchy()[0]
            if type(container) is music21.stream.Voice:
                return int(container.id)
        return 1

    @staticmethod
    def _is_pickup_measure(m21_measure):
        return m21_measure.number == 0



