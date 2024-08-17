import os, io

from dlsite_data_collector import dlsite_data_collector
from wav_to_flac import wav_to_flac



def main():
  # 入力
  #wav_file = input("wavファイルの読み込み:")
  wav_folder_path = input("folder path?:")

  # アートワークの入手
  artwork_filepath = dlsite_data_collector()


  # メタデータの入力
  album_artist_name = input("album artist name?:")
  genre_name = input("genre name?: ")


  # 処理
  for filename in os.listdir(wav_folder_path):
    if filename.lower().endswith('.wav'):
      input_file = os.path.join(wav_folder_path, filename)
      output_file = wav_to_flac(input_file, album_artist_name, genre_name,artwork_filepath)
      print(f"{output_file}")
      print("Converted")
      

  print("Success")


if __name__ == "__main__":
  main()