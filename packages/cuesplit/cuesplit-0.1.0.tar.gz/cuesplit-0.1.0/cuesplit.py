#!/usr/bin/env python3

import os
import subprocess
from concurrent.futures import Future, ThreadPoolExecutor
from os import path
from typing import Literal

import pylibcue

__all__ = ["split_cue", "msf2seconds"]


def msf2seconds(msf: tuple[int, int, int], ndigits: int = 2) -> float:
    return round(msf[0] * 60 + msf[1] + msf[2] / 75, ndigits)


def _ffmpeg_run(cmd: list[str]) -> int:
    cmd_base = ["ffmpeg", "-hide_banner", "-loglevel", "error"]
    res = subprocess.run(cmd_base + cmd)
    return res.returncode


def _add_metadata(cmd: list[str], k: str, v: str | int | None) -> None:
    if v is not None:
        cmd.extend(("-metadata", f"{k}={v}"))


def split_cue(
    cue_file: str,
    wav_file: str | None = None,
    output_dir: str = ".",
    encode_format: Literal["wav", "mp3", "flac"] = "flac",
    overwrite: bool = False,
    no_metadata: bool = False,
    jobs: int = os.cpu_count() or 1,
) -> bool:
    cmd = ["-y" if overwrite else "-n"]

    match encode_format:
        case "wav": cmd.extend(("-c", "copy", "-f", "wav"))
        case "mp3": cmd.extend(("-c:a", "libmp3lame", "-b:a", "320k", "-id3v2_version", "3"))
        case "flac": cmd.extend(("-c:a", "flac", "-compression_level", "8"))

    cd = pylibcue.Cd.from_file(cue_file)

    if encode_format != "wav" and not no_metadata:
        _add_metadata(cmd, "album_artist", cd.cdtext.performer)
        _add_metadata(cmd, "album", cd.cdtext.title)
        _add_metadata(cmd, "date", cd.rem.date)

    jobs_pool = ThreadPoolExecutor(max_workers=1 if encode_format == "wav" else jobs)
    futures: list[Future[int]] = []

    for i in range(len(cd)):
        tr = cd[i]
        if tr.start is None:
            raise ValueError(
                f"Cannot find start time for Track {tr.index:02d} in cue file"
            )
        if wav_file is not None:
            input_file = wav_file
        elif tr.filename is not None:
            input_file = path.join(path.dirname(cue_file), tr.filename)
        else:
            raise FileNotFoundError(f"Cannot find audio file for Track {tr.index:02d}")
        if not path.exists(input_file):
            raise FileNotFoundError(
                f"Input audio file {input_file} for Track {tr.index:02d} does not exist"
            )

        tr_cmd = ["-i", input_file]
        tr_cmd.extend(cmd)

        tr_cmd.extend(("-ss", f"{msf2seconds(tr.start):.2f}"))
        if tr.length:
            tr_cmd.extend(("-t", f"{msf2seconds(tr.length):.2f}"))

        if encode_format != "wav" and not no_metadata:
            _add_metadata(tr_cmd, "title", tr.cdtext.title)
            _add_metadata(tr_cmd, "artist", tr.cdtext.performer or cd.cdtext.performer)
            _add_metadata(tr_cmd, "composer", tr.cdtext.composer or cd.cdtext.composer)
            _add_metadata(tr_cmd, "track", tr.index)
            _add_metadata(tr_cmd, "genre", tr.cdtext.genre or cd.cdtext.genre)

        if no_metadata is True:
            tr_cmd.append(path.join(
                output_dir, f"{path.splitext(path.basename(input_file))[0]}_{tr.index:02d}.{encode_format}"
            ))
        else:
            tr_cmd.append(path.join(
                output_dir, f"{tr.index:02d} - {tr.cdtext.title or "Unknown"}.{encode_format}"
            ))
        futures.append(jobs_pool.submit(_ffmpeg_run, tr_cmd))
    jobs_pool.shutdown(wait=True)
    return all(f.result() == 0 for f in futures)


def cuesplit_cli() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="CD audio splitter based on CUE sheet.")
    parser.add_argument("--cue", "-i", help="Path to the CUE sheet file.", required=True)
    parser.add_argument(
        "--wav",
        help="Path to the WAV file if not specified in the CUE sheet.",
        default=None,
    )
    parser.add_argument(
        "--output_dir", "-o", help="Directory to save the splited audio files.", default="."
    )
    parser.add_argument(
        "-f",
        "--encode_format",
        choices=["wav", "mp3", "flac"],
        default="flac",
        help="Output audio files format.",
    )
    parser.add_argument(
        "--overwrite", action="store_true", help="Overwrite existing files."
    )
    parser.add_argument(
        "--no-metadata", action="store_true", help="Do not write metadata tags to audio files."
    )
    parser.add_argument(
        "--jobs",
        "-j",
        type=int,
        default=os.cpu_count() or 1,
        help="Number of parallel encode jobs.",
    )
    args = parser.parse_args()
    return int(
        not split_cue(
            args.cue,
            args.wav,
            args.output_dir,
            args.encode_format,
            args.overwrite,
            args.no_metadata,
            args.jobs,
        )
    )


if __name__ == "__main__":
    import sys
    sys.exit(cuesplit_cli())
