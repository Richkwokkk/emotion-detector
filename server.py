"""
This module provides a Flask web application for emotion detection.

It includes routes for rendering the home page and handling emotion
detection requests.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Handle the emotion detection request.

    This function retrieves the text to analyze from the request,
    processes it using the emotion_detector function, and returns
    the analysis results.

    Returns:
        str: A message containing the analysis results or an error message.
    """
    data = request.json
    text_to_analyze = data.get("statement", "")

    response = emotion_detector(text_to_analyze)

    if response:
        if response['dominant_emotion'] is None:
            return "Invalid text! Please try again!"

        output_message = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']}, "
            f"and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
        return output_message

    return "Unable to process the statement."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
