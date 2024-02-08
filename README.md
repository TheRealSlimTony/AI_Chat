##AI_Chat

#AI_Chat is a Django-based project that leverages Django REST Framework (DRF) to create an API for a chat application integrated with AI functionalities. The project utilizes LangChain to handle document embeddings and similarity searches to provide intelligent responses based on the input prompts.

## Features
- Accepts prompts through a POST request and processes them to generate AI-based responses.
- Utilizes VectorialDatabase for managing document embeddings and performing similarity searches.
- Provides an interface to load and embed documents into a vectorial database for future searches.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
- Python 3.8+
- Django 3.2+
- Django REST Framework
- LangChain and its dependencies

## Installation
Clone the repository
bash
Copy code
git clone https://github.com/yourusername/AI_Chat.git
cd AI_Chat
Setup a virtual environment
bash
Copy code
python -m venv venv
For Windows:
bash
Copy code
.\venv\Scripts\activate

For Unix or MacOS:
bash
Copy code
source venv/bin/activate
Install the dependencies
bash
Copy code
pip install -r requirements.txt
Set up environment variables
Rename .env.example to .env and update the values accordingly, including the OPENAI_API_KEY.

Run migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
Start the development server
bash
Copy code
python manage.py runserver
The API should now be accessible at http://127.0.0.1:8000/.

## Usage
Initialize the Vectorial Database
Make a POST request to /api/initialize/ with the necessary document files to load and embed them into the vectorial database.

Ask a Question
Send a POST request to /api/search_question/ with a JSON body containing the prompt. For example:

json
Copy code
{
  "prompt": "What is AI?"
}
You'll receive an AI-generated response based on the embedded documents and similarity search.

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
LangChain for providing the tools for document embeddings and similarity searches.
Django and Django REST Framework for the web framework and API toolkit.
