import os, io
from dlsite_data_collector import dlsite_data_collector
from wav_to_flac import wav_to_flac
import time
import tkinter as tk
import tkinter.filedialog

def btn_apply(txt_id, txt_artist_name, txt_album_artist, txt_genre_name,root, wav_folder_path):
  """
  作品id入力後の、applyボタン押下後の処理

  Parameters
  ----------
  txt_id : tkinterオブジェクト
    dlsiteの作品id入力
  txt_artist_name : tkinterオブジェクト
    アーティスト名入力
  txt_album_artist : tkinterオブジェクト
    アルバムアーティスト名入力
  txt_genre_name : tkinterオブジェクト
    ジャンル名入力
  root : tkinterオブジェクト
    GUIウィンドウ
  wav_folder_path : String 
    wavフォルダのパス
  """
  # tkinterオブジェクトからテキストを取得
  id = txt_id.get()
  artist_name = txt_artist_name.get()
  album_artist_name = txt_album_artist.get()
  genre_name = txt_genre_name.get()

  # idは最低限必要なので入力必須
  if not id:
    tkinter.messagebox.showerror("エラー", "IDが入力されていません")
    return
  
  root.destroy() # GUIウィンドウを一旦非表示

  print(f"ID:{id}の処理を開始...")
  #try:
  print("アートワークを取得中・・・")
  # アートワークの入手
  title, artwork_filepath = dlsite_data_collector(id)
  print(f"アートワークを保存しました。path:{artwork_filepath}")

  # ファイル返還処理
  found_wav_files = False
  for filename in os.listdir(wav_folder_path):
    if filename.lower().endswith('.wav'):
      found_wav_files = True

      print(f"\n変換中...:{filename}")
      # フォルダパスとファイル名から入力ファイルパスを取得
      input_file = os.path.join(wav_folder_path, filename)
      # 入力ファイル、アーティスト名、アルバムアーティスト名、ジャンル名、アートワーク画像のパス、作品タイトル(アルバム名になる)
      output_file = wav_to_flac(input_file,artist_name, album_artist_name, genre_name,artwork_filepath,title)
      print(f"\n返還完了: {output_file}")

  if not found_wav_files:
    print("=================================================")
    print("指定されたフォルダにwavファイルが見つかりませんでした")
    print("=================================================")

    
  print("\nすべての処理が終了しました")
  #except Exception as e:
  #  print(f"エラーが発生しました：{e}")
  #  tkinter.messagebox.showerror("エラー", f"処理中にエラーが発生しました：\n{e}")

    

def main():
  """
  DLSiteの作品に、作品idからアートワークとメタデータを入手するプログラムのメインプログラム
  """
  

  #wav_file = input("wavファイルの読み込み:")
  print("====dlsite2flac====")

  # ===== 入力 =====
  print("wavファイルが格納されているフォルダを選択してください。")
  time.sleep(1)

  # ウィンドウの表示
  root = tk.Tk()
  root.withdraw()

  # フォルダの選択
  wav_folder_path = tkinter.filedialog.askdirectory()
  if not wav_folder_path:
    print("フォルダが選択されませんでした")
    return
  
  root.deiconify()
  root.geometry("400x300")
  # 画面タイトル　
  root.title("dlsite2flac")
  # idの入力
  lbl_id = tk.Label(text="作品id (例：RJ123456)")
  lbl_id.place(x=30, y=70)

  txt_id = tkinter.Entry(width=20) # id入力欄の作成
  txt_id.place(x=180,y=70)

  # アーティスト名の入力
  lbl_artist_name = tk.Label(text="アーティスト名")
  lbl_artist_name.place(x=30, y=100)

  txt_artist_name = tkinter.Entry(width=20) 
  txt_artist_name.place(x=180, y=100)

  # アルバムアーティスト名の入力
  lbl_album_artist = tk.Label(text="アルバムアーティスト名")
  lbl_album_artist.place(x=30, y=130)
  
  txt_album_artist = tkinter.Entry(width=20)
  txt_album_artist.place(x=180, y=130)

  # ジャンル名の入力
  lbl_genre_name = tk.Label(text="ジャンル名")
  lbl_genre_name.place(x=30, y=160)

  txt_genre_name = tkinter.Entry(width=20)
  txt_genre_name.place(x=180, y=160)


  btn = tkinter.Button(root, 
                       text="apply", 
                       command=lambda: btn_apply(txt_id,txt_artist_name,txt_album_artist,txt_genre_name, root,wav_folder_path))
  btn.place(x=140, y=200)

  #表示
  root.mainloop()


if __name__ == "__main__":
  main()