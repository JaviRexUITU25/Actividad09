movies = []
add_movie = []
genre_ = []
while True:
    print("-"*8 + "CATALOGO DE PELICULAS" + "-" *8)
    print("1. Agregar peliculas\n"
          "2. Mostrar peliculas registradas\n"
          "3. Buscar peliculas por género\n"
          "4. Ver estadisticas del catalogo\n"
          "5. Salir")

    user_o = input("Ingrese la opcion que desea registrar: ")

    match user_o:
        case "1":
            print("Lista actual: ", movies)
            print("-"*5 + "Agregar peliculas: "+"-"*5)
            tittle = input("Ingrese el titulo de la pelicula: ")
            premiere = input("Ingrese el año de estreno de la pelicula: ")
            genre = input("Ingrese el genero de la pelicula: ")
            print("¡Pelicula agregada con exito!")
            add_movie.append((tittle, premiere, genre))
            movies.append((tittle, premiere, genre))
            genre_.append(genre)
        case "2":
            print("\n" + "-" * 5 + " Peliculas Registradas " + "-" * 5)
            if movies:
                for i in movies:
                    print(f"{i +1}, Titulo: {movies[0]},Año: {movies[1]}, Estreno: {movies[2]}")
            else:
                print("No hay peliculas registradas")
        case "3":
            print("Lista actual: ", movies)
            print("-"*5 + "Buscar peliculas por genero: "+ "-" * 5)
            if movies:
                search_movie = input("Ingrese el genero de la pelicula que desea buscar: ")
                found_movies = [movie for movie in movies if movie[2].lower() == search_movie.lower()]
                if found_movies:
                    print(f"\nPeliculas encontradas para el genero '{search_movie}':")
                    for i in found_movies:
                        print(f"{i+1}, genero: {movies[i]}")
                else:
                    print("No se encontr<UNK> el genero")
        case "4":
            print("Lista actual: ", movies)
            remove_movie = input("¿Que pelicula desea eliminar?: ")
            movies.remove(remove_movie)
            print("Pelicula eliminada con exito.")
        case "5":
            print("Lista actual: ", movies)
            print("-"*5 + "estadisticas del catalogo: "+ "-" * 5)
            print("Peliculas registradas: ", movies)
            print("Peliculas por genero: ", genre_)
            print("pelicula mas antigua: ", movies)
        case "6": print("Gracias por usar el programa!!")
        case _:
            print("Opcion no valida, intente de nuevo.")
    break