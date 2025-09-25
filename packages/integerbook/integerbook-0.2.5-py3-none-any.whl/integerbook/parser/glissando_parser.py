import music21

from integerbook.parser.note_parser import NoteParser
from integerbook.note import Glissando

class GlissandoParser(NoteParser):
    def __init__(self, stream_obj, settings):
        super().__init__(stream_obj, settings)
        self.glissandos = []

    def parse_glissandos(self):
        for glissando_spanner in self.stream_obj[music21.spanner.Glissando]:
            self._parse_glissando(glissando_spanner)
        return self.glissandos

    def _parse_glissando(self, glissando_spanner):
        m21_note, m21_note_next = glissando_spanner.getSpannedElements()
        position_difference = (self._get_position(m21_note_next) - self._get_position(m21_note)) / 2
        start = True
        for m21_note_i in [m21_note, m21_note_next]:
            glissando = Glissando(offset=self._get_offset(m21_note_i),
                                  duration=float(m21_note_i.quarterLength),
                                  position=self._get_position(m21_note_i),
                                  number=self._get_number_and_accidental_note(m21_note_i)[0],
                                  accidental=self._get_number_and_accidental_note(m21_note_i)[1],
                                  circle_of_fifths_idx=self._get_circle_of_fifths_idx(m21_note),
                                  thick_barline_at_start=self._note_has_thick_barline_at_start(m21_note_i),
                                  thick_barline_at_end=self._note_has_thick_barline_at_end(m21_note_i),
                                  position_difference=position_difference,
                                  start=start)
            self.glissandos.append(glissando)
            start = False
