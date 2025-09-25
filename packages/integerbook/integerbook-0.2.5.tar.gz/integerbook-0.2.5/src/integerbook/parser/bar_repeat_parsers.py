import music21

from integerbook.parser.base_parser import BaseParser
from integerbook.bar import RepeatBracket

class RepeatBracketParser(BaseParser):

    def parse_repeat_brackets(self):
        repeat_brackets = []
        for m21_repeat_bracket in self.stream_obj[music21.spanner.RepeatBracket]:
            first_measure = m21_repeat_bracket.getSpannedElements()[0]
            last_measure = m21_repeat_bracket.getSpannedElements()[-1]
            repeat_bracket = RepeatBracket(
                number=m21_repeat_bracket.number,
                offset_start=self._get_offset(first_measure),
                offset_end=self._get_offset(last_measure) + last_measure.quarterLength,
            )
            repeat_brackets.append(repeat_bracket)
        return repeat_brackets
