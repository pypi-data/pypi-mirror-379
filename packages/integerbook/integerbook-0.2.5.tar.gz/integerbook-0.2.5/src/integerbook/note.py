class Note:
    def __init__(self, offset, duration,  position, number, accidental, circle_of_fifths_idx, tie=None,
                 thick_barline_at_start=False, thick_barline_at_end=False,
                 is_glissando=False, is_vibrato=False, is_grace_note=False, is_ghost_note=False, voice_number=1,
                 is_chord_note=False, slur=None):
        self.offset = offset
        self.duration = duration
        self.position = position
        self.number = number
        self.accidental = accidental
        self.circle_of_fifths_idx = circle_of_fifths_idx
        self.tie = tie   # None, 'start', 'stop', or 'continue'
        self.thick_barline_at_start = thick_barline_at_start
        self.thick_barline_at_end = thick_barline_at_end
        self.is_glissando = is_glissando
        self.is_vibrato = is_vibrato
        self.is_grace_note = is_grace_note
        self.is_ghost_note = is_ghost_note
        self.voice_number = voice_number
        self.is_chord_note = is_chord_note
        self.slur = slur


class Glissando(Note):
    def __init__(self, offset, duration, position, number, accidental, circle_of_fifths_idx,
                 thick_barline_at_start, thick_barline_at_end, position_difference, start):
        super().__init__(offset, duration, position, number, accidental, circle_of_fifths_idx, None,
                         thick_barline_at_start, thick_barline_at_end, True)
        self.position_difference = position_difference
        self.start = start

class StringArticulation:
    def __init__(self, offset, type, start_position, end_position):
        self.offset = offset
        self.type = type
        self.start_position = start_position
        self.end_position = end_position



class Lyric:
    def __init__(self, text, offset, line_idx, voice, syllabic):
        self.text = text
        self.offset = offset
        self.line_idx = line_idx
        self.voice = voice
        self.syllabic = syllabic  # 'single', 'begin', 'middle', 'end'

class GraceNote:
    def __init__(self, offset, position, number, accidental, circle_of_fifths_idx, position_in_beam, length_beam):
        self.offset = offset
        self.position = position
        self.number = number
        self.accidental = accidental
        self.circle_of_fifths_idx = circle_of_fifths_idx
        self.position_in_beam = position_in_beam
        self.length_beam = length_beam
