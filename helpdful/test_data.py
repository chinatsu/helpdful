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
