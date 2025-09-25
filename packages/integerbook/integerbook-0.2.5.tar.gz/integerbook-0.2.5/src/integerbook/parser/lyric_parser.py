import music21

from integerbook.parser.base_parser import BaseParser
from integerbook.note import Lyric

class LyricParser(BaseParser):
    def __init__(self, stream_obj, settings):
        super().__init__(stream_obj, settings)
        self.num_lines_lyrics_per_voice = {1: 0}

    def parse_lyrics(self):
        lyrics = []
        for m21_note in self.stream_obj[music21.note.Note]:
            for m21_lyric in m21_note.lyrics:
                lyric = Lyric(
                    text=m21_lyric.text,
                    offset=self._get_offset(m21_note),
                    line_idx=m21_lyric.number - 1,
                    voice=self.get_voice_number(m21_note),
                    syllabic=m21_lyric.syllabic
                )
                lyrics.append(lyric)

                self._update_num_lines_lyrics_per_voice(lyric)
        return lyrics, self.num_lines_lyrics_per_voice

    def _update_num_lines_lyrics_per_voice(self, lyric):
        if lyric.voice in self.num_lines_lyrics_per_voice:
            if lyric.line_idx + 1 > self.num_lines_lyrics_per_voice[lyric.voice]:
                self.num_lines_lyrics_per_voice[lyric.voice] = lyric.line_idx + 1
        else:
            self.num_lines_lyrics_per_voice[lyric.voice] = lyric.line_idx + 1