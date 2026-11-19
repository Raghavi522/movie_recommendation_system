# 🎬 Movie Recommendation System

A machine learning web app that recommends movies similar to one you pick, built with Python and deployed with Streamlit.

**🔗 Live demo:** [add your Streamlit link]

## Overview

Choosing what to watch next is hard. This project uses the MovieLens dataset and cosine similarity to suggest movies that are closest to a title the user selects. The app is interactive and runs in the browser.

## Features

- Select a movie and get a ranked list of similar recommendations
- Similarity scoring with cosine similarity (scikit-learn)
- Data cleaning and preparation with Pandas
- Simple, interactive Streamlit interface
- Deployed online so anyone can try it

## Tech Stack

| Area | Tools |
|------|-------|
| Language | Python |
| Data handling | Pandas, NumPy |
| ML | scikit-learn (cosine similarity) |
| Web app | Streamlit |
| Dataset | MovieLens |

## How It Works

1. **Load data:** Read the MovieLens movies [and ratings] data with Pandas.
2. **Prepare features:** Clean the data and build a [movie-feature / user-rating] matrix.
3. **Compute similarity:** Use cosine similarity to measure how close each movie is to every other movie.
4. **Recommend:** For the selected movie, return the top N most similar titles.
5. **Display:** Show the results in the Streamlit app.

## Project Structure

```
movie-recommendation-system/
├── app.py              # Streamlit app
├── data/               # MovieLens dataset files
├── notebook.ipynb      # Exploration and model building
├── requirements.txt
└── README.md
```

## Installation and Usage

```bash
# Clone the repository
git clone https://github.com/Raghavi522/[your-repo-name].git
cd [your-repo-name]

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Future Improvements

- Add movie posters and ratings to the results
- Combine genre-based and rating-based recommendations
- Try a larger MovieLens dataset

## Author

Laxmipathi Raghavi
[GitHub](https://github.com/Raghavi522)
