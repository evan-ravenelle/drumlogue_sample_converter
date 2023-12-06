# Korg Drumlogue File Renaming Script

The purpose of this script is to automate the process of renaming and numbering samples for the Korg Drumlogue. This script is written in Python and requires some dependencies to run.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install and how to install them:
- Python3: [Download Here](https://www.python.org/downloads/)
- FFmpeg: [Download Here](https://ffmpeg.org/download.html)

Python libraries:
- pydub
- os
- re
- argparse

You can install all Python dependencies from `requirements.txt` by running:

```shell
pip install -r requirements.txt
```

### Installing

Clone this repository or download the files. Run the Python script in your desired IDE or from the command-line interface.

### How to Use

The script is used to automate the renaming and numbering of audio samples. Please ensure the samples are placed in the right directory before processing.

```shell
python <nameofthescript.py>   \
  --sample_rate=<desired_sample_rate> \
  --channels=<desired_channels> \
  --include_dir=<True_or_False> \
  --bit_depth=<desired_bit_depth>
```
The above command is Linux/UNIX based. If you’re using a different OS, the process for adding a directory to your PATH may vary.
The script modifies the file names and gives an ordered numbering to all of them, increasing by one for each new file. The bit depth can also be chosen, with the default being 16, but 32 can be chosen for higher quality. Please note that choosing 32 would result in doubling the storage requirements.
### Notice

This script works with various audio file extensions such as 'wav', 'mp3', 'flac', 'ogg', 'm4a'. It aims to convert these files into '.wav' extension with specified sample rate and channels.

Please note that the original files will be deleted after processing. Make sure to keep a backup before running the script.

### Environment Setup

Add FFmpeg to your environment variable PATH for the script to use it.

## MIT License

Please refer to the LICENSE file for details.