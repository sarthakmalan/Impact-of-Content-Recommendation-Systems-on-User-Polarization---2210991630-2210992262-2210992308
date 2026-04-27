import pandas as pd
import matplotlib.pyplot as plt

print("Loading data...")
reddit = pd.read_csv("Reddit_Data.csv").head(1000)

print("Preparing data...")
reddit = reddit.dropna()
reddit['sentiment'] = reddit['category']
 
reddit['engagement'] = reddit.index

print("Running engagement-based model...")
engagement_df = reddit.sort_values(by='engagement', ascending=False).head(100)

engagement_variance = engagement_df['sentiment'].var()
engagement_avg = engagement_df['sentiment'].mean()

print("Running diversity-based model...")
 
neutral = reddit[reddit['sentiment'] == 0].sample(50, replace=True)
positive = reddit[reddit['sentiment'] == 1].sample(30, replace=True)
negative = reddit[reddit['sentiment'] == -1].sample(20, replace=True)

diversity_df = pd.concat([neutral, positive, negative])

diversity_variance = diversity_df['sentiment'].var()
diversity_avg = diversity_df['sentiment'].mean()

print("\n===== RESULTS =====")
 
print("Engagement-Based Variance:", round(engagement_variance, 3))
print("Engagement-Based Avg:", round(engagement_avg, 3))

print("Diversity-Based Variance:", round(diversity_variance, 3))
print("Diversity-Based Avg:", round(diversity_avg, 3))

print("\nGenerating graph...")

models = ['Engagement', 'Diversity']
variances = [engagement_variance, diversity_variance]

plt.figure()
plt.bar(models, variances)

plt.title("Sentiment Variance Comparison")
plt.xlabel("Model")
plt.ylabel("Variance")

plt.show()

print("Done!")