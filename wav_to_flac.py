import os, io
from pydub import AudioSegment # ffmpegが必要
from mutagen.flac import FLAC, Picture
from PIL import Image

def wav_to_flac(wav_path, artist_name, album_artist_name, genre_name, artwork_filepath,album_name):
  """
  wavからflacにしつつ受け取ったデータを元にメタデータを付与するプログラム

  Parameters:
  -----------
  wav_path : String(パス文字列)
    wavファイルのパス名
  artist_name : String
    アーティスト名
  album_artist_name : String
    アルバムアーティスト名
  genre_name : String
    ジャンル名
  artwork_filepath : String(パス文字列)
    アートワーク画像のパス文字列
  """

  # === ファイルの前処理 ===
  # フォルダ名とファイル名に分割
  input_folder, input_filename = os.path.split(wav_path) 
  # ファイル名と拡張子に分割 
  file_name, _ = os.path.splitext(input_filename)

  # === 出力先の設定 === 
  # Musicフォルダ内の出力先のパスを取得
  home_dir = os.path.expanduser("~")
  # アルバム名をフォルダ名に設定
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
  
  print("filename:" + file_name)
  
  # メタデータの入力
  track_num= input("tracknumer?: ")

  # メタデータの追加
  flac_audio = FLAC(output_file)
  flac_audio["TITLE"] = file_name
  flac_audio["ALBUM"] = album_name
  flac_audio["ARTIST"] = artist_name
  flac_audio["ALBUMARTIST"] = album_artist_name
  flac_audio["TRACKNUMBER"] = track_num
  flac_audio["genre"] = genre_name

  flac_audio.save()

  if artwork_filepath and os.path.exists(artwork_filepath):
    add_artwork(output_file, artwork_filepath)

  return output_file


def add_artwork(flac_file, artwork_path):
  """
  flacファイルにアートワークを付与する

  Parameters
  ----------
  flac_file : String(パス文字列)
    flacファイルのパス
  artwork_path : String(パス文字列)
    アートワーク画像のパス
  """
  audio = FLAC(flac_file)

  # アートワークの削除
  audio.clear_pictures()

  with open(artwork_path, 'rb') as img_file:
    img_data = img_file.read()
  
  picture = Picture()
  picture.type = 3
  picture.mime = 'image/jpeg'
  picture.desc = 'Front cover'

  # 画像サイズの取得
  img = Image.open(io.BytesIO(img_data))
  picture.width, picture.height = img.size

  picture.data = img_data

  audio.add_picture(picture)
  audio.save()