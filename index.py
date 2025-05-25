from PyPDF2 import PdfReader
from gtts import gTTS

def pdf_to_speech(pdf_path, audio_file):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            print(content)  # Verify text extraction
            if content:
                text += content
        if text:
            tts = gTTS(text=text, lang='en')
            tts.save(audio_file)
            print("Audio file saved successfully.")
        else:
            print("No text extracted from PDF.")
    except Exception as e:
        print(f"Error: {e}")

pdf_to_speech("Ms_Dhoni.pdf", "output.mp3")







