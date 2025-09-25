from integerbook.plotter.note_plotter import NotePlotter

class GlissandoPlotter(NotePlotter):
    def __init__(self, sheet, settings, canvas_manager, x_location_finder, y_location_finder):
        super().__init__(sheet, settings, canvas_manager, x_location_finder, y_location_finder)  # Pass canvas

    def plot_glissandos(self):

        if self.PlotSettings.plot_melody:
            for glissando in self.sheet.glissandos:
                self.plot_parallelogram(glissando)
                self.plot_symbol(glissando)

    def plot_parallelogram(self, glissando):
        x, y, page = self._get_pos_note(glissando.offset, glissando.position)

        shape, x, x_length = self._get_shape_x_pos_x_length(glissando, x)

        y_difference = self.YLocationFinder.get_y_length(glissando.position_difference)

        if glissando.start:
            left_bottom = [x, y]
            left_top = [x, y + self.PlotSettings.bar_space]
            right_bottom = [x + x_length, y + y_difference]
            right_top = [x + x_length, y + y_difference + self.PlotSettings.bar_space]
        else:
            left_bottom = [x, y - y_difference]
            left_top = [x, y - y_difference + self.PlotSettings.bar_space]
            right_bottom = [x + x_length, y]
            right_top = [x + x_length, y + self.PlotSettings.bar_space]

        self.CanvasManager.create_parallelogram(
            page_index=page,
            left_bottom=left_bottom,
            left_top=left_top,
            right_bottom=right_bottom,
            right_top=right_top,
            alpha=self._get_alpha(glissando),
            facecolor=self._get_facecolor(glissando),
            hatch=self._get_hatch(glissando),
            shape=shape,
            zorder=self.PlotSettings.z_order_rectangle_melody
        )

    def plot_symbol(self, glissando):
        x, y, page = self._get_pos_note(glissando.offset, glissando.position)
        x_length = self.get_x_length(glissando.duration)

        if glissando.start:
            x += self.PlotSettings.x_shift_number_note
            y += self._get_y_shift_number() + self._get_y_shift_number_glissando(glissando)
        else:
            x += x_length - self.PlotSettings.x_shift_number_note
            y += self._get_y_shift_number() - self._get_y_shift_number_glissando(glissando)

        self.CanvasManager.add_text(page, x, y, f'{glissando.accidental}{glissando.number}',
                                    font_path=self.PlotSettings.font_path, fontsize=self.PlotSettings.font_size_notes,
                                    border=self.PlotSettings.border_text_notes, horizontalalignment='center',
                                    verticalalignment='baseline', zorder=self.PlotSettings.z_order_text_melody)

    def _get_shape_x_pos_x_length(self, glissando, x_pos):
        x_length = self.get_x_length(glissando.duration)

        if glissando.start:
            shape = 'left_rounded'
            if not glissando.thick_barline_at_start:
                x_pos += self.PlotSettings.x_margin_note
                x_length -= self.PlotSettings.x_margin_note
            else:
                x_pos += self.PlotSettings.x_margin_note_thick_barline
                x_length -= self.PlotSettings.x_margin_note_thick_barline

        else:
            shape = 'right_rounded'
            if not glissando.thick_barline_at_end:
                x_length -= self.PlotSettings.x_margin_note
            else:
                x_length -= self.PlotSettings.x_margin_note_thick_barline

        return shape, x_pos, x_length

    def _get_y_shift_number_glissando(self, glissando):
        x_length = self.get_x_length(glissando.duration)

        y_difference = self.YLocationFinder.get_y_length(glissando.position_difference)

        return y_difference / x_length * self.PlotSettings.x_shift_number_note