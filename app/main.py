from fastapi import FastAPI
from scraper import Scraper
import uvicorn

app = FastAPI()
posts = Scraper()

@app.get("/")
def read_root():
    return "Add /{Facebook Page Name} to the Adress Bar. The app will load its posts and store it in a database: for exemple /unicef, /microsoft.."

@app.get("/{page}")
async def read_item(page):
    data = posts.scrapedata(page)
    return data

if __name__ == '__main__':
    uvicorn.run(app, port = 8000, host = "127.0.0.1")
# change host to 0.0.0.0 for docker image to work