font_path = "helpdful/resources/fonts/source-sans-pro-v11-latin-{}.ttf"


def get_font(style):
    return "source-sans-pro-v11-latin-{}".format(style)


def scale(drawing, scaling_factor):
    drawing.width = drawing.minWidth() * scaling_factor
    drawing.height = drawing.height * scaling_factor
    drawing.scale(scaling_factor, scaling_factor)
    return drawing
