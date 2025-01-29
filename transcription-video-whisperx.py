import os
import warnings
import torch
import whisperx
from moviepy import VideoFileClip

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

def extract_audio(video_path, output_audio="audio.mp3"):
    try:
        print("[INFO] Extracting audio...")
        video = VideoFileClip(video_path)
        abs_audio_path = os.path.abspath(output_audio)
        video.audio.write_audiofile(abs_audio_path, logger=None)  # Elimina 'verbose'
        print(f"[SUCCESS] Audio saved as {abs_audio_path}")
        return abs_audio_path
    except Exception as e:
        print(f"[ERROR] Extracting audio: {e}")
        return None


def transcribe_audio(audio_file):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    compute_type = "float16" if torch.cuda.is_available() else "int8"  # Mejor rendimiento en CPU
    
    try:
        print("[INFO] Loading WhisperX model...")
        model = whisperx.load_model("medium", device, compute_type=compute_type)  # Modelo más rápido
        
        print("[INFO] Loading audio...")
        audio = whisperx.load_audio(audio_file)
        
        print("[INFO] Starting transcription...")
        result = model.transcribe(audio, language="es")
        
        print("[INFO] Aligning transcription...")
        align_model, metadata = whisperx.load_align_model(language_code="es", device=device)
        aligned_result = whisperx.align(result["segments"], align_model, metadata, audio, device)
        
        transcription = "\n".join([seg["text"] for seg in aligned_result["segments"]])
        print("[SUCCESS] Transcription completed.")
        
        return transcription
    except RuntimeError as e:
        print(f"[ERROR] {e}")
        return None

if __name__ == "__main__":
    video_path = "videoplayback.mp4"
    
    if not os.path.exists(video_path):
        print(f"[ERROR] Video file \"{video_path}\" not found.")
    else:
        audio_file = extract_audio(video_path, "audio.mp3")
        if audio_file:
            transcription = transcribe_audio(audio_file)
            if transcription:
                with open("transcription-whisperX.txt", "w", encoding="utf-8") as file:
                    file.write(transcription)
                print("[SUCCESS] Transcription saved to 'transcription-whisperX.txt'")
            
            if os.path.exists(audio_file):
                os.remove(audio_file)
