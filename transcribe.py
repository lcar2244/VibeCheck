from faster_whisper import WhisperModel
from pathlib import Path

AUDIO_PATH = Path("data/raw/audio/videoplayback.wav")
OUTPUT_PATH = Path("data/processed/videoplayback_transcript.txt")

def main():
    model = WhisperModel("small", compute_type="int8")
    segments, info = model.transcribe(
        str(AUDIO_PATH),
        beam_size=5,
        vad_filter=True
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for segment in segments:
            line = f"[{segment.start:.2f} - {segment.end:.2f}] {segment.text.strip()}\n"
            f.write(line)

    print(f"Transcript saved to {OUTPUT_PATH}")
    print(f"Detected language: {info.language}")

if __name__ == "__main__":
    main()
