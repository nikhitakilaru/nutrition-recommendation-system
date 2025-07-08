import pandas as pd
from modules.nutrition import analyze_nutrition
from modules.activity import analyze_activity
from modules.recommend import give_recommendations

def evaluate(file_path, expected_keywords):
    print(f"\n🔍 Evaluating: {file_path}")
    data = pd.read_csv(file_path)

    # Run engine
    nutri = analyze_nutrition(data)
    activity = analyze_activity(data)
    actual_recs = give_recommendations(nutri, activity)

    # Match expected keywords (not full sentence match, just keyword-based)
    matched = 0
    for keyword in expected_keywords:
        for rec in actual_recs:
            if keyword.lower() in rec.lower():
                matched += 1
                break  # count keyword only once

    total = len(expected_keywords)
    accuracy = (matched / total) * 100

    print("\n✅ Expected Behaviors:")
    for kw in expected_keywords:
        print("  ✓", kw)

    print("\n📤 Actual Recommendations:")
    for rec in actual_recs:
        print("  ➤", rec)

    print(f"\n🎯 Accuracy: {matched}/{total} matched → {accuracy:.2f}%")

# Evaluate healthy user (should get "healthy track" only)
evaluate('data/sample_user(healthy).csv', [
    "healthy track"
])

# Evaluate unhealthy user (should get multiple improvement tips)
evaluate('data/sample_user(unhealthy).csv', [
    "reduce sugar",
    "short walk",
    "exercise",
    "caloric intake"
])
