from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

# Simulated tweets (replace with scraped tweets in real project)
tweets = [
    "I love the new AI features in my phone!",
    "This is the worst update ever.",
    "I'm not sure how I feel about this weather.",
    "Absolutely thrilled to start my internship!",
    "Feeling a bit down today.",
    "Just an average day, nothing special.",
    "Wow, this new movie is amazing!",
    "I hate waiting in long queues.",
    "Nothing seems to be working today.",
    "Enjoyed a peaceful walk in the park."
]

# Analyze sentiment
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0.1:
        return 'Positive'
    elif analysis.sentiment.polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

# Create DataFrame
df = pd.DataFrame(tweets, columns=['Tweet'])
df['Sentiment'] = df['Tweet'].apply(analyze_sentiment)

# Count sentiment categories
sentiment_counts = df['Sentiment'].value_counts()

# Plotting
plt.figure(figsize=(6,6))
colors = ['green', 'red', 'gray']
sentiment_counts.plot.pie(autopct='%1.1f%%', colors=colors, startangle=90, shadow=True)
plt.title("Mood Analysis of Tweets")
plt.ylabel('')
plt.tight_layout()
plt.show()
