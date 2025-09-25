
class XLocationFinder:
    def __init__(self, sheet, settings):  # Accept canvas
        self.sheet = sheet
        self.PlotSettings = settings

        self.offsets_end_line = self.sheet.offsets_start_line[1:] + [self.sheet.offset_length]

        self.max_h_pos_a4 = self._get_max_h_pos_a4()
        self.minimal_pickup_measure_h_space = self.max_h_pos_a4 * self.PlotSettings.minimal_pickup_measure_space_fraction
        self.pickup_measure_h_space = max(self.minimal_pickup_measure_h_space, self._get_pick_up_measure_length())

        self.x_length_per_h_length = (1 - 2 * self.PlotSettings.width_margin_line) / \
                                     (self.max_h_pos_a4 + 2 * self.pickup_measure_h_space)
        self.x_start_line = self.PlotSettings.width_margin_line + self.pickup_measure_h_space * self.x_length_per_h_length


    def get_line_and_x_pos(self, offset, is_maybe_at_end_of_line=False):
        line, h_pos_within_line = self._get_line_and_h_pos_within_line(offset, is_maybe_at_end_of_line)
        return line, self._get_x_pos(h_pos_within_line)

    def get_x_length(self, h_length):
        return h_length * self.x_length_per_h_length

    def get_offset_end_line(self, line):
        return self.offsets_end_line[line]

    def is_at_end_of_line(self, offset):
        return offset in self.offsets_end_line

    def get_x_width_canvas(self):
        if not self.PlotSettings.scroll:
            return 1
        else:
            return self.x_start_line + self.sheet.offset_length * self.x_length_per_h_length + self.x_start_line

    def get_x_margin_metadata(self):
        return self.get_x_length(self.minimal_pickup_measure_h_space) + self.PlotSettings.width_margin_line

    def _get_max_h_pos_a4(self):
        if not self.PlotSettings.scroll:     
            h_lengths_line = [offset_end_line - offset_start_line for offset_start_line, offset_end_line in
                              zip(self.sheet.offsets_start_line, self.offsets_end_line)]

            num_lines = len(self.sheet.offsets_start_line)
            max_h_pos = 0
            for line_idx in range(num_lines):
                max_h_pos_line = h_lengths_line[line_idx] + self.sheet.h_shifts_line[line_idx]
                max_h_pos = max(max_h_pos, max_h_pos_line)
            return max_h_pos
        else:
            return self.PlotSettings.h_length_per_a4_width

    def _get_pick_up_measure_length(self):
        if not self.PlotSettings.scroll:
            return self.sheet.pickup_measure_length
        else:
            return 0


    def _get_line_and_h_pos_within_line(self, offset, is_maybe_at_end_of_line=False):
        line = -1
        for offset_start_line in self.sheet.offsets_start_line:
            if offset >= offset_start_line if not is_maybe_at_end_of_line else offset > offset_start_line:
                line += 1
            else:
                break
        h_pos_within_line = offset - self.sheet.offsets_start_line[line] + self.sheet.h_shifts_line[line]
        return line, h_pos_within_line


    def _get_x_pos(self, h_pos_within_line):
        return self.x_start_line + h_pos_within_line * self.x_length_per_h_length


