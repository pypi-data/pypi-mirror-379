""" Note that not all encodings of string articulations (hammer on, pull off) are parsed correctly
into the music21 stream object. """

import music21

from integerbook.parser.note_parser import NoteParser
from integerbook.note import StringArticulation


class StringArticulationParser(NoteParser):
    def __init__(self, stream_obj, settings):
        super().__init__(stream_obj, settings)
        self.string_articulations = []

    def parse_string_articulations(self):
        for m21_string_articulation in self.stream_obj[music21.articulations.HammerOn, music21.articulations.PullOff]:
            self._parse_string_articulation(m21_string_articulation)
        return self.string_articulations

    def _parse_string_articulation(self, m21_string_articulation):
        m21_note, m21_note_next = m21_string_articulation.getSpannedElements()
        string_articulation = StringArticulation(
            offset=self._get_offset(m21_note_next),
            type=m21_string_articulation.name,
            start_position=self._get_position(m21_note),
            end_position=self._get_position(m21_note_next)
        )
        self.string_articulations.append(string_articulation)
