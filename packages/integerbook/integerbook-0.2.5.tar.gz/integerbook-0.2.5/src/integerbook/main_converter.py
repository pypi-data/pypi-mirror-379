import os
import json

from integerbook.parser.main_parser import MainParser
from integerbook.plotter.main_plotter import MainPlotter


class MainConverter:

    def convert(self, input_path, output_dir, user_settings):

        self.check_settings(user_settings)

        parser = MainParser(input_path, user_settings)
        sheet = parser.parse_stream()

        plotter = MainPlotter(sheet, user_settings)
        plotter.plot()
        plotter.save(output_dir + f'/{sheet.title}.pdf')

    @staticmethod
    def check_settings(user_settings):
        path_settings = os.path.join(os.path.dirname(__file__), 'parser/parse_settings.json')
        f = open(path_settings)
        parse_settings = json.load(f)

        path_settings = os.path.join(os.path.dirname(__file__), 'plotter/plot_settings.json')
        f = open(path_settings)
        plot_settings = json.load(f)

        settings = parse_settings | plot_settings

        for key in user_settings.keys():
            if key not in settings.keys():
                raise ValueError(f"{key} is not a setting that can be passed")
            if key in {"minor_perspective", "subdivision", "note_coloring"}:
                if user_settings[key] not in settings[f"_{key}_options"]:
                    raise ValueError(f"{user_settings[key]} is not a valid value for {key} setting")
