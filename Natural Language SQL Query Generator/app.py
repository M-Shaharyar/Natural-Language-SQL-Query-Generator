from dotenv import load_dotenv
load_dotenv()  # Load all environment variables from a .env file

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure the API key for Google Gemini model from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get a SQL query response from Google Gemini model based on user question and prompt
def get_gemini_response(question, prompt):
    # Initialize the 'gemini-pro' model
    model = genai.GenerativeModel('gemini-pro')
    
    # Generate a response by providing the prompt and question
    response = model.generate_content([prompt[0], question])
    
    # Return the text of the response (assumed to be a SQL query)
    return response.text

# Function to execute the SQL query on the specified database and retrieve results
def read_sql_query(sql, db):
    # Connect to the SQLite database
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    # Execute the SQL query provided by the Gemini model
    cur.execute(sql)
    
    # Fetch all rows resulting from the query
    rows = cur.fetchall()
    
    # Commit any changes and close the connection to free resources
    conn.commit()
    conn.close()
    
    # Print each row in the console for verification
    for row in rows:
        print(row)
    
    # Return the rows fetched from the database
    return rows

# Define the prompt to guide the Gemini model in generating SQL queries
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION
    
    Example queries:
    1. How many entries of records are present? 
       SQL: SELECT COUNT(*) FROM STUDENT;
    
    2. Tell me all the students studying in Data Science class? 
       SQL: SELECT * FROM STUDENT WHERE CLASS="Data Science";

    Note: The generated SQL should not include code formatting symbols (```) or "sql" in the output.
    """
]

# Set up the Streamlit web app interface
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App to Retrieve SQL Data")

# User input field for their question (e.g., "How many students are in Data Science class?")
question = st.text_input("Input: ", key="input")

# Submit button to process the question
submit = st.button("Ask the question")

# When the submit button is clicked
if submit:
    # Get the SQL query generated by the Gemini model
    response = get_gemini_response(question, prompt)
    print(response)  # Print the SQL query for debugging
    
    # Execute the SQL query on the 'student.db' database and get the data
    data = read_sql_query(response, "student.db")
    
    # Display the retrieved data on the Streamlit app
    st.subheader("The Response is:")
    for row in data:
        print(row)   # Print each row for verification
        st.header(row)  # Display each row in the app interface
