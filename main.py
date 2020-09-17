import os
from pydub import AudioSegment


def combine_multiple_audio(combined_filename="CombinedAudio.wav", directory=''):
    combined_audio_name = f"{directory}/{combined_filename}"
    audio_files = list()
    for filename in sorted(os.listdir(directory)):
        if filename[-4:] == '.wav':
            audio_files.append(AudioSegment.from_wav(f"{directory}/{filename}"))
    if audio_files:
        combined_audio = sum(audio_files)
        combined_audio.export(combined_audio_name, format="wav")


def cut_audio_files(filename, intervals, directory=''):
    if not intervals:
        return
    intervals.sort()
    audio = AudioSegment.from_wav(f"{directory}/{filename}")
    intervals_size = len(intervals)
    if intervals_size == 1:
        new_audio1 = audio[:intervals[0] * 1000]
        new_audio2 = audio[intervals[0] * 1000:]
        new_audio1.export(f'{directory}/0_{intervals[0]}.wav', format="wav")
        new_audio2.export(f'{directory}/{intervals[0]}_.wav', format="wav")
    else:
        new_audio = audio[:intervals[0] * 1000]
        new_audio.export(f'{directory}/0_{intervals[0]}.wav', format="wav")

        new_audio = audio[intervals[intervals_size - 1] * 1000:]
        new_audio.export(f'{directory}/{intervals[intervals_size - 1]}_.wav', format="wav")

        for i in range(intervals_size - 1):
            new_audio = audio[intervals[i] * 1000:intervals[i + 1] * 1000]
            new_audio.export(f'{directory}/{intervals[i]}_{intervals[i + 1]}.wav', format="wav")


def reversed_audio(filename, directory=''):
    audio = AudioSegment.from_wav(f"{directory}/{filename}")
    new_audio = audio.reverse()
    new_audio.export(f'{directory}/reversed_{filename}.wav', format="wav")


if __name__ == "__main__":
    directory = "/"
    combine_multiple_audio(directory=directory)
    cut_audio_files(filename="file.wav", intervals=[], directory=directory)
    reversed_audio(filename="file.wav", directory=directory)
