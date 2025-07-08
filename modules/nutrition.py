def analyze_nutrition(data):
    avg_calories = data['Calories (kcal)'].mean()
    avg_sugar = data['Sugars (g)'].mean()
    return {
        "Average Calories": round(avg_calories, 2),
        "Average Sugar": round(avg_sugar, 2)
    }
