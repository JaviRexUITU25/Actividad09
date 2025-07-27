movies = []
add_movie = []
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
            gender = input("Ingrese el genero de la pelicula: ")
            add_movie.append((tittle, premiere, gender))
            movies.append((tittle, premiere, gender))
        case "2":
            print("Lista actual: ", movies)
        case "3":
            print("Lista actual: ", movies)
            print("-"*5 + "Buscar peliculas por genero: "+ "-" * 5)
            show_movies = input("Ingrese el genero de la pelicula que desea buscar: ")
            print("Generos: ",)
        case "4":
            print("Lista actual: ", add_movie)