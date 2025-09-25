import music21

from integerbook.parser.base_parser import BaseParser
from integerbook.bar import KeyOrigin

class MiscParser(BaseParser):
    def __init__(self, stream_obj, settings):
        super().__init__(stream_obj, settings)


    def get_offset_length(self):
        return self.stream_obj.quarterLength

    def parse_key_origins(self):
        key_origins = []

        for measure in self.stream_obj[music21.stream.Measure]:
            for key in self.stream_obj[music21.key.Key]:
                key_origin = KeyOrigin(
                    origin=self._get_origin(key),
                    offset=self._get_offset_key_origin(key, measure)
                )
                key_origins.append(key_origin)
            return key_origins

    def _get_offset_key_origin(self, key, measure):
        offset = self._get_offset(key)

        if measure.number == 0:
            offset = measure.quarterLength
        return offset


    def get_num_positions(self):
        return self._get_highest_midi() - self._get_lowest_midi() + 1

    def _get_origin(self, key):

        tonic_is_origin = key.mode == 'major' or not self.ParseSettings.minor_perspective == "parallel"

        if tonic_is_origin:
            letter = key.tonic.name[0]
            accidental = key.tonic.accidental
        else:
            letter = key.relative.tonic.name[0]
            accidental = key.relative.tonic.accidental

        if accidental:
            letter += accidental.unicode

        if key.mode == 'minor' and self.ParseSettings.minor_perspective == "minor":
            enDash = u'\u2013'
            letter += enDash

        return letter

    def get_pickup_measure_length(self):
        first_measure = self.stream_obj[music21.stream.Measure].first()
        if first_measure.number == 0:
            return float(first_measure.quarterLength)
        else:
            return 0

    def get_song_title(self):
        try:
            song_title = self.stream_obj.metadata.bestTitle
        except:
            song_title = "no title"
        return song_title

    def get_composer(self):
        try:
            composer = self.stream_obj.metadata.composer
        except:
            composer = "no composer"
        return composer

    def get_arranger(self):
        player = ""
        try:
            contributors = self.stream_obj.metadata.contributors
            for contributor in contributors:
                if contributor.role == 'arranger':
                    player = contributor.name
        except:
            pass
        return player

