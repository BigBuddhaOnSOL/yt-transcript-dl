from flask import Flask, request, render_template
from youtube_transcript_api import YouTubeTranscriptApi  # ✅ Diese Zeile ist entscheidend
from youtube_transcript_api.formatters import TextFormatter
import os