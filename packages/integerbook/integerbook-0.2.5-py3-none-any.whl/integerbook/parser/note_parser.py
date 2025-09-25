import music21

from integerbook.parser.base_parser import BaseParser
from integerbook.note import Note

class NoteParser(BaseParser):

    def parse_notes(self):
        notes = []
        for m21_note in self.stream_obj[music21.note.Note]:
            notes.append(self._parse_note(m21_note))

        for m21_chord in self.stream_obj[music21.chord.Chord]:
            if type(m21_chord) == music21.chord.Chord:
                offset = self._get_offset(m21_chord)
                for m21_note in m21_chord.notes:
                    notes.append(self._parse_note(m21_note, offset))
        return notes

    def _parse_note(self, m21_note, offset=None, is_chord_note=False):
        if offset is None:
            offset = self._get_offset(m21_note)
        note = Note(
            offset=offset,
            duration=float(m21_note.quarterLength),
            position=self._get_position(m21_note),
            number=self._get_number_and_accidental_note(m21_note, offset)[0],
            accidental=self._get_number_and_accidental_note(m21_note, offset)[1],
            circle_of_fifths_idx=self._get_circle_of_fifths_idx(m21_note, offset),
            tie=self._get_tie(m21_note),
            thick_barline_at_start=self._note_has_thick_barline_at_start(m21_note, offset),
            thick_barline_at_end=self._note_has_thick_barline_at_end(m21_note, offset),
            is_glissando=self._is_glissando(m21_note),
            is_vibrato=self._is_vibrato(m21_note),
            is_grace_note=self._is_grace_note(m21_note),
            is_ghost_note=self.is_ghost_note(m21_note),
            voice_number=self.get_voice_number(m21_note),
            is_chord_note=is_chord_note,
            slur=self._slur(m21_note)
        )
        return note

    def _get_number_and_accidental_note(self, m21_note, offset=None):
        if offset is None:
            offset = self._get_offset(m21_note)
        if not self.ParseSettings.numbers_relative_to_chord:
            key = self._get_current_key(offset)
        else:
            key = self._get_key_from_current_chord(offset)
        pitch = m21_note.pitch
        return self._get_number_and_accidental_from_pitch(pitch, key)


    def _get_position(self, m21_note):
        return m21_note.pitch.midi - self.lowest_midi

    def _get_circle_of_fifths_idx(self, m21_note, offset=None):
        if offset is None:
            offset = self._get_offset(m21_note)
        key = self._get_current_key(offset)
        pitch_key = key.getTonic().ps
        pitch_note = m21_note.pitch.ps
        relative_pitch = (pitch_note - pitch_key) % 12
        pitches_circle_of_fifths = [(i * 7) % 12 for i in range(12)]
        return pitches_circle_of_fifths.index(relative_pitch)

    @staticmethod
    def _get_tie(m21_note):
        if m21_note.tie:
            return m21_note.tie.type
        else:
            return None

    @staticmethod
    def _is_glissando(m21_note):
        if m21_note.getSpannerSites():
            sp = m21_note.getSpannerSites()[0]
            return type(sp) is music21.spanner.Glissando
        else:
            return False

    def _is_vibrato(self, m21_note):
        for trill_extension in self.stream_obj[music21.expressions.TrillExtension]:
            first_spanned_element = trill_extension.getSpannedElements()[0]
            if first_spanned_element.id == m21_note.id:
                return True
        return False

    @staticmethod
    def _is_grace_note(m21_note):
        return not m21_note.duration.linked

    @staticmethod
    def is_ghost_note(m21_note):
        return m21_note.notehead == 'x'

    def _get_key_from_current_chord(self, offset):
        key = self._get_current_key(0)
        for chord_symbol in self.stream_obj[music21.harmony.ChordSymbol]:
            if self._get_offset(chord_symbol) <= offset:
                key = music21.key.Key(chord_symbol.root())
        return key

    def _note_has_thick_barline_at_start(self, m21_note, offset=None):
        if offset is None:
            offset = self._get_offset(m21_note)
        for measure in self.stream_obj[music21.stream.Measure]:
            if measure.offset == offset:
                return self._measure_has_thick_barline_at_start(measure)
        return False

    def _note_has_thick_barline_at_end(self, m21_note, offset=None):
        if offset is None:
            offset = self._get_offset(m21_note)
        for measure in self.stream_obj[music21.stream.Measure]:
            if measure.offset + measure.quarterLength == offset + m21_note.quarterLength:
                return self._measure_has_thick_barline_at_end(measure)
        return False

    def _measure_has_thick_barline_at_start(self, measure):
        for barline in measure[music21.bar.Barline]:
            if type(barline) is music21.bar.Repeat and barline.offset == 0:
                return True
        return False

    def _measure_has_thick_barline_at_end(self, measure):
        for barline in measure[music21.bar.Barline]:
            if (type(barline) is music21.bar.Repeat or barline.type == 'final') and barline.offset == measure.quarterLength:
                return True
        return False

    def _slur(self, m21_note):
        for spanner in m21_note.getSpannerSites():
            if type(spanner) is music21.spanner.Slur:
                if spanner.getFirst() == m21_note:
                    return 'start'
                elif spanner.getLast() == m21_note:
                    return 'end'
                else:
                    return 'continue'
        return None


