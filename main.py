from pytube import YouTube


class YouTubeObject:
    def __init__(self, url: str):
        self.__url = url
        self.__yt = YouTube(url)

    def get_info(self):
        print(f'Канал: {self.__yt.author}')
        print(f'Название: {self.__yt.title}')
        print(f'Длина: {self.convert_time(self.__yt.length)}')

    @classmethod
    def convert_time(cls, seconds: int):

        sec = seconds % (24 * 3600)
        hours = sec // 3600
        sec = sec % 3600
        minutes = sec // 60
        sec = sec % 60
        return f'{hours}:{minutes}:{sec}'


obj = YouTubeObject('https://www.youtube.com/watch?v=0jZNKV5ROBM')
obj.get_info()