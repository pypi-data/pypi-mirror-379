import music21

from integerbook.parser.note_parser import NoteParser
from integerbook.note import Note

class ChordNoteParser(NoteParser):
    def __init__(self, stream_obj, settings):
        super().__init__(stream_obj, settings)
        self.chord_notes = []
        self._lowest_midi = self._get_lowest_midi()
        self._highest_midi = self._get_highest_midi()

    def parse_chord_notes(self):
        last_chord_symbol = None
        for measure in self.stream_obj[music21.stream.Measure]:
            chord_symbols = self._get_chord_symbols_in_measure(measure)
            self._parse_last_chord_previous_measure(chord_symbols, last_chord_symbol, measure)
            if len(chord_symbols) > 0:
                self._parse_chord_symbols_except_last(chord_symbols)
                self._parse_last_chord_symbol(chord_symbols, measure)
                last_chord_symbol = chord_symbols[-1]

        return self.chord_notes

    def _parse_last_chord_previous_measure(self, chord_symbols, last_chord_symbol, measure):
        if len(chord_symbols) == 0:
            if self._last_chord_goes_into_next_measure(measure):
                tie = 'continue'
            else:
                tie = 'stop'
            self._parse_chord_notes_chord_symbol(last_chord_symbol, measure.quarterLength, tie=tie,
                                                 offset=self._get_offset(measure))
        else:
            if chord_symbols[0].offset > 0:
                self._parse_chord_notes_chord_symbol(last_chord_symbol, chord_symbols[0].offset, tie='stop',
                                                     offset=self._get_offset(measure))

    def _parse_chord_symbols_except_last(self, chord_symbols):
        for i in range(len(chord_symbols) - 1):
            duration = chord_symbols[i + 1].offset - chord_symbols[i].offset
            self._parse_chord_notes_chord_symbol(chord_symbols[i], duration, tie=None)

    def _parse_last_chord_symbol(self, chord_symbols, measure):
        if self._last_chord_goes_into_next_measure(measure):
            tie = 'start'
        else:
            tie = None
        self._parse_chord_notes_chord_symbol(chord_symbols[-1], measure.quarterLength - chord_symbols[-1].offset,
                                             tie=tie)


    def _parse_chord_notes_chord_symbol(self, chord_symbol, duration, tie, offset=None):
        if offset is None:
            offset = self._get_offset(chord_symbol)
        if chord_symbol:
            for m21_note in chord_symbol.notes:
                m21_note.quarterLength = duration
                m21_note.octave = -1
                if tie:
                    m21_note.tie = music21.tie.Tie(tie)

                for octave in range(11):
                    if m21_note.pitch.midi >= self._lowest_midi and m21_note.pitch.midi <= self._highest_midi:
                        chord_note = self._parse_note(m21_note, offset=offset,
                                                      is_chord_note=True)
                        self.chord_notes.append(chord_note)

                    m21_note.octave += 1

    def _get_chord_symbols_in_measure(self, measure):
        "this is necessary so that the chord symbols keep their offset within the hierarchy of the stream_obj"
        chord_symbols_in_measure = []
        for chord_symbol in self.stream_obj[music21.harmony.ChordSymbol]:
            if self._chord_symbol_is_in_measure(chord_symbol, measure):
                chord_symbols_in_measure.append(chord_symbol)
        return chord_symbols_in_measure

    def _chord_symbol_is_in_measure(self, chord_symbol, measure):
        return self._get_offset(chord_symbol) >= self._get_offset(measure) and self._get_offset(
            chord_symbol) < self._get_offset(measure) + measure.quarterLength


    def _last_chord_goes_into_next_measure(self, measure):
        if not self._is_last_measure(measure):
            next_measure = self.stream_obj.measure(measure.number + 1)
            if not self._measure_starts_with_chord_symbol(next_measure):
                return True
        return False

    def _is_last_measure(self, measure):
        return self.stream_obj[music21.stream.Measure].last().number == measure.number

    def _measure_starts_with_chord_symbol(self, measure):
        if len(measure[music21.harmony.ChordSymbol]) > 0:
            if measure[music21.harmony.ChordSymbol][0].offset == 0:
                return True
        return False



