import pandas as pd
category=input("Book/Movie/Show> ")
creator=input("> ")
movies = pd.read_csv('./CSV/movies.csv')
books = pd.read_csv('./CSV/books.csv')

a ="test"
b = "test"
# Filter the dataframe where the 'cast' column contains the actor's name
movies_with_actor = movies[movies['cast'].str.contains(creator, case=False, na=False)]
books_with_actor = books[books['Book-Author'].str.contains(creator, case=False, na=False)]


# Print the titles of those movies
if category == "Book":
    print(books_with_actor['Book-Title'])
else:
    print(movies_with_actor['title'])
