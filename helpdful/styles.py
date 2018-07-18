from reportlab.lib.styles import ParagraphStyle
from helpdful import utils


class StyleContainer:
    def __init__(self, theme):
        self.style = {}
        self.theme = theme
        self.create_themes()

    def __getitem__(self, key):
        return self.style[key]

    def create_themes(self):
        self.style["header"] = ParagraphStyle(
            name="header",
            fontName=utils.get_font(self.theme["header"]["font_weight"]),
            fontSize=self.theme["header"]["font_size"],
            leading=self.theme["header"]["font_size"],
        )

        self.style["id"] = ParagraphStyle(
            name="id",
            fontName=utils.get_font(self.theme["information"]["id"]["font_weight"]),
            fontSize=self.theme["information"]["name"]["font_size"],
        )

        self.style["date"] = ParagraphStyle(
            name="date",
            fontName=utils.get_font(self.theme["information"]["date"]["font_weight"]),
            fontSize=self.theme["information"]["date"]["font_size"],
        )

        self.style["name"] = ParagraphStyle(
            name="name",
            fontName=utils.get_font(self.theme["information"]["name"]["font_weight"]),
            fontSize=self.theme["information"]["name"]["font_size"],
        )

        self.style["infoheader"] = ParagraphStyle(
            name="infoheader",
            fontName=utils.get_font(self.theme["question"]["header"]["font_weight"]),
            fontSize=self.theme["question"]["header"]["font_size"],
        )

        self.style["footer"] = ParagraphStyle(
            name="footer", fontName=utils.get_font("regular"), fontSize=7
        )

        self.style["svartype"] = {}

        for answer_type in utils.answer_types:
            if "padding_left" in self.theme["question"]["svartype"][answer_type]:
                leftIndent = self.theme["question"]["svartype"][answer_type][
                    "padding_left"
                ]
            else:
                leftIndent = 0
            self.style["svartype"][answer_type] = ParagraphStyle(
                name="PERIODER",
                fontName=utils.get_font(
                    self.theme["question"]["svartype"][answer_type]["font_weight"]
                ),
                fontSize=self.theme["question"]["svartype"][answer_type]["font_size"],
                leftIndent=leftIndent,
            )
