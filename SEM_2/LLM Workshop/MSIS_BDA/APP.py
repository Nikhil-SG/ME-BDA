import os
import streamlit as st
from llama_index.core.llms import ChatMessage
from llama_index.llms.groq import Groq
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.schema import TextNode
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from tqdm import tqdm
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.core import get_response_synthesizer
from llama_index.core import PromptTemplate

# Initialize the LLM and other variables
llm = Groq(model="llama3-70b-8192", api_key='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')

# Initialize PDF Reader
pdf_folder = 'DOC'  # Path to your PDF folder
pdf_reader_obj = PDFReader(return_full_document=True)

# Load documents in a loop to handle multiple files
documents = []
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):  # Process only PDF files
        file_path = os.path.join(pdf_folder, filename)
        documents.extend(pdf_reader_obj.load_data(file_path))  # Use extend to add documents to the list

# Concatenate the text from pages (documents) into a single string
full_text = ""
for doc in documents:
    full_text += doc.text + "\n"

# Split the text into smaller chunks
text_parser = TokenTextSplitter(chunk_size=128, chunk_overlap=8)
chunks = text_parser.split_text(text=full_text)

# Convert chunks into Llama nodes
nodes = [TextNode(text=chunk_text) for chunk_text in chunks]

# Load the embedding model from Hugging Face
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Create embeddings for the chunks
for node in tqdm(nodes):
    node_embedding = embed_model.get_text_embedding(node.get_content(metadata_mode="all"))
    node.embedding = node_embedding

# Create a collection in ChromaDB
db = chromadb.EphemeralClient()
chroma_collection = db.get_or_create_collection("MSISBDA")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Create a vector store index
index = VectorStoreIndex(nodes=nodes, storage_context=storage_context, embed_model=embed_model)

# Create a retriever object
retriever = VectorIndexRetriever(index=index, similarity_top_k=10)

# Create a prompt template for the chatbot
template = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\n"
    "Query: {query_str}\n"
    "Answer: "
)

qa_template = PromptTemplate(template)

# Configure response synthesizer
response_synthesizer = get_response_synthesizer(llm, text_qa_template=qa_template)

# Assemble query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
    node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.4)]
)

# Streamlit UI
def main():
    st.title("Welcome to MSIS BDA Chatbot")
    st.write("Please enter your query:")

    query = st.text_input("Query")

    if query:
        # Process the query and get the response
        response = query_engine.query(query)
        st.write("Answer: ")
        st.write(response)

if __name__ == "__main__":
    main()
