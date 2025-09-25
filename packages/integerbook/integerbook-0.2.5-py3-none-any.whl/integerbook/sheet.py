import json

class Sheet:
    def __init__(self):
        self.notes = []
        self.chords = []
        self.glissandos = []
        self.string_articulations = []
        self.grace_notes = []
        self.chord_notes = []
        self.key_origins = []
        self.lyrics = []
        self.num_positions = 0
        self.offsets_start_line = []
        self.h_shifts_line = []
        self.pickup_measure_length = 0
        self.num_lines_lyrics_per_voice = {1: 0}
        self.offset_length = 0
        self.barlines = []
        self.measure_dividers = []
        self.measure_subdividers = []
        self.repeat_brackets = []
        self.repeat_expressions = []
        self.title = ""
        self.composer = ""
        self.arranger = ""


    def add_notes(self, notes):
        for note in notes:
            self.add_note(note)

    def add_note(self, note):
        self.notes.append(note)


    def to_json(self):
        def serialize(obj):
            if isinstance(obj, list):  # Check if the object is a list
                return [serialize(item) for item in obj]  # Serialize each item in the list
            elif hasattr(obj, '__dict__'):
                return obj.__dict__  # Serialize custom objects
            return obj  # Return primitive types as is

        return json.dumps({key: serialize(value) for key, value in self.__dict__.items()})

    def save_to_json(self, file_path):
        with open(file_path, 'w') as json_file:
            json_file.write(self.to_json())  # Write the JSON string to the file
        print(f'Sheet JSON saved to {file_path}')  # Confirmation message

