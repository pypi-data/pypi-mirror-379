from integerbook.plotter.base_plotter import BasePlotter

class ChordPlotter(BasePlotter):
    def __init__(self, sheet, settings, canvas_manager, x_location_finder, y_location_finder):
        super().__init__(sheet, settings, canvas_manager, x_location_finder, y_location_finder)

    def plot_chords(self):
        for chord in self.sheet.chords:
            self._plot_chord(chord)
            self._plot_secondary_chord(chord)

    def _plot_chord(self, chord):
        line, x_pos = self.XLocationFinder.get_line_and_x_pos(chord.offset)
        x_pos += self.PlotSettings.x_shift_chords
        y_pos_chord = self.YLocationFinder.get_y_pos_chord(line)
        page = self.YLocationFinder.get_page(line)

        x_pos_last = self.CanvasManager.add_text(page, x_pos, y_pos_chord, chord.numeral,
                                                 font_path=self.PlotSettings.font_path_roman,
                                                 fontsize=self.PlotSettings.font_size_chords,
                                                 border=self.PlotSettings.border_text_chords,
                                                 zorder=self.PlotSettings.z_order_text_melody,
                                                 color=self.PlotSettings.color_text_chords)
        y_pos_chord_type = y_pos_chord + 0.6 * self.PlotSettings.cap_height_chords
        x_pos_last = self.CanvasManager.add_text(page, x_pos_last, y_pos_chord_type, chord.kind,
                                                 font_path=self.PlotSettings.font_path_roman,
                                                 fontsize=self.PlotSettings.font_size_chord_types,
                                                 border=self.PlotSettings.border_text_chords,
                                                 zorder=self.PlotSettings.z_order_text_melody,
                                                 color=self.PlotSettings.color_text_chords)

        y_pos_bass = y_pos_chord - 0.5 * self.PlotSettings.cap_height_chords
        if chord.bass:
            self.CanvasManager.add_text(page, x_pos_last, y_pos_bass, '/' + chord.bass,
                                        font_path=self.PlotSettings.font_path_roman,
                                        fontsize=self.PlotSettings.font_size_chord_types,
                                        border=self.PlotSettings.border_text_chords,
                                        zorder=self.PlotSettings.z_order_text_melody,
                                        color=self.PlotSettings.color_text_chords)

    def _plot_secondary_chord(self, chord):
        if chord.secondary_numeral_function:
            line, x_pos = self.XLocationFinder.get_line_and_x_pos(chord.offset)
            x_pos += self.PlotSettings.x_shift_chords
            y_pos_secondary_chord = self.YLocationFinder.get_y_pos_secondary_chord(line)
            page = self.YLocationFinder.get_page(line)

            x_pos_last = self.CanvasManager.add_text(page, x_pos, y_pos_secondary_chord,
                                                     chord.secondary_numeral_function,
                                                     font_path=self.PlotSettings.font_path_roman,
                                                     fontsize=self.PlotSettings.font_size_chords,
                                                     border=self.PlotSettings.border_text_chords,
                                                     zorder=self.PlotSettings.z_order_text_melody,
                                                     color=self.PlotSettings.color_text_chords)

            y_pos_chord_type = y_pos_secondary_chord + 0.6 * self.PlotSettings.cap_height_chords
            x_pos_last = self.CanvasManager.add_text(page, x_pos_last, y_pos_chord_type, chord.kind,
                                                     font_path=self.PlotSettings.font_path_roman,
                                                     fontsize=self.PlotSettings.font_size_chord_types,
                                                     border=self.PlotSettings.border_text_chords,
                                                     zorder=self.PlotSettings.z_order_text_melody,
                                                     color=self.PlotSettings.color_text_chords)

            self.CanvasManager.add_text(page, x_pos_last, y_pos_secondary_chord, '/' + chord.secondary_numeral_key,
                                        font_path=self.PlotSettings.font_path_roman,
                                        fontsize=self.PlotSettings.font_size_chords,
                                        border=self.PlotSettings.border_text_chords,
                                        zorder=self.PlotSettings.z_order_text_melody,
                                        color=self.PlotSettings.color_text_chords)



