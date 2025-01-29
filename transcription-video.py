import os
import warnings
import whisper
from moviepy import VideoFileClip

# Ignore warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

def extract_audio_from_video(video_file, audio_file="extracted_audio.mp3"):
    """
    Extracts audio from a video file and saves it as an MP3 file.
    
    Args:
        video_file (str): Path to the video file.
        audio_file (str): Path to save the extracted audio file.
    
    Returns:
        str: Path to the extracted audio file, or None if an error occurs.
    """
    try:
        print("Extracting audio from video...")
        # Load the video file
        video = VideoFileClip(video_file)
        # Extract the audio and save it as an MP3 file
        video.audio.write_audiofile(audio_file)
        print(f"Audio extracted and saved as {audio_file}")
        return audio_file
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return None

def transcribe_audio(audio_file):
    """
    Transcribes an audio file using the Whisper model.
    
    Args:
        audio_file (str): Path to the audio file.
    
    Returns:
        str: The transcribed text, or None if an error occurs.
    """
    try:
        # Load the Whisper model
        model = whisper.load_model("base")
        print("Transcribing... Please wait.")
        # Transcribe the audio file
        result = model.transcribe(audio_file, language="es")
        transcription = result['text']
        print("Transcription completed.")
        return transcription
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Path to the media file (video or audio)
    media_file = "videoplayback.mp4"  # Change this to the file you want to process

    # Check if the media file exists
    if not os.path.exists(media_file):
        print(f"Error: Media file \"{media_file}\" not found.")
    else:
        # Check if the file is a video
        if media_file.endswith((".mp4", ".avi", ".mov", ".mkv")):
            # Extract audio from the video
            audio_file = extract_audio_from_video(media_file)
            if not audio_file:
                exit(1)
        else:
            # If it's already an audio file, use it directly
            audio_file = media_file

        # Transcribe the audio file
        transcription = transcribe_audio(audio_file)
        if transcription:
            # Save the transcription to a text file
            with open("transcription.txt", "w", encoding="utf-8") as file:
                file.write(transcription)
            print("Transcription saved to 'transcription.txt'")