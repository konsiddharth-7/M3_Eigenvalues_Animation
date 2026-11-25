"""Build script and Manim entry point for Eigenvalues & Eigenvectors (1080p, 16:9, silent).

Usage:
    .venv/bin/python main.py              # Render all 6 scenes at 1920x1080 and stitch output MP4
    .venv/bin/python main.py --preview    # Fast 854x480 15fps preview render
    .venv/bin/python main.py --scene 3    # Render only Scene 3 at 1920x1080
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from manim import Scene, config, tempconfig

from scenes.scene_1_hook import Scene1Hook
from scenes.scene_2_transformations import Scene2Transformations
from scenes.scene_3_eigen_concept import Scene3EigenConcept
from scenes.scene_4_derivation import Scene4Derivation
from scenes.scene_5_eigenvectors import Scene5Eigenvectors
from scenes.scene_6_conclusion import Scene6Conclusion

PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_ROOT / "output"
SCENE_CACHE_DIR = PROJECT_ROOT / "media" / "rendered_scenes"

SCENES: list[tuple[int, type[Scene], str]] = [
    (1, Scene1Hook, "scene_1_hook"),
    (2, Scene2Transformations, "scene_2_transformations"),
    (3, Scene3EigenConcept, "scene_3_eigen_concept"),
    (4, Scene4Derivation, "scene_4_derivation"),
    (5, Scene5Eigenvectors, "scene_5_eigenvectors"),
    (6, Scene6Conclusion, "scene_6_conclusion"),
]


class FullEigenvaluesVideo(Scene):
    """Combined 6-scene Manim class for single-command Manim rendering."""

    def construct(self) -> None:
        for _, scene_cls, _ in SCENES:
            scene_cls.construct(self)


def get_media_duration(video_path: Path) -> float:
    """Return video duration in seconds using ffprobe."""
    out = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(video_path),
        ],
        text=True,
    ).strip()
    return float(out)


def render_single_scene(
    scene_cls: type[Scene],
    name: str,
    width: int,
    height: int,
    fps: int,
) -> Path:
    """Render one Manim scene to a silent MP4 file and return its path."""
    SCENE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    target_mp4 = SCENE_CACHE_DIR / f"{name}.mp4"

    with tempconfig(
        {
            "pixel_width": width,
            "pixel_height": height,
            "frame_rate": fps,
            "output_file": name,
            "media_dir": str(PROJECT_ROOT / "media"),
            "disable_caching": False,
            "flush_cache": False,
            "write_to_movie": True,
            "save_last_frame": False,
        }
    ):
        scene = scene_cls()
        scene.render()
        written_path = Path(scene.renderer.file_writer.movie_file_path)

    if written_path.resolve() != target_mp4.resolve():
        shutil.copy2(written_path, target_mp4)
    return target_mp4


def stitch_scenes(scene_mp4s: list[Path], final_output: Path) -> None:
    """Concatenate rendered scene MP4s cleanly into one silent 1080p MP4."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    concat_file = SCENE_CACHE_DIR / "concat_list.txt"
    lines = [f"file '{p.resolve()}'\n" for p in scene_mp4s]
    concat_file.write_text("".join(lines), encoding="utf-8")

    # Strip any audio streams (-an) and copy H.264 video stream losslessly with faststart
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_file),
            "-c:v",
            "copy",
            "-an",
            "-movflags",
            "+faststart",
            str(final_output),
        ],
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Render M3 Eigenvalues & Eigenvectors animation.")
    parser.add_argument("--scene", type=int, choices=[1, 2, 3, 4, 5, 6], help="Render only a single scene (1-6).")
    parser.add_argument("--preview", action="store_true", help="Render fast 854x480 15fps preview.")
    parser.add_argument("--fps", type=int, default=30, help="Frame rate for Full HD render (default: 30).")
    args = parser.parse_args()

    width, height, fps = (854, 480, 15) if args.preview else (1920, 1080, args.fps)

    selected = [item for item in SCENES if args.scene is None or item[0] == args.scene]
    rendered_paths: list[Path] = []
    total_dur = 0.0

    for idx, scene_cls, name in selected:
        print(f"\n=== Rendering Scene {idx}: {name} ({width}x{height} @ {fps}fps) ===", flush=True)
        mp4 = render_single_scene(scene_cls, name, width, height, fps)
        dur = get_media_duration(mp4)
        total_dur += dur
        print(f"--- Scene {idx} rendered: {mp4} ({dur:.2f}s) ---", flush=True)
        rendered_paths.append(mp4)

    if args.scene is None:
        out_name = "eigenvalues_eigenvectors_preview.mp4" if args.preview else "eigenvalues_eigenvectors.mp4"
        final_mp4 = OUTPUT_DIR / out_name
        print(f"\n=== Stitching {len(rendered_paths)} scenes into {final_mp4} ===", flush=True)
        stitch_scenes(rendered_paths, final_mp4)
        final_dur = get_media_duration(final_mp4)
        print(f"SUCCESS: {final_mp4} | Total Duration: {final_dur:.2f}s (sum={total_dur:.2f}s)", flush=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())
