from fastapi import FastAPI
from lead_processor import process_lead
from router import route_request
from similarity import find_similar

app = FastAPI()

@app.get("/")
def home():
    return {"message": "KeaBuilder AI Service Running"}

# Lead processing endpoint
@app.post("/process-lead")
def process(data: dict):
    return process_lead(data)

# Content generation routing
@app.post("/generate")
def generate(data: dict):
    content_type = data.get("type")
    prompt = data.get("prompt")
    return route_request(content_type, prompt)

# Similarity search
@app.get("/similar")
def similar(query: str):
    result = find_similar(query)
    return {"query": query, "match": result}
