import music21

from integerbook.parser.base_parser import BaseParser

class Preprocessor:
    def __init__(self, stream_obj, ParseSettings):
        self.stream_obj = stream_obj
        self.ParseSettings = ParseSettings

    def preprocess_stream_obj(self):
        if self.ParseSettings.apply_preprocessing:
            self._make_key_signature_into_key()
            self._add_middle_notes_to_slur()
            self._remove_second_chord_symbol_in_same_place()
            self._make_keys_minor(self.ParseSettings.force_minor)
            self._add_key_when_key_is_missing()
            self._remove_bass_staff()
            self._correct_pickup_measure()
        return self.stream_obj

    def _make_key_signature_into_key(self):
        for measure in self.stream_obj[music21.stream.Measure]:
            for key_or_key_signature in measure[music21.key.KeySignature]:
                if type(key_or_key_signature) == music21.key.KeySignature:
                    offset = key_or_key_signature.offset
                    new_key = key_or_key_signature.asKey()
                    measure.remove(key_or_key_signature)
                    measure.insert(offset, new_key)
                    print('mode key missing')

    def _add_middle_notes_to_slur(self):
        for slur in self.stream_obj[music21.spanner.Slur]:
            spanner_storage = []
            for note in self.stream_obj[music21.note.Note]:
                if self._should_be_included_in_slur(note, slur.getFirst(), slur.getLast()):
                    spanner_storage.append(note)
            slur.spannerStorage.elements = spanner_storage

    def _should_be_included_in_slur(self, note, first_note, last_note):
        after_first_note = note.getOffsetInHierarchy(self.stream_obj) >= first_note.getOffsetInHierarchy(self.stream_obj)
        before_last_note = note.getOffsetInHierarchy(self.stream_obj) <= last_note.getOffsetInHierarchy(self.stream_obj)
        same_voice = BaseParser.get_voice_number(note) == BaseParser.get_voice_number(first_note)

        return after_first_note and before_last_note and same_voice

    def _remove_second_chord_symbol_in_same_place(self):
        for measure in self.stream_obj[music21.stream.Measure]:
            last_chord_symbol = None
            for chord_symbol in measure[music21.harmony.ChordSymbol]:
                if last_chord_symbol:
                    if chord_symbol.offset == last_chord_symbol.offset:
                        measure.remove(chord_symbol)
                        print('removed chord symbol', chord_symbol)
                last_chord_symbol = chord_symbol

    def _make_keys_minor(self, force_minor):
        for measure in self.stream_obj[music21.stream.Measure]:
            for key in measure[music21.key.Key]:
                if key.mode == 'major' and force_minor:
                    offset = key.offset
                    new_key = key.relative
                    measure.remove(key)
                    measure.insert(offset, new_key)

    def _add_key_when_key_is_missing(self):
        if len(self.stream_obj[music21.key.KeySignature]) == 0:
            print('no key specified')
            try:
                key = self.stream_obj.analyze('key')
            except:
                key = music21.key.Key('C')
                print('key analysis failed')
            self.stream_obj[music21.stream.Measure].first.insert(key)

    def _remove_bass_staff(self):
        staffs = self.stream_obj[music21.stream.PartStaff]
        if staffs:
            if len(staffs) > 1:
                self.stream_obj.remove(staffs[1])
                print("removed staff")

        parts = self.stream_obj[music21.stream.Part]
        if parts:
            if len(parts) > 1:
                self.stream_obj.remove(parts[1:])
                print("removed part(s)")

    def _correct_pickup_measure(self):
        measures = self.stream_obj[music21.stream.Measure]
        if measures[0].number == 1:
            if len(measures) > 1 and measures[0].quarterLength < measures[1].quarterLength:
                self._renumber_measures()

    def _renumber_measures(self):
        measures = self.stream_obj[music21.stream.Measure]
        for i in range(len(measures)):
            measures[i].number = i
