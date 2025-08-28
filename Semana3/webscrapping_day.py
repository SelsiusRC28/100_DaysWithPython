import requests
from bs4 import BeautifulSoup


def seach_wiki(word):
    url = f"https://en.wikipedia.org/wiki/{word.replace('_', ' ')}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/114.0.0.0 Safari/537.36"
    }

    
    response = requests.get(url, headers=headers)

    if response.status_code == 200 :
        data_parse = BeautifulSoup(response.text, "html.parser")
        return data_parse
    else:
        print("Pagina no encontrada")

def parser_h1(soup):
    soup_h1 = soup.find('h1').text
    print(f"TITLE: {soup_h1}")

def parser_headers(soup):
    soup_headers = soup.find_all(['h2', 'h3', 'h4'])
    headers = [header.text.strip() for header in soup_headers]
    
    for index, header in enumerate(headers):
        print(f"{index} - {header}")

def get_related_links(soup):
    links = []
    
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        
        if href.startswith('/wiki/') and ':' not in href:
            links.append(f"https://en.wikipedia.org{href}")
    links = list(set(links)) 
    for link in links[:5]:
        print(link)


def main():
    input_name = input("Seach the wiki: ").strip()
    data = seach_wiki(input_name)
    if data:
      parser_h1(data)
      parser_headers(data)
      get_related_links(data)
       
        
        
if __name__ == "__main__":
    main()