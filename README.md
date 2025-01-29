# 🎓 Studiengangs-Chatbot der H2

Willkommen zum **Studiengangs-Chatbot der Hochschule Magdeburg-Stendal**!  
Dieser Chatbot hilft Studierenden, Informationen zu verschiedenen Studiengängen im Fachbereich IWID zu erhalten.  

Er beantwortet Fragen zur **Regelstudienzeit, Prüfungsarten, Modulen, Berufsperspektiven und mehr**.

---

## 🚀 **Funktionen**
✅ **Studiengang auswählen** (Elektrotechnik, Maschinenbau, Wirtschaftsingenieurwesen, u. a.)  
✅ **Fragen zur Studienordnung stellen**  
✅ **Antworten basierend auf vorab extrahierten Informationen**  
✅ **Schön gestaltete Streamlit-Webseite mit Icons & Farben**  
✅ **Backup-Antworten durch KI-Modell (Google FLAN-T5)**  

---

## 🛠️ **Installation & Setup**
### **1️⃣ Repository klonen**
Falls du das Repository noch nicht hast, klone es:
```bash
git clone https://github.com/annakusch17/kai.h2.git
cd kai.h2
```

### **2️⃣ Python & Abhängigkeiten installieren**
Stelle sicher, dass du **Python 3.8 oder neuer** installiert hast. Installiere dann die benötigten Bibliotheken:
```bash
pip install -r requirements.txt
```

Falls **Streamlit** nicht installiert ist:
```bash
pip install streamlit
```

Falls **Transformers** (Hugging Face) fehlt:
```bash
pip install transformers
```

---

## 🎮 **Chatbot starten**
Führe den Chatbot mit **Streamlit** aus:
```bash
streamlit run chatbotapp.py
```

Anschließend öffnet sich der Chatbot in deinem Browser.

---

## 📚 **Unterstützte Studiengänge**
Dieser Chatbot enthält detaillierte Informationen für folgende Studiengänge:

| Studiengang                        | Regelstudienzeit | Abschluss       |
|-------------------------------------|-----------------|----------------|
| **Elektrotechnik**                  | 6 Semester      | B.Sc.          |
| **Maschinenbau**                    | 7 Semester      | B.Sc.          |
| **Wirtschaftsingenieurwesen**       | 7 Semester      | B.Sc.          |
| **Mensch-Technik-Interaktion**      | 6 Semester      | B.Sc.          |
| **Mechatronische Systemtechnik**    | 7 Semester      | B.Sc.          |
| **Industriedesign**                 | 7 Semester      | B.A.           |

---

## 🖥 **Funktionen im Detail**
🔹 **Regelstudienzeit anzeigen**: „Wie lange dauert das Studium?“  
🔹 **Prüfungsarten abrufen**: „Welche Prüfungsarten gibt es?“  
🔹 **Module auflisten**: „Welche Module sind enthalten?“  
🔹 **Berufsperspektiven**: „Welche Jobs kann ich damit machen?“  
🔹 **Backup-Antworten** durch das KI-Modell Google FLAN-T5  

---

## 🎭 **Design-Verbesserungen**
✅ **Moderne Streamlit-Oberfläche**  
✅ **Farbige Infoboxen & Icons für Lesbarkeit**  
✅ **Schnellübersicht des Studiengangs in der Seitenleiste**  
✅ **Klare strukturierte Antworten für bessere Nutzerführung**  

---

## 👨‍💻 **Entwickler & Beitragende**
💡 Entwickelt von **Anna Kusch, Nico Seidenberg und Deniz Benckenstein** 

📍 **Hochschule Magdeburg-Stendal**  

👨🏻‍🏫 **Prof. Dr.-Ing Freiherr von Enzberg**

💻 **KI umsetzen mit Python**

---

## 💡 **Mögliche Erweiterungen**
✅ **Mehr Studiengänge hinzufügen**  
✅ **Erweiterte KI-Modelle für bessere Antworten**  
✅ **Sprachunterstützung für internationale Studierende**  

---

## 🔗 **Links & Ressourcen**
- 📌 **GitHub-Repository**: [https://github.com/annakusch17/kai.h2.git](https://github.com/annakusch17/kai.h2.git)  
- 📝 **Dokumentation für Streamlit**: [https://docs.streamlit.io](https://docs.streamlit.io)  
- 🤖 **Hugging Face Modelle**: [https://huggingface.co/models](https://huggingface.co/models)  

---


Jede*r, der möchte, darf den Code verwenden, ändern und verbessern! 😊

---

🎉 **Viel Spaß beim Erkunden deines Studiengangs mit diesem Chatbot! 🚀**

