import yt_dlp
import os

def pobierz_mp3():
    # Pobiera ścieżkę do folderu, w którym znajduje się converter.py
    folder_skryptu = os.path.dirname(os.path.abspath(__file__))
    
    # Tworzymy ścieżkę do podfolderu 'config', gdzie trzymane jest ffmpeg.exe i ffprobe.exe
    sciezka_config = os.path.join(folder_skryptu, 'config')
    
    print(f"Lokalizacja skryptu: {folder_skryptu}")
    print(f"Szukam FFmpeg w: {sciezka_config}")

    url = input("\nWklej link do YouTube: ").strip()

    ydl_opts = {
        'format': 'bestaudio/best',
        # Wskazujemy folder config jako miejsce dla plików binarnych
        'ffmpeg_location': sciezka_config,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Zapisujemy mp3 w głównym folderze 'code' (tam gdzie skrypt)
        'outtmpl': os.path.join(folder_skryptu, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n Sukces!")
    except Exception as e:
        print(f"\n Wystąpił błąd: {e}")

if __name__ == "__main__":
    print("--- Program w fazie testowej ---")
    pobierz_mp3()