import json
import re

record = []

# 標準入力から10万文字の入力を受け取る
text = input()

# 正規表現を使って10桁の数字を抽出する
matches = re.findall(r'\d{10}', text)

# 抽出した数字を記録紙に追加する
for match in matches:
    record.append(match)

# 記録紙をJSON形式で保存する
with open('record.json', 'w') as f:
    json.dump(record, f)