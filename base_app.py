# Streamlit dependencies
import streamlit as st

# The main function where we will build the actual app
def main():
    """Anime Recommender System Info App with Streamlit"""

    # Creates a main title and subheader on your page -
    # these are static across all pages
    st.title("Anime Recommender System")
    st.subheader("Building an anime recommendation system")

    # Creating sidebar with selection box -
    # you can create multiple pages this way
    options = ["Project Overview", "How Recommender Systems Work", "Team Members"]
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
