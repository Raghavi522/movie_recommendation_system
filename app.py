import streamlit as st
from recommender import load_data, build_model, get_recommendations, get_all_titles

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

st.title("Movie Recommendation System")
st.markdown("Select a movie you like and get 10 similar recommendations instantly.")

@st.cache_data
def setup():
    movies, ratings = load_data()
    similarity_df = build_model(movies, ratings)
    return similarity_df

with st.spinner("Loading movie data..."):
    similarity_df = setup()

all_titles = get_all_titles(similarity_df)

selected_movie = st.selectbox(
    "Choose a movie you enjoy:",
    options=all_titles,
    index=all_titles.index("Toy Story (1995)") if "Toy Story (1995)" in all_titles else 0
)

if st.button("Get Recommendations"):
    results = get_recommendations(selected_movie, similarity_df)

    if results is None:
        st.error("Movie not found. Please try another one.")
    else:
        st.subheader(f"Top 10 movies similar to '{selected_movie}'")

        for i, (title, score) in enumerate(results.items(), 1):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{i}. {title}**")
                st.progress(float(score))
            with col2:
                st.metric(label="Score", value=f"{score:.2f}")
            st.divider()