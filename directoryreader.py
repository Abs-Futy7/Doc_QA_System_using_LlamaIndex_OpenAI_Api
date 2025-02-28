from llama_index.readers.web import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv

load_dotenv()

def main(directory_path: str) -> None:
    # Load documents from the specified directory
    document = SimpleDirectoryReader(html_to_text=True).load_data(path=directory_path)
    
    # Create the index from the documents
    index = VectorStoreIndex.from_documents(documents=document)
    
    # Set up the query engine
    query_engine = index.as_query_engine()
    
    # Perform a query
    response = query_engine.query("What is this about?")

    print(response)

if __name__ == "__main__":
    directory_path = r"C:\Users\Documents\GitHub\llama_index"
    main(directory_path)

