import music21.stream

from integerbook.sheet import Sheet
from integerbook.parser.note_parser import NoteParser
from integerbook.parser.chord_parser import ChordParser
from integerbook.parser.glissando_parser import GlissandoParser
from integerbook.parser.string_articulation_parser import StringArticulationParser
from integerbook.parser.grace_note_parser import GraceNoteParser
from integerbook.parser.location_parser import LocationParser
from integerbook.parser.parse_settings import ParseSettings
from integerbook.parser.misc_parser import MiscParser
from integerbook.parser.lyric_parser import LyricParser
from integerbook.parser.chord_note_parser import ChordNoteParser
from integerbook.parser.bar_vline_parsers import BarlineParser, MeasureDividerParser, MeasureSubdividerParser
from integerbook.parser.bar_repeat_parsers import RepeatBracketParser
from integerbook.parser.repeat_expression_parser import RepeatExpressionParser
from integerbook.parser.preprocessor import Preprocessor


class MainParser:
    def __init__(self, path_sheet, user_settings={}):
        self.sheet = Sheet()
        self.ParseSettings = ParseSettings(user_settings)
        stream_obj = music21.converter.parse(path_sheet)
        self.stream_obj = Preprocessor(stream_obj, self.ParseSettings).preprocess_stream_obj()
        self.MiscParser = MiscParser(self.stream_obj, self.ParseSettings)

    def parse_stream(self):
        self.sheet.add_notes(NoteParser(self.stream_obj, self.ParseSettings).parse_notes())
        self.sheet.chords = ChordParser(self.stream_obj, self.ParseSettings).parse_chords()
        self.sheet.glissandos = GlissandoParser(self.stream_obj, self.ParseSettings).parse_glissandos()
        self.sheet.string_articulations = StringArticulationParser(self.stream_obj, self.ParseSettings).parse_string_articulations()
        self.sheet.grace_notes = GraceNoteParser(self.stream_obj, self.ParseSettings).parse_grace_notes()
        self.sheet.add_notes(ChordNoteParser(self.stream_obj, self.ParseSettings).parse_chord_notes())
        self.sheet.key_origins = self.MiscParser.parse_key_origins()
        self.sheet.lyrics, self.sheet.num_lines_lyrics_per_voice = LyricParser(self.stream_obj, self.ParseSettings).parse_lyrics()
        self.sheet.offsets_start_line, self.sheet.h_shifts_line = LocationParser(self.stream_obj, self.ParseSettings).parse()
        self.sheet.pickup_measure_length = self.MiscParser.get_pickup_measure_length()
        self.sheet.offset_length = self.MiscParser.get_offset_length()
        self.sheet.barlines = BarlineParser(self.stream_obj, self.ParseSettings).parse_barlines()
        self.sheet.measure_dividers = MeasureDividerParser(self.stream_obj, self.ParseSettings).parse_measure_dividers()
        self.sheet.measure_subdividers = MeasureSubdividerParser(self.stream_obj, self.ParseSettings).parse_measure_subdividers()
        self.sheet.repeat_brackets = RepeatBracketParser(self.stream_obj, self.ParseSettings).parse_repeat_brackets()
        self.sheet.repeat_expressions = RepeatExpressionParser(self.stream_obj, self.ParseSettings).parse_repeat_expressions()
        self.sheet.title = self.MiscParser.get_song_title()
        self.sheet.composer = self.MiscParser.get_composer()
        self.sheet.arranger = self.MiscParser.get_arranger()
        self.sheet.num_positions = self.MiscParser.get_num_positions()

        return self.sheet

