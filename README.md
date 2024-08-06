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
