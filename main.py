from YouTubeVideo import YouTubeVideo
from pytube import YouTube
from enum import Enum




class ProgressiveStream:
    def __init__(self, video: YouTubeVideo):
        self.__video = video

    def get_video(self, res):
        return self.__video.streams.get_by_resolution(res)


if __name__ == '__main__':
    obj = YouTubeVideo('https://www.youtube.com/watch?v=V0cJRCehXKo')
    stream = ProgressiveStream(obj)
    video = stream.get_video('720p')
    video.download()
    # print(Resolution.high)

