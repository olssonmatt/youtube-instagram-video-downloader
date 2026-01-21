# packages
pip install yt-dlp
pip install typer rich

# vidgrab/main.py
import typer
from yt_dlp import YoutubeDL
from pathlib import Path

app = typer.Typer()

@app.command()
def download(
    url: str,
    out: Path = Path("downloads"),
    audio_only: bool = False,
):
    out.mkdir(exist_ok=True)

    ydl_opts = {
        "outtmpl": str(out / "%(title)s.%(ext)s"),
        "format": "bestaudio/best" if audio_only else "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    app()

# python main.py download <url>
