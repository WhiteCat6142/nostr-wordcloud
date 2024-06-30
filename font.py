import os
import matplotlib.font_manager as fm

def find_font(fontname):
    fonts = fm.findSystemFonts()
    for font in fonts:
        try:
            if os.path.splitext(os.path.basename(str(font)))[0] == fontname:
                return str(font)
        except Exception:
            pass
    return ''
