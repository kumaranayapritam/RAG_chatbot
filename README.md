# RAG-Based Question-Answering Chatbot

A Retrieval-Augmented Generation (RAG) powered chatbot that answers questions based on provided documents. Built with FastAPI and containerized with Docker.

## Features

- Document ingestion (PDF, DOCX, TXT)
- Vector database integration with Pinecone
- RAG-based question answering using Google's Gemini model
- REST API endpoints for document upload and queries
- Docker containerization
- Streamlit UI for interaction

## Prerequisites

- Python 3.9+
- Docker and Docker Compose
- Google API key
- Pinecone API key

## Environment Setup

1. Clone the repository
2. Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## Local Development Setup

1. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

4. Run the Streamlit UI (in a separate terminal):

```bash
streamlit run streamlit_ui.py
```

## Docker Deployment

1. Build and run using Docker Compose:

```bash
docker compose up --build
```

2. To stop and remove containers:

```bash
docker compose down
```

3. To clean up Docker system:

```bash
docker system prune -f
```

4. Run individual container:

```bash
docker run -d -p 8080:8080 --name my-app-container rag_chat-rag-api
```

## API Endpoints

### Upload Documents
- **URL**: `/upload`
- **Method**: POST
- **Content-Type**: multipart/form-data
- **Parameters**: files (PDF, DOCX, or TXT)

### Query
- **URL**: `/query`
- **Method**: POST
- **Content-Type**: application/json
- **Request Body**:
```json
{
    "question": "Your question here"
}
```
#### You can also run the curl commands individually from PowerShell:
# Health check
curl http://localhost:8000/health

# Upload document

curl -X POST -F "file=@data/sample.pdf" http://localhost:8000/upload

# Query

curl -X POST -H "Content-Type: application/json" -d "{\"question\":\"What is the main topic?\"}" http://localhost:8000/query

## Usage Example

1. Upload documents using the Streamlit UI or API endpoint
2. Ask questions about the uploaded documents
3. Receive AI-generated answers based on the document content

## Project Structure

```
├── app/
├── config/
│   └── config.yaml
├── data_ingestion/
├── data_models/
├── exception/
├── retriever/
├── utils/
├── docker-compose.yml
├── Dockerfile
├── main.py
├── requirements.txt
└── streamlit_ui.py
```

## Error Handling

The application includes comprehensive error handling for:
- Missing environment variables
- File upload issues
- Vector database connection problems
- Query processing errors

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

