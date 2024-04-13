import pytube

video_url = "https://www.youtube.com/watch?v=oesHE7elng8"
youtube = pytube.YouTube(video_url)
stream = youtube.streams.get_highest_resolution()
save_path = "youtube_videos"
stream.download(save_path)
print(f"Downloaded video: {youtube.title}")