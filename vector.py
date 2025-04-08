from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document 
import os 
import pandas as pd 

df = pd.read_csv('./data/realistic_restaurant_reviews.csv')

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"

add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"], # content
            metadata={"rating": row["Rating"], "date": row["Date"]}, # metadata
            id=str(i) # id
        )
        ids.append(stri(0))
        documents.append(document)

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location, # store presistently rather than in memory, not regenerated
    embedding_function=embeddings,
)

if add_documents:
    vector_sotre.add_documents(documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5} # look up 5 relevant reviews
)