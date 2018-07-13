from reportlab.pdfgen import canvas as canv
from reportlab.graphics import renderPDF
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import CMYKColor
from svglib.svglib import svg2rlg
from datetime import datetime
from helpdful.test_data import data
import webbrowser

font_path = 'helpdful/resources/fonts/source-sans-pro-v11-latin-{}.ttf'


def get_font(style):
    return 'source-sans-pro-v11-latin-{}'.format(style)


def scale(drawing, scaling_factor):
    drawing.width = drawing.minWidth() * scaling_factor
    drawing.height = drawing.height * scaling_factor
    drawing.scale(scaling_factor, scaling_factor)
    return drawing

def draw_header(canvas):
    # draw the header rectangle
    canvas.setFillColor(CMYKColor(0.2146, 0.0526, 0.0, 0.0314))
    canvas.rect(0, 841.89-55, 595.27, 55, stroke=0, fill=1)

    # draw a logo and the text
    canvas.setFillColor(CMYKColor(0, 0, 0, 1))
    canvas.setFont(get_font(700), 16)
    nav_logo = svg2rlg('helpdful/resources/Navlogo.svg')
    scaled_nav_logo = scale(nav_logo, scaling_factor=0.8)
    renderPDF.draw(scaled_nav_logo, canvas, 40, 800)
    canvas.drawString(85, 804, data["title"])

def draw_personal_info(canvas, anchor=736):
    # draw a person icon
    person_icon = svg2rlg('helpdful/resources/Personikon.svg')
    scaled_person_icon = scale(person_icon, scaling_factor=1)
    renderPDF.draw(scaled_person_icon, canvas, 40, anchor+2)
    canvas.setFillColor(CMYKColor(0, 0, 0, 1))

    # draw the person name
    canvas.setFont(get_font(700), 14)
    canvas.drawString(70, anchor+12, data["person"]["name"])

    # draw the person id number, grouped to 6 and 5 digits
    canvas.setFont(get_font('regular'), 12)
    canvas.drawString(70, anchor, "{} {}".format(str(data["person"]["id"])[:6], str(data["person"]["id"])[6:]))

def draw_date(canvas, anchor=736):
    date_string = data["date"].strftime("%d.%m.%y")

    canvas.setFillColor(CMYKColor(0, 0, 0, 1))
    canvas.setFont(get_font('regular'), 8)
    canvas.drawString(410, anchor+16, "Sendt til NAV {}".format(date_string))

def draw_application_id(canvas, anchor=20):
    canvas.setFillColor(CMYKColor(0, 0, 0, 1))
    canvas.setFont(get_font('regular'), 7)
    canvas.drawString(40, anchor, data["application_id"])

def draw_questions(canvas, anchor=669):
    canvas.setFillColor(CMYKColor(0, 0, 0, 1))

    for question in data["questions"]:
        canvas.setFont(get_font(600), 10)
        canvas.drawString(40, anchor+16, question["text"])

        if question["type"] == "PERIODER":
            canvas.setFont(get_font(600), 14)
            canvas.drawString(40, anchor, question["answer"])
        elif question["type"] == "CHECKBOKS":
            checkbox_icon = svg2rlg('helpdful/resources/Checkboks.svg')
            renderPDF.draw(checkbox_icon, canvas, 40, anchor-3)
            canvas.setFont(get_font('regular'), 10)
            canvas.drawString(60, anchor, question["answer"])
        elif question["type"] == "IKKE_RELEVANT":
            anchor += 20
            for info in question["information"]:
                information = Paragraph(info, getSampleStyleSheet()['Normal'], bulletText="●")
                w, h = information.wrap(595.27, anchor)
                anchor -= h + 10
                information.drawOn(canvas, 45, anchor)
            anchor -= 20
            checkbox_icon = svg2rlg('helpdful/resources/Checkboks.svg')
            renderPDF.draw(checkbox_icon, canvas, 40, anchor-3)
            canvas.setFont(get_font('regular'), 10)
            canvas.drawString(60, anchor, question["answer"])
        else:
            canvas.setFont(get_font('regular'), 10)
            canvas.drawString(40, anchor, question["answer"])
        anchor -= 50

def run():
    canvas = canv.Canvas('test.pdf')
    canvas.setPageCompression(0)

    fonts = ['600', '700', '900', 'regular']

    for font in fonts:
        pdfmetrics.registerFont(TTFont(get_font(font), font_path.format(font)))

    draw_header(canvas)
    draw_personal_info(canvas)
    draw_date(canvas)
    draw_questions(canvas)
    draw_application_id(canvas)

    canvas.showPage()
    canvas.save()

    webbrowser.open('test.pdf')

if __name__ == '__main__':
    run()
