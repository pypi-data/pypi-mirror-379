import math

class YLocationFinder:
    def __init__(self, sheet, settings):
        self.sheet = sheet
        self.PlotSettings = settings

        self.y_min, self.y_max = self._get_range_ys()
        self.height_line = self.y_max - self.y_min + self.PlotSettings.barline_extension + self.PlotSettings.y_margin_line_top

        self.lines_to_page = []
        self.lines_to_line_on_page = []

        self._divide_lines_over_pages(num_lines=len(self.sheet.offsets_start_line))

    def get_y_pos_note(self, line, pitch_position):
        return self.get_y_pos_line_base(line) + pitch_position * self.PlotSettings.bar_space * (1 - self.PlotSettings.overlap_factor)

    def get_y_pos_chord(self, line):
        return self.get_y_pos_line_base(line) + self.y_min

    def get_y_pos_secondary_chord(self, line):
        return self.get_y_pos_chord(line) - self._get_height_chords()

    def get_y_pos_repeat_bracket(self, line):
        return self.get_y_pos_line_base(line) + self.y_max + 2 * self.PlotSettings.barline_extension

    def get_y_pos_and_height_bar_v_line(self, line, extension=True):
        y_pos = self.get_y_pos_line_base(line)
        height = self.y_max
        if extension:
            y_pos += self.y_min
            height += self.PlotSettings.barline_extension - self.y_min
        return y_pos, height

    def get_page(self, line):
        return self.lines_to_page[line]

    def get_y_length(self, pitch_position_length):
        return pitch_position_length * self.PlotSettings.bar_space * (1 - self.PlotSettings.overlap_factor)

    def get_y_pos_lyric(self, voice, lyric_line_idx, sheet_line_idx):
        y_margin_lyrics = self.PlotSettings.y_margin_lyrics_relative * self.PlotSettings.cap_height_lyrics
        line_height_lyrics = self.PlotSettings.cap_height_lyrics + y_margin_lyrics
        global_line_idx = self._get_global_lyric_line_idx_lyric(voice, lyric_line_idx)
        return self.get_y_pos_line_base(sheet_line_idx) - (global_line_idx + 1) * line_height_lyrics


    def get_num_a4_heights(self):
        num_lines = len(self.sheet.offsets_start_line)
        crop_vertically = self.PlotSettings.scroll or (self.PlotSettings.crop_vertically and num_lines == 1)
        if not crop_vertically:
            return 1
        else:
            return 1 - self._get_y_pos_lowest()

    def _get_y_pos_lowest(self):
        return self.get_y_pos_line_base(0) + self.y_min - self.PlotSettings.y_margin_bottom_minimal


    def _get_global_lyric_line_idx_lyric(self, voice_lyric, lyric_line_idx):
        num_lines_previous_voices = 0
        for voice_i in self.sheet.num_lines_lyrics_per_voice.keys():
            if voice_i < voice_lyric:
                num_lines_previous_voices += self.sheet.num_lines_lyrics_per_voice[voice_i]

        return num_lines_previous_voices + lyric_line_idx



    def _divide_lines_over_pages(self, num_lines):
        page_index = 0
        is_first_page = True
        num_lines_to_make = num_lines
        while num_lines_to_make > 0:
            num_lines_page = min(self._get_num_lines_page_max(is_first_page), num_lines_to_make)
            num_lines_to_make -= num_lines_page
            self.lines_to_line_on_page += [line_on_page for line_on_page in range(num_lines_page)]
            self.lines_to_page += [page_index for _ in range(num_lines_page)]
            is_first_page = False  # TODO Use page_index
            page_index += 1
            if num_lines_page == 0:
                print("ax too big")
                break

    def _get_num_lines_page_max(self, is_first_page):
        """returns the number of lines that fits on the page"""
        if is_first_page:
            return math.floor((1 - self.PlotSettings.y_length_title_ax - self.PlotSettings.y_margin_bottom_minimal) / self.height_line)
        else:
            return math.floor((1 - self.PlotSettings.y_margin_first_line_top - self.PlotSettings.y_margin_bottom_minimal) / self.height_line)

    def get_num_pages(self):
        return self.lines_to_page[-1] + 1

    def get_y_pos_line_base(self, line):
        y_pos_line_base = 1 - self.y_max - self.PlotSettings.barline_extension - self.lines_to_line_on_page[line] * self.height_line
        if self._is_first_page(line) and self.PlotSettings.plot_metadata:
            y_pos_line_base -= self.PlotSettings.y_length_title_ax
        else:
            y_pos_line_base -= self.PlotSettings.y_margin_first_line_top
        return y_pos_line_base

    def _is_first_page(self, line):
        return self.lines_to_page[line] == 0

    def _get_range_ys(self):
        y_max = self.PlotSettings.bar_space + max(self.sheet.num_positions - 1, self.PlotSettings.min_num_note_positions) * self.PlotSettings.bar_space * (1 - self.PlotSettings.overlap_factor)
        y_min = 0

        if self.PlotSettings.plot_lyrics:
            y_min -= self._get_total_height_lyrics()

        if len(self.sheet.chords) > 0 and self.PlotSettings.plot_chords:
            y_min -= self._get_height_chords()

        return y_min, y_max

    def _get_height_chords(self):
        height = max(self.PlotSettings.height_chord_addition * self.PlotSettings.cap_height_chords + self.PlotSettings.cap_height_type, self.PlotSettings.cap_height_chords)
        margin_top = max(self.PlotSettings.cap_height_chords, self.PlotSettings.cap_height_lyrics) * self.PlotSettings.y_margin_chords_relative
        return height + margin_top

    def _get_total_height_lyrics(self):
        y_margin_lyrics = self.PlotSettings.y_margin_lyrics_relative * self.PlotSettings.cap_height_lyrics
        line_height_lyrics = self.PlotSettings.cap_height_lyrics + y_margin_lyrics

        num_lines_lyrics = sum(self.sheet.num_lines_lyrics_per_voice.values())

        return  num_lines_lyrics * line_height_lyrics


