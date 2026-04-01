# Starter
movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []  # list of (title, qty, price_each)
subtotal = 0
# TODO: use a while loop that continues until the user enters 'done'
while True:
    # 1) ask for movie title (case sensitive is fine)
    movie = input("Enter movie title or done: ").title()
    if movie == "Done":
        break

# 2) if title not in movies, print the available keys and continue
    if movie not in movies:
        print("Movie not available. Available movies are:\n"," , ".join(movies.keys()))
# 3) ask for quantity (int)
    else:
        try:
            qty = int(input("Enter quantity: "))
            if qty < 0:
                print("Please enter a positive number")
                continue
            else:
            # 4) append (title, qty, movies[title]) to purchases
                purchases.append((movie, qty, movies[movie]))
            # 5) optional: track running subtotal
            subtotal += movies[movie] * qty
            
            print(f"{movie} * {qty} = {subtotal}")
        except ValueError:
            print("Invalid quantity. Try again please.")
        

    

 



    
