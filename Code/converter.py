import yt_dlp
import os

def pobierz_mp3():
    # Pobiera ścieżkę do folderu, w którym DOKŁADNIE znajduje się ten plik .py
    folder_skryptu = os.path.dirname(os.path.abspath(__file__))
    
    print(f"Lokalizacja skryptu: {folder_skryptu}")
    print(f"Szukam plików: {os.path.join(folder_skryptu, 'ffmpeg.exe')}")

    url = input("\nWklej link do YouTube: ").strip()

    ydl_opts = {
        'format': 'bestaudio/best',
        # To wymusza użycie ffmpeg z folderu skryptu
        'ffmpeg_location': folder_skryptu,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(folder_skryptu, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n Sukces! Plik mp3 powinien być w folderze ze skryptem.")
    except Exception as e:
        print(f"\n Wystąpił błąd: {e}")

if __name__ == "__main__":
    pobierz_mp3()