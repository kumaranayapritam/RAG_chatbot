from setuptools import find_packages,setup

setup(name="ragchatbot",
       version="0.0.1",
       author="Pritam",
       author_email="ks.pritam83@gmail.com",
       packages=find_packages(),
       install_requires=['langchain_core','langchain-google-genai','python-dotenv','pydantic','fastapi','uvicorn','python-multipart','PyPDF2','pandas','pinecone','langchain','google-generativeai','numpy']
       )