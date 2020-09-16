import os
from pydub import AudioSegment


def combine_multiple_audio(directory, combined_audio_name="CombinedAudio.wav"):
    combined_audio_name = f"{directory}/{combined_audio_name}"
    audio_files = list()
    for filename in sorted(os.listdir(directory)):
        if filename[-4:] == '.wav':
            audio_files.append(AudioSegment.from_wav(f"{directory}/{filename}"))
    if audio_files:
        combined_audio = sum(audio_files)
        combined_audio.export(combined_audio_name, format="wav")


if __name__ == "__main__":
    combine_multiple_audio("/home/trsuser/Documents/PycharmProjects/audio/Audios")
