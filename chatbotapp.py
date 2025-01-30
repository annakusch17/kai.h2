import streamlit as st
from transformers import pipeline

# Vorab extrahierte Daten zu den Studiengängen
structured_data = {
    "Elektrotechnik": {
        "Regelstudienzeit": "6 Semester",
        "ECTS": 180,
        "Prüfungsarten": ["Klausur", "Projekt", "Präsentation"],
        "Praxissemester": "5. Semester",
        "Bachelorarbeit": {
            "ECTS": 12,
            "Voraussetzungen": "Alle Pflichtmodule müssen bestanden sein"
        },
        "Berufsperspektiven": [
            "Elektrotechnik",
            "Automatisierungstechnik",
            "Forschung und Entwicklung"
        ],
        "Module": [
            {"Name": "Grundlagen der Elektrotechnik", "Prüfungsform": "Klausur", "Semester": 1},
            {"Name": "Mathematik für Ingenieure", "Prüfungsform": "Klausur", "Semester": 1},
            {"Name": "Elektronik", "Prüfungsform": "Projekt", "Semester": 2},
            {"Name": "Physik für Ingenieure", "Prüfungsform": "Klausur", "Semester": 2},
            {"Name": "Schaltungstechnik", "Prüfungsform": "Klausur", "Semester": 3}
        ],
        "Abschluss": "Bachelor of Science (B.Sc.)"
    },
    "Maschinenbau": {
        "Regelstudienzeit": "7 Semester",
        "ECTS": 210,
        "Prüfungsarten": ["Klausur", "Projekt"],
        "Praxissemester": "6. Semester",
        "Bachelorarbeit": {
            "ECTS": 15,
            "Voraussetzungen": "Praktikum und 75% der Module müssen bestanden sein"
        },
        "Berufsperspektiven": [
            "Konstruktion",
            "Fertigungstechnik",
            "Forschung und Entwicklung"
        ],
        "Module": [
            {"Name": "Technische Mechanik", "Prüfungsform": "Klausur", "Semester": 1},
            {"Name": "Mathematik für Ingenieure", "Prüfungsform": "Klausur", "Semester": 1},
            {"Name": "Werkstoffkunde", "Prüfungsform": "Projekt", "Semester": 2},
            {"Name": "Maschinenkonstruktion", "Prüfungsform": "Projekt", "Semester": 3},
            {"Name": "Thermodynamik", "Prüfungsform": "Klausur", "Semester": 3}
        ],
        "Abschluss": "Bachelor of Science (B.Sc.)"
     },
    "Wirtschaftsingenieurwesen": {
        "Regelstudienzeit": "7 Semester",
        "ECTS": 210,
        "Prüfungsarten": ["Klausur", "Projekt", "Präsentation"],
        "Praxissemester": "6. Semester",
        "Bachelorarbeit": {
            "ECTS": 15,
            "Voraussetzungen": "Mindestens 75% der Module müssen bestanden sein"
        },
        "Berufsperspektiven": [
            "Produktion",
            "Logistik",
            "Controlling"
        ],
        "Module": [
            {"Name": "Grundlagen der BWL", "Prüfungsform": "Klausur", "Semester": 1},
            {"Name": "Mathematik für Ingenieure", "Prüfungsform": "Klausur", "Semester": 1},
            {"Name": "Statistik", "Prüfungsform": "Klausur", "Semester": 2},
            {"Name": "Projektmanagement", "Prüfungsform": "Projekt", "Semester": 3},
            {"Name": "Logistik", "Prüfungsform": "Klausur", "Semester": 4}
        ],
        "Abschluss": "Bachelor of Science (B.Sc.)"
    },
    "Mensch-Technik-Interaktion": {
        "Regelstudienzeit": "6 Semester",
        "ECTS": 180,
        "Prüfungsarten": ["Klausur", "Projekt", "Präsentation"],
        "Praxissemester": "5. Semester",
        "Bachelorarbeit": {
            "ECTS": 12,
            "Voraussetzungen": "Alle Pflichtmodule müssen bestanden sein"
        },
        "Berufsperspektiven": [
            "User Experience Design",
            "Usability Engineering",
            "Interaktionsdesign"
        ],
        "Module": [
            {"Name": "Grundlagen der Informatik", "Prüfungsform": "Klausur", "Semester": 1},
            {"Name": "Psychologie der Interaktion", "Prüfungsform": "Projekt", "Semester": 2},
            {"Name": "User Experience Design", "Prüfungsform": "Projekt", "Semester": 3},
            {"Name": "Technikethik", "Prüfungsform": "Präsentation", "Semester": 4},
            {"Name": "Prototyping", "Prüfungsform": "Projekt", "Semester": 5}
        ],
        "Abschluss": "Bachelor of Science (B.Sc.)"
    },
    "Mechatronische Systemtechnik": {
        "Regelstudienzeit": "7 Semester",
        "ECTS": 210,
        "Prüfungsarten": ["Klausur", "Projekt"],
        "Praxissemester": "6. Semester",
        "Bachelorarbeit": {
            "ECTS": 15,
            "Voraussetzungen": "Alle Pflichtmodule und Praxissemester abgeschlossen"
        },
        "Berufsperspektiven": [
            "Automatisierung",
            "Robotik",
            "Forschung und Entwicklung"
        ],
        "Module": [
            {"Name": "Grundlagen der Mechatronik", "Prüfungsform": "Klausur", "Semester": 1},
            {"Name": "Robotik", "Prüfungsform": "Projekt", "Semester": 3},
            {"Name": "Steuerungstechnik", "Prüfungsform": "Projekt", "Semester": 4},
            {"Name": "Fertigungsautomatisierung", "Prüfungsform": "Projekt", "Semester": 5},
            {"Name": "Sensorik und Aktorik", "Prüfungsform": "Klausur", "Semester": 6}
        ],
        "Abschluss": "Bachelor of Science (B.Sc.)"
    },
    "Industriedesign": {
        "Regelstudienzeit": "7 Semester",
        "ECTS": 210,
        "Prüfungsarten": ["Projekt", "Präsentation"],
        "Praxissemester": "5. Semester",
        "Bachelorarbeit": {
            "ECTS": 12,
            "Voraussetzungen": "Alle Pflichtmodule und Praxissemester abgeschlossen"
        },
        "Berufsperspektiven": [
            "Produktdesign",
            "Interfacedesign",
            "Forschung und Entwicklung"
        ],
        "Module": [
            {"Name": "Designgrundlagen", "Prüfungsform": "Projekt", "Semester": 1},
            {"Name": "Material- und Fertigungstechnik", "Prüfungsform": "Projekt", "Semester": 2},
            {"Name": "User Interface Design", "Prüfungsform": "Präsentation", "Semester": 3},
            {"Name": "Designgeschichte", "Prüfungsform": "Präsentation", "Semester": 4},
            {"Name": "Innovationsmanagement", "Prüfungsform": "Projekt", "Semester": 5}
        ],
        "Abschluss": "Bachelor of Arts (B.A.)"
    },
}

# Sprachmodell initialisieren
qa_model = pipeline("text2text-generation", model="google/flan-t5-base")

# Funktion zur Beantwortung von Fragen
def find_answer_in_data(question, data):
    """
    Beantwortet die Frage basierend auf den vorab definierten Daten.
    """
    question = question.lower()

    if "regelstudienzeit" in question:
        return f"Die Regelstudienzeit beträgt {data.get('Regelstudienzeit', 'nicht gefunden')}."

    if "module" in question:
        modules = data.get("Module", [])
        return "\n".join([f"- {m['Name']} ({m['Prüfungsform']}, {m['Semester']}. Semester)" for m in modules]) if modules else "Keine Module gefunden."

    if "ects" in question or "credits" in question:
        return f"Der Studiengang umfasst {data.get('ECTS')} ECTS."

    if "prüfungsarten" in question:
        pruefungsarten = data.get("Prüfungsarten", [])
        return "Die Prüfungsarten im Studiengang umfassen:\n" + "\n".join(f"- {p}" for p in pruefungsarten)

    if "praxissemester" in question:
        return f"Das Praxissemester findet im {data.get('Praxissemester', 'nicht gefunden')} statt."

    if "bachelorarbeit" in question:
        bachelor = data.get("Bachelorarbeit", {})
        ects = bachelor.get("ECTS", "keine Angabe")
        voraussetzungen = bachelor.get("Voraussetzungen", "keine Angabe")
        return f"Die Bachelorarbeit umfasst {ects} ECTS. Voraussetzungen: {voraussetzungen}."

    if "berufsperspektiven" in question or "beruf" in question:
        perspektiven = data.get("Berufsperspektiven", [])
        return "Die Berufsperspektiven umfassen:\n" + "\n".join(f"- {p}" for p in perspektiven)

    return None  # Fallback für das Sprachmodell

# Streamlit App
def main():
    st.set_page_config(
        page_title="Studiengangs-Chatbot",
        page_icon="🎓",
        layout="wide"
    )

    st.sidebar.image("KAI.Logo-removebg-preview.png", use_column_width=True)
    st.sidebar.title("Über KAI")
    st.sidebar.info("KAI - Dein Studiengangs-Chatbot für den Fachbereich IWID!")
    
    st.title("🎓 Willkommen zum Studiengangs-Chatbot der H2")
    st.subheader("Stelle Fragen zu den Studiengängen des Fachbereichs IWID!")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("🔍 Studiengangsinformationen")
        program = st.selectbox("Wähle einen Studiengang:", list(structured_data.keys()))
        question = st.text_input("❓ Stelle deine Frage:", placeholder="Beispiel: Welche Module gibt es?")
        if st.button("Antwort erhalten"):
            answer = find_answer_in_data(question, structured_data[program]) or "Ich konnte keine passende Antwort finden."
            st.success(f"📝 Antwort: {answer}")

    with col2:
        st.header("📘 Schnellübersicht")
        st.markdown(f"**Regelstudienzeit:** {structured_data[program]['Regelstudienzeit']}")
        st.markdown(f"**Praxissemester:** {structured_data[program]['Praxissemester']}")
        st.markdown(f"**Abschluss:** {structured_data[program]['Abschluss']}")

if __name__ == "__main__":
    main()
