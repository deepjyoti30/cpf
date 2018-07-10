# Copy Faster

### An utility to copy stuff faster.

## Prerequisites

 * Python 3.x

## Installation
```sh
git clone https://github.com/deepjyoti30/cpf
cd cpf
```

*You can add an alias to your bashrc or zshrc to use it like cp*

## Running
```sh

usage: cpf.py [-h] [-r] [-p] [-v] SRC DES

positional arguments:
  SRC            Source File Name.
  DES            Destinaion File Name.

optional arguments:
  -h, --help     show this help message and exit
  -r, --recursive  Copy the files recursively
  -p, --progress   Show a progress bar
  -v, --verbose  Explain what is being done

```

### How it Works

It uses multithreading in order to copy the files faster.
The file is broken into chunks and later combined into one big file.

### Being worked on

1. Progress Bar (Buggy).

### Things to Add

1. Try to make it more efficient.
2. Add Windows support (not tested yet, please notify me if it does).

### Issues

1. As of now space is an issue, since the filechunks are first copied, then combined and then deleted. That makes it use 2x the space.

2. Less RAM might also turn out to be an issue.
