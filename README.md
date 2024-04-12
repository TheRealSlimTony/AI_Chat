
# AI_Chat POC

AI_Chat is a Django-based project that leverages the Django REST Framework (DRF) to create an API for a chat application integrated with AI functionalities. This project utilizes LangChain to handle document embeddings and similarity searches, providing intelligent responses based on input prompts.

## Features

- **AI Responses**: Accepts prompts through a POST request and processes them to generate AI-based responses.
- **Document Embedding**: Utilizes VectorialDatabase for managing document embeddings and performing similarity searches.
- **Data Management**: Provides an interface to load and embed documents into a vectorial database for future searches.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Django REST Framework
- LangChain and its dependencies

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/TheRealSlimTony/AI_Chat.git
   cd AI_Chat
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   # For Windows
   .\venv\Scripts\activate
   # For Unix or MacOS
   source venv/bin/activate
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```plaintext
   Rename .env.example to .env and update the values accordingly, including the OPENAI_API_KEY.
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```
   The API should now be accessible at http://127.0.0.1:8000/.

## Usage

- **Initialize the Vectorial Database**
  Make a POST request to `/api/initialize/` with the necessary document files to load and embed them into the vectorial database.

- **Ask a Question**
  Send a POST request to `/api/search_question/` with a JSON body containing the prompt. For example:
  ```json
  {
    "prompt": "What is AI?"
  }
  ```
  You'll receive an AI-generated response based on the embedded documents and similarity search.
