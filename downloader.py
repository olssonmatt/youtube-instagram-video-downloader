from pathlib import Path
from typing import List, Optional
from yt_dlp import YoutubeDL
from rich.console import Console

console = Console()

def download_urls(
    urls: List[str],
    out: Path,
    audio_only: bool = False,
    cookies: Optional[Path] = None,
):
    out.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        "outtmpl": str(out / "%(uploader)s - %(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "format": (
            "bestaudio/best"
            if audio_only
            else "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4"
        ),
        "noplaylist": False,  # allow playlists
        "quiet": True,
        "no_warnings": True,
        "progress_hooks": [progress_hook],
    }

    if cookies:
        ydl_opts["cookiefile"] = str(cookies)

    console.print(f"[bold green]Starting download ({len(urls)} items)...[/bold green]")

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def progress_hook(d):
    if d["status"] == "finished":
        console.print(f"[green]✔ Downloaded:[/green] {d['filename']}")
