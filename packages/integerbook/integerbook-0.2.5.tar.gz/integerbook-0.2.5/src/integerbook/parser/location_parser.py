import music21

from integerbook.parser.base_parser import BaseParser


class LocationParser(BaseParser):
    def __init__(self, stream_obj, settings):
        super().__init__(stream_obj, settings)

    def parse(self):

        if not self.ParseSettings.scroll:
            offsets_start_line, h_shifts_line = self._parse_locations_for_a4()

        else:
            offsets_start_line = [0]
            h_shifts_line = [0]

        return offsets_start_line, h_shifts_line

    def _parse_locations_for_a4(self):
        offsets_start_line = []
        h_shifts_line = []

        length_first_measure = self.stream_obj.measure(1).quarterLength
        offset_line_max = length_first_measure * self.ParseSettings.measures_per_line

        measures = [measure for measure in self.stream_obj[music21.stream.Measure]]
        has_pickup_measure = measures[0].number == 0
        first_coda = True
        for measure in self.stream_obj.recurse().getElementsByClass(music21.stream.Measure):

            # initializing first line
            if measure.number == 0:  # pickup measure
                offsets_start_line.append(measure.offset)
                h_shifts_line.append(-measure.quarterLength)

            elif measure.number == 1 and not has_pickup_measure:
                offsets_start_line.append(measure.offset)
                h_shifts_line.append(0)

            # special conditions for starting new line

            # start new line when new section of song starts
            elif measure.flatten().getElementsByClass(
                    music21.expressions.RehearsalMark).first() and not measure.number == 1:
                offsets_start_line.append(measure.offset)
                h_shifts_line.append(0)

            # start new line for volta > 1 (RepeatBracket)
            elif measure.getSpannerSites():
                spanner = measure.getSpannerSites()[0]
                if type(spanner) == music21.spanner.RepeatBracket:
                    if int(spanner.number[0]) > 1:
                        if spanner.isFirst(measure):
                            offsets_start_line.append(measure.offset)
                            h_shifts_line.append(x_pos_spanner)

            # start new line for second volta
            elif self._has_coda(measure) and not first_coda:
                offsets_start_line.append(measure.offset)
                h_shifts_line.append(x_pos_coda)

            # standard condition for starting new line:
            if measure.offset + measure.quarterLength - offsets_start_line[-1] + h_shifts_line[-1] > offset_line_max:
                offsets_start_line.append(measure.offset)
                h_shifts_line.append(0)

            # save location of repetition signs

            # save position of first volta
            if measure.getSpannerSites():
                spanner = measure.getSpannerSites()[0]
                if type(spanner) == music21.spanner.RepeatBracket:
                    if spanner.number[0] == '1':
                        if spanner.isFirst(measure):
                            x_pos_spanner = measure.offset - offsets_start_line[-1] + h_shifts_line[-1]

            # save position of first coda
            if self._has_coda(measure) and first_coda:
                x_pos_coda = measure.offset + self._offset_coda(measure) - offsets_start_line[-1] + h_shifts_line[-1]
                first_coda = False

            # ? will not work if length of measure exceeds offset_line_max, then will be counted in first and last (el)if statement

        return offsets_start_line, h_shifts_line

    @staticmethod
    def _has_coda(measure):
        for el in measure:
            if type(el) == music21.repeat.Coda:
                return True
        return False

    @staticmethod
    def _offset_coda(measure):
        for el in measure:
            if type(el) == music21.repeat.Coda:
                return el.offset

    
