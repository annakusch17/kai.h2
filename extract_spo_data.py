import os
import re
import json
from PyPDF2 import PdfReader


def extract_text_from_pdf(file_path):
    """
    Extrahiert den Text aus einer PDF-Datei.
    """
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def process_spo(file_path, study_program):
    """
    Verarbeitet eine einzelne SPO-Datei und extrahiert wichtige Informationen.
    """
    text = extract_text_from_pdf(file_path)

    data = {
        "Studiengang": study_program,
        "Ziele": [
            "Entwicklung von Kompetenzen für aktuelle und zukünftige Herausforderungen im Studienbereich.",
            "Verknüpfung von Theorie und Praxis zur Förderung der Berufsfähigkeit."
        ],
        "Regelstudienzeit": "Nicht gefunden",
        "ECTS": 0,
        "Studienaufbau": {
            "Module": [],
            "Praxissemester": "Nicht gefunden",
            "Abschlussarbeit": "Nicht gefunden"
        },
        "Prüfungsanforderungen": {
            "Modulprüfungen": [],
            "Bestehen": "Nicht gefunden",
            "Wiederholungen": "Nicht gefunden"
        },
        "Besonderheiten": [
            "Praxisorientierung und Interdisziplinarität."
        ],
        "Abschluss": {
            "Grad": "Bachelor of Science (B.Sc.)",
            "Voraussetzungen": [
                "Erfolgreiche Absolvierung aller Module",
                "Abschluss der Bachelorarbeit"
            ]
        }
    }

    # Regelstudienzeit
    match = re.search(r"Regelstudienzeit.*?(\d+ Semester)", text, re.IGNORECASE)
    if match:
        data["Regelstudienzeit"] = match.group(1)

    # ECTS
    match = re.search(r"(\d+)\s*ECTS", text, re.IGNORECASE)
    if match:
        data["ECTS"] = int(match.group(1))

    # Module
    modules = re.findall(r"Modul[-\s]*Nr\.\s*\d+\s*(.*?)\s*(?:ECTS|Credits).*?(Klausur|mündlich|Projekt)", text, re.IGNORECASE)
    for module in modules:
        data["Studienaufbau"]["Module"].append({
            "Name": module[0].strip(),
            "Prüfungsform": module[1].strip(),
            "Semester": "Nicht angegeben"
        })

    # Prüfungsanforderungen
    if "Wiederholung" in text:
        data["Prüfungsanforderungen"]["Wiederholungen"] = "Prüfungen können wiederholt werden"

    if "Note" in text:
        data["Prüfungsanforderungen"]["Bestehen"] = "Mindestens die Note 'ausreichend' (4,0)"

    return data


# Studiengänge und zugehörige Dateien
study_programs = [
    {"file": "SPO_Dokumente/AB_28_2022_Erste_AEnd_u_AST_SPO_BA_ET.pdf", "program": "Elektrotechnik"},
    {"file": "SPO_Dokumente/AB_30_2022_Erste_AEnd_u_AST_SPO_BA_MB.pdf", "program": "Maschinenbau"},
    {"file": "SPO_Dokumente/AB_31_2022_Erste_AEnd_u_AST_SPO_BA_MST.pdf", "program": "Mechatronische Systemtechnik"},
    {"file": "SPO_Dokumente/AB_32_2022_Erste_AEnd_u_AST_SPO_BA_WIW-2.pdf", "program": "Wirtschaftsingenieurwesen"},
    {"file": "SPO_Dokumente/1_SPO_BA_MTI_AB_23_2018-1.pdf", "program": "Mensch-Technik-Interaktion"}
]

# Verarbeitung aller Dateien
structured_data = {}
for entry in study_programs:
    structured_data[entry["program"]] = process_spo(entry["file"], entry["program"])

# Speichern der Ergebnisse in einer JSON-Datei
with open("structured_spo_data.json", "w", encoding="utf-8") as f:
    json.dump(structured_data, f, ensure_ascii=False, indent=4)

print("Extraktion abgeschlossen. Daten gespeichert in 'structured_spo_data.json'.")