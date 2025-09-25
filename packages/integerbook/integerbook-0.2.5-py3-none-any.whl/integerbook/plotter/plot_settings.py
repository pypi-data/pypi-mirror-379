import json
import os

from matplotlib import font_manager as fm



class PlotSettings:

    def __init__(self, user_settings, get_cap_height):
        path_settings = os.path.join(os.path.dirname(__file__), 'plot_settings.json')
        f = open(path_settings)
        settings = json.load(f)

        settings.update(user_settings)

        self.scroll = settings["scroll"]
        self.h_length_per_a4_width = settings["h_length_per_a4_width"]

        self.subdivision = settings["subdivision"]

        self.font_size_notes = settings["font_size_notes"]
        self.font_size_grace_notes_per_font_size_notes = settings["font_size_grace_notes_per_font_size_notes"]
        self.font_size_metadata = settings["font_size_metadata"]
        self.font_size_lyrics = settings["font_size_lyrics"]
        self.font_size_string_articulations = settings["font_size_string_articulations"]
        self.font_size_chords_per_font_size_notes = settings["font_size_chords_per_font_size_notes"]
        self.font_size_secondary_chords_per_font_size_chords = settings["font_size_secondary_chords_per_font_size_chords"]
        self.font_size_chord_types_per_font_size_chords = settings["font_size_chord_types_per_font_size_chords"]
        self.height_chord_addition = settings["height_chord_addition"]

        if settings["font_path"]:
            self.font_path = settings["font_path"]
        else:
            self.font_path = fm.findfont(settings["font"])
        if settings["font_path_roman"]:
            self.font_path_roman = settings["font_path_roman"]
        else:
            self.font_path_roman = fm.findfont(settings["font_roman"])
        self.font_string_articulations = settings["font_string_articulations"]

        self.width_margin_line = settings["width_margin_line"]
        self.minimal_pickup_measure_space_fraction = settings["minimal_pickup_measure_space_fraction"]
        self.x_shift_number_note = settings["x_shift_number_note"]
        self.x_shift_grace_notes = settings["x_shift_grace_notes"]
        self.x_shift_chords = settings["x_shift_chords"]
        self.x_shift_lyrics = settings["x_shift_lyrics"]
        self.line_width_thick = settings["line_width_thick"]
        self.line_width_normal = settings["line_width_normal"]
        self.line_width_thin = settings["line_width_thin"]
        self.lyric_space_fraction = settings["lyric_space_fraction"]

        self.bar_space_per_cap_height = settings["bar_space_per_cap_height"]
        self.overlap_factor = settings["overlap_factor"]
        self.y_margin_line_top = settings["y_margin_line_top"]
        self.y_margin_first_line_top = settings["y_margin_first_line_top"]
        self.y_margin_bottom_minimal = settings["y_margin_bottom_minimal"]
        self.y_length_title_ax = settings["y_length_title_ax"]
        self.y_pos_title = settings["y_pos_title"]
        self.y_pos_composer = settings["y_pos_composer"]
        self.y_pos_arranger = settings["y_pos_arranger"]
        self.y_margin_lyrics_relative = settings["y_margin_lyrics_relative"]
        self.y_margin_chords_relative = settings["y_margin_chords_relative"]

        self.facecolor_first_voice = settings["facecolor_first_voice"]
        self.facecolor_second_voice = settings["facecolor_second_voice"]
        self.facecolor_chord_notes = settings["facecolor_chord_notes"]
        self.facecolor_ghost_notes = settings["facecolor_ghost_notes"]
        self.color_text_notes = settings["color_text_notes"]
        self.color_text_grace_notes = settings["color_text_grace_notes"]
        self.color_text_chords = settings["color_text_chords"]
        self.color_text_chord_notes = settings["color_text_chord_notes"]
        self.color_lyrics = settings["color_lyrics"]
        self.color_text_key = settings["color_text_key"]
        self.color_barlines = settings["color_barlines"]
        self.alpha_melody = settings["alpha_melody"]
        self.alpha_chord_notes = settings["alpha_chord_notes"]
        self.alpha_ghost_notes = settings["alpha_ghost_notes"]
        self.color_background = settings["color_background"]
        self.border_text_notes = settings["border_text_notes"]
        self.border_text_chords = settings["border_text_chords"]
        self.border_text_lyrics = settings["border_text_lyrics"]
        self.border_text_metadata = settings["border_text_metadata"]
        self.border_linewidth_per_font_size = settings["border_linewidth_per_font_size"]


        self.z_order_text_melody = settings["z_order_text_melody"]
        self.z_order_lyrics = settings["z_order_lyrics"]
        self.z_order_text_chord_notes = settings["z_order_text_chord_notes"]
        self.z_order_rectangle_melody = settings["z_order_rectangle_melody"]
        self.z_order_rectangle_chord_notes = settings["z_order_rectangle_chord_notes"]
        self.z_order_barlines = settings["z_order_barlines"]
        
        self.note_coloring = settings["note_coloring"]

        self.plot_melody = settings["plot_melody"]
        self.plot_chord_notes = settings["plot_chord_notes"]
        self.plot_lyrics = settings["plot_lyrics"]
        self.plot_barlines = settings["plot_barlines"]
        self.plot_metadata = settings["plot_metadata"]
        self.plot_chords = settings["plot_chords"]
        self.plot_thick_barlines = settings["plot_thick_barlines"]
        self.extend_barline_top = settings["extend_barline_top"]
        self.plot_arranger = settings["plot_arranger"]
        self.plot_time_signature = settings["plot_time_signature"]
        self.plot_first_key_within_bar = settings["plot_first_key_within_bar"]

        self.min_num_note_positions = settings["min_num_note_positions"]

        self.crop_vertically = settings["crop_vertically"]
        self.dpi = settings["dpi"]
        self.output_format = settings["output_format"]
        self.transparent_background = settings["transparent_background"]

        # compute font dimension

        self.x_margin_note = self.line_width_normal / 2
        self.x_margin_note_thick_barline = self.line_width_thick - 0.5 * self.line_width_normal

        self.font_size_chords = self.font_size_chords_per_font_size_notes * self.font_size_notes
        self.font_size_secondary_chords = self.font_size_secondary_chords_per_font_size_chords * self.font_size_chords
        self.font_size_chord_types = self.font_size_chord_types_per_font_size_chords * self.font_size_chords
        self.font_size_chord_types_secondary_chords = self.font_size_chord_types_per_font_size_chords * self.font_size_secondary_chords


        self.font_size_chords = self.font_size_chords_per_font_size_notes * self.font_size_notes
        self.font_size_grace_notes = self.font_size_grace_notes_per_font_size_notes * self.font_size_notes

        cap_height_per_font_size = get_cap_height(font_path=self.font_path)
        cap_height_per_font_size_chords = get_cap_height(font_path=self.font_path_roman)

        
        self.cap_height_notes = cap_height_per_font_size * self.font_size_notes
        self.cap_height_chords = cap_height_per_font_size_chords * self.font_size_chords
        self.cap_height_secondary_chords = cap_height_per_font_size_chords * self.font_size_secondary_chords
        self.cap_height_lyrics = cap_height_per_font_size * self.font_size_lyrics
        self.cap_height_type = cap_height_per_font_size_chords * self.font_size_chord_types
        self.cap_height_string_articulation = cap_height_per_font_size * self.font_size_string_articulations

        self.bar_space = self.bar_space_per_cap_height * self.cap_height_notes

        self.barline_extension = self.cap_height_notes

        # self.font_width_lyric = f_d_lyrics["width"] * self.font_size_lyrics



