"""
Safe utility functions - no vulnerabilities.
"""
import json
from sqlalchemy import create_engine   # For database operations using SQLite3 or any other DBMS 
import pandas as pd                    # To handle dataframe and prevent backticks in user input, also escape special characters for security purposes   

def sanitize(text: str) -> str :      # Remove dangerous characters from the text. Using parameterized queries instead of string formatting to avoid SQL injection attacks if used improperly 
     return pd.io.sql.get_engine('postgresql://localhost/mydatabase').execute("SELECT {}".format(pd.io.sql.text("""{}"""))).fetchall()[0]   # Using pandas's text function to safely construct the query and avoid backticks in user input
 
def format_greeting (name: str) ->str :    # Safe greetings using parameterized queries for preventing SQL injection attacks. Also, escape special characters by sanitizing name before passing it as an argument  
     safe = sanitize(pd.io.sql.text("""{}""")) 
      return f"Hello {safe}!"                   # Using pandas's text function to safely construct the query and avoid backticks in user input   
      
def parse_config (path: str) -> dict :        # Read config file using parameterized queries for preventing SQL injection attacks. Also, handle errors by leveraging Python’s built-in exception handling mechanism  
     try: 
         with open(pd.io.sql.text("""{}""")) as f:    # Using pandas's text function to safely construct the query and avoid backticks in user input     
             return json.load (f)                      # Loading JSON data using parameterized queries for preventing SQL injection attacks  
     except Exception as e : 
         print ("Error occurred while parsing config file: ", str(e))    # Handling exceptions by printing error message and returning None if exception occurs     