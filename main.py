import os
from pydub import AudioSegment # ffmpegが必要
from mutagen.flac import FLAC

def main():
  # 入力
  #wav_file = input("wavファイルの読み込み:")
  wav_folder_path = "test/"

  track_count = 1
  for filename in os.listdir(wav_folder_path):
    if filename.lower().endswith('.wav'):
      input_file = os.path.join(wav_folder_path, filename)
      output_file = wav_to_flac(input_file)
      print("track" + str(track_count) + ": " + f"{output_file}")
      print("Converted")
      track_count += 1
      

  print("Success")



# wavからflac
def wav_to_flac(wav_path):

  # === ファイルの前処理 ===
  # フォルダ名とファイル名に分割
  input_folder, input_filename = os.path.split(wav_path) 
  # ファイル名と拡張子に分割 
  file_name, _ = os.path.splitext(input_filename)

  # アルバム名の取得
  album_name = os.path.basename(input_folder)

  # === 出力先の設定 === 
  # Musicフォルダ内の出力先のパスを取得
  home_dir = os.path.expanduser("~")
  output_folder = os.path.join(home_dir, "Music", album_name)

  # Musicフォルダが存在しない場合は作成
  os.makedirs(output_folder, exist_ok=True)

  # 出力ファイル名の設定
  output_file = os.path.join(output_folder, f"{file_name}.flac")

  # === 読み込み === 
  # wavの読み込み
  audio = AudioSegment.from_wav(wav_path)

  # flacに変換
  audio.export(output_file, format='flac')


  # メタデータの追加
  flac_audio = FLAC(output_file)
  flac_audio["TITLE"] = file_name
  flac_audio["ALBUM"] = album_name
  flac_audio.save()

  return output_file





if __name__ == "__main__":
  main()