import requests
import json
import time

# jsonファイルから辞書を作成
with open('merged_file.json', 'r') as f:
    data = json.load(f)

# lct_cdに対応するURLを作成してhtmlをダウンロード
for lct_cd in data:
    url = f'https://success.shiga-u.ac.jp/Portal/Public/Syllabus/DetailMain.aspx?lct_year=2023&lct_cd={lct_cd}'
    response = requests.get(url)
    html = response.text
    time.sleep(2)
    # htmlをファイルに保存
    with open(f'downloaded/{lct_cd}.html', 'w', encoding='utf-8') as f:
        f.write(html)