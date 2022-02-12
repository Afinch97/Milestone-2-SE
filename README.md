# Project 1 - Movie Search https://project1-afinch6.herokuapp.com/

This demo explains how to take a Github repository and deploy it to the world!

## Copy this repo to your own personal one
1. On https://github.com/new, create a new repository (personal, not owned by org) called `project1`
2. In your terminal, in your home directory, clone the repo:`https://github.com/csc4350-sp22/project1-afinch6`
3. `cd` into the repository that is created and you should see all the files now.
4. Then, connect this cloned repo to your new personal repo made in Step 1: `git remote set-url origin https://www.github.com/{your-username}/project1.git` (be sure to change your username and remove the curly braces)
5. Run `git push origin main` to push the local repo to remote. You should now see this same code in your personal `project1` repo.

## Sign up for The Movie Database Developer Account
1. Follow the instructions here: https://developers.themoviedb.org/3/getting-started/introduction (if email verification is showing errors, just refresh the page)
2. When creating a New App, make sure you enable Article Search API.

## Install Requirements (if you don't already have them)
1. `pip install python-dotenv`
2. `pip install requests`

## Setup
1. Create `.env` file in your project directory
2. Add your NYT KEY (not Secret!) from https://www.themoviedb.org/settings/api with the line: `export TMDB_KEY='YOUR_KEY'`
3. In `app.py`, change Line 13 to a topic you want to get news about!
4. In `app.py`, add the following arguments to `app.run()`:
```
host='0.0.0.0',
port=int(os.getenv('PORT', 8080)),
```

## Run Application
1. Run command in terminal `python app.py`
2. Preview web page in browser '/'

## Deploy to Heroku
1. Install Heroku CLI: 

For WSL users, run `sudo curl https://cli-assets.heroku.com/install.sh | sh`. 

For Mac users, run `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` if you don't have Homebrew installed, then `brew tap heroku/brew && brew install heroku`. 

This could take a few minutes. In the meantime...

2. Create a free account on Heroku https://signup.heroku.com/login
3. Create a `requirements.txt` file with all your non-standard dependencies (based on any libraries you are importing), separated by a newline. In our case, they are `Flask` w/ a capital F, `requests`, and `python-dotenv`. Note that libraries like `os` are standard imports, so they don't need to be included.
4. Create a `Procfile`, which has the command that Heroku will use to run your app: `web: python app.py` (see documentation https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile)
5. Add + commit all changed files with git
6. Log in to Heroku: `heroku login -i`
5. Create a Heroku app: `heroku create`. This will create a new URL and associated host for you.
6. Push your code to Heroku: `git push heroku main`. This actually pushes your code to Heroku's remote repository.

You may get an error at this point relating to a buildpack. That means that Heroku can't figure out on its own what primary language your code is written in. You should be able to resolve this with `heroku buildpacks:set heroku/python`.

7. Open your app with your new URL: `heroku open`. Click the link to open if it doesn't open on its own. It shouldn't work, because it doeesn't have any environment variables (remember, your `.env` file is not in your git repository!)
8. Go to https://dashboard.heroku.com/apps and click your App, then go to Settings, and click "Reveal Config Vars"
10. Add your secret key from `.env` with the matching variable name (`TMBD_KEY`) and value (your key, without quotation marks!)
11. Run `heroku open` or refresh the URL if you have it open. Voila!

# Known Problems
1. One of the main problems is that not every movie has a correct wikipedia page link. Not sure what I can about that besides going and manually assign the links 
2. I originally wanted to be able to search by movie genre too but was unable to do that in the time period. I made a drop down menu I thought was cool but had to comment it out.
3. There's a little extra of the grey navbar hanging out there and it's a little annoying but don't really know how to correct that

# Issues Solved
1. I found the MediaWiki really annoying to use I'm not sure if that counts as an issue. 
2. There was an issue I had getting the taglines for the movies because they do not automatically come with the search results for the movies so I had to use another API that used the movie ID to find the taglines.
3. There was an error that popped up for bringing up the movie posters because sometimes there was not one available so just had to put an if statement making sure that if there wasn't one it just returned None.
