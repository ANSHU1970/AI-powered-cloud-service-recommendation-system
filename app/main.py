from fastapi import FastAPI
from app.routes.recommend import router as recommend_router

app = FastAPI(title="AWS ML Recommender")

app.include_router(recommend_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "AWS ML Recommendation API running"}