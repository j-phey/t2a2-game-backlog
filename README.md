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

- / root
- @app.route("/games", methods=["GET"])
- @app.route("/games", methods=["POST"])
- @app.route("/auth/register", methods=["POST"])
- @app.route("/auth/login", methods=["POST"])
- @app.route("/games/<int:id>", methods=["DELETE"])
- @games.route("/<int:id>/", methods=["GET"])
- @games.route("/<int:id>/", methods=["PUT"])
- @games.route("/search", methods=["GET"]) (http://127.0.0.1:5000/games/search?genre=FPS)
- @currently_playing.route("/", methods=["GET"])

### R6. Entity relationship diagram (ERD)
![Game Tracker ERD](./docs/Game_Tracker_ERD.png 'Game Tracker ERD')

### R7. Third party services used

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

