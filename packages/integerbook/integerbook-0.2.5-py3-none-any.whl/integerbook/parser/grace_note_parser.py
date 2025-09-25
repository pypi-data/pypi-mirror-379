import music21

from integerbook.parser.note_parser import NoteParser
from integerbook.note import GraceNote

class GraceNoteParser(NoteParser):
    def __init__(self, stream_obj, settings):
        super().__init__(stream_obj, settings)
        self.grace_notes = []


    def parse_grace_notes(self):
        m21_beamed_grace_notes = []
        for m21_note in self.stream_obj[music21.note.Note]:
            if self._is_grace_note(m21_note):
                if self._is_single_grace_note(m21_note):
                    self._parse_grace_note(m21_note, 0, 1)
                elif not self._is_last_grace_note_in_beam(m21_note):
                    m21_beamed_grace_notes.append(m21_note)
                elif self._is_last_grace_note_in_beam(m21_note):
                    m21_beamed_grace_notes.append(m21_note)
                    self._parse_beamed_grace_notes(m21_beamed_grace_notes)
                    m21_beamed_grace_notes = []
        return self.grace_notes

    def _parse_beamed_grace_notes(self, m21_beamed_grace_notes):
        for i, m21_grace_note in enumerate(m21_beamed_grace_notes):
            self._parse_grace_note(m21_grace_note, i, len(m21_beamed_grace_notes))

    def _parse_grace_note(self, m21_grace_note, position_in_beam, length_beam):
        grace_note = GraceNote(
            offset=self._get_offset(m21_grace_note),
            position=self._get_position(m21_grace_note),
            number=self._get_number_and_accidental_note(m21_grace_note)[0],
            accidental=self._get_number_and_accidental_note(m21_grace_note)[1],
            circle_of_fifths_idx=self._get_circle_of_fifths_idx(m21_grace_note),
            position_in_beam=position_in_beam,
            length_beam=length_beam
        )

        self.grace_notes.append(grace_note)

    @staticmethod
    def _is_single_grace_note(m21_grace_note):
        return not m21_grace_note.beams.beamsList

    @staticmethod
    def _is_last_grace_note_in_beam(m21_grace_note):
        return m21_grace_note.beams.beamsList[0].type == 'stop'
