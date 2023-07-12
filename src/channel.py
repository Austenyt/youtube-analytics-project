import json
from pprint import pprint
from re import search

from googleapiclient.discovery import build

from helper.youtube_api_manual import video_response


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key: str = 'AIzaSyD9xY2qA-bHKbLbxuRxlAePFglsHFrmkBY'
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.title: str = video_response['items'][0]['snippet']['title']
        self.description: str = video_response['items'][0]['snippet']['description']
        self.channel_url = "https: // www.youtube.com / watch?v = nApYYXYL9qA"
        self.subscriber_count : int = video_response['items'][0]['statistics']['subscriberCount']
        self.video_count: int = video_response['items'][0]['statistics']['videoCount']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        pprint(channel)

    def parse_channel_url(url):
        """
        This function takes channel `url` to check whether it includes a
        channel ID, user ID or channel name
        """
        path = p.urlparse(url).path
        id = path.split("/")[-1]
        if "/c/" in path:
            return "c", id
        elif "/channel/" in path:
            return "channel", id
        elif "/user/" in path:
            return "user", id
    def get_channel_id_by_url(youtube, url):
        method, id = youtube.parse_channel_url(url)
        if method == "channel":
            # if it's a channel ID, then just return it
            return id
        elif method == "user":
            # if it's a user ID, make a request to get the channel ID
            response = youtube.get_channel_details(youtube, forUsername=id)
            items = response.get("items")
            if items:
                channel_id = items[0].get("id")
                return channel_id
        elif method == "c":
            # if it's a channel name, search for the channel using the name
            # may be inaccurate
            response = search(youtube, q=id, maxResults=1)
            items = response.get("items")
            if items:
                channel_id = items[0]["snippet"]["channelId"]
                return channel_id
        raise Exception(f"Cannot find ID:{id} with {method} method")

    def get_channel_details(youtube, **kwargs):
        return youtube.channels().list(
            part="statistics,snippet,contentDetails",
            **kwargs
        ).execute()


    @classmethod
    def get_service(cls):
        pass

    def to_json(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


