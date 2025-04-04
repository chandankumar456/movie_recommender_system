import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=35a7d2adba2b834c9d21c27b165c49c4&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        # fetch the movie poster
       # movie_id = movies.iloc[i[0]].movie_id
       # recommended_movie_posters.append(fetch_poster(movie_id))
        #recommended_movie_names.append(movies.iloc[i[0]].title)
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movie_posters


st.header('Movie Recommender System')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies = pd.DataFrame(movies_dict)
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button('Show Recommendation'):
    names,posters = recommend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])




