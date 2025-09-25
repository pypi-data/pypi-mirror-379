import music21
import os
import json

from integerbook.parser.base_parser import BaseParser
from integerbook.chord import Chord

class ChordParser(BaseParser):
    def __init__(self, stream_obj, settings):
        super().__init__(stream_obj, settings)
        self.chords = []

        pathChordKindAbbreviations = os.path.join(os.path.dirname(__file__), 'chordKindAbbreviations.json')
        f = open(pathChordKindAbbreviations)
        self.chordKindAbbreviations = json.load(f)

    def parse_chords(self):
        for measure in self.stream_obj[music21.stream.Measure]:
            for local_chord_idx, m21_chord_symbol in enumerate(measure[music21.harmony.ChordSymbol]):
                self._parse_chord(m21_chord_symbol, measure.number, local_chord_idx)
        return self.chords

    def _parse_chord(self, m21_chord_symbol, measure_number, local_chord_idx):

        chord = Chord(
            offset=self._get_offset(m21_chord_symbol),
            numeral=self._get_numeral_and_accidental_chord_symbol(m21_chord_symbol)[0],
            accidental=self._get_numeral_and_accidental_chord_symbol(m21_chord_symbol)[1],
            kind=self.chordKindAbbreviations[m21_chord_symbol.chordKind],
            modifications=self._get_modifications(m21_chord_symbol),
            bass=self._get_bass(m21_chord_symbol),
            secondary_numeral_function=self._get_secondary_chord_info(measure_number, local_chord_idx)[0],
            secondary_numeral_key=self._get_secondary_chord_info(measure_number, local_chord_idx)[1],
        )
        self.chords.append(chord)

    def _get_bass(self, chord_symbol):

        if chord_symbol.root().name != chord_symbol.bass().name:
            key = self._get_current_key(self._get_offset(chord_symbol))
            pitch = chord_symbol.bass()
            number, accidental = self._get_number_and_accidental_from_pitch(pitch, key)
            return accidental + number
        else:
            return None


    def _get_secondary_chord_info(self, measure_number, local_chord_idx):
        secondary_numeral_function = None
        secondary_numeral_key = None

        global_chord_idx = (measure_number, local_chord_idx)
        if global_chord_idx in self.ParseSettings.manual_secondary_chords:
            secondary_numeral_function, secondary_numeral_key = self.ParseSettings.manual_secondary_chords[global_chord_idx]

        return secondary_numeral_function, secondary_numeral_key

    def _get_numeral_and_accidental_chord_symbol(self, m21_chord_symbol):
        offset = self._get_offset(m21_chord_symbol)
        key = self._get_current_key(offset)
        number, accidental = self._get_number_and_accidental_from_pitch(m21_chord_symbol.root(), key)
        numeral = self._int_to_roman(number)
        if self._is_minor(m21_chord_symbol):
            numeral = numeral.lower()

        return numeral, accidental


    def _int_to_roman(self, number):
        roman_mapping = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII"
        }
        return roman_mapping.get(int(number), "Invalid input")



    def _get_modifications(self, m21_chord_symbol):

        modificationsString = ""

        for csMod in m21_chord_symbol.chordStepModifications:
            modificationsString += self._get_mod_type(csMod, m21_chord_symbol.chordKind)
            modificationsString += self._interval_to_accidental_string(csMod.interval)
            modificationsString += str(csMod.degree)

        return modificationsString


    def _get_mod_type(self, csMod, chordKind):
        d = {
            "add": "add",
            "subtract": "omit",
            "alter": ""
        }
        mod_type = d[csMod.modType]
        if self._is_add_and_not_triad_and_accidental_modification(csMod, chordKind):
            mod_type = ""

        return mod_type

    def _is_minor(self, m21_chord_symbol):
        if not m21_chord_symbol.chordKind == 'other':
            return '-3' in self._get_scale_degrees_from_chord_kind(m21_chord_symbol.chordKind)
        else:
            print(m21_chord_symbol)

    def _interval_to_accidental_string(self, interval):
        if interval.semitones == 0:
            return ""
        else:
            return music21.pitch.Accidental(interval.semitones).unicode

    def _is_add_and_not_triad_and_accidental_modification(self, csMod, chordKind):
        """e.g. C7♭9. We check this to avoid having expressions like c7add♭9"""
        return csMod.modType == "add" and not self._is_triad(chordKind) and not csMod.interval.semitones == 0


    def _get_scale_degrees_from_chord_kind(self, chordKind):
        if chordKind in music21.harmony.CHORD_TYPES:
            return music21.harmony.CHORD_TYPES[chordKind][0].split(',')
        else:
            print("chord not recognized", chordKind)
            return [1, 3, 5]

    def _is_triad(self, chordKind):
        triadTypes = {"major", "minor", "augmented", "diminished", "suspended-second", "suspended-fourth"}
        return chordKind in triadTypes

    def _format_manual_numeral(self, manual_numeral):
        return manual_numeral.replace("#", "♯").replace("b", "♭")

