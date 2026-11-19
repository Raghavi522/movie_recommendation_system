import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    movies = pd.read_csv("movies.csv")
    ratings = pd.read_csv("ratings.csv")
    return movies, ratings

def build_model(movies, ratings):
    merged = ratings.merge(movies, on="movieId")
    movie_matrix = merged.pivot_table(
        index="userId",
        columns="title",
        values="rating"
    ).fillna(0)
    similarity = cosine_similarity(movie_matrix.T)
    similarity_df = pd.DataFrame(
        similarity,
        index=movie_matrix.columns,
        columns=movie_matrix.columns
    )
    return similarity_df

def get_recommendations(movie_title, similarity_df, n=10):
    if movie_title not in similarity_df.columns:
        return None
    similar_movies = similarity_df[movie_title].sort_values(ascending=False)
    similar_movies = similar_movies.drop(movie_title)
    return similar_movies.head(n)

def get_all_titles(similarity_df):
    return sorted(list(similarity_df.columns))
