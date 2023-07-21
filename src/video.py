from src.channel import Channel

class Video(Channel):
    def __init__(self, channel_id: str, video_id: str) -> None:
        super().__init__(channel_id)
        self._video_id = video_id
        video_response = self.get_video_info()
        self.video_title: str = video_response['items'][0]['snippet']['video_title']
        self.url = "https://www.youtube.com/channel/channel_id/" + video_id
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']

    @property
    def video_id(self):
        return self._video_id

    def get_video_info(self) -> None:
        youtube = self.get_service()
        video = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        return video
class PLVideo(Channel):
    def __init__(self, video_id: str, playlist_id: str) -> None:
        self._video_id = video_id
        self.playlist_id = playlist_id
        response = self.get_info()
        self.video_title: str = response['items'][0]['snippet']['video_title']
        self.url = "https://www.youtube.com/channel/channel_id/" + video_id
        self.view_count: int = response['items'][0]['statistics']['viewCount']
        self.like_count: int = response['items'][0]['statistics']['likeCount']
        self.like_count: int = response['items'][0]['statistics']['likeCount']