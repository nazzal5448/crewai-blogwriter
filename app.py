from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse
from main import crew

app = FastAPI()

@app.get("/")
async def home(request:Request):
    return JSONResponse(content={"message": "Hello from CrewAI!"})

@app.get("/generate")
async def generate(main_keyword:str, related_keywords:list[str]=Query(...)):
    inputs = {
        "main_keyword":main_keyword,
        "related_keywords":related_keywords
    }
    response = crew.kickoff(inputs=inputs)
    return JSONResponse(content={"response": response.raw})