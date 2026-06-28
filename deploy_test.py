from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Emotion Detection</title>
</head>
<body>
    <h1>Emotion Detection Application</h1>
    <form action="/emotionDetector" method="post">
        <textarea name="text" rows="4" cols="50" placeholder="Enter text here..."></textarea>
        <br>
        <button type="submit">Analyze Emotion</button>
    </form>
</body>
</html>
'''

def emotion_detector(text_to_analyse):
    if not text_to_analyse:
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }
    return {
        'anger': 0.01, 'disgust': 0.01, 'fear': 0.02,
        'joy': 0.95, 'sadness': 0.01, 'dominant_emotion': 'joy'
    }

@app.route('/')
def index():
    return render_template_string(HTML_FORM)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    text = request.form.get('text')
    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return "Invalid input! Please enter valid text."
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
