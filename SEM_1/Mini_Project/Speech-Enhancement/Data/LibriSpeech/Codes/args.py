import argparse

parser = argparse.ArgumentParser(description='Speech enhancement, data creation, training, and prediction')

# Mode to run the program (options: data creation, training, or prediction)
parser.add_argument('--mode', default='prediction', type=str, choices=['data_creation', 'training', 'prediction'], help='Mode to run the program')

# Folders for noise and clean voice audio (mode data_creation)
parser.add_argument('--noise_dir', default=r'D:\BDA_Sem_1\Mini_Project\Speech-Enhancement\Data\LibriSpeech\Trail.1.5\resampled\noise_files_8k', type=str, help='Directory for noise audio files')
parser.add_argument('--voice_dir', default=r'D:\BDA_Sem_1\Mini_Project\Speech-Enhancement\Data\LibriSpeech\Trail.1.5\resampled\audio_files_8k', type=str, help='Directory for clean voice audio files')

# Folders to save spectrograms, time series, and sounds
parser.add_argument('--path_save_spectrogram', default=r'D:\\BDA_Sem_1\\Mini_Project\\Speech-Enhancement\\Data\\LibriSpeech\\Trail.1.5\\Spectrogram_1.5\\', type=str, help='Directory to save spectrograms')
parser.add_argument('--path_save_time_serie', default=r'D:\BDA_Sem_1\Mini_Project\Speech-Enhancement\Data\LibriSpeech\Trail.1.5\Time_Serie_1.5', type=str, help='Directory to save time series')
parser.add_argument('--path_save_sound', default=r'D:\BDA_Sem_1\Mini_Project\Speech-Enhancement\Data\LibriSpeech\Trail.1.5\Sound_1.5', type=str, help='Directory to save sounds')

# Number of frames to create in data_creation mode
parser.add_argument('--nb_samples', default=595, type=int, help='Number of frames to create') #50 = 25 sec #18000 = 5:02:24 sec

# Training from scratch or pre-trained weights
parser.add_argument('--training_from_scratch', action='store_true', help='Train from scratch, otherwise use pre-trained weights')

# Folder for saved weights
parser.add_argument('--weights_folder', default='D:\BDA_Sem_1\Mini_Project\Speech-Enhancement\Data\LibriSpeech\Weights\\', type=str, help='Directory for saving model weights')

# Number of epochs for training
parser.add_argument('--epochs', default=10, type=int, help='Number of epochs for training')

# Batch size for training
parser.add_argument('--batch_size', default=20, type=int, help='Batch size for training')

# Name of saved model to read
parser.add_argument('--name_model', default='model_unet', type=str, help='Name of the model to read')

# Directory to read noisy sound for denoising (prediction mode)
parser.add_argument('--audio_dir_prediction', default='./demo_data/test', type=str, help='Directory to read noisy sound for denoising')

# Directory to save the denoised sound (prediction mode)
parser.add_argument('--dir_save_prediction', default='./demo_data/save_predictions/', type=str, help='Directory to save denoised sound')

# Noisy sound file(s) to denoise (prediction mode)
parser.add_argument('--audio_input_prediction', nargs='+', default=['noisy_voice_long_t2.wav'], type=str, help='List of noisy sound files to denoise')

# File name of sound output of denoised prediction
parser.add_argument('--audio_output_prediction', default='denoise_t2.wav', type=str, help='File name for the denoised sound output')

# Sample rate for reading audio
parser.add_argument('--sample_rate', default=8000, type=int, help='Sample rate for reading audio')

# Minimum duration of audio files to consider
parser.add_argument('--min_duration', default=1.0, type=float, help='Minimum duration of audio files to consider')

# Frame length for training data
parser.add_argument('--frame_length', default=8064, type=int, help='Frame length for training data')

# Hop length for clean voice files separation (no overlap)
parser.add_argument('--hop_length_frame', default=8064, type=int, help='Hop length for clean voice files separation')

# Hop length for noise files blending (adjusted)
parser.add_argument('--hop_length_frame_noise', default=4000, type=int, help='Hop length for noise files blending') #5000

# n_fft and hop_length_fft for squared spectrograms
parser.add_argument('--n_fft', default=255, type=int, help='Number of FFT components')
parser.add_argument('--hop_length_fft', default=63, type=int, help='Hop length for FFT')

args = parser.parse_args()
