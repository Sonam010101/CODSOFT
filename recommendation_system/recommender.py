import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


movies = pd.read_csv("movies.csv")


movies["title_lower"] = movies["title"].str.lower().str.strip()


vectorizer = TfidfVectorizer()
genre_vectors = vectorizer.fit_transform(movies["genres"])


similarity_matrix = cosine_similarity(genre_vectors)


def recommend(movie_name):
    
    movie_name = movie_name.strip().lower()

    
    if movie_name not in movies["title_lower"].values:
        return ["Movie not found in dataset"]

    
    idx = movies[movies["title_lower"] == movie_name].index[0]

    
    similarity_scores = list(enumerate(similarity_matrix[idx]))

    
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    
    top_movies = [movies.iloc[i[0]]["title"] for i in similarity_scores[1:6]]

    return top_movies
