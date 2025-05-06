## Project Description

This project demonstrates how to interact with a Redis database using a dataset of actors and movies. It covers loading data into Redis using Docker, interacting with Redis using Python, and performing simple data queries and analysis.

This project uses two datasets:

actors.redis: Contains data for around 1300 actors.
movies.redis: Contains data for around 900 movies.


The main goal is: 
- Deploy Redis and RedisInsight using Docker Compose.
- Load actor and movie data from `.redis` files using Redis CLI.
- Explore and manipulate the data using Python.
- Perform queries and aggregations on the dataset.
- Create additional data structures to support analytical queries.
- Clean up the environment after use.


Key technologies and tools used:
- **Redis**: for data storage and querying.
- **Docker**: to quickly spin up Redis and RedisInsight environments.
- **Python**: to interact programmatically with the Redis database using the `redis` package.

- ### Key Functionalities

1. **Setup & Deployment**
   - Uses Docker Compose to run Redis , RedisInsight and Jypyter. 

2. **Data Loading**
   - Load data into Redis via:
     ```
     Get-Content .\data\movies.redis | docker exec -i redis-server redis-cli
     Get-Content .\data\actors.redis | docker exec -i redis-server redis-cli
     ```

3. **Exploration & Queries**
 
   Through Python, I answer questions like:
        How many actors and movies are stored in Redis?
        List 5 actors born before 1980.
        Retrieve the genre and rating of the movie "The Imitation Game".
        List the top 5 highest-rated movies.
        How many movies have a rating above 7.5?
        Update the rating of the movie "The Imitation Game" to 8.5.
        Add a new actor: "Zendaya", born in 1996.
        Delete the movie with title "The Room".

5. **Advanced Python Analysis**
   A Python script (`python_redis_Part2`) automates several operations:
        Connects to Redis.
        Loads all actor hashes and counts how many actors have a last name starting with “P”.
        Gets all movies released after 2010 with more than 100,000 votes.
        Creates a new hash: top_movies_by_genre:<genre> with the highest-rated movie per genre.


### Deliverables

The GitHub repository includes:
- `docker-compose.yml`: To deploy Redis and RedisInsight.
- `data/` folder: Contains the original Redis data files (`actors.redis`, `movies.redis`).
- `python_redis_Part2.py`: A Python script for querying and analyzing Redis data.
- `README.md`: Instructions and explanation of the project.
- `results.pdf`: Answers to the required exploration queries.


