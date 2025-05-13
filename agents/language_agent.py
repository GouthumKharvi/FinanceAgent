from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

def generate_narrative(retrieved_data):
    llm = ChatOpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retrieved_data.as_retriever(),
        return_source_documents=False
    )
    query = "Give me a market brief based on the uploaded data"
    result = qa_chain.run(query)
    return result
