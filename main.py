import whisper

def transcribe_audio(audio_path):
    print("Loading model...")
    model = whisper.load_model("small")  # Options: tiny, base, small, medium, large

    print(f"Transcribing file: {audio_path}")
    result = model.transcribe(audio_path)

    print("\nTranscribed Text:\n")
    print(result["text"])

    with open("transcription_output.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])
    print("\nTranscription saved to 'transcription_output.txt'")

# Correct file path
audio_file_path = "C:/Users/satya/pythonProject/venv/audio.m4a"
transcribe_audio(audio_file_path)
