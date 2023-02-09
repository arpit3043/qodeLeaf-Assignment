# Assignment Link:
- [Notion Assignment Link](https://tiny-tuck-cca.notion.site/Backend-Assignment-Qodeleaf-b495923671e942b3a118ef0acb381dab)
# Youtube-searchapi

This is django project which will scrap music videos details asynchronous every hour from youtube using selenium to avoid api limit of google


## Run Locally

Clone the project

```bash
git clone https://link-to-project
```

Go to the project directory

```
cd Youtube-API
```
Create Virtual env
```
python -m venv .venv
```
Activate virtual environment

Install dependencies
```
pip install -r requrements.txt

```
makemigrations and migrate
```
python manage.py makemigrations
python manage.py migrate
```
Start the server

```
python manage.py runserver
```

# Generated API
```
  API Key:
  AIzaSyBcvQYU9bArXdLJLuY_6X6OhQL4UzMqXb0
```
# Issue Faced in the working with this API:
 - The API was able to fetch 100 results per day and in total.
 - The main issue I faced while working with API is the data confliction and the results it was fetching each time
 - We used Selenium Scapper to scrap the API and then we make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.
## API Reference
- YouTube data v3 API: [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)
- Search API reference: [https://developers.google.com/youtube/v3/docs/search/list](https://developers.google.com/youtube/v3/docs/search/list)
    - To fetch the latest videos you need to specify these: type=video, order=date, publishedAfter=<SOME_DATE_TIME>
    - Without publishedAfter, it will give you cached results which will be too old

#### Create a new user

```http
  POST /api/createUser/
```
### Request JWT token
```
POST /api/token/
```
### Request JWT access token
```
POST /api/token/refresh/
```
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
## Authors

- [@arpit3043](https://www.github.com/arpit3043)