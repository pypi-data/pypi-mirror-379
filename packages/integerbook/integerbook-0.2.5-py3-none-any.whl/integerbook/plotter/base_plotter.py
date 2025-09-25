from typing import Type
from integerbook.sheet import Sheet
from integerbook.canvas.canvas_manager import CanvasManager
from integerbook.plotter.x_location_finder import XLocationFinder
from integerbook.plotter.y_location_finder import YLocationFinder
from integerbook.plotter.plot_settings import PlotSettings


class BasePlotter:

    def __init__(self, sheet, settings, canvas_manager,
                 x_location_finder, y_location_finder):
        self.sheet = sheet
        self.PlotSettings = settings
        self.CanvasManager = canvas_manager
        self.XLocationFinder = x_location_finder
        self.YLocationFinder = y_location_finder

    def get_position(self, offset):
        line, x_pos = self.XLocationFinder.get_line_and_x_pos(offset)
        y_pos_line_base = self.YLocationFinder.get_y_pos_line_base(line)
        page = self.YLocationFinder.get_page(line)
        return x_pos, y_pos_line_base, page

    def get_x_length(self, h_length):
        return self.XLocationFinder.get_x_length(h_length)

    def create_barline_rectangle(self, page, x, y, width, height):
        self.CanvasManager.create_straight_rectangle(page, x, y, width, height,
                                                     zorder=self.PlotSettings.z_order_barlines,
                                                     facecolor=self.PlotSettings.color_barlines)



