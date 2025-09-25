from integerbook.plotter.note_plotter import NotePlotter

class StringArticulationPlotter(NotePlotter):

    def plot_string_articulations(self):
        for string_articulation in self.sheet.string_articulations:
            self._plot_string_articulation(string_articulation)

    def _plot_string_articulation(self, string_articulation):
        line, x_pos_middle = self.XLocationFinder.get_line_and_x_pos(string_articulation.offset)
        page = self.YLocationFinder.get_page(line)

        y_pos_start = self.YLocationFinder.get_y_pos_note(line, string_articulation.start_position)
        y_pos_end = self.YLocationFinder.get_y_pos_note(line, string_articulation.end_position)

        y_pos_low = min(y_pos_start, y_pos_end)
        y_pos_high = max(y_pos_start, y_pos_end) + self.PlotSettings.bar_space

        y_length_difference = y_pos_high - y_pos_low
        y_length_letter_space = self.PlotSettings.cap_height_string_articulation * 1.27

        y_length_bar = (y_length_difference - y_length_letter_space) / 2

        x_pos_start = x_pos_middle - self.PlotSettings.x_margin_note
        width = self.PlotSettings.x_margin_note * 2

        self.CanvasManager.create_straight_rectangle(page, x_pos_start, y_pos_low, width, y_length_bar, zorder=self.PlotSettings.z_order_rectangle_melody)
        self.CanvasManager.create_straight_rectangle(page, x_pos_start, y_pos_high - y_length_bar, width, y_length_bar,
                                                     zorder=self.PlotSettings.z_order_rectangle_melody)

        y_pos_middle = (y_pos_high + y_pos_low) / 2
        y_pos_letter = y_pos_middle - self.PlotSettings.cap_height_string_articulation / 2
        text = string_articulation.type[0].capitalize()

        self.CanvasManager.add_text(page, x_pos_middle, y_pos_letter, text,
                                    fontsize=self.PlotSettings.font_size_string_articulations, ha='center',
                                    va='baseline', border=self.PlotSettings.border_text_notes,
                                    font=self.PlotSettings.font_string_articulations,
                                    zorder=self.PlotSettings.z_order_text_melody)
        self.CanvasManager.create_circle(page, x_pos_middle, y_pos_middle, y_length_letter_space,
                                                    facecolor=self.PlotSettings.color_background,
                                         zorder=self.PlotSettings.z_order_rectangle_melody)










