from reportlab.graphics import renderPDF
from reportlab.platypus import Paragraph
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import CMYKColor
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas as canv
from helpdful import test_data, styles, utils
from bs4 import BeautifulSoup
from io import BytesIO


class Helpdful:
    def __init__(self, name="test.pdf", data=test_data.data, theme=test_data.theme):
        self.buffer = BytesIO()
        self.data = data
        self.theme = theme
        self.style = styles.StyleContainer(self.theme)
        self.name = name
        self.canvas = canv.Canvas(self.buffer)
        self.canvas.setPageCompression(0)
        self.canvas.setTitle(name)
        self.page_width, self.page_height = self.canvas._pagesize
        self.page = 1
        self.y_position = self.page_height  # goes from top to bottom of the page

        fonts = ["600", "700", "900", "regular"]

        for font in fonts:
            pdfmetrics.registerFont(
                TTFont(utils.get_font(font), utils.font_path.format(font))
            )

    def render(self):
        self._create_new_page()
        self._draw_subheader()
        self._draw_questions()
        self.canvas.showPage()
        self.canvas.save()
        return self.buffer.getvalue()

    def needs_next_page(self, next_paragraph_height):
        absolute_height = (
            self.y_position - self.theme["footer"]["height"] - next_paragraph_height
        )
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
        nav_logo = svg2rlg("helpdful/{}".format(self.theme["images"]["logo"]))
        scaled_nav_logo = utils.scale(
            nav_logo, scaling_factor=self.theme["header"]["logo"]["scale"]
        )

        # create a paragraph to calculate header height later
        header = Paragraph(
            utils.type_to_title(self.data["soknadstype"]), self.style["header"]
        )
        header_text_boundary = self.page_width - (
            (self.theme["page_margin"] * 2)
            + scaled_nav_logo.width
            + self.theme["header"]["logo"]["margin_right"]
        )
        w, h = header.wrap(header_text_boundary, self.theme["header"]["base_height"])

        # draw the header rectangle
        self.canvas.setFillColor(CMYKColor(*self.theme["header"]["background"]))
        self.y_position = self.y_position - self.theme["header"]["base_height"] - h

        self.canvas.rect(
            0,
            self.y_position,
            self.page_width,
            self.theme["header"]["base_height"] + h,
            stroke=0,
            fill=1,
        )

        # draw a logo and the text
        renderPDF.draw(
            scaled_nav_logo, self.canvas, self.theme["page_margin"], 806 - (h / 2)
        )  # TODO: Fix magical value 806 :(

        header.drawOn(
            self.canvas,
            self.theme["page_margin"]
            + scaled_nav_logo.width
            + self.theme["header"]["logo"]["margin_right"],
            820 - h,
        )  # TODO: Fix magical value 820 :(
        self.y_position -= self.theme["header"]["margin_bottom"]

    def _draw_subheader(self):
        date_string = utils.isostr_to_norwegian(self.data["opprettetDato"])
        date = Paragraph("Sendt til NAV {}".format(date_string), self.style["date"])
        date_w, date_h = date.wrap(
            self.page_width - 410, self.theme["information"]["name"]["font_size"]
        )  # TODO: Fix magical value 410 :(
        date.drawOn(self.canvas, 410, self.y_position)  # TODO: Fix magical value 410 :(

        person_icon = svg2rlg("helpdful/{}".format(self.theme["images"]["person"]))

        # the position at which the text next to the icon should be drawn
        text_x = (
            self.theme["page_margin"] + person_icon.width + self.theme["icon_margin"]
        )

        name_width_boundary = (
            self.page_width - ((self.theme["page_margin"] * 2)) - date_w
        )

        # draw the person name
        name = Paragraph(self.data["person"]["name"], self.style["name"])
        name_w, name_h = name.wrap(
            name_width_boundary, self.theme["information"]["name"]["font_size"]
        )
        self.y_position -= name_h

        name.drawOn(
            self.canvas,
            text_x,
            self.y_position + self.theme["information"]["name"]["font_size"],
        )

        renderPDF.draw(
            person_icon, self.canvas, self.theme["page_margin"], self.y_position
        )

        # draw the person id number, grouped to 6 and 5 digits
        id = Paragraph(
            "{} {}".format(
                str(self.data["person"]["id"])[:6], str(self.data["person"]["id"])[6:]
            ),
            self.style["id"],
        )
        id.wrap(name_width_boundary, self.theme["information"]["id"]["font_size"])
        id.drawOn(self.canvas, text_x, self.y_position)

    def __process_question(self, question):
        # TODO: ... make this function pretty
        self.canvas.setFillColor(CMYKColor(0, 0, 0, 1))

        self.canvas.setFont(utils.get_font(600), 10)

        answer = None

        if not question["svartype"] == "CHECKBOX_PANEL":
            infoheader = Paragraph(question["sporsmalstekst"], self.style["infoheader"])
            info_w, info_h = infoheader.wrap(
                self.page_width - (self.theme["page_margin"] * 2),
                self.theme["question"]["header"]["font_size"],
            )
            infoheader.drawOn(self.canvas, self.theme["page_margin"], self.y_position)
            self.y_position -= info_h + 5

        if question["svartype"] == "PERIODER":
            answer = "{}–{}".format(
                utils.isostr_to_norwegian(question["svar"][0]["verdi"]),
                utils.isostr_to_norwegian(question["svar"][1]["verdi"]),
            )

        elif question["svartype"] == "JA_NEI":
            checkbox_icon = svg2rlg("helpdful/resources/Checkboks.svg")
            renderPDF.draw(
                checkbox_icon,
                self.canvas,
                self.theme["page_margin"],
                self.y_position + self.theme["icon_offset"],
            )
            answer = question["svar"][0]["verdi"].capitalize()

        elif question["svartype"] == "IKKE_RELEVANT":
            # TODO: make this answer type behave properly at the end of pages
            self.y_position += 20
            style = self.style["svartype"][question["svartype"]]
            text = BeautifulSoup(question["undertekst"], "lxml")
            for info in text.find_all("li"):
                information = Paragraph(info.text, style, bulletText="●")
                w, h = information.wrap(
                    self.page_width
                    - style.leftIndent
                    - (self.theme["page_margin"] * 2),
                    self.y_position,
                )
                self.y_position -= h + 10
                information.drawOn(self.canvas, 45, self.y_position)
            self.y_position -= 20
            answer = ""

        elif question["svartype"] == "CHECKBOX_PANEL":
            checkbox_icon = svg2rlg("helpdful/resources/Checkboks.svg")
            renderPDF.draw(
                checkbox_icon,
                self.canvas,
                self.theme["page_margin"],
                self.y_position + self.theme["icon_offset"],
            )
            answer = question["sporsmalstekst"]

        else:
            answer = question["svar"][0]["verdi"]

        answer_paragraph = Paragraph(
            answer, self.style["svartype"][question["svartype"]]
        )
        answer_paragraph_w, answer_paragraph_h = answer_paragraph.wrap(
            self.page_width - (self.theme["page_margin"] * 2),
            self.theme["question"]["svartype"][question["svartype"]],
        )
        answer_paragraph.drawOn(self.canvas, self.theme["page_margin"], self.y_position)
        self.y_position -= answer_paragraph_h

        if not question["svartype"] == "IKKE_RELEVANT":
            self.y_position -= 20
            if self.needs_next_page(
                20 + self.theme["footer"]["height"] + answer_paragraph_h
            ):
                self.canvas.showPage()
                self._create_new_page()

        for subquestion in question["undersporsmal"]:
            self.__process_question(subquestion)

    def _draw_questions(self):
        self.y_position -= self.theme["header"]["margin_bottom"] + 20
        for question in self.data["sporsmal"]:
            self.__process_question(question)

    def _draw_footer(self):
        footer = Paragraph(self.data["id"], self.style["footer"])
        page_counter = Paragraph("Side {}".format(self.page), self.style["footer"])
        w, h = page_counter.wrap(20, self.theme["footer"]["height"])
        page_counter.drawOn(
            self.canvas,
            self.page_width - self.theme["page_margin"] - w,
            self.theme["footer"]["height"],
        )
        w, h = footer.wrap(
            self.page_width - (self.theme["page_margin"] * 2),
            self.theme["footer"]["height"],
        )
        footer.drawOn(
            self.canvas, self.theme["page_margin"], self.theme["footer"]["height"]
        )
