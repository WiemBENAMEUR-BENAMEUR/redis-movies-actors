import redis
from collections import defaultdict

# Connect to Redis
rd = redis.Redis(host='localhost', port=6379, decode_responses=True)


# 1. Count actors with last name starting with "P"
def count_actors_lastname_P():
    actor_keys = rd.keys("actor:*")
    count = 0
    for key in actor_keys:
        l_name = rd.hget(key, "last_name")
        if l_name and l_name.startswith("P"):
            count += 1
    return count

# 2. Movies released after 2010 with more than 100,000 votes
def movies_after_2010_votes_100k():
    movie_keys = rd.keys("movie:*")
    results = []
    for key in movie_keys:
        r_year = rd.hget(key, "release_year")
        votes = rd.hget(key, "votes")
        if r_year and votes:
            if int(r_year) > 2010 and int(votes) > 100000:
                results.append(rd.hget(key, "title"))
    return results

# 3. Create top_movies_by_genre:<genre>
def create_top_movies_by_genre():
    genre_dict = defaultdict(list)
    movie_keys = rd.keys("movie:*")

    for key in movie_keys:
        genre = rd.hget(key, "genre")
        rating = rd.hget(key, "rating")
        title = rd.hget(key, "title")
        if genre and rating:
            genre_dict[genre].append((title, float(rating)))

    for genre, movies in genre_dict.items():
        top_movie = max(movies, key=lambda x: x[1])  
        rd.hset(f"top_movies_by_genre:{genre}", mapping={
            "title": top_movie[0],
            "rating": top_movie[1]
        })

# Main execution
if __name__ == "__main__":
    print("✅ Actors with last name starting with 'P':", count_actors_lastname_P())
    print("🎬 Movies after 2010 with >100k votes:")
    for movie in movies_after_2010_votes_100k():
        print("*", movie)
    
    print("🏆 Creating top_movies_by_genre...")
    create_top_movies_by_genre()
    print("Done!! Good Wiem!")
