from fpdf import FPDF
from PIL import ImageColor
import os

import colorsys

from mdl.utils_ import color_dict

cd = color_dict

assets_folder = os.path.join(os.path.dirname(__file__), '_assets_/')

class PDF(FPDF):

    # def __init__(self, asset_folder):
    #     FPDF.__init__(self)
    #     self.assets_folder = assets_folder

    def header(self):
        #Logo
        self.image(assets_folder+'LetterHead - header - Mindsett_weekly.png', 0, 0, self.w)
        #Fontsize and type
        self.set_font('Arial', 'B', 15)
        self.image(assets_folder+"2024_Mindsett_Logo_White.png", 10, 8, 60)
        # self.image(assets_folder+"mindsett_logo_white_transparent.png", 15, 15, 45)
        
    def footer(self):
        #Logo
        footer_height = 32
        img_path = assets_folder+'LetterHead - Footer - Mindsett_weekly.png'
        footer_width = 210
        self.image(img_path, 0, self.h-footer_height, footer_width)
        self.set_font('Arial', 'B', 15)
        
        self.set_y(self.h-footer_height + 5)
        self.set_x(20)
        self.set_font('Arial', "I", 8)
        color_rgb = ImageColor.getcolor(cd["Mindsett Blue"], "RGB")
        color_hsv = colorsys.rgb_to_hsv(*color_rgb)
        color_rgb_changed = colorsys.hsv_to_rgb(color_hsv[0], color_hsv[1], color_hsv[2])
        self.set_text_color(*color_rgb_changed)
        #self.cell(pdf.w - 30, 10, '**BBP benchmarking (REEB) ', 0, 0, 'B')
        
    from .write_multicell_with_styles import write_multicell_with_styles