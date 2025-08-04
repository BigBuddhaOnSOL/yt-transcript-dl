from flask import Flask, request, render_template
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import os
print("Module path:", youtube_transcript_api.__file__)
print("Methods available:", dir(YouTubeTranscriptApi))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    transcript_text = ""
    error = None
    if request.method == 'POST':
        youtube_url = request.form.get('youtube_url', '')
        try:
            if "v=" in youtube_url:
                video_id = youtube_url.split("v=")[-1].split("&")[0]
            elif "youtu.be/" in youtube_url:
                video_id = youtube_url.split("youtu.be/")[-1].split("?")[0]
            else:
                raise ValueError("Invalid YouTube URL format")

            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            formatter = TextFormatter()
            transcript_text = formatter.format_transcript(transcript)

        except Exception as e:
            error = f"Error: {e}"

    return render_template('index.html', transcript=transcript_text, error=error)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
