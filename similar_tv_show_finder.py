#Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# Function to scrape TV show data from IMDb.
def scrape_data(base_url, num_pages=1):

    # Initialize DataFrame to store all TV show data.
    all_tv_show_data = pd.DataFrame()

    # Loop through the specified number of pages to scrape data.
    for i in range(1, num_pages + 1):
        # Construct the URL for the current page.
        url = base_url + f'&start={1 + (i - 1) * 50}'
        # Make a request to the page and get the HTML content.
        response = requests.get(url) 
        # Parse the HTML content using BeautifulSoup.
        soup = BeautifulSoup(response.text, 'html.parser')
         # Find all the divs containing TV show information.
        tv_show_divs = soup.find_all('div', class_='lister-item mode-advanced')

        # Lists to store the title, rating, and genre of each TV show.
        titles = []
        ratings = []
        genres = []

         # Loop through each TV show div and extract relevant information.
        for div in tv_show_divs:
            # Extract and store the title.
            title = div.find('h3', class_='lister-item-header').find('a').text
            titles.append(title)

            # Extract and store the rating.
            rating = float(div.find('div', class_='ratings-bar').find('div', class_='inline-block ratings-imdb-rating')['data-value'])
            ratings.append(rating)

            # Extract and store the genre.
            genre = div.find('span', class_='genre').text.strip()
            genres.append(genre)

        # Combine the data for the current page and concatenate it with the main DataFrame.
        page_tv_show_data = pd.DataFrame({'title': titles, 'rating': ratings, 'genre': genres})
        all_tv_show_data = pd.concat([all_tv_show_data, page_tv_show_data], ignore_index=True)
    # Return the DataFrame containing all TV show data.
    return all_tv_show_data

# Function to find TV shows that are similar to a given TV show based on genre and rating.
def get_similar_tv_shows(tv_show, data):
    # Convert the genre to lowercase, remove spaces, and vectorize it.
    data['genre'] = data['genre'].str.lower().str.replace(' ', '')
    # Initialize the TfidfVectorizer.
    vectorizer = TfidfVectorizer(analyzer='char')
    # Fit and transform the genre data.
    genre_matrix = vectorizer.fit_transform(data['genre'])
    # Find the index of the input TV show in the data.
    tv_show_index = data[data['title'] == tv_show].index[0]
    # Get the genre vector of the input TV show.
    tv_show_vector = genre_matrix[tv_show_index]
    # Calculate cosine similarities between the input TV show and all others.
    cosine_similarities = linear_kernel(tv_show_vector, genre_matrix).flatten()
    # Get indices of shows that are most similar in genre.
    genre_similar_indices = cosine_similarities.argsort()[-11:-1][::-1]
    # Get the rating of the input TV show.
    tv_show_rating = data.loc[tv_show_index, 'rating']
    rating_filtered_data = data[data['rating'] >= tv_show_rating]
    
    # Find the indices of the TV shows that meet both the genre and rating criteria 
    rating_genre_similar_indices = list(set(genre_similar_indices) & set(rating_filtered_data.index))
    # Return the titles of the TV shows that meet both the genre and rating criteria
    return data.loc[rating_genre_similar_indices, 'title']


# Define the base URL 
base_url = 'https://www.imdb.com/search/title/?title_type=tv_series&num_votes=5000,&sort=user_rating,desc'
# Scrape data from IMDB for 50 pages 
data = scrape_data(base_url, 50)


# Get user input for a TV show name 
tv_show = input('Enter a TV show name: ')
# Find similar TV shows 
similar_tv_shows = get_similar_tv_shows(tv_show, data)

# Output the similar TV shows 
print(f'The TV shows that have a similar rating and similar genre to {tv_show} are:')
print(similar_tv_shows.to_string(index=False))

