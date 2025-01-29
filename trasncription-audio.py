import os
import warnings
import whisper

# Ignorar advertencias
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

def transcribe_audio(audio_file):
    try:
        # Cargar el modelo de Whisper
        model = whisper.load_model("base")
        print("Transcribing... Please wait.")
        result = model.transcribe(audio_file, language="es")
        transcription = result['text']
        print("Transcription completed.")
        return transcription
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Ruta al archivo de audio
    audio_file = "audioplayback.mp3"

    if not os.path.exists(audio_file):
        print(f"Error: Audio file \"{audio_file}\" not found.")
    else:
        transcription = transcribe_audio(audio_file)
        if transcription:
            with open("transcription.txt", "w", encoding="utf-8") as file:
                file.write(transcription)
            print("Transcription saved to 'transcription.txt'")
