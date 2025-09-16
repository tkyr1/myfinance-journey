import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

db_file = 'university.db'
conn = None

try:
    conn = sqlite3.connect(db_file)

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
    print("sending query to the database...")
    top_students_df = pd.read_sql_query(query, conn)

    print("\nsuccessfully loaded. results:")
    print("\nresults:")
    print(top_students_df)

    #this is the new part that makes the chart
    print("\ncreating chart...")
    plt.figure() # creates a new figure for the plot
    
    # creates the bar chart using student names for the x-axis and grades for the y-axis
    plt.bar(top_students_df['student_name'], top_students_df['grade'])
    
    plt.title('top 5 students by grade') # adds a title to the chart
    plt.ylabel('grade') # adds a label to the y-axis
    
    plt.show() # opens a new window to display the chart

except Exception as e:
    print(f"\nan error occurred: {e}")

finally:
    if conn:
        conn.close()
        print("\ndatabase connection closed.")