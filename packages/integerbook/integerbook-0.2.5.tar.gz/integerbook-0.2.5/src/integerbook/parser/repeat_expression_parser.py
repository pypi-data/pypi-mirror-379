import inspect
import music21

from integerbook.parser.base_parser import BaseParser
from integerbook.bar import RepeatExpression


class RepeatExpressionParser(BaseParser):

    def parse_repeat_expressions(self):

        # Find all repeat expressions
        repeat_expressions = []
        for measure in self.stream_obj[music21.stream.Measure]:
            for el in measure.recurse():
                if self._isRepeatExpression(el):

                    repeat_expression = RepeatExpression(
                        type=el.name,
                        offset=el.getOffsetInHierarchy(self.stream_obj),
                        at_start_of_measure=(el.offset == 0)
                    )
                    repeat_expressions.append(repeat_expression)
        return repeat_expressions

    def _isRepeatExpression(self, el):
        return type(el).__module__ == 'music21.repeat' and music21.repeat.RepeatExpression in inspect.getmro(type(el))



