# Image Reorder

[![pypi](https://img.shields.io/pypi/v/image-reorder.svg)](https://pypi.org/project/image-reorder/)
[![license](https://img.shields.io/github/license/pronovic/image-reorder)](https://github.com/pronovic/image-reorder/blob/main/LICENSE)
[![wheel](https://img.shields.io/pypi/wheel/image-reorder.svg)](https://pypi.org/project/image-reorder/)
[![python](https://img.shields.io/pypi/pyversions/image-reorder.svg)](https://pypi.org/project/image-reorder/)
[![Test Suite](https://github.com/pronovic/image-reorder/workflows/Test%20Suite/badge.svg)](https://github.com/image-reorder/actions?query=workflow%3A%22Test+Suite%22)
[![coverage](https://coveralls.io/repos/github/image-reorder/badge.svg?branch=main)](https://coveralls.io/github/pronovic/image-reorder?branch=main)

Reorder images from multiple cameras into a single folder.

> _Note:_ Developer documentation is found in [DEVELOPER.md](DEVELOPER.md).  See that file for notes about how the code is structured, how to set up a development environment, etc.

To use, create a source directory (say, `pictures`) with a subdirectory for
each camera (`pictures/mom`, `pictures/dad`, etc.).  Run the `analyze` command
to get some basic info about what images exist in the source directory:

```
$ reorder analyze --help
Usage: reorder analyze [OPTIONS] <source-dir>

  Analyze images in a source directory.

  Finds all images in a source directory and generates some information about
  those images, including camera models.

Options:
  -h, --help  Show this message and exit.
```

Then, run the `copy` command to copy files from the source directory to some
target directory:

```
$ reorder copy --help
Usage: reorder copy [OPTIONS] <source-dir> <target-dir>

  Reorder images from a source directory into a target directory.

  Finds all images in a source directory and reorders them into a target
  directory by EXIF creation date, taking into account any offsets.  The
  target folder will be created if it does not already exist.

  The copied filenames will get a prefix like "image001__".  This way, you can
  sort the images by filename, and they'll have the correct order.  The file
  names start with index 1 by default, but you can use --start-index to change
  this.

  If the clocks on the cameras are not in sync, you may optionally provide a
  time offset by camera model.  The configured hours and minutes will be added
  to or removed from the the actual EXIF time.  Use a format like "PowerShot
  A70=+06:55" or "Pixel 2=-00:03".  The `reorder analyze` command will show
  you all of the different camera models among your images.  You can provide
  the --offset switch multiple times.

Options:
  -o, --offset <offset>      Time offset like 'PowerShot A70=+06:55'
  -s, --start-index <index>  Start index to use'  [x>=0]
  -h, --help                 Show this message and exit.
```

