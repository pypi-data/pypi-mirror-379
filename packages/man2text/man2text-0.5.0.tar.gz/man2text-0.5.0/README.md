# man2text

`man2text` is a Python library and CLI tool that converts all system **man pages** into clean, plain text files.  
This makes it easy to index, vectorize, or otherwise process Unix documentation.

> [!NOTE]  
> This is the very first version of `man2text`. Any contributions are appreciated!


## Features
- Converts all available English manpages (`/usr/share/man/man*`) into `.txt`.
- Uses the standard `man <cmd> | col -bx` pipeline for accurate rendering.
- Optional multiprocessing for faster conversion on large systems.
- Provides both a **CLI command** and a **Python API**.


## Installation

Clone and install locally in editable mode:

```bash
git clone https://github.com/yourusername/man2text.git
cd man2text
pip install -e .
````

Or using `pip`:

```bash
pip install man2text
```


## Usage

### CLI

Convert all manpages to text and save them in `./man-txt`:

```bash
man2text --output ./man-txt
```

Options:

* `--output DIR` → output directory (default: `./man-txt`)
* `--processes N` → number of processes to use (default: auto)

### Python API

```python
from man2text.core import convert_all

# Convert all manpages to ./txt-pages with 4 processes
convert_all(output_dir="./txt-pages", processes=4)
```


## Example Output

For example, the `ls` manpage will produce `ls.txt` containing the plain text version of the manual page.
