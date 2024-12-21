import argparse
from pydub import AudioSegment
import os
import numpy as np

# Argument parser setup
parser = argparse.ArgumentParser(description='Speech enhancement, data creation, training, and prediction')
parser.add_argument('--mode', default='prediction', type=str, choices=['data_creation', 'training', 'prediction'], help='Mode to run the program')
parser.add_argument('--noise_dir', default=r'D:\BDA_Sem1\Mini_Project\Speech-Enhancement\Data\LibriSpeech\Trail.1.5\resampled\noise_files_16k', type=str, help='Directory for noise audio files')
parser.add_argument('--voice_dir', default=r'D:\BDA_Sem1\Mini_Project\Speech-Enhancement\Data\LibriSpeech\Trail.1-Train-100-10min', type=str, help='Directory for clean voice audio files')
parser.add_argument('--output_dir', default=r'D:\BDA_Sem1\Mini_Project\Speech-Enhancement\Output', type=str, help='Directory to save output audio files')
parser.add_argument('--sample_rate', default=16000, type=int, help='Sample rate for reading audio')
args = parser.parse_args()

# Function to concatenate multiple audio files into one
def concatenate_audio(files, target_length):
    total_duration = 0
    combined_audio = AudioSegment.empty()
    
    for file in files:
        audio = AudioSegment.from_file(file)
        combined_audio += audio
        total_duration += len(audio) / 1000  # Convert to seconds
        
        if total_duration >= target_length:
            break
    
    if total_duration > target_length:
        excess_duration = total_duration - target_length
        combined_audio = combined_audio[:-int(excess_duration * 1000)]  # Trim the excess
    
    return combined_audio

# Function to stretch or repeat noise to match the target length
def stretch_or_repeat_noise(noise, target_length):
    noise_duration = len(noise) / 1000  # Convert to seconds
    repeats = int(np.ceil(target_length / noise_duration))
    stretched_noise = noise * repeats
    
    return stretched_noise[:target_length * 1000]  # Trim to exact target length

# Main logic to create the noisy_voice_long file
def create_noisy_audio():
    # Load voice files from the specified directory
    voice_files = [os.path.join(args.voice_dir, f) for f in os.listdir(args.voice_dir) if f.endswith('.wav')]
    
    # Target length is 600 seconds (10 minutes)
    target_length = 600
    
    # Concatenate the voice files
    voice_long = concatenate_audio(voice_files, target_length)
    print(f"voice_long duration: {len(voice_long) / 1000} seconds")
    
    # Load noise files from the specified directory
    noise_files = [os.path.join(args.noise_dir, f) for f in os.listdir(args.noise_dir) if f.endswith('.wav')]
    
    # Concatenate the noise files (assuming they sum up to 1 minute total)
    noise_long = concatenate_audio(noise_files, 60)
    
    # Stretch or repeat the noise to match the 10-minute target length
    noise_long = stretch_or_repeat_noise(noise_long, target_length)
    print(f"noise_long duration: {len(noise_long) / 1000} seconds")
    
    # Blend the voice_long and noise_long files
    noisy_voice_long = voice_long.overlay(noise_long)
    print(f"noisy_voice_long duration: {len(noisy_voice_long) / 1000} seconds")
    
    # Save the resulting noisy voice long file
    output_file = os.path.join(args.output_dir, 'noisy_voice_long.wav')
    noisy_voice_long.export(output_file, format='wav')
    print(f"Noisy voice long file saved at: {output_file}")

# Run the process if the mode is set to data creation
if args.mode == 'data_creation':
    create_noisy_audio()
