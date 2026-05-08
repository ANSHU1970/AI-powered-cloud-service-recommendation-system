import faiss
import numpy as np

from app.utils.provider_data import SERVICES
from app.services.embedder import create_embedding

texts = [
    service["description"]
    for service in SERVICES
]

embeddings = np.array(
    [create_embedding(text) for text in texts]
).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("FAISS vector database initialized")