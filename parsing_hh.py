import requests as req
from bs4 import BeautifulSoup
import json
import tqdm

data = {
    "data": []
}

for page in range(1, 3):
    url = f"https://hh.ru/search/vacancy?text=python+разработчик&salary=&clusters=true&area=113&ored_clusters=true&enable_snippets=true&{page}=1&hhtmFrom=vacancy_search_list"
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs={"data-marker": "item-title"})
    for iter in tqdm.tqdm(tags):
        url_obj = 'https://www.avito.ru' + iter.attrs["href"]
        resp_obj = req.get(url_obj)

        soup_obj = BeautifulSoup(resp_obj.text, "lxml")
        tags_price = soup_obj.find(attrs={"itemprop": "offers"}).find(attrs={"itemprop": "price"}).text

        tag_reg = soup_obj.find(attrs={"itemtype": "http://schema.org/ListItem"}).find_all(attrs={"itemprop": "name"})[0].text
        data["data"].append({"Title": iter.text, "Salary": tags_price, "Region": tag_reg})

with open("data.json", "w") as file:
    json.dump(data, file)


