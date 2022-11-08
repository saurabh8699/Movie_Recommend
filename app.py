# only names
import streamlit as st
import pickle
import pandas as pd
import requests

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b4003f9324c0181b27e7674ce4025bc6&language=en-US'.format(movie_id))
#     data = response.json()
#     print(data)
#     st.text(data)
#     st.text('https://api.themoviedb.org/3/movie/{}?api_key=b4003f9324c0181b27e7674ce4025bc6&language=en-US'.format(movie_id))
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    # recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fecthing poster from api
        # recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    names= recommend(selected_movie_name)
    for i in names:
        st.write(i)
# #     col1, col2, col3 = st.beta_columns(3)
# #     with col1:
# #         st.text(names[0])
# #         st.image(posters[0])
# #     with col2:
# #         st.text(names[1])
# #         st.image(posters[1])
# #     with col3:
# #         st.text(names[2])
# #         st.image(posters[2])




# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#    url = 'https://api.themoviedb.org/3/movie/{}?api_key=b4003f9324c0181b27e7674ce4025bc6&language=en-US'.format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = 'https://image.tmdb.org/t/p/w500/' + poster_path
#     return full_path
#     # data = response.json()
#     # # print(data)
#     # st.text(data)
#     # st.text('https://api.themoviedb.org/3/movie/{}?api_key=b4003f9324c0181b27e7674ce4025bc6&language=en-US'.format(movie_id))
#     # return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     #distances = similarity[index]
#     #movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         # fecthing poster from api
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#     return recommended_movie_names, recommended_movie_posters
#
# st.header('Movie Recommendation System')
#
# movies = pickle.load(open('movie_dict.pkl', 'rb'))
# #movies = pd.DataFrame(movies_dict)
#
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# #st.title('Movie Recommendation System')
#
# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     'Select a movie',
#     movie_list)
#
# if st.button('Recommend'):
#     names, posters= recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])







# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     url = 'https://api.themoviedb.org/3/movie/{}?api_key=b4003f9324c0181b27e7674ce4025bc6&language=en-US'.format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = 'https://image.tmdb.org/t/p/w500/' + poster_path
#     return full_path
#     #data = response.json()
#     # print(data)
#     # st.text(data)
#     # st.text('https://api.themoviedb.org/3/movie/{}?api_key=b4003f9324c0181b27e7674ce4025bc6&language=en-US'.format(movie_id))
#     #return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     #distances = similarity[index]
#     #movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         # fecthing poster from api
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#     return recommended_movie_names, recommended_movie_posters
#
# st.header('Movie Recommendation System')
#
# movies = pickle.load(open('movie_dict.pkl', 'rb'))
# #movies = pd.DataFrame(movies_dict)
#
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# #st.title('Movie Recommendation System')
#
# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     'Select a movie',
#     movie_list)
#
# if st.button('Recommend'):
#     names, posters= recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])


#
#
# # #MAIN
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b4003f9324c0181b27e7674ce4025bc6&language=en-US'.format(movie_id))
#     data = response.json()
#     print(data)
#     st.text(data)
#     st.text('https://api.themoviedb.org/3/movie/{}?api_key=b4003f9324c0181b27e7674ce4025bc6&language=en-US'.format(movie_id))
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = similarity[index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#
#         recommended_movies.append(movies.iloc[i[0]].title)
#         # fecthing poster from api
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters
#
#
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# st.title('Movie Recommendation System')
#
# selected_movie_name = st.selectbox(
#     'How would you like to be contacted?',
#     movies['title'].values)
#
# if st.button('Recommend'):
#     names, posters= recommend(selected_movie_name)
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     # with col4:
#     #     st.text(names[3])
#     #     st.image(posters[3])
#     # with col5:
#     #     st.text(names[4])
#     #     st.image(posters[4])


# import pickle
# import streamlit as st
# import requests
#
# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=b4003f9324c0181b27e7674ce4025bc6&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#
#     return recommended_movie_names,recommended_movie_posters
#
#
# st.header('Movie Recommender System')
# movies = pickle.load(open('movie_dict.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl','rb'))
#
# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     'Type or select a movie from the dropdown',
#     movie_list
# )
#
# if st.button('Show Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])



