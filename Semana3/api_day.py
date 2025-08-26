import requests






def get_characters(page):
    
    try:
        url = f"https://rickandmortyapi.com/api/character/?page={page}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            data_results = data['results']
            characters = []
            
            for item in data_results:
                characters.append({
                    'ID' : item['id'],
                    "Nombre" : item['name'],
                    "Genero" : item['gender'],
                    "Episodio" : item['episode'][0]
                })
            
            return characters
        else:
            print(response.status_code)
    except Exception as e:
        print(e)
        
def show_characters(characters):
    print("------ Results ---------")
    for char in characters:
        print(f"{char['ID']} : {char['Nombre']}")
        

while True:
    print("------ Rick And Morty ---------")
    option = input("Select the page (q or quit for exit): ").strip()
    if option == 'q' or option == 'quit':
        break
    data = get_characters(option)
    if data:
        show_characters(data)