# Coder Academy - T2A2 - Jonathan Phey

## API Webserver: Video Game Tracker

### R1. Identification of the problem(s) this app solves

There are several problems when it comes to keeping up with video games. As life happens, people who play video games often accumulate a backlog of unfinished games, leading to indecision and stress about which game to play next. This problem simply compounds as new games are released on a weekly basis. In this day and age, there is a steady and constant stream of new games being released weekly, leading to missed release dates and the choice paralysis of finishing a currently owned game compared to the desire to play the latest release. 

<p>Also, when one does finish a game, there isn't an easy way to reflect and preserve your thoughts on the game. It's an even greater issue when a game hasn't been played for weeks or years, and trying to pick up where it was left is a huge challenge, because of not knowing where the story was left or not remembering how to play it.

<p> This app attempts to solve these problems by becoming a single source of information and data for all of your beloved games — finished, unfinished and unreleased.

### R2. Why do these problems need solving?

Many people face the challenge of drowning in a large gaming backlog and the constant fear of missing out on the greatest new releases. The vast sea of video games, the constant stream of releases and the fact that life gets in the way means it's hard to focus on what to play when we finally get some time. A solution is needed to help gamers efficiently manage their backlog, allowing them to focus on the joy of playing rather than feeling burdened by choices.

<p> Without a reliable way to stay informed about upcoming game releases important to the user (as compared to <i>all</i> releases), users may miss out on their most anticipated games. There's a need for an app or tool that keeps users informed about these releases to ensure these eagarly anticipated releases are not missed.

<p> When completing a game, not celebrating this can diminish the sense of personal accomplishment. Also, not playing a game for an extended amount of time can make it difficult to recall the story or how to play it. This needs to be solved by an app so that users can track their personal victories and achievements, as well as make it simpler to allow the player to quickly pick up a game again to maximise their playing time.

By solving these problems, game backlogs, libraries and upcoming releases can be streamlined and personal achievements and thoughts and notes on games can be centralised.

### R3. The chosen database system - benefits and drawbacks

For this app, I have chosen to use PostgreSQL as the database management system.

PostgreSQL is open-source, meaning it is completely free to use, and its source code can be modified and redistributed. This will keep the cost of the database system for my app down. As a result of being open-source, it has a large community that can support it and has active users to continually update and improve it, which allows me to draw on the experience of the community if I hit roadblocks with the database system throughout the build. As it is known to be highly extensible and supportive of a wide array of different data types and languages, the community and the users of PostgreSQL can further create custom functions for it, which may not be possible through an alternative DBMS. As I am building this app largely in Python, this is beneficial to me.

Also, PostgreSQL is built to handle a large number of transactions and large amounts of data, making it suitable for applications that may require a high amount of scalability. Given that this app is meant to support players of any game library size, small or large, of games owned and on their wishlists, this ensures the number of transactions and stored data can scale to meet anyone's game tracking needs.

Given that the application and the stored personal game data may be sensitive in nature, PostgreSQL also includes a high level of security features, supporting advanced authentication methods, SSL certificates and data encryption to keep users safe. Not only is it secure, but it is known to have a great level of uptime and measures for server failure recovery, meaning players can reliably access and track their games at all times. 


### R4. An ORM - key functionalities and benefits
ORM in general, SQLAlchemy

### R5. List of endpoints

### R6. Entity relationship diagram (ERD)

### R7. Third party services used

#### Python package dependencies

#### Other third party services used to create this project
- **Version control:** [GitHub](https://github.com/jjjjjjpppppp/)
- **Project management:** [Linear](https://linear.app/)

### R8. Project models and relationships

### R9. Database relations implemented

### R10. Software development plan

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

