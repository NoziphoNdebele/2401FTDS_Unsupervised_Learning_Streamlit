# Anime Recommendation System

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Packages](#packages)
4. [Environment](#environment)
5. [Streamlit App](#streamlit-app)
6. [Team Members](#team-members)

## Project Overview
The Anime Recommendation System allows users to receive anime recommendations using Content-Based Filtering and Collaborative-Based Filtering. The system is built using Streamlit to provide a user-friendly interface.

## Dataset
The dataset consists of thousands of users and thousands of anime titles, gathered from myanimelist.net.

### Dataset Features:

| Column     | Description                                    |
|------------|------------------------------------------------|
| user_id    | Unique identifier for each user                |
| anime_id   | Unique identifier for each anime               |
| rating     | Rating given by the user to the anime (1-10)   |
| name       | Name of the anime                              |
| genre      | Genre of the anime                             |
| type       | Type of the anime (e.g., TV, Movie)            |
| episodes   | Number of episodes                             |
| release    | Release year of the anime                      |
| members    | Number of members who have rated the anime     |

## Packages
The following packages are used in this project:
- Pandas 2.2.2
- Numpy 1.26
- Matplotlib 3.8.4
- Seaborn 0.12.2
- Scikit-learn 1.2.2
- Surprise 1.1.1
- Nltk 3.8.1
- IPython 8.20.0
- IPython Sql 0.3.9
- Python 3.11.8
- Pymysql 1.0.2
- ML Flow 2.14.1

## Environment
To set up the environment and install dependencies, follow these instructions:

1. Create and activate a virtual environment:
    ```bash
    conda create --name env_name python=3
    conda activate env_name
    conda install pip
    ```

2. Install packages:
    ```bash
    pip install -r requirements.txt
    ```

## Streamlit App
What is Streamlit?
Streamlit is a framework that acts as a web server with dynamic visuals, multiple responsive pages, and robust deployment of your models.

In its own words:

Streamlit ... is the easiest way for data scientists and machine learning engineers to create beautiful, performant apps in only a few hours! All in pure Python. All for free.

It’s a simple and powerful app model that lets you build rich UIs incredibly quickly.

Streamlit takes away much of the background work needed in order to get a platform which can deploy your models to clients and end users. Meaning that you get to focus on the important stuff (related to the data), and can largely ignore the rest. This will allow you to become a lot more productive.

Description of files
For this repository, we are only concerned with a single file:

File Name	Description
base_app.py	Streamlit application definition.
6.1 Running the Streamlit web app on your local machine
As a first step to becoming familiar with our web app's functioning, we recommend setting up a running instance on your own local machine. To do this, follow the steps below by running the given commands within a Git bash (Windows), or terminal (Mac/Linux):

Ensure that you have the prerequisite Python libraries installed on your local machine:

pip install -U streamlit numpy pandas scikit-learn
Navigate to the base of your repo where your base_app.py is stored, and start the Streamlit app.

cd 2401FTDS_Unsupervised_Learning_Streamlit/
streamlit run base_app.py
If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session: Screenshot (246)

Congratulations! You've now officially deployed your first web application!

6.2 Deploying your Streamlit web app
To deploy your app for all to see, click on deploy.

Please note: If it's your first time deploying it will redirect you to set up an account first. Please follow the instructions.
To access our Streamlit app, click on the link below:
[Streamlit App Link](#)

## Team Members
| Names              | Emails                          |
|--------------------|---------------------------------|
| Tikedzani Vele     | geraldinevele@gmail.com         |
| Nozipho Ndebele    | nozihstheh@gmail.com            |
| Sibukiso Nhlengethwa | sibukisot@gmail.com          |
| Keneilwe Madihlaba | keneilwemadihlaba@gmail.com     |
| Koketso Moraka     | moraka1952@gmail.com            |
| Akhona Nzama       | sthokonzama@gmail.com           |
