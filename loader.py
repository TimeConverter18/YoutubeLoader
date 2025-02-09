from yt_dlp import YoutubeDL

def download_video(url, path):
    try:
        ydl_opts = {
            'outtmpl': f'{path}\%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
        'ffmpeg_location': 'C:/Users/Kiril/Downloads/ffmpeg-7.1-essentials_build/ffmpeg-7.1-essentials_build/bin/ffmpeg.exe'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return 'Скачивание завершено!'
    except Exception as e:
        return f'Произошла ошибка: {e}'

def video_name(url):
    try:
        with YoutubeDL() as ydl:
            s = ydl.extract_info(url=url, download=False).get('title')
            return s
    except:
        return 'Не найдено'
if __name__ == "__main__":
    download_video('https://youtu.be/AH-qc_Ab8lA?si=Lg1AlvdvjYftQNsE')

#https://youtu.be/AH-qc_Ab8lA?si=Lg1AlvdvjYftQNsE