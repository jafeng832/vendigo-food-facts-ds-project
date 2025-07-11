import requests
import csv
from tabulate import tabulate

# List of barcodes
barcodes = [
    "0028400012546",
    "0850251004018",
    "3168930167983"
]

def fetch_product_info(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    data = response.json()
    
    if data.get("status") == 1:
        product = data["product"]
        return {
            "Barcode": barcode,
            "Name": product.get("product_name", "N/A"),
            "Brand": product.get("brands", "N/A"),
            "Calories (kcal)": product.get("nutriments", {}).get("energy-kcal_100g", "N/A"),
            "Fat (g)": product.get("nutriments", {}).get("fat_100g", "N/A"),
            "Sugars (g)": product.get("nutriments", {}).get("sugars_100g", "N/A"),
            "Protein (g)": product.get("nutriments", {}).get("proteins_100g", "N/A"),
            "Ingredients": product.get("ingredients_text", "N/A"),
        }
    else:
        return {
            "Barcode": barcode,
            "Name": "❌ Not Found",
            "Brand": "-",
            "Calories (kcal)": "-",
            "Fat (g)": "-",
            "Sugars (g)": "-",
            "Protein (g)": "-",
            "Ingredients": "-",
        }

# Collect data
products_data = [fetch_product_info(code) for code in barcodes]

# Print as a table
print(tabulate(products_data, headers="keys", tablefmt="fancy_grid"))

# Save to CSV
csv_file = "products_info.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=products_data[0].keys())
    writer.writeheader()
    writer.writerows(products_data)

print(f"\n✅ Data written to {csv_file}")


