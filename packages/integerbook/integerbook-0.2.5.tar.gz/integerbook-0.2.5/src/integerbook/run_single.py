import music21
from integerbook.parser.main_parser import MainParser
from integerbook.plotter.main_plotter import MainPlotter

from integerbook.main_converter import MainConverter

# stream_obj = music21.converter.parse("tinynotation: 4/4 c d e c e f# g2 '")

p1 = "/Users/jvo/Downloads/All_Of_Me.musicxml"
p2 = "/Users/jvo/Downloads/Autumn_Leaves_18ae0812-5600-4fcc-8a30-170c9edcd876.musicxml"
p3 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/glissando.mxl"
p4 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/hammer-on.musicxml"
p5 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/voices.musicxml"
p6 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/vibrato3.musicxml"
p7 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/gracenotes.musicxml"
p8 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/lyrics-voices.musicxml"
p9 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/lyrics-syllabic-melisma.musicxml"
p10 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/ties.musicxml"
p11 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/string-articulations2.musicxml"
p12 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/slash-chords.musicxml"
p13 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/repeat-brackets-long.musicxml"
p14 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/barlines.musicxml"
p15 = "/Users/jvo/Downloads/Lonestar.musicxml"
p16 = "/Users/jvo/Documents/programming/music-visualization-new/integerbook/tests/test-files/slurs.musicxml"
p17 = "/Users/jvo/Downloads/lonestar soundslice.xml"
p18 = "/Users/jvo/Downloads/the nearness of you.xml"
p19 = "/Users/jvo/Documents/programming/sheet-music/sheets/basslines/1612_04b2fe67-9a19-4b78-a6b0-51dd1a7184c5.musicxml"
p20 = "/Users/jvo/Documents/programming/sheet-music/sheets/popular-sheets/Fly_Me_To_The_Moon_e03e7ee9-9127-4de9-8ab8-602f758b67eb.musicxml"
p21 = "/Users/jvo/Documents/programming/music-visualization/src/integerbook/tests/test-files/repeat-expression.musicxml"
p22 = "/Users/jvo/Documents/programming/music-visualization/src/integerbook/tests/test-files/repeat-brackets-long.musicxml"
p23 = "/Users/jvo/Documents/programming/sheet-music/sheets/DSAll/Misty_57dd99fc-ce06-483a-bfa6-7ffb502d7c7b.musicxml"
p24 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/key-signature-multiple.musicxml"
p25 = "/Users/jvo/Documents/programming/music-visualization/src/integerbook/tests/test-files/key_origin_repeat_expression.musicxml"
p26 = "/Users/jvo/Documents/programming/music-visualization/src/integerbook/tests/test-files/barlines.musicxml"
p27 = "/Users/jvo/Downloads/Fly_Me_To_The_Moon_first_line.musicxml"
p28 = "/Users/jvo/Documents/programming/sheet-music/sheets/christmas-selection/Baby_Its_Cold_Outside_74cb8436-d4de-409e-9f78-7437a722256b.musicxml"

file_path = p28

# manual_secondary_chords = {(1, 0): ["ii", "III"]} # [[(measure number, chord index within measure), secondary_function, secondary_key]
manual_secondary_chords = {}

user_settings = {
    "scroll": False,
    "manual_secondary_chords": manual_secondary_chords,
    "measures_per_line": 2,
    "roman_numerals": False
}

user_settings = {}

# user_settings["measures_per_line"] = 4
# user_settings["subdivision"] = "sixteenth"
# user_settings['plot_thick_barlines'] = False
# user_settings['crop_vertically'] = True
# user_settings['plot_arranger'] = True

user_settings["plot_chord_notes"] = False
user_settings["plot_melody"] = True
user_settings["measures_per_line"] = 4
user_settings['overlap_factor'] = 0
user_settings["chord_progression"] = False
user_settings["plot_lyrics"] = True
user_settings["note_coloring"] = "voices"
user_settings["alpha_melody"] = 0.8
user_settings["font_size_lyrics"] = 8
user_settings["y_margin_lyrics_relative"] = 0.25
user_settings["y_margin_chords_relative"] = 0.45
user_settings["color_background"] = 'white'

# user_settings["font_path"] = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/fonts/Vulf Mono/Vulf Mono/Desktop/VulfMono-LightItalic.otf"
# user_settings["font_path_roman"] = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/fonts/Vulf Mono/Vulf Mono/Desktop/VulfMono-LightItalic.otf"

user_settings["font_path"] = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/fonts/Vulf Mono/Vulf Mono/Desktop/VulfMono-Italic.otf"
user_settings["font_path_roman"] = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/fonts/Vulf Mono/Vulf Mono/Desktop/VulfMono-Italic.otf"

user_settings["color_text_chords"] = 'black'
user_settings["font_size_chords_per_font_size_notes"] = 1.1
user_settings["border_linewidth_per_font_size"] = 0.03
user_settings["scroll"] = True
# user_settings["subdivision"] = "quarter"

# user_settings["plot_chord_notes"] = True
# user_settings["plot_melody"] = False
# user_settings["measures_per_line"] = 8

user_settings["minor_perspective"] = "parallel"


output_dir = "/Users/jvo/Downloads/output"
c = MainConverter()

c.convert(file_path, output_dir, user_settings)
