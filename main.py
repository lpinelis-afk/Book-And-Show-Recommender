import pandas as pd
movies = pd.read_csv('./CSV/movies.csv')
books = pd.read_csv('./CSV/books.csv')
shows = pd.read_csv('./CSV/shows.csv')
category=input("Book/Movie/Show> ")



# Filter the dataframe where the 'cast' column contains the actor's name

# Print the titles of those movies
if category.lower() == "book":
    creator=input("Author's name> ")
    books_with_author = books[books['authors'].str.contains(creator, case=False, na=False)]

    print(books_with_author['title'] + " " + str(books_with_author['publication_date']))
elif category.lower() == "movie":
    creator=input("Choose Director or Actor> ")
    if creator.lower() == "director":
        creator = input("Director's Name> ")
        movies_with_director = movies[movies['director'].str.contains(creator, case=False, na=False)]
        print(movies_with_director['title'] + " " + movies_with_director['genres'])
    else:
        creator = input("Actor's Name> ")
        movies_with_actor = movies[movies['cast'].str.contains(creator, case=False, na=False)]
        print(movies_with_actor['title'] + " " + movies_with_actor['genres'])
elif category.lower() == "show":
    creator=input("Director's Name> ")
    shows_with_director = shows[shows['directors'].str.contains(creator, case=False, na=False)]
    print(shows_with_director['primaryTitle'] + " " + shows_with_director['genres'])