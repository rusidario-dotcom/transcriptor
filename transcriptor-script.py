from youtube_transcript_api import YouTubeTranscriptApi

video_id = "3UPSUAH_0kM"  # sostituisci con l'ID del video (la parte dopo "v=" nell'URL)
transcript = YouTubeTranscriptApi().fetch(video_id)
print(" ".join(snippet.text for snippet in transcript))