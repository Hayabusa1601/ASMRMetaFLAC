import requests
import os
from bs4 import BeautifulSoup


def fetch_dlsite_artwork_url(product_id):
  """
  dlsiteの商品id(RJxxxxxxxx)を用いて、商品ページから商品名とアートワークのURLを取得する。

  Parameters
  ----------
  product_id : String
    対象のdlsite商品の商品id
  
  Returns
  -------
  artwork_url : String
    対象のdlsite商品のアートワークのURL
  title : String
    対象のdlsite商品のタイトル
  """
  # idからURLの生成
  url = "https://www.dlsite.com/maniax/work/=/product_id/" + product_id + ".html"
  
  res = requests.get(url)
  soup = BeautifulSoup(res.content, 'html.parser')
  
  # タイトルを取得
  title = soup.title.string


  # slider_itemからメイン画像URLの取得
  slider_items = soup.find_all(class_="slider_item")
  slider_item = slider_items[0]

  if slider_item:
    img_tag = slider_item.find("img")

    if img_tag and img_tag.has_attr('srcset'):
      # imgタグのsrcset属性の値を取得
      artwork_url = img_tag['srcset']
      #print("srcset URL:", artwork_url)
    else:
      print("img tag or srcset attribute not found")
  else:
    print("img tag or srcset attribute not found")

  # URLの形に整形
  artwork_url = "https:" + artwork_url
  return title, artwork_url


def download_artwork(url, file_path):
  """
  画像URLから画像を取得する。

  Parameters
  ----------
  url : 画像のURL
  file_path : 保存先のファイルパス
  """
  response = requests.get(url)
  if response.status_code == 200:
    with open(file_path, 'wb') as f:
      f.write(response.content)
      print(f"Downloaded: {file_path}")
  else:
    print(f"Failed to download: {url}")


#def fetch_dlsite_metadata(product_id):
#  """
#  dlsiteの商品id(RJxxxxxxxx)を用いて、商品ページからアーティスト名や作品名などのメタデータを取得する。
#
#  Parameters
#  ----------
#  product_id : String
#    対象のdlsite商品の商品id
#  
#  """


def dlsite_data_collector(id):
  """
  dlsite_data_collector
  アートワークを保存し、dlsiteのid名で保存する

  Parameters
  ----------
  id: DLSiteの作品id (例：RJ123456)

  """
  #id = input("id?(RJxxxxxxx) :")

  # === 出力先の設定 === 
  # Picturesフォルダ内の出力先のパスを取得
  home_dir = os.path.expanduser("~")
  output_folder = os.path.join(home_dir, "Pictures", "artworks")

  # Picturesフォルダが存在しない場合は作成
  os.makedirs(output_folder, exist_ok=True)
  artwork_filepath = output_folder + "/" + id +".jpg"

  # fetch_dlsite_artwork_urlでアートワークの画像URLと作品タイトルを取得
  title, artwork_url = fetch_dlsite_artwork_url(id)
  print("title: ", title)
  print("srcset URL:", artwork_url)

  # 画像URLからアートワークのダウンロード
  download_artwork(artwork_url, artwork_filepath)
  return artwork_filepath

