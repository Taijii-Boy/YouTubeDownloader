from pytube import YouTube


class YouTubeVideo:
    def __init__(self, url: str):
        self.__url = url
        self.__yt = YouTube(url)

    def get_info(self):
        print(f'Канал: {self.__yt.author}')
        print(f'Название: {self.__yt.title}')
        print(f'Длительность: {self.__convert_duration(self.__yt.length)}')

    @property
    def streams(self):
        return self.__yt.streams

    @classmethod
    def __convert_duration(cls, seconds: int) -> str:
        sec = seconds % (24 * 3600)
        hours = sec // 3600
        sec = sec % 3600
        minutes = sec // 60
        sec = sec % 60
        return f'{hours:02}:{minutes:02}:{sec:02}'
