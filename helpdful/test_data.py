from datetime import datetime

data = {
    # fields that i'm missing :(
    "person": {"name": "Kari Normann Paulsrud Granholt", "id": 12068745698},
    # mockup data of application
    "id": "bea4a339-5740-4f96-9e72-0ddef4d4dfeb",
    "sykmeldingId": None,
    "soknadstype": "OPPHOLD_UTLAND",
    "status": "SEND",
    "fom": None,
    "tom": None,
    "opprettetDato": "2018-07-10",
    "sporsmal": [
        {
            "id": "100",
            "tag": "PERIODEUTLAND",
            "sporsmalstekst": "Når skal du være utenfor Norge?",
            "undertekst": None,
            "svartype": "PERIODER",
            "min": "2018-04-10",
            "max": "2019-01-10",
            "kriterieForVisningAvUndersporsmal": None,
            "svar": [
                {"svarverdiType": "FOM", "verdi": "2018-06-04"},
                {"svarverdiType": "TOM", "verdi": "2018-07-04"},
            ],
            "undersporsmal": [],
        },
        {
            "id": "101",
            "tag": "LAND",
            "sporsmalstekst": "Hvilket land skal du reise til?",
            "undertekst": None,
            "svartype": "FRITEKST",
            "min": None,
            "max": None,
            "kriterieForVisningAvUndersporsmal": None,
            "svar": [{"svarverdiType": None, "verdi": "TEST"}],
            "undersporsmal": [],
        },
        {
            "id": "102",
            "tag": "ARBEIDSGIVER",
            "sporsmalstekst": "Har du arbeidsgiver?",
            "undertekst": None,
            "svartype": "JA_NEI",
            "min": None,
            "max": None,
            "kriterieForVisningAvUndersporsmal": "JA",
            "svar": [{"svarverdiType": None, "verdi": "JA"}],
            "undersporsmal": [
                {
                    "id": "103",
                    "tag": "SYKMELDINGSGRAD",
                    "sporsmalstekst": "Er du 100% sykmeldt?",
                    "undertekst": None,
                    "svartype": "JA_NEI",
                    "min": None,
                    "max": None,
                    "kriterieForVisningAvUndersporsmal": None,
                    "svar": [{"svarverdiType": None, "verdi": "JA"}],
                    "undersporsmal": [],
                }
            ],
        },
        {
            "id": "104",
            "tag": "BEKREFT_OPPLYSNINGER_UTLAND_INFO",
            "sporsmalstekst": "Før du reiser trenger vi denne bekreftelsen fra deg",
            "undertekst": "<ul>\n    <li>Reisen vil ikke gjøre at jeg blir dårligere</li>\n    <li>Reisen vil ikke gjøre at sykefraværet blir lengre</li>\n    <li>Reisen vil ikke hindre planlagt behandling eller oppfølging</li>\n</ul>",
            "svartype": "IKKE_RELEVANT",
            "min": None,
            "max": None,
            "kriterieForVisningAvUndersporsmal": None,
            "svar": [],
            "undersporsmal": [
                {
                    "id": "105",
                    "tag": "BEKREFT_OPPLYSNINGER_UTLAND",
                    "sporsmalstekst": "Jeg har lest all informasjonen jeg har fått i søknaden og bekrefter at opplysningene jeg har gitt er korrekte.",
                    "undertekst": None,
                    "svartype": "CHECKBOX_PANEL",
                    "min": None,
                    "max": None,
                    "kriterieForVisningAvUndersporsmal": None,
                    "svar": [{"svarverdiType": None, "verdi": "CHECKED"}],
                    "undersporsmal": [],
                }
            ],
        },
    ],
}

theme = {
    "footer": {"height": 20},
    "page_margin": 40,
    "header": {
        "background": (0.2146, 0.0526, 0.0, 0.0314),
        "logo": {"scale": 0.8, "margin_right": 4},
        "color": (0, 0, 0, 1),
        "font_size": 16,
        "font_weight": "700",
        "base_height": 43,
        "margin_bottom": 40,
    },
    "information": {
        "name": {"font_size": 14, "font_weight": "700"},
        "id": {"font_size": 12, "font_weight": "regular"},
        "date": {"font_size": 8, "font_weight": "regular"},
    },
    "icon_margin": 10,
    "images": {
        "logo": "resources/Navlogo.svg",
        "person": "resources/Personikon.svg",
        "checkboks": "resources/Checkboks.svg",
    },
}
