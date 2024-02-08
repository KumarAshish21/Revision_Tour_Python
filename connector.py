import json
import mysql.connector
import pandas as pd

class InvoiceProcessor:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def process_invoices(self):
        request_content_query = """
            SELECT invoice_made.request_content 
            FROM invoice_made 
            WHERE invoice_made.channel IN ('mid_month', 'end_month', 'manual') 
                AND invoice_made.created_at BETWEEN '2023-04-01' AND CURDATE();
        """
        self.cursor.execute(request_content_query)

        data = []

        for row in self.cursor.fetchall():
            json_data = row[0]

            try:
                data_dict = json.loads(json_data)

                utl_ordr = data_dict.get('U_UTL_ORDR')
                document_lines = data_dict.get('DocumentLines', [])
                bill_to_city = data_dict.get('AddressExtension', {}).get('BillToCity')

                for line in document_lines:
                    if isinstance(line, dict):
                        account_code = line.get('AccountCode')
                        if account_code == "413001":
                            item_description = line.get('ItemDescription')
                            if item_description:
                                item_description = item_description.split('|', 1)[0].strip()

                                # Append processed data to the list
                                data.append({
                                    "Item Description": item_description,
                                    "U_UNE_QTY": line.get('U_UNE_QTY'),
                                    "U_UNIT_RATE": line.get('U_UNIT_RATE'),
                                    "UnitPrice": line.get('UnitPrice'),
                                    "Price": line.get('Price'),
                                    "Job_order": utl_ordr,
                                    "City": bill_to_city
                                })

                if utl_ordr:
                    # Append company and location name to the processed data
                    sql_query = """
                        SELECT customer_masters.company, locations.location_name
                        FROM locations
                        JOIN orders ON locations.id = orders.billing_godown
                        JOIN customers ON orders.customer_id = customers.id
                        JOIN customer_masters ON customers.customer_master_id = customer_masters.id
                        WHERE orders.job_order = %s
                    """
                    self.cursor.execute(sql_query, (utl_ordr,))
                    result = self.cursor.fetchone()

                    if result:
                        company, location_name = result
                        data[-1]["Company"] = company
                        data[-1]["Location Name"] = location_name

            except json.decoder.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

        df = pd.DataFrame(data)

        # Export DataFrame to Excel
        df.to_excel("/Users/youngmanindia/Documents/invoice_data.xlsx", index=False)
    def close_connection(self):
        self.cursor.close()
        self.db.close()

# Usage
processor = InvoiceProcessor(host='65.1.49.65', user='readonly', password='readonly%^&', database='youngman2')
processor.process_invoices()
processor.close_connection()
