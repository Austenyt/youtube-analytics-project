from src.channel import Channel


class Video(Channel):
    def __init__(self, video_id: str):
        try:
            self._video_id = video_id
            self.youtube = self.get_service()
            self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                             id=self._video_id
                                                             ).execute()
            self.url = 'https://www.youtube.com/watch?v=' + video_id
            self.video_title: str = self.video_response['items'][0]['snippet']['title']
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
        except:
            self._video_id = video_id
            self.url = None
            self.title = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return f"{self.video_title}"


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        self._video_id = video_id
        self.playlist_id = playlist_id
        self.youtube = self.get_service()
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=self._video_id
                                                         ).execute()
        self.video_title: str = self.video_response['items'][0]['snippet']['title']
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
    def __str__(self):
        return f"{self.video_title}"
