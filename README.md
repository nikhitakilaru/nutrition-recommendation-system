 AI-Powered Nutrition & Exercise Recommendation System

This project analyzes a user's dietary habits and physical activity data to generate personalized, actionable recommendations for better health and disease prevention.

Problem Statement- Nutrition and Exercise Recommendation Engine

Created a system that:
- Analyzes user lifestyle data (food & activity)
- Identifies unhealthy patterns
- Suggests improvements using nutrition science
- Classifies users with clustering (AI/ML)
- Tracks accuracy on known test data

 Features

-Rule-based recommendation engine  
- Modular structure with nutrition & activity analyzers  
-KMeans clustering for lifestyle classification  
- Smart goal-based suggestions  
- Pop-up summary with HEALTHY/UNHEALTHY verdict  
- Functional accuracy testing on sample users  
- Works with `.csv` files — easy to extend!

Accuracy Evaluation

This project uses a rule-based recommendation engine, not a machine learning classifier.  
Therefore, "accuracy" here refers to how many expected health suggestions (tips) are correctly triggered by the system.

 How It Works

- The file `evaluate_accuracy.py` runs the recommendation system on test users:
  - `sample_user_1_healthy.csv`
  - `sample_user_2_unhealthy.csv`
- Each test case has a known set of expected recommendations
- The evaluator compares actual output vs expected tips and reports an accuracy percentage

 Accuracy is not shown for `food_activity.csv` (main input file), because:
- It represents real user input
- There is no predefined "correct answer" to compare against
- The goal is to generate personalized recommendations, not to predict a label

 Sample Accuracy Output


Evaluating: sample_user(unhealthy).csv
Accuracy: 4/4 matched → 100.00%




