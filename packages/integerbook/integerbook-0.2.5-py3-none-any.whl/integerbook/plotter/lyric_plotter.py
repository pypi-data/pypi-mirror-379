from integerbook.plotter.note_plotter import NotePlotter


"note that lyric_line_idx is local to the voice"

class LyricPlotter(NotePlotter):
    def __init__(self, sheet, settings, canvas_manager, x_location_finder, y_location_finder):
        super().__init__(sheet, settings, canvas_manager, x_location_finder, y_location_finder)
        self.position_last_lyric = self._create_position_last_lyric_dict()
        self.x_length_space = self.CanvasManager.get_x_length_text(text=" ",
                                                                   font_size=self.PlotSettings.font_size_lyrics,
                                                                   font_path=self.PlotSettings.font_path)
        self.x_length_hyphen = self.CanvasManager.get_x_length_text(text="-",
                                                                    font_size=self.PlotSettings.font_size_lyrics,
                                                                    font_path=self.PlotSettings.font_path)
        self.x_length_around_hyphen = 0 #self.x_length_space/20

    def plot_lyrics(self):
        if self.PlotSettings.plot_lyrics:
            for lyric in self.sheet.lyrics:
                self._plot_lyric(lyric)

    def _plot_lyric(self, lyric):
        sheet_line_idx, x_pos = self.XLocationFinder.get_line_and_x_pos(lyric.offset)
        y_pos = self.YLocationFinder.get_y_pos_lyric(lyric.voice, lyric.line_idx, sheet_line_idx)
        page_idx = self.YLocationFinder.get_page(sheet_line_idx)

        if self._has_hyphen_before(lyric):
            self._plot_hyphen(x_pos, lyric.voice, lyric.line_idx, sheet_line_idx, page_idx)

        x_pos = self._adjust_x_pos(x_pos, lyric.voice, lyric.line_idx, sheet_line_idx, self._has_hyphen_before(lyric))
        x_pos_end = self.CanvasManager.add_text(page_idx=page_idx, x=x_pos, y=y_pos, text=lyric.text,
                                                font_path=self.PlotSettings.font_path,
                                                fontsize=self.PlotSettings.font_size_lyrics,
                                                border=self.PlotSettings.border_text_lyrics, background=True,
                                                zorder=self.PlotSettings.z_order_lyrics)

        self._update_position_last_lyric(lyric.voice, lyric.line_idx, x_pos_end, sheet_line_idx)

    def _plot_hyphen(self, x_pos, voice, lyric_line_idx, sheet_line_idx, page_idx):
        sheet_line_idx_last_lyric = self.position_last_lyric[voice][lyric_line_idx][1]
        x_pos_end_last_lyric = self.position_last_lyric[voice][lyric_line_idx][0]
        if sheet_line_idx == sheet_line_idx_last_lyric:
            x_pos_hyphen = max(x_pos_end_last_lyric + self.x_length_around_hyphen,
                               x_pos_end_last_lyric + (x_pos + self.PlotSettings.x_shift_lyrics - x_pos_end_last_lyric)/2 - 0.5 * self.x_length_hyphen)
        else:
            # plot hyphen simply after the last lyric (in the future we could check whether in some cases plotting
            # it on the next line might be more appropriate.
            x_pos_hyphen = x_pos_end_last_lyric + self.x_length_around_hyphen

        y_pos_hyphen = self.YLocationFinder.get_y_pos_lyric(voice, lyric_line_idx, sheet_line_idx_last_lyric)

        x_pos_end = self.CanvasManager.add_text(page_idx=page_idx, x=x_pos_hyphen, y=y_pos_hyphen, text="-",
                                                font_path=self.PlotSettings.font_path,
                                                fontsize=self.PlotSettings.font_size_lyrics,
                                                border=self.PlotSettings.border_text_lyrics,
                                                zorder=self.PlotSettings.z_order_lyrics)
        self._update_position_last_lyric(voice, lyric_line_idx, x_pos_end, sheet_line_idx_last_lyric)


    def _create_position_last_lyric_dict(self):
        # format {voice: {lyric_line_idx: (x_pos_last_lyric, sheet_line_idx_last_lyric)
        position_last_lyric = {}
        for voice in self.sheet.num_lines_lyrics_per_voice.keys():
            position_last_lyric_per_voice = {}
            for lyric_line_idx in range(self.sheet.num_lines_lyrics_per_voice[voice]):
                position_last_lyric_per_voice[lyric_line_idx] = (0, 0)
            position_last_lyric[voice] = position_last_lyric_per_voice
        return position_last_lyric

    @staticmethod
    def _has_hyphen_before(lyric):
        return lyric.syllabic == 'middle' or lyric.syllabic == 'end'

    def _update_position_last_lyric(self, voice, lyric_line_idx, x_pos_end, sheet_line_idx):
        self.position_last_lyric[voice][lyric_line_idx] = (x_pos_end, sheet_line_idx)

    def _adjust_x_pos(self, x_pos, voice, lyric_line_idx, sheet_line_idx, has_hyphen_before=False):
        sheet_line_idx_last_lyric = self.position_last_lyric[voice][lyric_line_idx][1]
        x_length_space = self.x_length_space * self.PlotSettings.lyric_space_fraction
        if has_hyphen_before:
            x_length_space = self.x_length_around_hyphen
        if sheet_line_idx == sheet_line_idx_last_lyric:
            x_pos_end_last_lyric = self.position_last_lyric[voice][lyric_line_idx][0]
            x_pos = max(x_pos + self.PlotSettings.x_shift_lyrics, x_pos_end_last_lyric + x_length_space)
        return x_pos
