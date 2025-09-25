from integerbook.plotter.base_plotter import BasePlotter

class KeyOriginPlotter(BasePlotter):
    def plot_key_origins(self):

        for idx, key_origin in enumerate(self.sheet.key_origins):

            if idx == 0 and not self.PlotSettings.scroll:
                self._plot_key_origin(key_origin, 0, self.XLocationFinder.get_x_margin_metadata(), self.PlotSettings.y_pos_arranger)
                continue

            line, x_pos = self.XLocationFinder.get_line_and_x_pos(key_origin.offset)
            page = self.YLocationFinder.get_page(line)
            y_pos_line_base = self.YLocationFinder.get_y_pos_line_base(line)
            y_pos = y_pos_line_base + self.YLocationFinder.y_max

            x_pos += self.PlotSettings.x_shift_chords
            if self._measure_has_repeat_expression_at_start(key_origin.offset):
                x_pos += self._get_shift_repeat_expression()

            self._plot_key_origin(key_origin, page, x_pos, y_pos)

    def _plot_key_origin(self, key_origin, page, x_pos, y_pos):
        self.CanvasManager.add_text(page, x_pos, y_pos, f"1 = {key_origin.origin}",
                                    font_path=self.PlotSettings.font_path,
                                    fontsize=self.PlotSettings.font_size_metadata, ha='left', va='baseline',
                                    border=self.PlotSettings.border_text_metadata)

    def _measure_has_repeat_expression_at_start(self, offset):
        for repeat_expression in self.sheet.repeat_expressions:
            if repeat_expression.offset == offset and repeat_expression.at_start_of_measure:
                return True

    def _get_shift_repeat_expression(self):
        return self.PlotSettings.cap_height_notes * self.CanvasManager.xy_ratio * 0.9 + self.PlotSettings.x_shift_chords