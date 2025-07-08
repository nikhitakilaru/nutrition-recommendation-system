def give_recommendations(nutri, activity):
    recs = []

    # Nutrition
    if nutri["Average Sugar"] > 25:
        recs.append("🍬 Reduce sugar: Choose unsweetened drinks, avoid packaged sweets, and check food labels.")

    if nutri["Average Calories"] > 2200:
        recs.append("🍽️ Lower calorie intake: Replace fried foods with grilled, reduce portion size, and eat slowly.")

    # Physical activity
    if activity["Sedentary Time"] > 500:
        recs.append("🚶‍♀️ Break sedentary time: Stand up every hour, take 5-minute walks, or stretch between tasks.")

    if activity["Avg Active Minutes"] < 30:
        recs.append("🏃 Add exercise: Try brisk walking for 15 mins twice a day or follow a short home workout.")

    # All good
    if not recs:
        recs.append("✅ Great job! You're on a healthy track. Maintain consistency and hydrate well.")

    return recs
