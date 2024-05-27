from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, validator 
import tasks

app = FastAPI()

# Route 1 : /
# Test if everything is working
@app.get("/")
def get_root():
    return {"message": "Hello world"}

# Route 2: /translate
# take in a translation request, and store it to the db
# Return a translation id

# Route 3: /results
# Take in a translation id
# Return a translated text