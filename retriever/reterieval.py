import os
from langchain.tools import tool
from langchain_community.tools import TavilySearchResults
from langchain_community.tools.polygon.financials import PolygonFinancials
from data_models.models import RagToolSchema
from langchain_pinecone import PineconeVectorStore
from utils.model_loaders import ModelLoader
from utils.config_loader import load_config
from dotenv import load_dotenv
from pinecone import Pinecone
from typing import List, Dict, Any

class Retriever:
    def __init__(self):
        print("Initializing Retriever...")
        self.model_loader = ModelLoader()
        self.config = load_config()
        self._load_env_variables()
        self._initialize_vector_store()

    def _load_env_variables(self):
        load_dotenv()
        required_vars = ["GOOGLE_API_KEY", "PINECONE_API_KEY"]
        missing_vars = [var for var in required_vars if os.getenv(var) is None]
        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")

    def _initialize_vector_store(self):
        """Initialize Pinecone vector store and retriever"""
        try:
            print("Connecting to Pinecone...")
            pc = Pinecone(api_key=self.pinecone_api_key)
            self.vector_store = PineconeVectorStore(
                index=pc.Index(self.config["vector_db"]["index_name"]),
                embedding=self.model_loader.load_embeddings()
            )
            print("Vector store initialized")
            
            self.retriever = self.vector_store.as_retriever(
                search_type="similarity_score_threshold",
                search_kwargs={
                    "k": self.config["retriever"]["top_k"],
                    "score_threshold": self.config["retriever"]["score_threshold"]
                }
            )
            print("Retriever initialized successfully")
        except Exception as e:
            print(f"Error initializing vector store: {str(e)}")
            raise

    def retrieve(self, question: str) -> List[Dict[str, Any]]:
        """
        Retrieve relevant documents for a given question
        Args:
            question (str): The question to search for
        Returns:
            List[Dict[str, Any]]: List of relevant documents
        """
        try:
            return self.retriever.invoke(question)
        except Exception as e:
            print(f"Error during retrieval: {str(e)}")
            raise
