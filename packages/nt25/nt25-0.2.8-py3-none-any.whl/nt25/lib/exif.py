import os
import json
import argparse

from pathlib import Path
from math import ceil
from random import randint

from PIL import Image, ImageOps

from ._exif_util import (
  IMAGE_EXT,
  OPTIMIZE_WIDTH,
  THUMBNAIL_WIDTH,
  _check,
  _run,
  getWH,
  parseExif,
  mergeExif,
  genComment,
)

VERSION = "0.1.0"


def _shrink(file, output, maxWidth=None, merge=True, magic=False):
  shrink = False

  if not os.path.exists(file):
    return shrink

  if magic:
    t, w, h = getWH(file)
    if t == "null" or w < 0 or h < 0:
      return shrink

    if not _check():
      return shrink

    path = str(Path(file).resolve())
    shell = ["ffmpeg", "-i", path]

    if maxWidth is not None:
      m = max(w, h)
      if m > maxWidth:
        scale = maxWidth / m
        h = int(ceil(scale * h))
        shell += ["-vf", f"scale={h}:-1"]

    suffix = str(randint(1000, 9999)) + t
    ofile = file + suffix

    shell += ["-y", path + suffix]
    sr = _run(shell)

    if sr.returncode != 0:
      print(sr.stderr)

  else:
    img = Image.open(file)
    img = ImageOps.exif_transpose(img)

    w, h = img.size

    if maxWidth is not None:
      m = max(w, h)
      if m > maxWidth:
        scale = maxWidth / m
        w = int(scale * w)
        h = int(scale * h)
        img = img.resize((w, h))

    _, ext = os.path.splitext(file)
    end = ext.lower()

    if img.mode == "RGB":
      end = ".jpg"

    suffix = str(randint(1000, 9999)) + end
    ofile = file + suffix
    img.save(ofile, optimize=True)
    img.close()

  if not os.path.exists(ofile):
    return shrink

  if merge:
    mergeExif(file, ofile)
  else:
    genComment(ofile)

  times = float(os.path.getsize(ofile)) / os.path.getsize(file)
  shrink = times < 1

  if file == output and not shrink:
    os.remove(ofile)
  else:
    os.replace(ofile, output)

  print(f"{output} has shrink {times:.1%}")
  return shrink


def shrinkFile(
  file,
  optimizeWidth=OPTIMIZE_WIDTH,
  thumbnailWidth=THUMBNAIL_WIDTH,
  override=True,
  magic=False,
):
  name, ext = os.path.splitext(file)
  result = False

  if override:
    result = _shrink(file, file, magic=magic)
  else:
    result = _shrink(file, name + "-new" + ext, magic=magic)

  _shrink(file, name + "-o" + ext, maxWidth=optimizeWidth, merge=False, magic=magic)
  _shrink(
    file, name + "-thumbnail" + ext, maxWidth=thumbnailWidth, merge=False, magic=magic
  )

  return result


def main():
  parser = argparse.ArgumentParser(description="EXIF tool")
  parser.add_argument("-f", "--file", type=str, help="parse image Exif info")
  parser.add_argument("-v", "--version", action="store_true", help="echo version")
  parser.add_argument(
    "-m",
    "--magic",
    action="store_true",
    help="shrink with magic",
    default=False,
  )
  parser.add_argument(
    "-o",
    "--override",
    action="store_true",
    help="override original file",
    default=False,
  )
  parser.add_argument(
    "-s",
    "--shrink",
    type=str,
    help="shrink file or folder with optimize and thumbnail generated",
  )

  args = parser.parse_args()

  if args.file:
    result = parseExif(args.file)

  elif args.shrink:
    if os.path.isdir(args.shrink):
      total = 0
      shrink = 0
      for d, _, f in os.walk(args.shrink):
        for file in f:
          _, e = os.path.splitext(file)
          if e.lower() in IMAGE_EXT:
            path = os.path.join(d, file)
            total += 1

            if shrinkFile(path, override=args.override, magic=args.magic):
              shrink += 1

      result = {
        "total": total,
        "shrink": shrink,
        "override": args.override,
        "magic": args.magic,
      }

    elif os.path.isfile(args.shrink):
      result = {
        "result": shrinkFile(args.shrink, override=args.override, magic=args.magic),
        "override": args.override,
        "magic": args.magic,
      }

  elif args.version:
    result = {"version": VERSION, "magic": _check()}
  else:
    print("usage: ex [-h] [-v] [-f FILE] [[-o] [-m] -s FILE]")
    return

  print(json.dumps(result, indent=2))


if __name__ == "__main__":
  main()
