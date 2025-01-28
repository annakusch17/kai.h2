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
qa_model = pipeline("text2text-generation", model="google/flan-t5-xl")  # Größeres Modell für detailliertere Antworten

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


# Haupt-Chatbot-Logik
def chatbot():
    """
    Hauptlogik des Chatbots, der die extrahierten Daten nutzt und das Sprachmodell als Fallback verwendet.
    """
    print("Willkommen beim Studien- und Prüfungsordnungs-Chatbot!")
    print("Zu welchem Studiengang des Fachbereichs IWID hast du Fragen?")
    
    selected_program = None
    while not selected_program:
        user_input = input("Gib den Studiengang ein (z. B. 'Maschinenbau', 'Elektrotechnik'): ").strip().capitalize()
        if user_input in structured_data:
            selected_program = structured_data[user_input]
            print(f"Du hast den Studiengang '{user_input}' ausgewählt.")
        else:
            print("Dieser Studiengang wurde nicht gefunden. Bitte versuche es erneut.")

    print("\nStelle deine Fragen (z. B. 'Wie lange ist die Regelstudienzeit?', 'Welche Module gibt es?').")
    print("Gib 'exit' oder 'quit' ein, um den Chat zu beenden.")

    while True:
        question = input("\nDeine Frage: ").strip()
        if question.lower() in ["exit", "quit"]:
            print("Vielen Dank, dass du den Chatbot genutzt hast!")
            break

        # Suche Antwort in den Daten
        answer = find_answer_in_data(question, selected_program)
        if answer is not None:
            print("\nAntwort:", answer)
        else:
            # Nutze das Sprachmodell als Fallback
            context = (
                f"Studiengangsinformationen:\nRegelstudienzeit: {selected_program['Regelstudienzeit']}\n"
                f"ECTS: {selected_program['ECTS']}\n"
                f"Module: {', '.join([m['Name'] for m in selected_program['Module']])}\n"
                f"Praxissemester: {selected_program['Praxissemester']}\n"
                f"Berufsperspektiven: {', '.join(selected_program['Berufsperspektiven'])}"
            )
            model_response = qa_model(
                f"Frage: {question} Kontext: {context}",
                max_length=300,
                do_sample=True,
                temperature=0.9,
                top_p=0.95
            )
            print("\nAntwort (Sprachmodell):", model_response[0]['generated_text'])


if __name__ == "__main__":
    chatbot()