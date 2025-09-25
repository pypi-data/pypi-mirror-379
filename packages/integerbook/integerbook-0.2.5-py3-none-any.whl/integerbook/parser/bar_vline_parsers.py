import music21

from integerbook.parser.base_parser import BaseParser
from integerbook.bar import Barline, MeasureDivider, MeasureSubdivider

class BarlineParser(BaseParser):
    def parse_barlines(self):
        barlines = []
        for measure in self.stream_obj[music21.stream.Measure]:
            for m21_barline in measure[music21.bar.Barline]:
                if m21_barline.type != 'regular':
                    barline = Barline(offset=self._get_offset(m21_barline), location=m21_barline.location,
                                      type=self._get_type(m21_barline))
                    barlines.append(barline)
        return barlines

    @staticmethod
    def _get_type(m21_barline):
        if type(m21_barline) is music21.bar.Repeat:
            return 'repeat'
        else:
            return m21_barline.type


class MeasureDividerParser(BaseParser):
    def parse_measure_dividers(self):

        measure_dividers = []
        measures = self.stream_obj[music21.stream.Measure]

        self._append_first_measure_divider(measure_dividers, measures)
        self._append_middle_measure_dividers(measure_dividers, measures)
        self._append_last_measure_divider(measure_dividers, measures)

        return measure_dividers

    def _append_first_measure_divider(self, measure_dividers, measures):
        first_measure = measures[0]
        if not self._is_pickup_measure(first_measure):
            measure_divider = MeasureDivider(
                offset=self._get_offset(first_measure),
                overlaps_with_right_barline=False,
                overlaps_with_left_barline=self._has_left_barline(first_measure)
            )
            measure_dividers.append(measure_divider)
    def _append_middle_measure_dividers(self, measure_dividers, measures):
        for measure, measure_next in zip(measures, measures[1:]):
            measure_divider = MeasureDivider(
                offset=self._get_offset(measure_next),
                overlaps_with_right_barline=self._has_right_barline(measure),
                overlaps_with_left_barline=self._has_left_barline(measure_next)
            )
            measure_dividers.append(measure_divider)

    def _append_last_measure_divider(self, measure_dividers, measures):
        last_measure = measures[-1]
        measure_divider = MeasureDivider(
            offset=self._get_offset(last_measure) + last_measure.quarterLength,
            overlaps_with_right_barline=self._has_right_barline(last_measure),
            overlaps_with_left_barline=False
        )
        measure_dividers.append(measure_divider)

    def _has_left_barline(self, measure):
        return self._is_not_regular_barline(measure.leftBarline)

    def _has_right_barline(self, measure):
        return self._is_not_regular_barline(measure.rightBarline)

    @staticmethod
    def _is_not_regular_barline(m21_barline):
        if m21_barline:
            if m21_barline.type != 'regular':
                return True
        else:
            return False


class MeasureSubdividerParser(BaseParser):

    def parse_measure_subdividers(self):
        measure_subdividers = []

        for measure in self.stream_obj[music21.stream.Measure]:

            self._parse_quarter_subdividers(measure, measure_subdividers)
            self._parse_16th_subdividers(measure, measure_subdividers)

        return measure_subdividers

    def _parse_quarter_subdividers(self, measure, measure_subdividers):
        for local_offset in range(1, int(measure.quarterLength)):
            measure_subdivider = MeasureSubdivider(
                offset=self._get_offset(measure) + local_offset,
                type='quarter',
                indicates_time_signature=self._has_time_signature(measure)
            )
            measure_subdividers.append(measure_subdivider)

    def _parse_16th_subdividers(self, measure, measure_subdividers):
        for local_offset in range(0, int(measure.quarterLength)):
            for i in range(1,4):
                measure_subdivider = MeasureSubdivider(
                    offset=self._get_offset(measure) + local_offset + i * 0.25,
                    type='sixteenth',
                )
                measure_subdividers.append(measure_subdivider)


    @staticmethod
    def _has_time_signature(measure):
        if measure.number == 0 or measure.number == 1:
            return True
        else:
            return len(measure[music21.meter.TimeSignature]) > 0









