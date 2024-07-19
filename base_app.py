# Import necessary libraries
import streamlit as st
import pandas as pd

# import pickle
import joblib

# Placeholder for loading your model and vectorizer
# animes_dict = pickle.load(open('models/animes_dict.pkl','rb'))

# Placeholder DataFrame for anime data
anime_df = pd.DataFrame({
    'name': ['Naruto', 'One Piece', 'Attack on Titan', 'My Hero Academia', 'Sword Art Online'],
    'genre': ['Action', 'Adventure', 'Action', 'Action', 'Adventure'],
    'rating': [8.5, 8.8, 9.1, 8.2, 7.9],
    'members': [1000000, 950000, 890000, 870000, 820000]
})

# Placeholder for recommendation indices
rec_indices = {anime: idx for idx, anime in enumerate(anime_df['name'])}

# Placeholder for sigmoid kernel
sig = [[1, 0.9, 0.8, 0.7, 0.6],
       [0.9, 1, 0.85, 0.75, 0.65],
       [0.8, 0.85, 1, 0.78, 0.68],
       [0.7, 0.75, 0.78, 1, 0.77],
       [0.6, 0.65, 0.68, 0.77, 1]]

# Recommendation Function
def give_recommendation(title, sig=sig):
    # Get the index corresponding to the provided anime title
    idx = rec_indices[title]

    # Calculate pairwise similarity scores using sigmoid kernel
    sig_score = list(enumerate(sig[idx]))

    # Sort the similarity scores in descending order
    sig_score = sorted(sig_score, key=lambda x: x[1], reverse=True)

    # Keep the top 10 most similar animes (excluding itself)
    sig_score = sig_score[1:6]
    anime_indices = [i[0] for i in sig_score]

    # Create a DataFrame with the top 10 similar animes
    rec_dic = {
        "No": range(1, 6),
        "Anime Name": anime_df["name"].iloc[anime_indices].values,
        "Rating": anime_df["rating"].iloc[anime_indices].values
    }
    dataframe = pd.DataFrame(data=rec_dic)
    dataframe.set_index("No", inplace=True)

    return dataframe.style.set_properties(**{"background-color": "#2a9d8f", "color": "white", "border": "1.5px solid black"})

# The main function where we will build the actual app
def main():
    """Anime Recommender System Info App with Streamlit"""

    # Creates a main title and subheader on your page -
    # these are static across all pages
    st.title("Anime Recommender System")


    # Creating sidebar with selection box -
    # you can create multiple pages this way
    options = ["Project Overview", "How Recommender Systems Work", "Recommendation Engine", "Team Members"]
    selection = st.sidebar.selectbox("Choose Option", options)

    # Building out the "Project Overview" page
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

    # Building out the "How Recommender Systems Work" page
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


    # Building out the "Recommendation Engine" page
    elif selection == "Recommendation Engine":
        

        # Title
        st.title('Anime Recommendation Engine')

        # Search Box
        selected_anime = st.selectbox(
            'Which anime did you like?',
            (anime_df['name'].values))

        # Recommendation Button
        if st.button('Recommend'):
            with st.spinner(text='In progress'):
                user_input = selected_anime
                if user_input:
                    recommendations = give_recommendation(user_input)
                    st.subheader(f"Top 10 Recommendations for {selected_anime}")
                    st.table(recommendations)

                    selected_anime_details = anime_df[anime_df['name'] == selected_anime][['name', 'genre', 'rating', 'members']]
                    st.table(selected_anime_details)

    # Building out the "Team Members" page
    elif selection == "Team Members":
        st.info("Team Members")
        st.markdown("""
        Meet the team members working on this project:

        - **Akhona Nzama**
        - **Nozipho Ndebele**
        - **Keneilwe Madihlaba**
        - **Koketso Bambo**
        - **Sibukiso Nhlengethwa**
        - **Tikedzani Vele**
        """)

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    main()

