# Solysis - A Social Media Analysis and Schedule Posting Web Application


![logo](/images/HomePage.png)

# Introduction

## The Project

Easily manage all aspects of your social media presence with Solysis. From planning and scheduling posts to evaluating and analyzing your social media performance, these are necessary steps towards optimizing your marketing strategies and maximizing sales and profit📈. By carefully examining key metrics such as engagement rates, follower growth, content reach, and conversion rates, you gain valuable insights into what's working well and where improvements can be made.

With our user-friendly interface, you can effortlessly organize your campaigns and ensure timely delivery of your content, you can say goodbye to using multiple tools to improve your brand social media presence, this involves handling day-to-day operations across various social channels, including Tweets(now called Posts), Facebook updates, and LinkedIn posts. Our platform will also analyze usage patterns, providing insights into the most utilized social platforms and the volume of data consumed on each. 

Whether you're a person trying to build a social presence, a solo entrepreneur or part of a large team, our platform is designed to meet your needs. Stay on top of your social media game and reach your audience effectively. Simplify your workflow, boost productivity, and achieve your marketing goals with less stress☺️ .

### What inspired this project?
From Nenye’s days studying statistics to her time in sales, She has always been captivated by the power of data. There's something magical about turning numbers into actionable insights, especially when it comes to understanding customer behaviors and engagement. This shared passion with Tobi led to the creation of Solysis. We wanted to craft a tool that not only simplifies but also enhances the way brands interact with their audience. Our mission? To harness the strength of data to supercharge marketing strategies and boost sales.

### Deployed Website
[SOLYSIS DEPLOYED PAGE](https://solysis.vercel.app/)

### Blog posts
* *Ojo Oluwatobiloba* [Slonjoh's blog post](https://medium.com/@slonjoh/the-purpose-of-this-project-is-to-manage-brands-social-presence-this-involves-handling-day-to-day-4bb38a0d0cd2) "Solysis a Social media analytics web application."
* *Chinenye Genevieve Onyema* [Nenye's blog post](https://www.linkedin.com/feed/update/urn:li:activity:7183914754279690240/) "Meet Solysis our brainchild social media dashboard designed to analyze user engagement across multiple social media platforms"

### Authors
* *Ojo Oluwatobiloba* [Slonjoh's Linkedin](https://www.linkedin.com/in/slonjoh/) - Software Engineer | Occasional Writer | Graphics designer | Chemist.
* *Chinenye Genevieve Onyema* [Nenye's Linkedin](https://www.linkedin.com/in/chinenyeonyema/) - Cloud Solutions Architect | Software Developer | DevOps Engineer | Statistician.

# Installation and Usage 
1. Clone this repository to your local machine using the command:
*            git clone https://github.com/nenyeonyema/solysis.git

2. For the handling user and interacting with the database to perform CRUD (Create, Read, Update, Delete) operations on the data.
*            Run the console.py file[./console.py] and use the create, all, show, destroy,create_post functions, as defined in the console.py file.
*            Note: Run "apt install mysql-server" if you got a "sqlalchemy not defined" error at first ./console.py run.

You can also run console.py using MYSQL database to create user and create post:
* echo 'create User email="example@mail.com" password=your_password first_name="your name" last_name="your lastname" username="your_username"' | SOLYSIS_MYSQL_USER=solysis_dev SOLYSIS_MYSQL_PWD=solysis_dev_pwd SOLYSIS_MYSQL_HOST=localhost SOLYSIS_MYSQL_DB=solysis_dev_db SOLYSIS_TYPE_STORAGE=db ./console.py

* echo 'create_post 6dbb99a9-14f1-4b8e-9112-778e5b91b852 facebook "The first message" --schedule 2024-03-30T19:32:01' | SOLYSIS_MYSQL_USER=solysis_dev SOLYSIS_MYSQL_PWD=solysis_dev_pwd SOLYSIS_MYSQL_HOST=localhost SOLYSIS_MYSQL_DB=solysis_dev_db SOLYSIS_TYPE_STORAGE=db ./console.py
*[Arguments are "previously generated user_id", "platform to send post", "Message to be posted", "Scheduled time of post".]*

3. Run Web_flask:
*              SOLYSIS_MYSQL_USER=solysis_dev SOLYSIS_MYSQL_PWD=solysis_dev_pwd SOLYSIS_MYSQL_HOST=localhost SOLYSIS_MYSQL_DB=solysis_dev_db SOLYSIS_TYPE_STORAGE=db SOLYSIS_API_HOST=0.0.0.0 SOLYSIS_API_PORT=5000 python3 -m web_flask.solysis_flask

### Architecture
![Architectyre](/images/architecture.jpg)

### APIs and Methods

#### API Routes for Web Client Communication:

1. /api/social-media/posts
* GET: Retrieves recent social media posts for the authenticated user.
* POST: Allows the user to create a new social media post.

2. /api/social-media/analytics
* GET: Fetches analytics data for the user's social media posts, including engagement metrics and audience demographics.

3. /api/user/profile
* GET: Returns the user's profile information, such as username, email, and profile picture.
* POST: Allows the user to update their profile information.

#### API Endpoints for External Clients:
1. Class: SocialMediaAPI
* Method: getRecentPosts(user_id)
         *Retrieves recent social media posts for the specified user.*
* Method: analyzePostEngagement(post_id)
         *Analyzes the engagement metrics of a specific social media post.*

2. Class: UserProfileAPI
* Method: getUserProfile(user_id)
         *Retrieves the profile information of the specified user.*
* Method: updateUserProfile(user_id, profile_data)
         *Updates the profile information of the specified user with the provided data.*
#### 3rd Party APIs:
1. Twitter API
* POST statuses/update: Allows posting new tweets.
* POST statuses/destroy/:id: Deletes a tweet by its ID.
* GET statuses/show/:id: Retrieves a specific tweet by its ID.
* GET statuses/oembed: Generates an HTML representation of a tweet.
* GET statuses/lookup: Retrieves multiple tweets by their IDs.

2. Facebook Graph API
* GET /{user-id}/posts: Retrieves posts from a user's timeline.
* GET /{post-id}/insights: Fetches insights data for a specific post.
* POST /{page-id}/feed: Publishes a new post on a Facebook Page.

3. LinkedIn API
* GET /v2/me: Retrieves the profile information of the authenticated user.
* GET /v2/ugcPosts: Fetches posts created by the authenticated user.
* POST /v2/ugcPosts: Allows the user to create a new post on LinkedIn.

These APIs and methods facilitate communication between the web client and server, as well as providing functionalities for external clients to interact with the system. Additionally, integration with 3rd party APIs such as Twitter, Facebook, and LinkedIn enriches the platform's capabilities by leveraging data and functionalities from these social media platforms.

## User Usage
![Analysis](/images/Social-media-overview-dashboard-followers.png)

![Post](/images/socials-1.png)

# Contributing
* *Ojo Oluwatobiloba* [Slonjoh's Github](https://github.com/Slonjoh) - Software Engineer | Occasional Writer | Graphics designer | Chemist.
* *Chinenye Genevieve Onyema* [Nenye's Github](https://github.com/nenyeonyema/) - Cloud Solutions Architect | Software Developer | DevOps Engineer | Statistician.

# Related projects
1. [AirBnB Clone](https://github.com/nenyeonyema/AirBnB_clone_v3.git) : A web Apllication made in Python, Flask, and JQuery.
2. [Simple_shell](https://github.com/Slonjoh/simple_shell.git) : The Simple Shell implementation of a Unix shell, provides a command line interface for users to interact with their operating system.

# LICENSE
MIT License
