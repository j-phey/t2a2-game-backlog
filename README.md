# Coder Academy - T2A2 - Jonathan Phey

## API Webserver: Video Game Tracker

### R1. Identification of the problem you are trying to solve by building this particular app

There are several problems when it comes to keeping up with video games. As life happens, people who play video games often accumulate a backlog of unfinished games, leading to indecision and stress about which game to play next. This problem simply compounds as new games are released on a weekly basis. In this day and age, there is a steady and constant stream of new games being released weekly, leading to missed release dates and the choice paralysis of finishing a currently owned game compared to the desire to play the latest release. 

Also, when one does finish a game, there isn't an easy way to reflect and preserve your thoughts on the game. It's an even greater issue when a game hasn't been played for weeks or years, and trying to pick up where it was left is a huge challenge, because of not knowing where the story was left or not remembering how to play it.

This app attempts to solve these problems by becoming a single source of information and data for all of your beloved games — finished, unfinished and unreleased.

### R2. Why is it a problem that needs solving?

Many people face the challenge of drowning in a large gaming backlog and the constant fear of missing out on the greatest new releases. The vast sea of video games, the constant stream of releases and the fact that life gets in the way means it's hard to focus on what to play when we finally get some time. A solution is needed to help gamers efficiently manage their backlog, allowing them to focus on the joy of playing rather than feeling burdened by choices.

Without a reliable way to stay informed about upcoming game releases important to the user (as compared to <i>all</i> releases), users may miss out on their most anticipated games. There's a need for an app or tool that keeps users informed about these releases to ensure these eagarly anticipated releases are not missed.

When completing a game, not celebrating this can diminish the sense of personal accomplishment. Also, not playing a game for an extended amount of time can make it difficult to recall the story or how to play it. This needs to be solved by an app so that users can track their personal victories and achievements, as well as make it simpler to allow the player to quickly pick up a game again to maximise their playing time.

By solving these problems, game backlogs, libraries and upcoming releases can be streamlined and personal achievements and thoughts and notes on games can be centralised.

### R3. Why have you chosen this database system. What are the drawbacks compared to others?

For this app, I have chosen to use PostgreSQL as the database management system.

PostgreSQL is open-source, meaning it is completely free to use, and its source code can be modified and redistributed. This will keep the cost of the database system for my app down. As a result of being open-source, it has a large community that can support it and has active users to continually update and improve it, which allows me to draw on the experience of the community if I hit roadblocks with the database system throughout the build. As it is known to be highly extensible and supportive of a wide array of different data types and languages, the community and the users of PostgreSQL can further create custom functions for it, which may not be possible through an alternative DBMS. As I am building this app largely in Python, this is beneficial to me.

Also, PostgreSQL is built to handle a large number of transactions and large amounts of data, making it suitable for applications that may require a high amount of scalability. Given that this app is meant to support players of any game library size, small or large, of games owned and on their wishlists, this ensures the number of transactions and stored data can scale to meet anyone's game tracking needs.

Given that the application and the stored personal game data may be sensitive in nature, PostgreSQL also includes a high level of security features, supporting advanced authentication methods, SSL certificates and data encryption to keep users safe. Not only is it secure, but it is known to have a great level of uptime and measures for server failure recovery, meaning players can reliably access and track their games at all times. 

That said, compared to other database systems, namely MongoDB, PostgreSQL does have certain drawbacks. As PostgresSQL enforces a predefined schema, changing the structure of the database can be difficult and slow, leading to a bottleneck and bringing development to a stop. Comparatively, MongoDB supports a fast and iterative approach as it is essentially without a predefined schema, allowing developers to adapt the database to their app's requirements on the fly.

In terms of querying, PostgreSQL relies on SQL for querying. While SQL is considered to be commonly used, it does come with a learning curve and can be considered to be less intuitive for those actively developing, especially when compared to MongoDB, which uses a JSON-based query language. Complex joining of tables can also become problematic when using SQL.

Finally, while PostgreSQL does have scaling capabilities as mentioned earlier, it does use a scale-up strategy, meaning in cases where high-performance is required, a ceiling may be met and resources may need to be diverted or scaled through caching. However, in MongoDB, scalability is completed through sharding, which enables a horizontal scale-out approach and ability to add more instances as required. 

With the benefits and drawbacks to other database systems (such as MongoDB) considered, I have decided that PostgreSQL is appropriate for the requirements of this app.

### R4. Identify and discuss the key functionalities and benefits of an ORM

An ORM, or Object Relational Mapper, bridges the gap between data representations in databases (often relational databases) and object-oriented programs. 

In most cases, when one wants to interact with a database using objected-oriented programming languages, regular operations such as creating, reading, updating and deleting (CRUD) data from a database is the norm. And usually, this would occur through using SQL to perform these operations in a relational database. That's why one of the key functionalities and benefits of an ORM is that it helps simplify this by allowing users the ability to use their language of choice to interact with the database, without needing to necessarily learn or use SQL. 

Additionally, relationship mapping is made easier with an ORM as it allows users to define the classes or objects, which then map to the database table. This includes mapping the object instances, the attributes and even the type of relationship, such as one-to-one, many-to-many, etc., which greatly simplifies the relationship between many entities.

One such ORM is called SQLAlchemy, and is the ORM that will be used for this project. A function and benefit of SQLAlchemy is that it will allow Python code to be used to map the database schema to the app's Python objects. Technically, by using SQLAlchemy, no SQL would be required to create, maintain and query the database. This will allow SQLAlchemy to handle the underlying database. 

A benefit many developers enjoy with SQLAlchemy is that it allows them to write Python code in their project to map from the database schema to the applications' Python objects. No SQL is required to create, maintain and query the database. The mapping allows SQLAlchemy to handle the underlying database so developers can work with their Python objects instead of writing bridge code to get data in and out of relational tables. As SQLAlchemy enables queries written in Python, it makes it simpler for the developer and for those already familiar with Python to read. Similarly, construction of queries that may be complex or unknown in SQL are made easier through writing the query in Python instead. Also, on the security front, because SQLAlchemy automatically escapes user input, it can effectively prevent malicious attempts of SQL injection or code execution.

### R5. List of endpoints

#### User authentication endpoints (`auth_controller.py`)
**`/auth/register`**
- **HTTP Request Verb:** POST
- **Description:** Allows for user registration, where the information is stored in the database.
- **Required data:** `email`, `password`
- **Expected response:** `200 OK` response with return of `email` and `token`.
- **Authentication method:** Authentication not required for new registrations. However, Bcrypt still hashes the password and stores it securely in the database.
- ![Endpoint - /auth/register](./docs/endpoint_auth_register.png 'Endpoint - /auth/register')

**`/auth/login`**
- **HTTP Request Verb:** POST
- **Description:** Allows user to login, generating a JWT token for authorisation.
- **Required data:** `email`, `password`
- **Expected response:** `200 OK` response with return of `email` and `token`.
- **Authentication method:** Valid email and password
- ![Endpoint - /auth/login](./docs/endpoint_auth_login.png 'Endpoint - /auth/login')

#### Games endpoints (`games_controller.py`)
**`/games`**
- **HTTP Request Verb:** GET
- **Description:** Get a list of all games in the app catalogue.
- **Required data:** None
- **Expected response:** `200 OK` response with return of games and game fields in the database.
- **Authentication method:** None
- ![Endpoint - /games](./docs/endpoint_get_games.png 'Endpoint - /games')

**`/games/<int:id>`**
- **HTTP Request Verb:** GET
- **Description:** Get a single game entry by Game ID.
- **Required data:** Valid game ID in the URL (e.g. /games/2)
- **Expected response:** `200 OK` response with return of the corresponding game and it's details.
- **Authentication method:** None
- ![Endpoint - /games/id](./docs/endpoint_get_game_id.png 'Endpoint - /games/id')


**`/games`**
- **HTTP Request Verb:** POST
- **Description:** Create a new game entry
- **Required data:** `title`, `description`, `release_date`, `genre`, `platform`
- **Expected response:** `200 OK` response, with the details of the created game and it's assigned game_id.
- **Authentication method:** Valid JWT token
- ![Endpoint - POST /games](./docs/endpoint_post_games.png 'Endpoint - POST /games')

**`/games/<int:id>`**
- **HTTP Request Verb:** PUT
- **Description:** Update an existing game entry in the catalogue.
- **Required data:** Existing game ID in the URL, `title`, `description`, `release_date`, `genre`, `platform`
- **Expected response:** `200 OK` response, with the details of the updated game.
- **Authentication method:** Valid JWT token, admin required
- ![Endpoint - PUT /games](./docs/endpoint_put_game.png 'Endpoint - PUT /games')

**`/games/<int:id>`**
- **HTTP Request Verb:** DELETE
- **Description:** Delete a game entry in the catalogue
- **Required data:** Existing game ID in the URL
- **Expected response:** `200 OK` response, with the details of the deleted game.
- **Authentication method:** Valid JWT token, admin required
- ![Endpoint - DELETE /games](./docs/endpoint_delete_game.png 'Endpoint - DELETE /games')

**`/games/search`**
- **HTTP Request Verb:** GET
- **Description:** Allows for searching of the game catalogue by specified filters or fields
- **Required data:** Valid filter / search parameters in the URL e.g. /games/search?genre=FPS
- **Expected response:** Details of the matching game(s) based on the filter / search paramaters
- **Authentication method:** None
- ![Endpoint - search /games](./docs/endpoint_search_game.png 'Endpoint - search /games')

#### Currently Playing endpoints (`currently_playing_controller.py`)
**`/currently_playing`**
- **HTTP Request Verb:** GET
- **Description:** Get a list of games currently being played
- **Required data:** None
- **Expected response:** `200 OK` response with return of the user and the details of the game(s) currently playing.
- **Authentication method:** Valid JWT token
- ![Endpoint - GET /currently_playing](./docs/endpoint_get_currently_playing.png 'Endpoint - GET /currently_playing')

**`/currently_playing/<int:id>`**
- **HTTP Request Verb:** GET
- **Description:** Get a single entry from the list of currently played games.
- **Required data:** Valid ID in the URL (e.g. /currently_playing/2)
- **Expected response:** `200 OK` response with return of the user and the details of the game currently playing.
- **Authentication method:** Valid JWT token
- ![Endpoint - /currently_playing/id](./docs/endpoint_currently_playing_id.png 'Endpoint - /currently_playing/id')

**`/currently_playing`**
- **HTTP Request Verb:** POST
- **Description:** Creates a new entry in the list of games currently playing
- **Required data:** `game_id`, `progress`
- **Expected response:** `200 OK` response with return of the user and the details of the game currently playing.
- **Authentication method:** Valid JWT token
- ![Endpoint - POST /currently_playing](./docs/endpoint_post_currently_playing.png 'Endpoint - POST /currently_playing')

**`/currently_playing/<int:id>`**
- **HTTP Request Verb:** PUT
- **Description:** Update an existing entry in the list of currently playing games
- **Required data:** Valid ID in the URL (e.g. /currently_playing/2), `progress`
- **Expected response:** `200 OK` response with return of the updated details (progress) and the game
- **Authentication method:** Valid JWT token, admin required
- ![Endpoint - PUT /currently_playing](./docs/endpoint_put_currently_playing.png 'Endpoint - PUT /currently_playing')

**`/currently_playing/<int:id>`**
- **HTTP Request Verb:** DELETE
- **Description:** Delete an existing currently playing entry by ID
- **Required data:** Valid ID in the URL (e.g. /currently_playing/2)
- **Expected response:** `200 OK` response with return of the deleted details (progress) and the game
- **Authentication method:** Valid JWT token, admin required
- ![Endpoint - DELETE /currently_playing](./docs/endpoint_delete_currently_playing.png 'Endpoint - DELETE /currently_playing')

**`/currently_playing/users`**
- **HTTP Request Verb:** GET
- **Description:** Retrieve a list of users and the games they are currently playing.
- **Required data:** None
- **Expected response:** `200 OK` response with return of the users and the game details that are currently being played
- ![Endpoint - /currently_playing/users](./docs/endpoint_currently_playing_users.png 'Endpoint - /currently_playing/users')

#### Backlog endpoints (`backlog_controller.py`)
**`/backlog`**
- **HTTP Request Verb:** GET
- **Description:** Get a list of games in the backlog
- **Required data:** None
- **Expected response:** `200 OK` response with return of the user and the details of the game(s) currently in the backlog
- **Authentication method:** None
- ![Endpoint - GET /backlog](./docs/endpoint_get_backlog.png 'Endpoint - GET /backlog')

**`/backlog/<int:id>`**
- **HTTP Request Verb:** GET
- **Description:** Get a single entry from the backlog.
- **Required data:** Valid ID in the URL (e.g. /backlog/1)
- **Expected response:** `200 OK` response with return of the user and the corresponding backlog game
- **Authentication method:** None
- ![Endpoint - /backlog/id](./docs/endpoint_backlog_id.png 'Endpoint - /backlog/id')

**`/backlog`**
- **HTTP Request Verb:** POST
- **Description:** Adds a game into the backlog (defaults to `Not Played` status)
- **Required data:** `game_id`
- **Expected response:** `200 OK` response with return of the user and the game title/id added to backlog
- **Authentication method:** Valid JWT token
- ![Endpoint - POST /backlog](./docs/endpoint_post_backlog.png 'Endpoint - POST /backlog')

**`/backlog/<int:id>`**
- **HTTP Request Verb:** PUT
- **Description:** Updates the status of a backlog entry
- **Required data:** Valid ID in the URL (e.g. /currently_playing/2), `status` (expected, not mandatory)
- **Expected response:** `200 OK` response with return of the user and the game title/id updated in the backlog
- **Authentication method:** Valid JWT token, admin required
- ![Endpoint - PUT /backlog](./docs/endpoint_put_backlog.png 'Endpoint - PUT /backlog')


**`/backlog/<int:id>`**
- **HTTP Request Verb:** DELETE
- **Description:** Delete an entry in the game backlog
- **Required data:**  Valid ID in the URL (e.g. /currently_playing/1)
- **Expected response:** `200 OK` response with return of the game and details deleted
- **Authentication method:** Valid JWT token, admin required
- ![Endpoint - DELETE /backlog](./docs/endpoint_delete_backlog.png 'Endpoint - DELETE /backlog')

#### Wishlist endpoints (`wishlist_controller.py`)
**`/wishlist`**
- **HTTP Request Verb:** GET
- **Description:** Get a list of games currently in the wishlist
- **Required data:** None
- **Expected response:** `200 OK` response with return of the user and the details of the game(s) in the wishlist
- **Authentication method:** None
- ![Endpoint - GET /wishlist](./docs/endpoint_get_wishlist.png 'Endpoint - GET /wishlist')

**`/wishlist/<int:id>`**
- **HTTP Request Verb:** GET
- **Description:** Get a single entry from the wishlist.
- **Required data:** Valid ID in the URL (e.g. /wishlist/1)
- **Expected response:** `200 OK` response with return of the user and the corresponding wishlisted game
- **Authentication method:** None
- ![Endpoint - /wishlist/id](./docs/endpoint_get_wishlist_id.png 'Endpoint - /wishlist/id')

**`/wishlist`**
- **HTTP Request Verb:** POST
- **Description:** Adds a game into the wishlist
- **Required data:** `game_id`, `priority`
- **Expected response:** `200 OK` response with return of the user and the game title/id added to wishlist
- **Authentication method:** Valid JWT token
- ![Endpoint - POST /wishlist](./docs/endpoint_post_wishlist.png 'Endpoint - POST /wishlist')

**`/wishlist/<int:id>`**
- **HTTP Request Verb:** PUT
- **Description:** Updates the status of a wishlist entry
- **Required data:** Valid ID in the URL (e.g. /wishlist/1), `priority` 
- **Expected response:** `200 OK` response with return of the user and the game title/id updated in the wishlist
- **Authentication method:** Valid JWT token, admin required
- ![Endpoint - PUT /wishlist](./docs/endpoint_put_wishlist.png 'Endpoint - PUT /wishlist')

**`/wishlist/<int:id>`**
- **HTTP Request Verb:** DELETE
- **Description:** Delete an entry in the game wishlist
- **Required data:**  Valid ID in the URL (e.g. /wishlist/1)
- **Expected response:** `200 OK` response with return of the game and details deleted
- **Authentication method:** Valid JWT token, admin required
- ![Endpoint - DELETE /wishlist](./docs/endpoint_delete_wishlist.png 'Endpoint - DELETE /wishlist')

### R6. Entity relationship diagram (ERD)

Below is the Entity Relationship Diagram (ERD) for the game tracker app. The entities are users, games, currently playing games (currently_playing), games in backlog (backlog) and wishlisted games (wishlist). 

The one-to-many relationship between users and currently_playing, backlog and wishlist enable users to have multiple (game) entries in those respective entities or lists. Likewise, the many-to-one relationship between games and currently_playing, backlog and wishlist allows more than one game to be within those entities or lists.

The users columns are purposely kept at a minimum to reduce unnecessary PII. The columns in games could be increased in the future, such as with information about how long a game would take to beat. Likewise, the columns in the currently_playing, backlog, and wishlist tables could be expanded on, but currently have the necessities for the tables to meet their purposes.

![Game Tracker ERD](./docs/Game_Tracker_ERD.png 'Game Tracker ERD')

### R7. Third party services used

**Flask (`flask`)**
- Description: Flask is a lightweight web application framework for Python, providing tools and libraries for building web applications.
- Usage: Flask is the core framework that organises the overarching templates and blueprints for the app and facilitates features such as API routes for the user authentication and game backlog.

- **SQLAlchemy (`flask_sqlalchemy`)**


LAZY LOAD THING

#### Python package dependencies

#### Other third party services used to create this project
- **Version control:** [GitHub](https://github.com/jjjjjjpppppp/)
- **Project management:** [Linear](https://linear.app/)

### R8. Projects models in terms of the relationships they have with each other

### R9. Database relations to be implemented in the application

### R10. How tasks are allocated and tracked in this project

### GitHub Repo
[**t2a2-game-backlog** - GitHub repository link](https://github.com/j-phey/t2a2-game-backlog)

### Python package dependencies
- colorama==0.4.6
- rich==13.6.0
- art==6.1

### Software development and implementation plan

- To build my plan and track my tasks and timelines, I utilised [Linear](https://linear.app/)
- Generally, I took two screenshots of my plan every day - at the mid point of my working day and when I decided to stop coding
- I moved the `Done` tasks to an archive daily, to keep the list clean
- Most days, I moved tasks to the `Todo` column when I wanted to attempt to complete it on a given day, while attempting to clear `In progress` as a priority (besides the slide deck and README files, which were constants)


- 28 October 2023
![Plan screenshot 14](./docs/2023-10-28_5.06.56pm.png 'Plan screenshot 2023-10-28_5.06.56pm')
- 29 October 2023
![Plan screenshot 15](./docs/2023-10-29_6.01.26pm.png 'Plan screenshot 2023-10-29_6.01.26pm')


### References

