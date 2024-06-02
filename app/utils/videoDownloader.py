'''
Download Playlist function needs to be added
'''

import yt_dlp as yt



#Function to get URL metadata
def get_url_metadata(url,quiet=True):
    ydl_opts={
        'quiet':quiet,
        'noplaylist':False
    }
    try:
        with yt.YoutubeDL(ydl_opts) as ydl:
            info_dict=ydl.extract_info(url,download=False)
        
        if 'entries' in info_dict:
            metadata={
                'name':info_dict.get('title'),
                'Uploader':info_dict.get('uploader','N/A'),
                'entries':info_dict.get('entries',[])
            }
            return 'playlist',metadata
        else:
            metadata = {
                'name': info_dict.get('title'),
                'size': info_dict.get('filesize_approx', 'N/A'),  # 'filesize_approx' is an estimated size
                'description': info_dict.get('description', 'N/A'),
                'title': info_dict.get('title', 'N/A'),
                'duration': info_dict.get('duration', 'N/A'),
                'uploader': info_dict.get('uploader', 'N/A'),
                'upload_date': info_dict.get('upload_date', 'N/A')
            }
            
            return 'video', metadata

    except Exception as e:
        if not quiet : print(f'Error {e}')
        return None,None



#Function to download video
def download_video(url,path,format,quiet=True):
    if format not in ['mp3','mp4']:
        raise ValueError("Format must br 'mp3 or 'mp4")
    
    ydl_opts = {
        'format': 'bestaudio/best' if format == 'mp3' else 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if format == 'mp3' else [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',

        }],
        'outtmpl': f"{path}/%(title)s",
    }
    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
