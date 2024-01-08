from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def download_youtube_video(youtube_url, save_path):
    yt = YouTube(youtube_url)
    video_stream = yt.streams.filter(file_extension='mp4').first()
    video_path = video_stream.download(output_path=save_path)
    return video_path

def crop_video(video_path, start_time, end_time, output_path):
    with VideoFileClip(video_path) as video:
        video = video.subclip(start_time, end_time)
        video.write_videofile(output_path, codec='libx264', audio_codec='aac')

youtube_url = input('Video url: ')
video_path = download_youtube_video(youtube_url, '.')
start_time = int(input("Start Time: "))
end_time = int(input("End Time: "))
output_path = 'endpoint.mp4'
crop_video(video_path, start_time, end_time, output_path)
os.remove(video_path)
