from integerbook.plotter.note_plotter import NotePlotter

class GraceNotePlotter(NotePlotter):
    def __init__(self, sheet, settings, canvas_manager, x_location_finder, y_location_finder):
        super().__init__(sheet, settings, canvas_manager, x_location_finder, y_location_finder)

    def plot_grace_notes(self):

        if self.PlotSettings.plot_melody:
            for grace_note in self.sheet.grace_notes:
               self._plot_grace_note(grace_note)

    def _plot_grace_note(self, grace_note):
        x, y, page = self._get_pos_note(grace_note.offset, grace_note.position)

        num_shifts = grace_note.length_beam - grace_note.position_in_beam
        x_shift_grace_notes = num_shifts * self.PlotSettings.x_shift_grace_notes

        self.CanvasManager.add_text(page, x + self.PlotSettings.x_shift_number_note - x_shift_grace_notes,
                                    y + self._get_y_shift_number(), f'{grace_note.accidental}{grace_note.number}',
                                    font_path=self.PlotSettings.font_path,
                                    fontsize=self.PlotSettings.font_size_grace_notes,
                                    border=self.PlotSettings.border_text_notes, horizontalalignment='left',
                                    verticalalignment='baseline', color=self.PlotSettings.color_text_grace_notes,
                                    zorder=self.PlotSettings.z_order_text_melody)

