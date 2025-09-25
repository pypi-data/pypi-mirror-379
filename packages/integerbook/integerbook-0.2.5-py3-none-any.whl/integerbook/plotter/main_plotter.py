from integerbook.plotter.plot_settings import PlotSettings
from integerbook.plotter.x_location_finder import XLocationFinder
from integerbook.plotter.y_location_finder import YLocationFinder
from integerbook.canvas.canvas_manager import CanvasManager
from integerbook.plotter.note_plotter import NotePlotter
from integerbook.plotter.chord_plotter import ChordPlotter
from integerbook.plotter.glissando_plotter import GlissandoPlotter
from integerbook.plotter.grace_note_plotter import GraceNotePlotter
from integerbook.plotter.lyric_plotter import LyricPlotter
from integerbook.plotter.string_articulation_plotter import StringArticulationPlotter
from integerbook.plotter.barline_plotter import BarlinePlotter
from integerbook.plotter.repeat_bracket_plotter import RepeatBracketPlotter
from integerbook.plotter.repeat_expression_plotter import RepeatExpressionPlotter
from integerbook.plotter.measure_divider_plotter import MeasureDividerPlotter
from integerbook.plotter.key_origin_plotter import KeyOriginPlotter
from integerbook.plotter.metadata_plotter import MetadataPlotter

class MainPlotter:
    def __init__(self, sheet, user_settings={}):

        self.sheet = sheet

        self.CanvasManager = CanvasManager()

        self.PlotSettings = PlotSettings(user_settings, self.CanvasManager.get_cap_height_per_font_size)

        self.CanvasManager.update_attributes(self.PlotSettings.color_background, self.PlotSettings.border_linewidth_per_font_size)

        self.XLocationFinder = XLocationFinder(sheet, self.PlotSettings)
        self.YLocationFinder = YLocationFinder(sheet, self.PlotSettings)

        self.CanvasManager.create_canvas(self.YLocationFinder.get_num_pages(), self.XLocationFinder.get_x_width_canvas(),
                                         self.YLocationFinder.get_num_a4_heights())


    def save(self, path_name):
        self.CanvasManager.save(path_name, self.PlotSettings.transparent_background)

    def plot(self):
        NotePlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_notes()
        GlissandoPlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_glissandos()
        GraceNotePlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_grace_notes()
        LyricPlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_lyrics()
        ChordPlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_chords()
        StringArticulationPlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_string_articulations()
        BarlinePlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_barlines()
        RepeatBracketPlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_repeat_brackets()
        RepeatExpressionPlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_repeat_expressions()
        MeasureDividerPlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_measure_dividers()
        MeasureDividerPlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_measure_subdividers()
        KeyOriginPlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_key_origins()
        MetadataPlotter(self.sheet, self.PlotSettings, self.CanvasManager, self.XLocationFinder, self.YLocationFinder).plot_metadata()

