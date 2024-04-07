import pandas as pd
from collections import Counter

# Load the cleaned data
df = pd.read_csv('cleaned_responses.csv')
all_responses = ' '.join(df['response_column_name']).split()  # Replace 'response_column_name'

# Frequency analysis
word_counts = Counter(all_responses)
most_common_words = word_counts.most_common(10)

# Convert to DataFrame for visualization
df_common_words = pd.DataFrame(most_common_words, columns=['Word', 'Frequency'])
df_common_words.to_csv('word_frequencies.csv', index=False)
