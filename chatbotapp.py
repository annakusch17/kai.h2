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
    }
}

# Sprachmodell initialisieren
qa_model = pipeline("text2text-generation", model="google/flan-t5-xl")

# Funktion zur Beantwortung von Fragen
def find_answer_in_data(question, data):
    """
    Beantwortet die Frage basierend auf den vorab definierten Daten.
    """
    if "regelstudienzeit" in question.lower():
        return f"Die Regelstudienzeit des Studiengangs beträgt {data.get('Regelstudienzeit', 'nicht gefunden')}."

    if "module" in question.lower():
        modules = data.get("Module", [])
        if modules:
            return "Die Module des Studiengangs sind:\n" + "\n".join(
                [f"- {m['Name']} (Prüfungsform: {m['Prüfungsform']}, Semester: {m['Semester']})" for m in modules]
            )
        return "Es wurden keine Module gefunden."

    if "ects" in question.lower() or "credits" in question.lower():
        return f"Der Studiengang umfasst insgesamt {data.get('ECTS', 'keine Angaben')} ECTS."

    if "prüfungsarten" in question.lower():
        pruefungsarten = data.get("Prüfungsarten", [])
        return "Die Prüfungsarten im Studiengang umfassen:\n" + "\n".join(f"- {p}" for p in pruefungsarten)

    if "praxissemester" in question.lower():
        return f"Das Praxissemester findet im {data.get('Praxissemester', 'nicht gefunden')} statt."

    if "bachelorarbeit" in question.lower():
        bachelor = data.get("Bachelorarbeit", {})
        ects = bachelor.get("ECTS", "keine Angabe")
        voraussetzungen = bachelor.get("Voraussetzungen", "keine Angabe")
        return f"Die Bachelorarbeit umfasst {ects} ECTS. Voraussetzungen: {voraussetzungen}."

    if "berufsperspektiven" in question.lower():
        perspektiven = data.get("Berufsperspektiven", [])
        return "Die Berufsperspektiven umfassen:\n" + "\n".join(f"- {p}" for p in perspektiven)

    return None  # Fallback für das Sprachmodell


# Streamlit App
def main():
    st.title("Studien- und Prüfungsordnungs-Chatbot")
    st.subheader("Stelle deine Fragen zu den Studiengängen der Hochschule!")

    # Auswahl des Studiengangs
    program = st.selectbox("Wähle einen Studiengang:", list(structured_data.keys()))
    st.write(f"Du hast den Studiengang **{program}** ausgewählt.")

    # Eingabefeld für die Frage
    question = st.text_input("Stelle deine Frage:")
    if st.button("Frage beantworten"):
        if question.strip():
            # Suche in den Daten
            answer = find_answer_in_data(question, structured_data[program])
            if answer:
                st.success(f"Antwort: {answer}")
            else:
                # Sprachmodell als Fallback
                context = f"Studiengangsinformationen:\n{structured_data[program]}"
                model_response = qa_model(
                    f"Frage: {question} Kontext: {context}",
                    max_length=300,
                    do_sample=True,
                    temperature=0.9,
                    top_p=0.95
                )
                st.success(f"Antwort (Sprachmodell): {model_response[0]['generated_text']}")
        else:
            st.warning("Bitte gib eine Frage ein.")

if __name__ == "__main__":
    main()