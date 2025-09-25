import json
import glob
import os

import music21
from integerbook.parser.main_parser import MainParser
from integerbook.plotter.main_plotter import MainPlotter

dir_songs = os.path.join(os.path.dirname(__file__), "test-files")
lines = glob.glob(dir_songs + '/' + '*' + '.musicxml')
lines = [os.path.basename(line) for line in lines]
lines.sort()

user_settings = {
    "scroll": False
}

for line in lines:

    print(line)

    path_sheet = dir_songs + '/' + line

    parser = MainParser(path_sheet, user_settings)
    sheet = parser.parse_stream()

    # Create visualization
    plotter = MainPlotter(sheet, user_settings)
    plotter.plot()
    plotter.save(f'/Users/jvo/Downloads/output/{line}.pdf')

    # Save JSON
    # json_file_path = '/Users/jvo/Documents/programming/swift/integerbook/integerbook/sheet2.json'
    # sheet.save_to_json(json_file_path)
    print(sheet.to_json())
