import os, io
from dlsite_data_collector import dlsite_data_collector
from wav_to_flac import wav_to_flac
import time
import tkinter as tk
import tkinter.filedialog

def btn_apply():
  id = txt_id.get()
  


def main():
  
  # 入力
  #wav_file = input("wavファイルの読み込み:")
  print("====dlsite2flac====")
  print("wavファイルが格納されているフォルダを選択してください。")
  time.sleep(1)
  wav_folder_path = tkinter.filedialog.askdirectory()

  # ウィンドウの表示
  root = tk.Tk()
  root.geometry("500x500")
  # 画面タイトル　
  root.title("dlsite2flac")
  # idの入力
  lbl_id = tk.Label(text="id (RJを含む)")
  lbl_id.place(x=30, y=70)


  txt_id = tkinter.Entry(width=20)
  txt_id.place(x=150,y=70)

  btn = tkinter.Button(root, text="apply", commant=btn_apply)
  btn.place(x=140, y=170)

  #表示
  root.mainloop()


  # アートワークの入手
  artwork_filepath = dlsite_data_collector(txt_id.get)


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