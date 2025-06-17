# 1. Import necessary modules
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# 2. Initialize the Flask app
app = Flask("Sentiment Analyzer")

# 3. Define route for the sentiment analyzer
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Get text input from the GET request (from JavaScript)
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Run sentiment analysis
    response = sentiment_analyzer(text_to_analyze)
    
    # Extract results
    label = response['label']
    score = response['score']

    # Return formatted result
    return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

# 4. Define route to render index.html
@app.route("/")
def render_index_page():
    return render_template('index.html')

# 5. Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
