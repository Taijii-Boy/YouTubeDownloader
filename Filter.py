from abc import ABC, abstractmethod
from main import YouTubeStreams


class FilterStrategy(ABC):
    def __init__(self, streams: YouTubeStreams):
        self.__streams = streams

    @property
    def streams(self):
        return self.__streams

    @abstractmethod
    def get_streams(self):
        pass


class FilterByProgressive(FilterStrategy):
    def get_streams(self):
        return self.streams.filter(progressive=True)


class FilterByAdaptive(FilterStrategy):
    def get_streams(self):
        return self.streams.filter(adaptive=True)


class FilterByAudioOnly(FilterStrategy):
    def get_streams(self):
        return self.streams.filter(only_audio=True)


class FilterByMp4(FilterStrategy):
    def get_streams(self):
        return self.streams.filter(file_extension='mp4')


class FilterByResolution(FilterStrategy):
    def get_streams(self):
        return self.streams.filter(resolution: str)



