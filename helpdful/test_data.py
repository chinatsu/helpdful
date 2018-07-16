from datetime import datetime

data = {
    "title": "Søknad om å beholde sykepenger utenfor Norge",
    "date": datetime(2017, 2, 1),
    "application_id": "3c87f6e2-66ee-4376-9d4d-2444dea8368e",
    "person": {
        "id": 12068745698,
        "name": "Kari Normann Paulsrud Granholt"
    },
    "questions": [
        {
            "text": "Når skal du oppholde deg utenfor Norge?",
            "type": "PERIODER",
            "answer": "01.01.2017 – 31.01.2017"
        },
        {
            "text": "Hvilket land skal du reise til?",
            "type": "LAND",
            "answer": "Tyskland"
        },
        {
            "text": "Har du arbeidsgiver?",
            "type": "CHECKBOKS",
            "answer": "Ja"
        },
        {
            "text": "Er du 100% sykmeldt?",
            "type": "CHECKBOKS",
            "answer": "Ja"
        },
        {
            "text": "Før du reiser må du bekrefte at",
            "information": [
                "Oppholdet utenfor Norge ikke medfører at helsetilstanden din blir forverret",
                "Oppholdet utenfor Norge ikke vil forlenge arbeidsuførheten din eller hindre planlagt behandling",
                "Du har avklart dette med sykmelderen din"
            ],
            "type": "IKKE_RELEVANT",
            "answer": "Jeg bekrefter at jeg har gjort med kjent med pliktene mine"
        }
    ],
}

theme = {
    "footer": {
        "height": 20,
    },
    "page_margin": 40,
    "header": {
        "background": (0.2146, 0.0526, 0.0, 0.0314),
        "logo": {
            "scale": 0.8,
            "margin_right": 4,
        },
        "color": (0, 0, 0, 1),
        "font_size": 16,
        "font_weight": "700",
        "base_height": 43,
        "margin_bottom": 40,
    },
    "information": {
        "name": {
            "font_size": 14,
            "font_weight": "700",
        },
        "id": {
            "font_size": 12,
            "font_weight": "regular",
        },
        "date": {
            "font_size": 8,
            "font_weight": "regular",
        }
    },
    "icon_margin": 10,
    "images": {
        "logo": "resources/Navlogo.svg",
        "person": "resources/Personikon.svg",
        "checkboks": "resources/Checkboks.svg",
    }
}
