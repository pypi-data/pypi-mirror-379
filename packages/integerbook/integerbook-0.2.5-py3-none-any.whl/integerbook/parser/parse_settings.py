import json
import os


class ParseSettings:

    def __init__(self, user_settings):
        path_settings = os.path.join(os.path.dirname(__file__), 'parse_settings.json')
        f = open(path_settings)
        settings = json.load(f)

        settings.update(user_settings)

        self.scroll = settings["scroll"]
        self.measures_per_line = settings["measures_per_line"]
        self.numbers_relative_to_chord = settings["numbers_relative_to_chord"]
        self.force_minor = settings["force_minor"]
        self.minor_perspective = settings["minor_perspective"]
        self.roman_numerals = settings["roman_numerals"]
        self.chord_verbosity = settings["chord_verbosity"]
        self.manual_secondary_chords = settings["manual_secondary_chords"]
        self.apply_preprocessing = settings["apply_preprocessing"]
        self.chord_progression = settings["chord_progression"]



