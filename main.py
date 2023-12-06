from pydub import AudioSegment
import os
import re
import argparse


def convert_and_rename_files(directory, target_sample_rate=48000,
                             target_channels=2,
                             include_dir=False, bit_depth=16):
    AUDIO_EXTENSIONS = ['wav', 'mp3', 'flac', 'ogg', 'm4a']
    counter = 0
    base_dir = os.path.normpath(directory).split(os.sep)

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.split('.')[-1] in AUDIO_EXTENSIONS:
                old_path = os.path.join(root, filename)

                # Modify the file name
                counter += 1
                base_parts = os.path.abspath(directory).split(os.sep)
                root_absolute = os.path.abspath(
                    root)  # get the absolute path for the root directory

                file_parts = root_absolute.split(os.sep)[len(base_parts):] + [
                    filename.rsplit('.', 1)[0]]
                print(file_parts)
                new_file_name = f"{counter:#03}_{'_'.join([re.sub(' ', '_', part) for part in (file_parts if include_dir else file_parts[-1:])])}.wav"
                # Create the new path - place the file in the top level directory, regardless of the original subdirectory
                new_path = os.path.join(directory, new_file_name)
                codec = "pcm_s32le" if bit_depth == 32 else "pcm_s16le"
                # Use pydub to convert the audio file
                audio = AudioSegment.from_file(old_path)
                audio = audio.set_frame_rate(target_sample_rate)
                audio = audio.set_channels(target_channels)
                audio.export(new_path, codec=codec, parameters=["-ac", "2"], format="wav")

                # Remove the old file
                os.remove(old_path)
                print(f'Converted and renamed: {old_path} -> {new_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert and rename audio files in the given directory.')
    parser.add_argument('directory', type=str,
                        help='The directory containing the audio files to convert and rename.')
    parser.add_argument('--sample_rate', type=int, default=48000,
                        help='The desired sample rate for the converted files. Default is 48000.')
    parser.add_argument('--channels', type=int, default=2,
                        help='The desired number of channels for the converted files. Default is 2 (stereo).')
    parser.add_argument('--include_dir', action='store_true',
                        help='Include directory path in filename. Default is False.')
    parser.add_argument('--bit_depth', type=int, default=16,
                        help='The desired bit depth for the converted files. Default is 16. Use 32 for higher quality (uses 2x as much storage).')


    args = parser.parse_args()
    convert_and_rename_files(args.directory, args.sample_rate, args.channels,
                             args.include_dir, args.bit_depth)