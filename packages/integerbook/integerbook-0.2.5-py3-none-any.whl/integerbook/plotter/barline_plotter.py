from integerbook.plotter.base_plotter import BasePlotter

class BarlinePlotter(BasePlotter):

    def plot_barlines(self):
        for barline in self.sheet.barlines:
            if barline.type == 'final':
                self._plot_final_barline(barline)
            if barline.type == 'repeat':
                self._plot_repeat_barline(barline)
            if barline.type == 'double':
                self._plot_double_barline(barline)

    def _plot_double_barline(self, barline):
        if barline.location == 'right':
            is_maybe_at_end_of_line = True
            x_shift_second_barline = -0.004
        else:
            is_maybe_at_end_of_line = False
            x_shift_second_barline = 0.02
        line, x_pos = self.XLocationFinder.get_line_and_x_pos(barline.offset, is_maybe_at_end_of_line)
        y_pos, height = self.YLocationFinder.get_y_pos_and_height_bar_v_line(line, extension=True)
        page = self.YLocationFinder.get_page(line)

        line_width = self.PlotSettings.line_width_normal
        x_pos -= line_width / 2

        self.create_barline_rectangle(page, x_pos, y_pos, line_width, height)

        x_pos += x_shift_second_barline

        self.create_barline_rectangle(page, x_pos, y_pos, line_width, height)

    def _plot_final_barline(self, barline):
        height, page, width, x_pos, y = self._get_positions_thick_barline(barline)

        self.create_barline_rectangle(
            page=page,
            x=x_pos,
            y=y,
            width=width,
            height=height
        )

    def _plot_repeat_barline(self, barline):
        total_height, page, width, x_pos, y = self._get_positions_thick_barline(barline)

        y_space_dots = 0.033

        height = total_height / 2 - y_space_dots / 2

        self.create_barline_rectangle(
            page=page,
            x=x_pos,
            y=y,
            width=width,
            height=height
        )

        self.create_barline_rectangle(
            page=page,
            x=x_pos,
            y=y + height + y_space_dots,
            width=width,
            height=height
        )

        x_pos_dots = x_pos + 0.5 * width
        y_pos_middle = y + 0.5 * total_height
        distance = 0.007

        for i in [-1, 1]:
            self.CanvasManager.create_circle_x_diameter(page, x_pos_dots, y_pos_middle + i * distance,
                                                        x_diameter=self.PlotSettings.line_width_thick,
                                                        facecolor=self.PlotSettings.color_barlines)

        # plot hbars
        width_h_bar = 0.008
        if barline.location == 'left':
            x_pos_h_bar = x_pos
        else:
            x_pos_h_bar = x_pos - (width_h_bar - self.PlotSettings.line_width_thick)

        for i in [0, 1]:
            self.create_barline_rectangle(
                page=page,
                x=x_pos_h_bar,
                y=y + i * (total_height - self.PlotSettings.line_width_thick),
                width=width_h_bar,
                height=self.PlotSettings.line_width_thick
            )


    def _get_positions_thick_barline(self, barline):
        if barline.location == 'right':
            is_maybe_at_end_of_line = True
            x_shift = - self.PlotSettings.line_width_thick + 0.5 * self.PlotSettings.line_width_normal
        else:
            is_maybe_at_end_of_line = False
            x_shift = - 0.5 * self.PlotSettings.line_width_normal
        line, x_pos = self.XLocationFinder.get_line_and_x_pos(barline.offset, is_maybe_at_end_of_line)
        x_pos += x_shift
        y, height = self.YLocationFinder.get_y_pos_and_height_bar_v_line(line, extension=True)
        page = self.YLocationFinder.get_page(line)
        width = self.PlotSettings.line_width_thick

        return height, page, width, x_pos, y

