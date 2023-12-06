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
python main.py \
  --sample_rate=<desired_sample_rate> \ 
  --channels=<desired_channels> \
  --include_dir \
  --bit_depth=32 \
  path/to/sample/dir 
```
The above command is Linux/UNIX based. If you’re using a different OS, the process for adding a directory to your PATH may vary.
The script modifies the file names and gives an ordered numbering to all of them, increasing by one for each new file. The bit depth can also be chosen, with the default being 16, but 32 can be chosen for higher quality. Please note that choosing 32 would result in doubling the storage requirements.

All flags are optional. The path to the sample dir is required. 

To view help, run `python main.py -h|--help`:
```shell
usage: main.py [-h] [--sample_rate SAMPLE_RATE] [--channels CHANNELS] [--include_dir] [--bit_depth BIT_DEPTH]
               directory

Convert and rename audio files in the given directory.

positional arguments:
  directory             The directory containing the audio files to convert and rename.

options:
  -h, --help            show this help message and exit
  --sample_rate SAMPLE_RATE
                        The desired sample rate for the converted files. Default is 48000.
  --channels CHANNELS   The desired number of channels for the converted files. Default is 2 (stereo).
  --include_dir         Include directory path in filename. Default is False.
  --bit_depth BIT_DEPTH
                        The desired bit depth for the converted files. Default is 16. Use 32 for higher quality (uses
                        2x as much storage).
```

### Notice

This script works with various audio file extensions such as 'wav', 'mp3', 'flac', 'ogg', 'm4a'. It aims to convert these files into '.wav' extension with specified sample rate and channels.

Please note that the original files will be deleted after processing. Make sure to keep a backup before running the script.

### Environment Setup

Add FFmpeg to your environment variable PATH for the script to use it.

## Troubleshooting

#### Error: RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work

This warning occurs when the system cannot find the FFmpeg software, which is required for handling multimedia data.

To address this issue:

1. Ensure that FFmpeg has been installed on your system. If not, download and install it from the official [FFmpeg site](https://www.ffmpeg.org/download.html).

2. Once installed, you need to add FFmpeg to your system's environment variables (PATH).

   **Windows user:**
   Open the start menu and search for 'Environment Variables', click on 'Edit the system environment variables'. In the window that pops up, click on 'Environment Variables'. In the 'System variables' section, scroll until you find the 'Path' variable, select it and click on 'Edit'. In the new window, click on 'New' and add the path to the FFmpeg bin folder (it should look something like this: `C:\ffmpeg\bin`).

   **Linux/Mac user:**
   Open a terminal and type the following command:
   ```
   export PATH=$PATH:/path/to/ffmpeg/bin
   ```
   Replace '/path/to/ffmpeg/bin' with the actual directory path where FFmpeg is installed.

3. If you've done these steps correctly, you should be able to open a new command prompt or terminal window and execute the command `ffmpeg` without any errors. If this is not the case, retry the steps and ensure that FFmpeg is installed and properly added to your system's PATH variable.

## MIT License

Please refer to the LICENSE file for details.