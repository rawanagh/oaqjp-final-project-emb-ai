"""Flask application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the submitted text and return emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"{result['dominant_emotion']}. "
        f"Anger: {result['anger']}, "
        f"Disgust: {result['disgust']}, "
        f"Fear: {result['fear']}, "
        f"Joy: {result['joy']}, "
        f"Sadness: {result['sadness']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
