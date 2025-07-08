import pandas as pd
from sklearn.cluster import KMeans
from modules.nutrition import analyze_nutrition
from modules.activity import analyze_activity
from modules.recommend import give_recommendations



# Load the dataset
data = pd.read_csv('data/food_activity.csv')
# --- Clustering to classify lifestyle pattern ---
try:
    # Use only relevant columns for clustering
    cluster_data = data[["Calories (kcal)", "Sugars (g)", "ActivityMinutes", "SedentaryMinutes"]]
    kmeans = KMeans(n_clusters=2, random_state=42)
    clusters = kmeans.fit_predict(cluster_data)

    # Identify this user's cluster
    cluster_label = clusters[0]  # first row = current user pattern
    print(f"\n📊 Based on clustering, this user belongs to lifestyle cluster #{cluster_label}")
except Exception as e:
    print("⚠️ Clustering skipped due to error:", e)


# Run all modules
nutrition_summary = analyze_nutrition(data)
activity_summary = analyze_activity(data)
recommendations = give_recommendations(nutrition_summary, activity_summary)

# Display output
print("\nNutrition Summary:")
print(nutrition_summary)

print("\nActivity Summary:")
print(activity_summary)

print("\nRecommendations:")
for rec in recommendations:
    print("- " + rec)
    print("\n========== Lifestyle Summary Report ==========")
print("📊 Calories:", nutrition_summary["Average Calories"])
print("🍬 Sugar:", nutrition_summary["Average Sugar"])
print("🏃‍♂️ Active Minutes:", activity_summary["Avg Active Minutes"])
print("🪑 Sedentary Time:", activity_summary["Sedentary Time"])
print("\n📝 Recommendations:")
for r in recommendations:
    print(" -", r)
print("==============================================\n")
import tkinter as tk
from tkinter import font

# --------- HEALTH STATUS LOGIC ---------
is_healthy = len(recommendations) == 1 and "healthy track" in recommendations[0].lower()
health_status = "HEALTHY" if is_healthy else "UNHEALTHY"

# --------- CLUSTERING INFO ---------
try:
    cluster_data = data[["Calories (kcal)", "Sugars (g)", "ActivityMinutes", "SedentaryMinutes"]]
    kmeans = KMeans(n_clusters=2, random_state=42)
    clusters = kmeans.fit_predict(cluster_data)
    cluster_label = clusters[0]
    cluster_line = f"\n📊 Based on clustering, this user belongs to lifestyle cluster #{cluster_label}"
except:
    cluster_line = "\n📊 Clustering info unavailable."

# --------- FULL OUTPUT STRING ---------
full_output = f"""
🔷 LIFESTYLE STATUS: {health_status}

📊 Nutrition Summary:
 - Calories: {nutrition_summary['Average Calories']}
 - Sugar: {nutrition_summary['Average Sugar']}

🏃 Activity Summary:
 - Active Minutes: {activity_summary['Avg Active Minutes']}
 - Sedentary Time: {activity_summary['Sedentary Time']}

📝 Recommendations:
"""
for rec in recommendations:
    full_output += f" - {rec}\n"

full_output += cluster_line

# --------- TERMINAL OUTPUT ---------
print("\n========== LIFESTYLE SUMMARY ==========")
print(full_output)
print("=======================================\n")

# --------- POPUP TEXT WINDOW ---------
root = tk.Tk()
root.title("Lifestyle Report")
root.geometry("550x500")
root.resizable(False, False)

# Centered HEALTH STATUS in bold
status_font = font.Font(family='Arial', size=18, weight='bold')
status_label = tk.Label(root, text=health_status, fg="green" if is_healthy else "red", font=status_font)
status_label.pack(pady=(20, 10))

# Scrollable Text Box for Details
text_box = tk.Text(root, wrap='word', font=("Arial", 11), padx=10, pady=10)
text_box.insert('1.0', full_output)
text_box.config(state='disabled')
text_box.pack(expand=True, fill='both', padx=15, pady=10)

root.mainloop()


