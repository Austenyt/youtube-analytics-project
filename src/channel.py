import json
from pprint import pprint
from re import search
import os

from googleapiclient.discovery import build



class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YouTube_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        response = self.get_info()
        self.title: str = response['items'][0]['snippet']['title']
        self.description: str = response['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/channel/" + channel_id
        self.subscriber_count : int = response['items'][0]['statistics']['subscriberCount']
        self.video_count: int = response['items'][0]['statistics']['videoCount']
        self.view_count: int = response['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f"{self.title}({self.url})"

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    @property
    def channel_id(self):
        return self._channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.get_info()
        pprint(channel)

    def get_info(self) -> None:
        youtube = self.get_service()
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube

    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def to_json(self, path):
        path_to_file = os.path.join("..", "homework-2", path)
        attributes = self.__dict__
        with open(path_to_file, 'w', encoding='utf-8') as file:
            json.dump(attributes, file, indent=4, separators=(',', ': '), ensure_ascii=False)
