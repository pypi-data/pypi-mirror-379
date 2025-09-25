from integerbook.plotter.base_plotter import BasePlotter

class NotePlotter(BasePlotter):

    def plot_notes(self):

        for note in self.sheet.notes:
            if self._note_should_be_plotted(note):
                self.plot_rectangle(note)
                if not self._is_tied_at_start(note):
                    self.plot_symbol(note)

    def _note_should_be_plotted(self, note):
        if note.is_glissando or note.is_grace_note:
            return False
        if note.is_chord_note:
            return self.PlotSettings.plot_chord_notes
        else:
            return self.PlotSettings.plot_melody


    def plot_rectangle(self, note):
        x, y, page = self._get_pos_note(note.offset, note.position)

        shape, x, x_length = self._get_shape_x_pos_x_length(note, x)

        self.CanvasManager.create_rectangle(
            page,
            x=x,
            y=y,
            width=x_length,
            height=self.PlotSettings.bar_space,  # Fixed height for notes
            alpha=self._get_alpha(note),
            facecolor=self._get_facecolor(note),
            hatch=self._get_hatch(note),
            shape=shape,
            zorder=self.PlotSettings.z_order_rectangle_melody
        )

    def plot_symbol(self, note):

        symbol = f'{note.accidental}{note.number}'
        x, y, page = self._get_pos_note(note.offset, note.position)

        x_length_text = self.CanvasManager.get_x_length_text(symbol, font_size=self.PlotSettings.font_size_notes,
                                                             font_path=self.PlotSettings.font_path)
        x_length_rectangle = self.get_x_length(note.duration)

        if not self._symbol_is_wider_than_rectangle(note, x_length_rectangle, x_length_text):
            x += self.PlotSettings.x_shift_number_note
        else:
            x += 0.5 * x_length_rectangle - 0.5 * x_length_text

        y = y + self._get_y_shift_number()

        self.CanvasManager.add_text(page, x, y, symbol, font_path=self.PlotSettings.font_path,
                                    fontsize=self.PlotSettings.font_size_notes, ha='left',
                                    border=self.PlotSettings.border_text_notes, color=self._get_text_color(note),
                                    zorder=self._get_z_order_text(note))

    def _symbol_is_wider_than_rectangle(self, note, x_length_rectangle, x_length_text):
        return x_length_text + 2 * self.PlotSettings.x_shift_number_note > x_length_rectangle and not note.tie

    def _get_pos_note(self, offset, pitch_position):
        line, x_pos = self.XLocationFinder.get_line_and_x_pos(offset)
        y_pos = self.YLocationFinder.get_y_pos_note(line, pitch_position)
        page = self.YLocationFinder.get_page(line)
        return x_pos, y_pos, page

    def _get_y_shift_number(self):
        return (self.PlotSettings.bar_space - self.PlotSettings.cap_height_notes) / 2

    @staticmethod
    def _is_tied_at_start(note):
        return note.tie == 'continue' or note.tie == 'stop'
    def _get_shape_x_pos_x_length(self, note, x_pos):
        x_length = self.get_x_length(note.duration)

        if not note.tie and not note.slur:
            shape = 'rounded'
            if not note.thick_barline_at_start:
                x_pos += self.PlotSettings.x_margin_note
                x_length -= self.PlotSettings.x_margin_note
            else:
                x_pos += self.PlotSettings.x_margin_note_thick_barline
                x_length -= self.PlotSettings.x_margin_note_thick_barline
            if not note.thick_barline_at_end:
                x_length -= self.PlotSettings.x_margin_note
            else:
                x_length -= self.PlotSettings.x_margin_note_thick_barline

        elif note.tie == 'start' or note.slur == 'start':
            shape = 'left_rounded'
            if not note.thick_barline_at_start:
                x_pos += self.PlotSettings.x_margin_note
                x_length -= self.PlotSettings.x_margin_note
            else:
                x_pos += self.PlotSettings.x_margin_note_thick_barline
                x_length -= self.PlotSettings.x_margin_note_thick_barline

        elif note.tie == 'continue' or note.slur == 'continue':
            shape = 'straight'

        else:  # note.tie == 'end' or note.slur == 'end'
            shape = 'right_rounded'
            if not note.thick_barline_at_end:
                x_length -= self.PlotSettings.x_margin_note
            else:
                x_length -= self.PlotSettings.x_margin_note_thick_barline

        if note.is_vibrato:
            shape = 'squiggly'

        return shape, x_pos, x_length

    def _get_alpha(self, note):
        if note.is_chord_note:
            return self.PlotSettings.alpha_chord_notes
        elif note.is_ghost_note:
            return self.PlotSettings.alpha_ghost_notes
        else:
            return self.PlotSettings.alpha_melody

    def _get_facecolor(self, note):
        if note.is_chord_note:
            return self.PlotSettings.facecolor_chord_notes
        elif note.is_ghost_note:
            return self.PlotSettings.facecolor_ghost_notes
        elif self.PlotSettings.note_coloring == "circle_of_fifths":
            return self._colorwheel(note.circle_of_fifths_idx)
        elif self.PlotSettings.note_coloring == "voices" and note.voice_number == 1:
            return self.PlotSettings.facecolor_first_voice
        elif self.PlotSettings.note_coloring == "voices" and note.voice_number == 2:
            return self.PlotSettings.facecolor_second_voice

    def _get_z_order_rectangle(self, note):
        if not note.is_chord_note:
            return self.PlotSettings.z_order_rectangle_melody
        else:
            return self.PlotSettings.z_order_rectangle_chord_notes

    def _get_z_order_text(self, note):
        if not note.is_chord_note:
            return self.PlotSettings.z_order_text_melody
        else:
            return self.PlotSettings.z_order_text_chord_notes
    def _get_text_color(self, note):
        if note.is_chord_note:
            return self.PlotSettings.color_text_chord_notes
        else:
            return self.PlotSettings.color_text_notes

    def _get_hatch(self, note):
        if note.is_ghost_note:
            return 'xxxxx'
        else:
            return None

    def _colorwheel(self, circle_of_fifth_idx):
        rgbs = [(126/255, 127/255, 234/255, 1.0),
                (181/255, 132/255, 231/255, 1.0),
                (234/255, 128/255, 235/255, 1.0),
                (241/255, 128/255, 188/255, 1.0),
                (239/255, 122/255, 125/255, 1.0),
                (204/255, 159/255, 111/255, 1.0),
                (197/255, 198/255, 110/255, 1.0),
                (162/255, 203/255, 111/255, 1.0),
                (125/255, 234/255, 118/255, 1.0),
                (130/255, 240/255, 191/255, 1.0),
                (127/255, 240/255, 237/255, 1.0),
                (140/255, 184/255, 234/255, 1.0)]

        rgb = rgbs[circle_of_fifth_idx]

        return rgb