import mysql.connector

# Establish a connection to the MySQL server
db = mysql.connector.connect(
    host='127.0.0.1',
    user='sammy',
    password='password',
    database='youngman'
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Define the job_site you want to select
selected_job_site = "DEL_BA"

# Execute a query
orders = "SELECT js.site_name, COUNT(orders.job_order) AS Orders FROM orders INNER JOIN quotations q ON orders.id = q.order_id INNER JOIN job_site js ON q.site_name = js.site_name WHERE js.site_name = %s;"

cursor.execute(orders, (selected_job_site,))

# Fetch the row returned by the query
row = cursor.fetchone()

# Process the row
if row is not None:
    site_name = row[0]
    order_count = row[1]
    print("Site Name:", site_name)
    print("Order Count:", order_count)
else:
    print("No orders found for the selected job site.")

# Close the cursor and the connection
cursor.close()
db.close()
