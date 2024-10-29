# Natural Language SQL Query Generator

A web-based application that enables users to interact with a SQLite database using natural language queries through Google’s Gemini language model. This app translates English questions into SQL queries, making it easy to retrieve database information without needing SQL knowledge.

## 🚀 Features

* **Natural Language to SQL Conversion**: Converts user questions in English into SQL queries using Google Gemini.
* **Database Interaction**: Executes SQL queries on a SQLite database and retrieves relevant data.
* **AI-Powered Query Generation**: Utilizes Google Generative AI for natural language processing to interpret user questions.
* **User-Friendly Interface**: Built with Streamlit for a clean and interactive user experience.
* **Dynamic Query Results**: Displays query results from the database directly in the app interface.

## 🛠️ Tech Stack

* **Python**: Core programming language used for development.
* **Streamlit**: Framework for building the web-based interface.
* **Google Generative AI**: Powers the natural language to SQL conversion.
* **SQLite3**: Database used to store and retrieve student data.
* **dotenv**: For securely loading environment variables.

## 📦 Installation

### Clone the Repository:
```
git clone https://github.com/M-Shaharyar/Natural-Language-SQL-Query-Generator.git
cd Natural-Language-SQL-Query-Generator
```
## Create a Virtual Environment:
```
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate     # For Windows
```

## Install Required Packages:
```
pip install -r requirements.txt
```

## Set Up Environment Variables:
1. Create a .env file in the project directory.
2. Add your API key to the .env file as follows:
```
GOOGLE_API_KEY=your_google_gemini_api_key
```

## 🖼️ Usage
```
Run the Application:
```
## Ask a Question:
* Enter a question in English, such as "How many students are in the Data Science class?" and click "Ask the question".

## View Results:
* The SQL query generated by the Gemini model will execute on the database, and the results will display on the Streamlit interface.

## Example Queries
1. "How many entries of records are present?"
*  Expected SQL: SELECT COUNT(*) FROM STUDENT;
2. "Tell me all the students studying in Data Science class?"
* Expected SQL: SELECT * FROM STUDENT WHERE CLASS="Data Science";



