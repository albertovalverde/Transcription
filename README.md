# WhisperX Video Transcription

This Python script extracts audio from a video file and transcribes it using WhisperX, an optimized version of OpenAI's Whisper model.

## Features
- Extracts audio from an MP4 video using `moviepy`.
- Transcribes audio using WhisperX with automatic speech recognition (ASR).
- Aligns the transcription for improved accuracy.
- Saves the transcription as a text file.
- Supports GPU acceleration for faster processing.

## Requirements
Make sure you have the following dependencies installed:

```bash
pip install torch whisperx moviepy
```

## Usage
1. Place your video file in the script's directory.
2. Update the `video_path` variable in the script with the video filename.
3. Run the script:

```bash
python script.py
```

4. The transcription will be saved in `transcription-whisperX.txt`.

## How It Works
### Audio Extraction
- Uses `moviepy` to extract audio from the input video.
- Saves the extracted audio as an MP3 file.

### Transcription Process
- Loads WhisperX on the available device (GPU if supported, otherwise CPU).
- Adjusts computation precision (`float16` for GPU, `int8` for CPU).
- Performs automatic speech recognition (ASR) and aligns the transcription.
- Saves the final transcription to a text file.

### Cleanup
- The temporary audio file is deleted after processing to save storage.

## Notes
- Ensure you have a compatible GPU for optimal performance.
- The script is optimized for Spanish (`es`), but you can modify the language parameter for other languages.

## License
This project is released under the MIT License.
