import duckdb
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns

csv_path = "/Users/jeffreyfeng/Downloads/en.openfoodfacts.org.products.csv.gz"

query = f"""
SELECT
    code,
    product_name,
    sugars_100g,
    fat_100g,
    proteins_100g,
    "energy-kcal_100g" AS calories
FROM read_csv_auto('{csv_path}')
WHERE
    sugars_100g IS NOT NULL AND
    fat_100g IS NOT NULL AND
    proteins_100g IS NOT NULL AND
    "energy-kcal_100g" IS NOT NULL AND
    (
        categories_tags ILIKE '%chips%' OR
        categories_tags ILIKE '%bars%' OR
        categories_tags ILIKE '%cookies%' OR
        categories_tags ILIKE '%popcorn%' OR
        categories_tags ILIKE '%nuts%' OR
        categories_tags ILIKE '%oatmeal%' OR
        categories_tags ILIKE '%fries%' OR
        categories_tags ILIKE '%crackers%'
    )
LIMIT 1000;
"""

# Execute query
df = duckdb.query(query).to_df()

# 🧪 Step 3: Standardize features
features = ['sugars_100g', 'fat_100g', 'proteins_100g', 'calories']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# 📊 Step 4: Apply K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# 🎨 Step 5: Plot the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='sugars_100g', y='fat_100g', hue='cluster', palette='Set2')
plt.title("Snack Clustering by Sugar and Fat")
plt.xlabel("Sugars (g per 100g)")
plt.ylabel("Fat (g per 100g)")
plt.grid(True)
plt.legend(title="Cluster")
plt.tight_layout()
plt.show()