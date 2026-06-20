import pyttsx3
import PyPDF2
import time

def speak():
    try:
        book = open('Your PDF File Path', 'rb')
        pdfReader = PyPDF2.PdfReader(book)
        pages = len(pdfReader.pages)
        
        engine = pyttsx3.init()
        
        # Collect all text first
        all_text = []
        for i in range(pages):
            page = pdfReader.pages[i]
            text = page.extract_text()
            if text and text.strip():
                all_text.append(f"Page {i+1}: {text}")
                print(f"Page {i+1}: {text[:100]}...")  # Preview first 100 chars
            else:
                all_text.append(f"Page {i+1}: [No readable text]")
                print(f"Page {i+1}: No text found")
        
        book.close()
        
        # Speak all text together
        full_text = ". ".join(all_text)
        print("\nSpeaking all pages...")
        engine.say(full_text)
        engine.runAndWait()
        
        print("Finished reading.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    speak()