from src.channel import Channel
from datetime import timedelta
import isodate

class PlayList(Channel):
    def __init__(self, playlist_id: str):
        self._playlist_id = playlist_id
        self.youtube = self.get_service()
        self.playlist_response = self.youtube.playlists().list(part='snippet,contentDetails',id=playlist_id).execute()
        self.title: str = self.playlist_response['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + playlist_id

    @property
    def total_duration(self):
        duration_list = []
        playlist_videos = self.youtube.playlistItems().list(playlistId=self._playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                         id=','.join(video_ids)
                                                         ).execute()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            duration_list.append(duration)
        sum_duration = timedelta()

        for duration in duration_list:
            sum_duration += duration
        return sum_duration


    def show_best_video(self):
        best_likes = 0
        playlist_response = self.youtube.playlists().list(part='snippet,contentDetails',id=self._playlist_id).execute()
        for video in playlist_response['items']:
            if int(video['statistics']['likeCount']) > int(best_likes):
                best_likes = video['statistics']['likeCount']
                video_id = video['id']
        return playlist_response
