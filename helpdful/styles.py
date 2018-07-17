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

        self.style["info"] = ParagraphStyle(
            name="bulletpoint",
            fontName=utils.get_font("regular"),
            fontSize=10,
            leftIndent=14,
        )

        self.style["footer"] = ParagraphStyle(
            name="footer", fontName=utils.get_font("regular"), fontSize=7
        )
