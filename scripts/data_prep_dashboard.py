import pandas as pd
from datetime import datetime
cr = pd.read_excel("data/customer_rating.xlsx")


cr["TIMESTAMP"] = pd.to_datetime(cr["TIMESTAMP"], unit="s")
cr["ISSUE_RESOLVED_ENUM"] = cr["ISSUE_RESOLVED_ENUM"].fillna("Unknown")
cr["REGION"] = cr["REGION"].str.title()

product_columns = [col for col in cr.columns if col.endswith("YN")]

cr[product_columns] = cr[product_columns].replace({"Yes": 1, "No": 0})


cr["TOTAL_PRODUCTS"] = cr[product_columns].sum(axis=1)

# Export the modified DataFrame to an Excel file
output = "data/Customer_Data_with_Products.xlsx"
cr.to_excel(output, index=False)

print(f"Data exported to {output}")



