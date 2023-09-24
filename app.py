from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

# Function to process and generate a summary
def generate_summary(text):
    # Tokenization
    sentences = sent_tokenize(text)

    # Preprocess the text: remove stopwords, punctuation, and tokenize words
    stop_words = set(stopwords.words("english"))
    preprocessed_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        filtered_words = [
            word for word in words if word.lower() not in stop_words]
        preprocessed_sentences.append(filtered_words)

    # Calculate word frequency
    flat_preprocessed_words = [
        word for sentence in preprocessed_sentences for word in sentence]
    word_freq = FreqDist(flat_preprocessed_words)

    # Score sentences based on word frequency
    sentence_scores = {}
    for i, sentence in enumerate(preprocessed_sentences):
        for word in sentence:
            if word in word_freq:
                if i in sentence_scores:
                    sentence_scores[i] += word_freq[word]
                else:
                    sentence_scores[i] = word_freq[word]

    # Generate a summary by selecting top sentences
    summary_sentences = []
    if sentence_scores:
        sorted_scores = sorted(sentence_scores.items(),
                               key=lambda x: x[1], reverse=True)
        # Select the top 3 sentences as the summary
        top_sentences = sorted_scores[:3]
        for index, _ in top_sentences:
            summary_sentences.append(sentences[index])

    # Join the summary sentences to create the final summary
    summary = ' '.join(summary_sentences)
    return summary

def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity
    if sentiment_score > 0.1:
        sentiment = "Positive"
    elif sentiment_score < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, sentiment_score


@app.route('/')
def home():
    return render_template('index.html', summary=None, dark_mode=False)

@app.route('/about')
def about():
    return render_template('about.html', dark_mode=False)

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['input_text']
    summary = generate_summary(text)
    
    # Analyze sentiment for the original text
    original_sentiment, original_sentiment_score = analyze_sentiment(text)
    
    # Format the sentiment score with two decimal places
    original_sentiment_score = round(original_sentiment_score, 2)
    
    # Analyze sentiment for the summary text
    summary_sentiment, summary_sentiment_score = analyze_sentiment(summary)
    
    # Format the sentiment score for the summary with two decimal places
    summary_sentiment_score = round(summary_sentiment_score, 2)
    
    return render_template('index.html', summary=summary, original_text=text, 
                           original_sentiment=original_sentiment, original_sentiment_score=original_sentiment_score,
                           summary_sentiment=summary_sentiment, summary_sentiment_score=summary_sentiment_score, dark_mode=False)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
