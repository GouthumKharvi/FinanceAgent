import faiss
import numpy as np

def create_index(embeddings):
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index

def retrieve_top_k(index, query_embedding, k=5):
    distances, indices = index.search(query_embedding, k)
    return indices
