import requests
import random

movie_api_key = "69fd13f6d0ece99d21db4d6f2984a570"
base_url = "https://api.themoviedb.org/3"

try:
    genre_url = f"{base_url}/genre/movie/list?api_key={movie_api_key}&language=en-US"
    genre_response = requests.get(genre_url)
    genre_response.raise_for_status()
    genre_json = genre_response.json()

    genres = {g["name"].lower(): g["id"] for g in genre_json.get("genres", [])}
    print("🎞️ Mavjud janrlar:", ", ".join(genres.keys()))
    genre_input = input("Janr kiriting: ").lower()

    if genre_input in genres:
        genre_id = genres[genre_input]
        discover_url = f"{base_url}/discover/movie?api_key={movie_api_key}&with_genres={genre_id}&language=en-US"
        discover_response = requests.get(discover_url)
        discover_response.raise_for_status()
        movie_list = discover_response.json().get("results", [])

        if movie_list:
            selected_movie = random.choice(movie_list)
            print("\n🎬 Tavsiya qilinadigan kino:")
            print("Sarlavha:", selected_movie.get("title", "Noma'lum"))
            print("Tavsif:", selected_movie.get("overview", "Yo'q"))
            print("Reyting:", selected_movie.get("vote_average", "Noma'lum"))
            print("Chiqqan sana:", selected_movie.get("release_date", "Noma'lum"))
        else:
            print("Ushbu janrda kinolar topilmadi.")
    else:
        print("Bunday janr mavjud emas.")

except requests.exceptions.RequestException as e:
    print("API xatosi:", e)
except Exception as e:
    print("Noma'lum xato:", e)
