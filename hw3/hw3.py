# --- PART 1: READING DATA ---
from csv import reader

import pandas as pd


# 1.1
def read_movies_data(f):
	with open(f, 'r') as file:
		lines = file.readlines()
		moviesData = []
		index = []
		for line in lines:
			line = line.strip().split('|')
			line[0] = int(line[0])
			line[2] = int(line[2])
			index.append(line[0])
			moviesData.append(line[1:])
		moviesDF = pd.DataFrame(moviesData, index = index, columns = ['title', 'year', 'genre'])
		moviesDF.sort_index(axis = 0, inplace = True)
	return moviesDF

# 1.2
def read_ratings_data(f):
	with open(f, 'r') as file:
		rows = reader(file)
		movieRatings = {}
		for row in rows:
			movieID = int(row[1])
			if movieID not in movieRatings:
				movieRatings[movieID] = []
			movieRatings[movieID].append(float(row[2]))
	return movieRatings

# --- PART 2: PROCESSING DATA ---

# 2.1
def create_genre_dict(movies_df):
	genreDict = {}
	for genre in set(movies_df['genre'].tolist()):
		genreDict[genre] = movies_df[movies_df['genre'] == genre].index.tolist()
	return genreDict

# 2.2
def calculate_average_rating(ratings_dict, movies_df): 
	indices = movies_df.index.tolist()
	avgRatings = pd.Series([0.0] * len(indices), index = indices)
	for ind in indices:
		if ind in ratings_dict.keys():
			avgRatings.loc[ind] = sum(ratings_dict[ind]) / len(ratings_dict[ind])
	return avgRatings


# --- PART 3: RECOMMENDATION ---

# 3.1
def get_popular_movies(avg_ratings, n = 10):
	if (n >= len(avg_ratings)):
		return avg_ratings.sort_values(ascending = False)
	return avg_ratings.sort_values(ascending = False).head(n)

# 3.2
def filter_movies(avg_ratings, thres_rating=3):
	return avg_ratings[avg_ratings >= thres_rating]

# 3.3
def get_popular_in_genre(genre, genre_to_movies, avg_ratings, n = 5):
	if n == -1:
		return avg_ratings.loc[genre_to_movies.get(genre, [])].sort_values(ascending = False)
	return avg_ratings.loc[genre_to_movies.get(genre, [])].sort_values(ascending = False).head(n)

# 3.4
def get_genre_rating(genre, genre_to_movies, avg_ratings):
	return avg_ratings.loc[genre_to_movies.get(genre, [])].mean()

# 3.5
def get_movie_of_the_year(year, avg_ratings, movies_df):
	return movies_df.at[avg_ratings.loc[movies_df[movies_df['year'] == year].index].idxmax(), "title"]

# --- PART 4: USER FOCUSED ---

# 4.1
def read_user_ratings(f):
	with open(f, 'r') as file:
		rows = reader(file)
		userRatings = {}
		for row in rows:
			userID = int(row[0])
			if userID not in userRatings:
				userRatings[userID] = []
			userRatings[userID].append((int(row[1]), float(row[2])))
	return userRatings

# 4.2
def get_user_genre(user_id, user_to_movies, movies_df):
	genreRatings = {}
	for movieID, rating in user_to_movies.get(user_id, []):
		genre = movies_df.at[movieID, "genre"]
		if genre not in genreRatings:
			genreRatings[genre] = [0, 0, 0]
		genreRatings[genre][0] += rating
		genreRatings[genre][1] += 1
		genreRatings[genre][2] = genreRatings[genre][0] / genreRatings[genre][1] if genreRatings[genre][1] > 0 else 0
	return max(genreRatings, key = lambda x: genreRatings[x][2])

# 4.3
def recommend_movies(user_id, user_to_movies, movies_df, avg_ratings):
	genre = get_user_genre(user_id, user_to_movies, movies_df)
	moviesInGenre = movies_df[movies_df['genre'] == genre].index.tolist()
	moviesInGenreUnrated = moviesInGenre.copy()
	for movieID, _ in user_to_movies.get(user_id, []):
		if movieID in moviesInGenreUnrated:
			moviesInGenreUnrated.remove(movieID)
	if len(moviesInGenreUnrated) < 3:
		return avg_ratings.loc[moviesInGenre].sort_values(ascending = False)
	return avg_ratings.loc[moviesInGenreUnrated].sort_values(ascending = False).head(3)
