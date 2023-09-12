from bs4 import BeautifulSoup
import json
file_name = "4.html"
with open(file_name, 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

table = soup.find('table', {'id': 'ctl00_phContents_ucGrid_grv'})

result = []
for row in table.find_all('tr')[1:]:
    code = row.find_all('td')[1].get_text().strip()
    result.append(code)

with open(file_name+'result.json', 'w') as f:
    json.dump(result, f)
