def analyze_activity(data):
    avg_active = data['ActivityMinutes'].mean()
    avg_sedentary = data['SedentaryMinutes'].mean()
    return {
        "Avg Active Minutes": round(avg_active, 2),
        "Sedentary Time": round(avg_sedentary, 2)
    }
