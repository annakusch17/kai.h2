import os
import json
from PyPDF2 import PdfReader

def preprocess_pdfs(folder_path, output_file):
    """
    Liest alle PDFs in einem Ordner, extrahiert den Text und speichert ihn als JSON.
    """
    all_text_chunks = []
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            print(f"Verarbeite: {file_name}")
            pdf_path = os.path.join(folder_path, file_name)
            
            try:
                reader = PdfReader(pdf_path)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                
                # Text in kleinere Abschnitte (Chunks) teilen
                chunks = [text[i:i+1500] for i in range(0, len(text), 1500)]
                all_text_chunks.extend(chunks)
            except Exception as e:
                print(f"Fehler beim Verarbeiten von {file_name}: {e}")
    
    # Ergebnisse in einer JSON-Datei speichern
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_text_chunks, f, ensure_ascii=False, indent=2)
    
    print(f"Alle Dokumente verarbeitet. Anzahl der Chunks: {len(all_text_chunks)}")
    print(f"Daten gespeichert in: {output_file}")

if __name__ == "__main__":
    preprocess_pdfs("SPO_Dokumente", "processed_documents.json")