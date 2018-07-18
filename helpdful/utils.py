from datetime import datetime

font_path = "helpdful/resources/fonts/source-sans-pro-v11-latin-{}.ttf"

answer_types = ["PERIODER", "FRITEKST", "JA_NEI", "IKKE_RELEVANT", "CHECKBOX_PANEL"]


def get_font(style):
    return "source-sans-pro-v11-latin-{}".format(style)


def scale(drawing, scaling_factor):
    drawing.width = drawing.minWidth() * scaling_factor
    drawing.height = drawing.height * scaling_factor
    drawing.scale(scaling_factor, scaling_factor)
    return drawing


def type_to_title(type):
    titles = {"OPPHOLD_UTLAND": "Søknad om å beholde sykepenger utenfor Norge"}
    return titles[type]


def isostr_to_norwegian(datestr):
    return datetime.strptime(datestr, "%Y-%m-%d").strftime("%d.%m.%y")
