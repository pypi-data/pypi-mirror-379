class Barline:
    def __init__(self, offset, location, type):
        self.offset = offset
        self.location = location  # left, right
        self.type = type  # final, repeat, double


class MeasureDivider:
    def __init__(self, offset, overlaps_with_right_barline, overlaps_with_left_barline):
        self.offset = offset
        self.overlaps_with_right_barline = overlaps_with_right_barline
        self.overlaps_with_left_barline = overlaps_with_left_barline


class MeasureSubdivider:
    def __init__(self, offset, type, indicates_time_signature=False):
        self.offset = offset
        self.type = type  # 'quarter', 'sixteenth'
        self.indicates_time_signature = indicates_time_signature

class RepeatBracket:
    def __init__(self, number, offset_start, offset_end):
        self.number = number
        self.offset_start = offset_start
        self.offset_end = offset_end

class KeyOrigin:
    def __init__(self, origin, offset):
        self.origin = origin
        self.offset = offset

class RepeatExpression:

    def __init__(self, type, offset, at_start_of_measure):
        self.type = type
        self.offset = offset
        self.at_start_of_measure = at_start_of_measure