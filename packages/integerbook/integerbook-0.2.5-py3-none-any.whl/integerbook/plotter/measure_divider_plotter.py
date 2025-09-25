from integerbook.plotter.base_plotter import BasePlotter


class MeasureDividerPlotter(BasePlotter):

    def plot_measure_dividers(self):
        for measure_divider in self.sheet.measure_dividers:

            line, x_pos = self.XLocationFinder.get_line_and_x_pos(measure_divider.offset, is_maybe_at_end_of_line=False)
            measure_divider_is_on_two_lines = self.XLocationFinder.is_at_end_of_line(measure_divider.offset)
            y_pos, height = self.YLocationFinder.get_y_pos_and_height_bar_v_line(line, extension=True)
            page = self.YLocationFinder.get_page(line)

            line_width = self.PlotSettings.line_width_normal
            x_pos -= line_width / 2

            if self._measure_divider_does_not_overlap(measure_divider, measure_divider_is_on_two_lines, is_on_first_line=False):
                self.create_barline_rectangle(page, x_pos, y_pos, line_width, height)

            # plot measure divider at end of line
            if measure_divider_is_on_two_lines:
                line_2, x_pos_2 = self.XLocationFinder.get_line_and_x_pos(measure_divider.offset,
                                                                      is_maybe_at_end_of_line=True)
                y_pos, height = self.YLocationFinder.get_y_pos_and_height_bar_v_line(line_2, extension=True)
                page = self.YLocationFinder.get_page(line_2)

                x_pos_2 -= line_width / 2
                if self._measure_divider_does_not_overlap(measure_divider, measure_divider_is_on_two_lines, is_on_first_line=True):
                    self.create_barline_rectangle(page, x_pos_2, y_pos, line_width, height)

    def _measure_divider_does_not_overlap(self, measure_divider, is_on_two_lines, is_on_first_line=True):
        if not is_on_two_lines:
            return (not measure_divider.overlaps_with_right_barline and not measure_divider.overlaps_with_left_barline)
        elif is_on_two_lines and is_on_first_line:
            return not measure_divider.overlaps_with_right_barline
        else:  # is on second line
            return not measure_divider.overlaps_with_left_barline

    def plot_measure_subdividers(self):
        for measure_subdivider in self.sheet.measure_subdividers:
            line, x_pos = self.XLocationFinder.get_line_and_x_pos(measure_subdivider.offset)
            y_pos, height = self.YLocationFinder.get_y_pos_and_height_bar_v_line(line, extension=False)
            page = self.YLocationFinder.get_page(line)

            if self.PlotSettings.subdivision == 'measure':
                if measure_subdivider.indicates_time_signature:
                    line_width = self.PlotSettings.line_width_thin
                else:  # divider is indicating time signature
                    continue
            elif self.PlotSettings.subdivision == 'quarter':
                if measure_subdivider.type == 'quarter':
                    line_width = self.PlotSettings.line_width_thin
                else:  # type is sixteenth
                    continue
            else:  # subdivision = sixteenth
                if measure_subdivider.type == 'quarter':
                    line_width = self.PlotSettings.line_width_normal
                else:  # type = sixteenth
                    line_width = self.PlotSettings.line_width_thin

            x_pos -= line_width / 2

            self.create_barline_rectangle(page, x_pos, y_pos, line_width, height)


