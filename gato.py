import requests

def buscar_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        tipos = [t['type']['name'] for t in datos['types']]
        peso = datos['weight'] / 10  # peso en kg
        return f"{nombre.title()} es de tipo {', '.join(tipos)} y pesa {peso} kg."
    else:
        return "No encontré ese Pokémon."

def bot():
    print("¡Hola! Preguntame por un Pokémon o escribí 'salir' para terminar.")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() == "salir":
            print("Bot: ¡Chau!")
            break
        respuesta = buscar_pokemon(entrada)
        print("Bot:", respuesta)

if __name__ == "__main__":
    bot()
