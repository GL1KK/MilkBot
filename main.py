import requests
from bs4 import BeautifulSoup


def get_items():
    results = []
    for i in range(17):
        r = requests.get(f"https://милкагросервис.рф/category/{i}")
        content = r.text
        soup = BeautifulSoup(content, "html.parser")
        divs = soup.find_all("div", class_="product__details")
        for div in divs:
            link_list = div.find_all('a')
            for link_tag in link_list:
                if link_tag:
                    title = div.text
                    link = f"https://милкагросервис.рф{link_tag.get('href', '')}"
                    results.append(title.strip('\n'))
                    results.append(link.strip('\n'))
                with open("info.txt", "w", encoding="utf-8") as file:
                    for res in results:
                        file.write(f"{res}\n")

def main():
    get_items()
if __name__ == "__main__":
    main()