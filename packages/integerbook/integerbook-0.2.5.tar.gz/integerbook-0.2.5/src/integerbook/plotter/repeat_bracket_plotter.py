from integerbook.plotter.base_plotter import BasePlotter

class RepeatBracketPlotter(BasePlotter):

    def plot_repeat_brackets(self):
        for repeat_bracket in self.sheet.repeat_brackets:
            self._plot_repeat_bracket(repeat_bracket)

    def _plot_repeat_bracket(self, repeat_bracket):
        offset_start = repeat_bracket.offset_start
        line_start, x_pos = self.XLocationFinder.get_line_and_x_pos(offset_start)
        x_pos -= self.PlotSettings.line_width_normal / 2
        line_end, _ = self.XLocationFinder.get_line_and_x_pos(repeat_bracket.offset_end)
        line = line_start
        while line <= line_end:
            offset_end = min(repeat_bracket.offset_end, self.XLocationFinder.get_offset_end_line(line))
            h_length = offset_end - offset_start
            x_length = self.XLocationFinder.get_x_length(h_length)
            x_length += self.PlotSettings.line_width_normal
            x_length = self.shorten_x_length_when_next_bracket_is_on_same_line(line, line_end, offset_end, x_length)

            y_pos = self.YLocationFinder.get_y_pos_repeat_bracket(line)
            page = self.YLocationFinder.get_page(line)
            vertical_line_width = self.PlotSettings.line_width_normal * self.CanvasManager.xy_ratio

            length_space = self._plot_dotted_h_line(page, x_pos, y_pos, x_length, vertical_line_width)

            if line == line_start:
                self._plot_dotted_v_line(page, x_pos, y_pos + vertical_line_width, self.PlotSettings.line_width_normal,
                                         self.PlotSettings.barline_extension, length_space * self.CanvasManager.xy_ratio)
                self.CanvasManager.add_text(page, x_pos + 2.5 * self.PlotSettings.line_width_normal,
                                            y_pos - self.PlotSettings.barline_extension, repeat_bracket.number + '.',
                                            font_path=self.PlotSettings.font_path,
                                            fontsize=self.PlotSettings.font_size_notes - 1)

            offset_start = offset_end
            line, x_pos = self.XLocationFinder.get_line_and_x_pos(offset_start)
            if line == line_end:
                break

    def shorten_x_length_when_next_bracket_is_on_same_line(self, line, line_end, offset_end, x_length):
        if line == line_end and not self.XLocationFinder.is_at_end_of_line(offset_end):
            x_length -= 5 * self.PlotSettings.line_width_normal
        return x_length

    def _plot_dotted_h_line(self, page, x, y, width, line_width):
        width_dot = line_width * self.CanvasManager.height_a4 / self.CanvasManager.width_a4
        num_dots, length_space = self._get_num_dots_and_length_space(width, width_dot, preferred_spacing_factor=1.5)
        for i in range(num_dots):
            self.create_barline_rectangle(page, x, y, width_dot, line_width)
            x += width_dot + length_space
        return length_space

    def _plot_dotted_v_line(self, page, x, y_top, line_width, height, length_space):
        "note that we are specifying the top of the line, and draw downwards"
        height_dot = line_width * self.CanvasManager.xy_ratio
        num_dots = int(height / (height_dot + length_space)) + 1
        for i in range(num_dots):
            self.create_barline_rectangle(page, x, y_top - height_dot, line_width, height_dot)
            y_top -= height_dot + length_space


    def _get_num_dots_and_length_space(self, total_length, length_dot, preferred_spacing_factor):
        num_dots = round((total_length - length_dot) / (length_dot * (1 + preferred_spacing_factor))) + 1
        length_space = (total_length - num_dots * length_dot) / (num_dots - 1)
        return num_dots, length_space
