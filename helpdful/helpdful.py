from reportlab.graphics import renderPDF
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import CMYKColor
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas as canv
from helpdful import test_data

font_path = 'helpdful/resources/fonts/source-sans-pro-v11-latin-{}.ttf'


def get_font(style):
    return 'source-sans-pro-v11-latin-{}'.format(style)

def scale(drawing, scaling_factor):
    drawing.width = drawing.minWidth() * scaling_factor
    drawing.height = drawing.height * scaling_factor
    drawing.scale(scaling_factor, scaling_factor)
    return drawing, drawing.width

class Helpdful():
    def __init__(self, name="test.pdf", data=test_data.data, theme=test_data.theme):
        self.data = data
        self.theme = theme
        self.name = name
        self.canvas = canv.Canvas(self.name)
        self.canvas.setPageCompression(0)
        self.page_width, self.page_height = self.canvas._pagesize
        self.page = 1
        self.y_position = self.page_height # goes from top to bottom of the page

        fonts = ['600', '700', '900', 'regular']

        for font in fonts:
            pdfmetrics.registerFont(TTFont(get_font(font), font_path.format(font)))


    def render(self):
        self._create_new_page()
        self._draw_subheader()
        self.draw_questions()
        self.canvas.showPage()
        self.canvas.save()

    def needs_next_page(self, next_paragraph_height):
        absolute_height = self.y_position - \
            self.theme["footer"]["height"] - \
            next_paragraph_height
        if absolute_height < 0:
            return True
        return False

    def _create_new_page(self):
        self.y_position = self.page_height
        self._draw_header()
        self._draw_footer()
        self.page += 1

    def _draw_header(self):
        # load the header logo and get its width for later
        nav_logo = svg2rlg('helpdful/{}'.format(self.theme["images"]["logo"]))
        scaled_nav_logo, logo_width = scale(nav_logo, scaling_factor=self.theme["header"]["logo"]["scale"])

        # create a paragraph to calculate header height later
        header_style = ParagraphStyle(
            name='header',
            fontName=get_font(self.theme["header"]["font_weight"]),
            fontSize=self.theme["header"]["font_size"],
            leading=self.theme["header"]["font_size"]
        )
        header = Paragraph(self.data["title"], header_style)
        header_text_boundary = self.page_width-((self.theme["page_margin"]*2)+logo_width+self.theme["header"]["logo"]["margin_right"])
        w, h = header.wrap(header_text_boundary, self.theme["header"]["base_height"])

        # draw the header rectangle
        self.canvas.setFillColor(CMYKColor(*self.theme["header"]["background"]))
        self.y_position = self.y_position-self.theme["header"]["base_height"]-h

        self.canvas.rect(0, self.y_position, self.page_width, self.theme["header"]["base_height"]+h, stroke=0, fill=1)

        # draw a logo and the text

        renderPDF.draw(scaled_nav_logo, self.canvas, self.theme["page_margin"], 806-(h/2)) # TODO: Fix magical value 806 :(

        header.drawOn(self.canvas, self.theme["page_margin"]+logo_width+self.theme["header"]["logo"]["margin_right"], 820-h) # TODO: Fix magical value 820 :(
        self.y_position -= self.theme["header"]["margin_bottom"]

    def _draw_subheader(self):
        id_style = ParagraphStyle(
            name="id",
            fontName=get_font(self.theme["information"]["id"]["font_weight"]),
            fontSize=self.theme["information"]["name"]["font_size"]
        )

        date_style = ParagraphStyle(
            name="date",
            fontName=get_font(self.theme["information"]["date"]["font_weight"]),
            fontSize=self.theme["information"]["date"]["font_size"]
        )

        name_style = ParagraphStyle(
            name="name",
            fontName=get_font(self.theme["information"]["name"]["font_weight"]),
            fontSize=self.theme["information"]["name"]["font_size"]
        )

        date_string = self.data["date"].strftime("%d.%m.%y")
        date = Paragraph("Sendt til NAV {}".format(date_string), date_style)
        date_w, date_h = date.wrap(self.page_width-410, self.theme["information"]["name"]["font_size"]) # TODO: Fix magical value 410 :(
        date.drawOn(self.canvas, 410, self.y_position) # TODO: Fix magical value 410 :(

        person_icon = svg2rlg('helpdful/{}'.format(self.theme["images"]["person"]))
        _, icon_width = scale(person_icon, 1)

        # the position at which the text next to the icon should be drawn
        text_x = self.theme["page_margin"]+icon_width+self.theme["icon_margin"]


        name_width_boundary = self.page_width-((self.theme["page_margin"]*2))-date_w

        # draw the person name
        name = Paragraph(self.data["person"]["name"], name_style)
        name_w, name_h = name.wrap(name_width_boundary, self.theme["information"]["name"]["font_size"])
        self.y_position -= name_h

        name.drawOn(self.canvas, text_x, self.y_position+self.theme["information"]["name"]["font_size"])


        renderPDF.draw(person_icon, self.canvas, self.theme["page_margin"], self.y_position)

        # draw the person id number, grouped to 6 and 5 digits
        id = Paragraph("{} {}".format(str(self.data["person"]["id"])[:6], str(self.data["person"]["id"])[6:]), id_style)
        id.wrap(name_width_boundary, self.theme["information"]["id"]["font_size"])
        id.drawOn(self.canvas, text_x, self.y_position)


    def draw_questions(self):
        # TODO: Fix this function to use self.y_position instead of anchor
        anchor = self.y_position-self.theme["header"]["margin_bottom"]-20
        self.canvas.setFillColor(CMYKColor(0, 0, 0, 1))

        for question in self.data["questions"]:
            self.canvas.setFont(get_font(600), 10)
            self.canvas.drawString(40, anchor+16, question["text"])

            if question["type"] == "PERIODER":
                self.canvas.setFont(get_font(600), 14)
                self.canvas.drawString(40, anchor, question["answer"])
            elif question["type"] == "CHECKBOKS":
                checkbox_icon = svg2rlg('helpdful/resources/Checkboks.svg')
                renderPDF.draw(checkbox_icon, self.canvas, 40, anchor-3)
                self.canvas.setFont(get_font('regular'), 10)
                self.canvas.drawString(60, anchor, question["answer"])
            elif question["type"] == "IKKE_RELEVANT":
                info_style = ParagraphStyle(
                    name='bulletpoint',
                    fontName=get_font('regular'),
                    fontSize=10,
                    leftIndent=14
                )
                anchor += 20
                for info in question["information"]:
                    information = Paragraph(info, info_style, bulletText="●")
                    w, h = information.wrap(500, anchor)
                    anchor -= h + 10
                    information.drawOn(self.canvas, 45, anchor)
                anchor -= 20
                checkbox_icon = svg2rlg('helpdful/resources/Checkboks.svg')
                renderPDF.draw(checkbox_icon, self.canvas, 40, anchor-3)
                self.canvas.setFont(get_font('regular'), 10)
                self.canvas.drawString(60, anchor, question["answer"])
            else:
                self.canvas.setFont(get_font('regular'), 10)
                self.canvas.drawString(40, anchor, question["answer"])
            anchor -= 50

    def _draw_footer(self):
        footer_style = ParagraphStyle(
            name='footer',
            fontName=get_font('regular'),
            fontSize=7
        )
        footer = Paragraph(self.data["application_id"], footer_style)
        page_counter = Paragraph("Side {}".format(self.page), footer_style)
        w, h = page_counter.wrap(20, self.theme["footer"]["height"])
        page_counter.drawOn(self.canvas, self.page_width-self.theme["page_margin"]-w, self.theme["footer"]["height"])
        w, h = footer.wrap(self.page_width-(self.theme["page_margin"]*2), self.theme["footer"]["height"])
        footer.drawOn(self.canvas, self.theme["page_margin"], self.theme["footer"]["height"])
