from typing import List

from matplotlib.figure import Figure
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle, Ellipse
import matplotlib.patheffects as path_effects
from matplotlib import font_manager as fm



from matplotlib.transforms import Bbox

from integerbook.canvas.patches import Parallelogram
from integerbook.canvas.patches_repeat_expression import Segno, relativeWidthSegno, Coda



class CanvasManager:
    def __init__(self):
        self.figs = []
        self.axs = []

        self.renderers = []
        self.inv_trans = []
        self.test_renderer = None
        self.test_inv_trans = None

        self.test_fig, self.test_ax = self._create_test_fig_and_ax()
        self.width_a4 = 8.27
        self.height_a4 = 11.69
        self.xy_ratio = self.width_a4 / self.height_a4

        self.color_background = 'white'
        self.border_linewidth_per_font_size = 0.03


    def update_attributes(self, color_background, border_linewidth_per_font_size):
        self.color_background = color_background
        self.border_linewidth_per_font_size = border_linewidth_per_font_size


    def create_canvas(self, num_pages, num_a4_widths, num_a4_heights):
        for _ in range(num_pages):
            fig = Figure(figsize=(num_a4_widths * self.width_a4, num_a4_heights * self.height_a4))
            ax = fig.subplots()
            ax = self._format_ax(ax, num_a4_widths, num_a4_heights)
            self.figs.append(fig)
            self.axs.append(ax)

            self.renderers.append(ax.figure._get_renderer())
            self.inv_trans.append(ax.transData.inverted())

    def _format_ax(self, ax, num_a4_widths, num_a4_heights):
        ax.set_ylim(1 - num_a4_heights, 1)
        ax.set_xlim(0, num_a4_widths)
        ax.axis('off')
        ax.set_position([0, 0, 1, 1])
        return ax



    def save(self, path_name, transparent_background=False):

        with PdfPages(path_name) as pdf:
            for fig in self.figs:
                pdf.savefig(fig, transparent=transparent_background)

    def create_rectangle(self, page_index, x, y, width, height, alpha, facecolor, hatch, shape, zorder=0.5):
        parallelogram = Parallelogram(
            left_bottom=[x,y],
            left_top=[x, y + height],
            right_bottom=[x + width, y],
            right_top=[x+width, y + height],
            alpha=alpha,
            facecolor=facecolor,
            hatch=hatch,
            shape=shape,
            zorder=zorder
        )
        self.axs[page_index].add_patch(parallelogram)

    def create_parallelogram(self, page_index, left_bottom, left_top, right_bottom, right_top, alpha, facecolor, hatch, shape, zorder=0.5):
        parallelogram = Parallelogram(
            left_bottom=left_bottom,
            left_top=left_top,
            right_bottom=right_bottom,
            right_top=right_top,
            alpha=alpha,
            facecolor=facecolor,
            hatch=hatch,
            shape=shape,
            zorder=zorder
        )
        self.axs[page_index].add_patch(parallelogram)

    def add_text(self, page_idx, x, y, text, font_path=None, fontsize=10, ha='left', va='baseline', border=True, background=False,
        **kwargs):

        if not font_path:
            font_path = fm.findfont("DejaVu Sans")

        fontproperties = fm.FontProperties(fname=font_path)


        bbox = None
        if background:
            bbox = dict(facecolor=self.color_background, alpha=1, boxstyle='round,pad=-.1',
                                                           edgecolor='none', linewidth=0)

        plotted_object = self.axs[page_idx].text(x, y, text, fontsize=fontsize, ha=ha, va=va,
                                                 bbox=bbox, fontproperties=fontproperties, **kwargs)

        if border:
            plotted_object.set_path_effects([
                path_effects.Stroke(linewidth=self.border_linewidth_per_font_size*fontsize, foreground=self.color_background),  # Edge color and width
                path_effects.Normal()  # Normal rendering on top of the stroke
            ])

        bb = self._get_bb_plotted_object(plotted_object, test_ax=False, page_idx=page_idx)
        x_pos_end = bb.extents[2]
        return x_pos_end


    def create_straight_rectangle(self, page_idx, x, y, width, height, **kwargs):
        rectangle_patch = Rectangle(
            (x,y), width, height, **kwargs
        )
        self.axs[page_idx].add_patch(rectangle_patch)

    def create_circle(self, page_idx, x, y, y_diameter, **kwargs):
        x_diameter = y_diameter * self.height_a4 / self.width_a4
        ellipse = Ellipse(
            (x,y),
            x_diameter,
            y_diameter,
            **kwargs
        )
        self.axs[page_idx].add_patch(ellipse)

    def create_circle_x_diameter(self, page_idx, x, y, x_diameter, **kwargs):
        y_diameter = x_diameter * self.width_a4 / self.height_a4
        ellipse = Ellipse(
            (x,y),
            x_diameter,
            y_diameter,
            **kwargs
        )
        self.axs[page_idx].add_patch(ellipse)


    def create_segno(self, page, xPos, yPos, height, color, align_left=True):
        xyRatio = self.width_a4 / self.height_a4
        width = height / xyRatio * relativeWidthSegno()
        if not align_left:
            xPos -= width

        patches = Segno(xPos, yPos, height, xyRatio, color=color)
        for patch in patches:
            self.axs[page].add_patch(patch)


    def create_coda(self, page, xPos, yPos, height, color, align_left=True):

        xyRatio = self.width_a4 / self.height_a4

        width = height / xyRatio * .85

        if not align_left:
            xPos -= width

        patches = Coda(xPos, yPos, height, width, xyRatio, color=color)
        for patch in patches:
            self.axs[page].add_patch(patch)


    def get_cap_height_per_font_size(self, font_path):

        plotted_object = self.test_ax.text(0, 0, "3", fontsize=1000, va='baseline',
                                           fontproperties=fm.FontProperties(fname=font_path))

        bb = self._get_bb_plotted_object(plotted_object, test_ax=True)
        height_number = bb.extents[3]
        return height_number / 1000

    def get_x_length_text(self, text, font_size, font_path):
        plotted_object = self.test_ax.text(0, 0, text, fontsize=font_size, va='baseline',
                                           fontproperties=fm.FontProperties(fname=font_path))

        bb = self._get_bb_plotted_object(plotted_object, test_ax=True)
        return bb.width

    def _get_bb_plotted_object(self, plotted_object, test_ax=True, page_idx=0):
        if test_ax:
            renderer = self.test_renderer
            inv_trans = self.test_inv_trans
        else:
            renderer = self.renderers[page_idx]
            inv_trans = self.inv_trans[page_idx]

        return plotted_object.get_window_extent(renderer=renderer).transformed(inv_trans)

    def _create_test_fig_and_ax(self):
        fig = Figure(figsize=(8.27, 11.69))
        ax = fig.subplots()
        ax.set_position([0, 0, 1, 1])
        self.test_renderer = ax.figure._get_renderer()
        self.test_inv_trans = ax.transData.inverted()
        return fig, ax