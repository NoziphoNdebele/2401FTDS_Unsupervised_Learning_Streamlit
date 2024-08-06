import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split

# Load the dataset
anime_df = pd.read_csv('cleaned_anime.csv')

# Load the vectorizer
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Process the dataset
anime_df['genre'] = anime_df['genre'].fillna('')
anime_df['name'] = anime_df['name'].astype(str)
anime_df['genre'] = anime_df['genre'].astype(str)
anime_df['features'] = anime_df[['name', 'genre']].apply(lambda x: ' '.join(x), axis=1)

# Transform the features into TF-IDF matrix
tfidf_matrix = vectorizer.transform(anime_df['features'])

# Load the KNN model
knn_model = pickle.load(open('knn_model.pkl', 'rb'))

# Load and prepare SVD model
svd_model = pickle.load(open('SVD_model.pkl', 'rb'))

# KNN Recommendation Function
def knn_recommendations(anime_title, N=5):
    idx = anime_df[anime_df['name'] == anime_title].index[0]
    distances, indices = knn_model.kneighbors(tfidf_matrix[idx].reshape(1, -1), n_neighbors=N+1)
    recommendations = {
        "No": range(1, N + 1),
        "Anime Name": anime_df['name'].iloc[indices.flatten()[1:]].values,
        "Distance": distances.flatten()[1:]
    }
    return pd.DataFrame(recommendations).set_index("No")

# SVD Recommendation Function
def svd_recommendations(user_id, n_recommendations=5):
    user_ratings = svd_model.trainset.ur[svd_model.trainset.to_inner_uid(user_id)]
    watched_anime = [svd_model.trainset.to_raw_iid(inner_id) for (inner_id, _) in user_ratings]
    all_anime = set(anime_df['name'].values)
    unwatched_anime = list(all_anime - set(watched_anime))

    predictions = [svd_model.predict(user_id, anime).est for anime in unwatched_anime]
    anime_predictions = list(zip(unwatched_anime, predictions))
    anime_predictions = sorted(anime_predictions, key=lambda x: x[1], reverse=True)

    top_recommendations = anime_predictions[:n_recommendations]
    rec_dic = {
        "No": range(1, n_recommendations + 1),
        "Anime Name": [anime for anime, _ in top_recommendations],
        "Predicted Rating": [rating for _, rating in top_recommendations]
    }
    dataframe = pd.DataFrame(data=rec_dic)
    dataframe.set_index("No", inplace=True)

    return dataframe

def hybrid_recommendations(user_id, anime_title, N=5):
    # Get KNN-based recommendations (content-based)
    knn_recs = knn_recommendations(anime_title, N)
    if knn_recs.empty:
        return knn_recs
    
    # Get collaborative filtering recommendations
    collab_recs = svd_recommendations(user_id, N)
    
    # Combine and deduplicate
    combined_recs = pd.concat([knn_recs.reset_index(), collab_recs.reset_index()])
    combined_recs = combined_recs.drop_duplicates(subset=['Anime Name'])
    
    # Ensure unique index
    combined_recs.index = range(len(combined_recs))
    
    # Apply styling separately before returning
    return combined_recs

# The main function where we will build the actual app
def main():
    """Anime Recommender System Info App with Streamlit"""

    st.title("Anime Recommender System")
    options = ["Project Overview", "How Recommender Systems Work", "Recommendation Engine", "EDA", "Team Members"]
    selection = st.sidebar.selectbox("Navigation", options)

    if selection == "Project Overview":
        st.info("Project Overview")
        st.markdown("""
        In today’s technology-driven world, recommender systems are critical for helping users find relevant content.
        This project focuses on building a recommender system for anime titles, predicting user ratings based on their historical preferences.
        The dataset consists of thousands of users and anime titles gathered from myanimelist.net.
        """)

        st.markdown("### Project Goals")
        st.markdown("""
        - Build collaborative and content-based recommender systems.
        - Predict user ratings for anime titles accurately.
        - Evaluate models using Root Mean Square Error (RMSE).
        """)

    elif selection == "How Recommender Systems Work":
        st.info("How Recommender Systems Work")
        st.markdown("""
        Recommender systems predict user preferences for items, such as movies or anime, based on past interactions.
        They use collaborative filtering and content-based filtering techniques to make predictions.
        """)

        st.markdown("### Evaluation Metric: Root Mean Square Error (RMSE)")
        st.latex(r'''
        RMSE = \sqrt{\frac{\sum_{u,i}(r_{ui} - \hat{r}_{ui})^2}{R}}
        ''')
        st.markdown("""
        Here, \( r_{ui} \) is the true rating given by user \( u \) to anime \( i \), and \( \hat{r}_{ui} \) is the predicted rating.
        """)

    elif selection == "Recommendation Engine":
        st.title('Anime Recommendation Engine')
        st.image('Anime.png', caption='Anime Recommendation Engine')

        rec_method = st.selectbox(
            'Select Recommendation Method',
            ('Content-Based Filtering (KNN)', 'Collaborative Filtering (SVD)', 'Hybrid Filtering')
        )

        if rec_method == 'Content-Based Filtering (KNN)':
            selected_anime = st.selectbox(
                'Which anime did you like?',
                (anime_df['name'].values)
            )
            if st.button('Recommend'):
                with st.spinner(text='In progress'):
                    user_input = selected_anime
                    if user_input:
                        recommendations = knn_recommendations(user_input)
                        st.subheader(f"Top 5 Recommendations for {selected_anime}")
                        st.table(recommendations)

                        selected_anime_details = anime_df[anime_df['name'] == selected_anime][['name', 'genre', 'rating', 'members']]
                        st.table(selected_anime_details)

        elif rec_method == 'Collaborative Filtering (SVD)':
            user_id = st.number_input('Enter User ID', min_value=1, value=1)
            if st.button('Recommend'):
                with st.spinner(text='In progress'):
                    recommendations = svd_recommendations(user_id)
                    st.subheader(f"Top 5 Recommendations for User {user_id}")
                    st.table(recommendations)

        elif rec_method == 'Hybrid Filtering':
            selected_anime = st.selectbox(
                'Which anime did you like?',
                (anime_df['name'].values)
            )
            user_id = st.number_input('Enter User ID', min_value=1, value=1)
            if st.button('Recommend'):
                with st.spinner(text='In progress'):
                    recommendations = hybrid_recommendations(user_id, selected_anime)
                    st.subheader(f"Top 5 Hybrid Recommendations for {selected_anime} and User {user_id}")
                    st.write(recommendations)  # Use st.write() to render styled DataFrame

    elif selection == "EDA":
        st.info("Exploratory Data Analysis (EDA)")
        st.markdown("""
        Exploratory Data Analysis is the process of examining a dataset to understand its main characteristics, structure, patterns, and relationships. It often uses visual methods to gain insights, detect anomalies, and check assumptions before applying machine learning models.
        
        EDA helps us understand the data better by uncovering patterns, relationships, and anomalies. 
        For non-tech people, here's how EDA helps in this project:
        """)

        st.markdown("### Average Rating by Type")
        st.image('Avg_rating_by_type.png', caption='Average Rating by Type')

        st.markdown("### Distribution of Members by Type")
        st.image('Dis_of_members_by_type.png', caption='Distribution of Members by Type')

        st.markdown("### Top Anime by Popularity")
        st.image('Top_anime_by_popularity.png', caption='Top Anime by Popularity')

        st.markdown("### Top Anime by Rating")
        st.image('Top_anime_by_rating.png', caption='Top Anime by Rating')

    elif selection == "Team Members":
        st.info("Team Members")
        st.markdown("""
        Meet the team members working on this project:

        - **Akhona Nzama**
        - **Keneilwe Madihlaba**
        - **Koketso Bambo**
        - **Nozipho Ndebele**
        - **Sibukiso Nhlengethwa**
        - **Tikedzani Vele**
        """)

if __name__ == '__main__':
    main()
