from pydub import AudioSegment # ffmpegが必要

def main():

  # 入力
  wav_file = input("wavファイルの読み込み:")
  flac_file = "output.flac"

  print("converting wav to flac...")
  wav_to_flac(wav_file, flac_file)
  
  print("Success")



# wavからflac
def wav_to_flac(wav_file, flac_file):
  # wavの読み込み
  audio = AudioSegment.from_wav(wav_file)

  # flacに変換
  audio.export(flac_file, format='flac')


if __name__ == "__main__":
  main()