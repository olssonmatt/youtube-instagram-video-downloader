import typer
from pathlib import Path
from typing import List, Optional
from downloader import download_urls

app = typer.Typer(help="Download YouTube Shorts & Instagram Reels")

@app.command()
def download(
    urls: List[str] = typer.Argument(..., help="One or more video/playlist URLs"),
    out: Path = typer.Option(Path("downloads"), help="Output directory"),
    audio_only: bool = typer.Option(False, "--audio-only", help="Download audio only"),
    cookies: Optional[Path] = typer.Option(None, help="Cookies file (for Instagram/private content)"),
):
    download_urls(
        urls=urls,
        out=out,
        audio_only=audio_only,
        cookies=cookies,
    )

@app.command()
def batch(
    file: Path = typer.Argument(..., help="Text file with URLs (one per line)"),
    out: Path = typer.Option(Path("downloads")),
    audio_only: bool = typer.Option(False),
    cookies: Optional[Path] = typer.Option(None),
):
    urls = [line.strip() for line in file.read_text().splitlines() if line.strip()]
    download_urls(
        urls=urls,
        out=out,
        audio_only=audio_only,
        cookies=cookies,
    )

if __name__ == "__main__":
    app()
