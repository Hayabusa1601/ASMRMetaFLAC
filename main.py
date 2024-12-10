import os, io
from dlsite_data_collector import dlsite_data_collector
from wav_to_flac import wav_to_flac
import time
import tkinter as tk
import tkinter.filedialog
#import tkinter

def main():
  # ルートウィンドウの非表示
  # 入力
  #wav_file = input("wavファイルの読み込み:")
  print("====asmr2flac====")
  print("wavファイルが格納されているフォルダを選択してください。")
  time.sleep(1)
  wav_folder_path = tkinter.filedialog.askdirectory()

  # アートワークの入手
  artwork_filepath = dlsite_data_collector()


  # メタデータの入力
  artist_name = input("artist name?: ")
  album_artist_name = input("album artist name?:")
  genre_name = input("genre name?: ")


  # 処理
  for filename in os.listdir(wav_folder_path):
    if filename.lower().endswith('.wav'):
      print("Converting...")
      input_file = os.path.join(wav_folder_path, filename)
      output_file = wav_to_flac(input_file,artist_name, album_artist_name, genre_name,artwork_filepath)
      print(f"{output_file}")
      print("Converted")
      

  print("Success")


if __name__ == "__main__":
  main()