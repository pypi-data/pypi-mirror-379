from integerbook.plotter.base_plotter import BasePlotter


class RepeatExpressionPlotter(BasePlotter):

    def plot_repeat_expressions(self):
        for repeat_expression in self.sheet.repeat_expressions:
            line, x_pos = self.XLocationFinder.get_line_and_x_pos(repeat_expression.offset,
                                                                  is_maybe_at_end_of_line=not(repeat_expression.at_start_of_measure))
            page = self.YLocationFinder.get_page(line)
            y_pos_line_base = self.YLocationFinder.get_y_pos_line_base(line)
            y_pos = y_pos_line_base + self.YLocationFinder.y_max

            if repeat_expression.at_start_of_measure:
                x_pos += self.PlotSettings.x_shift_chords
            else:
                x_pos -= self.PlotSettings.x_shift_chords

            print(repeat_expression.at_start_of_measure)

            if repeat_expression.type == 'segno':
                self.CanvasManager.create_segno(page, x_pos, y_pos, self.PlotSettings.cap_height_notes,
                                                self.PlotSettings.color_text_notes,
                                                repeat_expression.at_start_of_measure)

            elif repeat_expression.type == 'coda':
                self.CanvasManager.create_coda(page, x_pos, y_pos, self.PlotSettings.cap_height_notes,
                                               self.PlotSettings.color_text_notes,
                                               repeat_expression.at_start_of_measure)


            else:
                if repeat_expression.at_start_of_measure:
                    ha='left'
                else:
                    ha='right'
                self.CanvasManager.add_text(page, x_pos, y_pos, repeat_expression.type,
                                            fontsize=self.PlotSettings.font_size_notes, ha=ha,
                                            color=self.PlotSettings.color_barlines)