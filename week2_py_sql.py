import pandas as pd
import sqlite3

db_file = 'university.db'
conn = None  #define connection as none initially

try:
    #1. connect to the database
    conn = sqlite3.connect(db_file)

    #2. define the sql query (without a semicolon at the end)
    query = """
    select
        student_name,
        grade
    from
        students
    order by
        grade desc
    limit 5
    """

    #3. run the query and load the results into a dataframe
    print("sending query to the database...")
    top_students_df = pd.read_sql_query(query, conn)

    #4. print the results to the screen
    print("\nsuccessfully loaded.")
    print("\nresults:")
    print(top_students_df)

except Exception as e:
    #if an error occurs, print the error
    print(f"\nan error occurred: {e}")

finally:
    #5. no matter what, close the connection if it exists
    if conn:
        conn.close()
        print("\ndatabase connection closed.")