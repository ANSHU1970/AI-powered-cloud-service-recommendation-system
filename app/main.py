from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.recommend import router as recommend_router

app = FastAPI(
    title="AI Infrastructure Recommendation Engine",
    description="Hybrid Vector + Scoring based AI workload recommendation system",
    version="1.0.0"
)

# CORS (for future React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(
    recommend_router,
    prefix="/api",
    tags=["Recommendations"]
)

# Health Check
@app.get("/")
def root():

    return {
        "message": "AI Infrastructure Recommendation Engine Running",
        "status": "success"
    }

# Health endpoint
@app.get("/health")
def health():

    return {
        "status": "healthy",
        "llm": "llama3",
        "vector_db": "FAISS",
        "embedding_model": "all-MiniLM-L6-v2"
    }