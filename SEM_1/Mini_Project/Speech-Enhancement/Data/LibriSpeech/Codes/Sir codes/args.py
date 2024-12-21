import argparse

parser = argparse.ArgumentParser(description='Speech enhancement,data creation, training and prediction')

#mode to run the program (options: data creation, training or prediction)
parser.add_argument('--mode',default='prediction', type=str, choices=['data_creation', 'training', 'prediction'])
#folders where to find noise audios and clean voice audio to prepare training dataset (mode data_creation)
parser.add_argument('--noise_dir', default='/home/raghu/Speech-enhancement-deeplearn-vbelz/data/Train/noise', type=str)

parser.add_argument('--voice_dir', default='/home/raghu/Speech-enhancement-deeplearn-vbelz/data/Train/clean_voice', type=str)
#folders where to save spectrograms, time series and sounds for training / QC
parser.add_argument('--path_save_spectrogram', default='/home/raghu/Speech-enhancement-deeplearn-vbelz/data/Train/spectrogram/', type=str)

parser.add_argument('--path_save_time_serie', default='/home/raghu/Speech-enhancement-deeplearn-vbelz/data/Train/time_serie/', type=str)

parser.add_argument('--path_save_sound', default='/home/raghu/Speech-enhancement-deeplearn-vbelz/data/Train/sound/', type=str)
#How much frame to create in data_creation mode
parser.add_argument('--nb_samples', default=18000, type=int)  #40
#Training from scratch or pre-trained weights
parser.add_argument('--training_from_scratch',default=True, type=bool)
#folder of saved weights
parser.add_argument('--weights_folder', default='./weights', type=str)
#Nb of epochs for training
parser.add_argument('--epochs', default=20, type=int) #10
#Batch size for training
parser.add_argument('--batch_size', default=25, type=int) #20
#Name of saved model to read
parser.add_argument('--name_model', default='model_best', type=str)  #model_unet, model_best
#directory where read noisy sound to denoise (prediction mode)
parser.add_argument('--audio_dir_prediction', default='./demo_data/test', type=str)
#directory to save the denoise sound (prediction mode)
parser.add_argument('--dir_save_prediction', default='./demo_data/save_predictions/', type=str)
#Noisy sound file to denoise (prediction mode)
parser.add_argument('--audio_input_prediction', default=['knm_00180_00011382081_8000Hz_5db.wav'], type=list)   # noisy_voice_long
#File name of sound output of denoise prediction
parser.add_argument('--audio_output_prediction', default='knm_00180_00011382081_8000Hz_5db_denoise1.wav', type=str)   # denoise.wav
# Sample rate chosen to read audio
parser.add_argument('--sample_rate', default=8000, type=int)
# Minimum duration of audio files to consider
parser.add_argument('--min_duration', default=1.0, type=float) #1.0
# Training data will be frame of slightly above 1 second
parser.add_argument('--frame_length', default=8064, type=int)
# hop length for clean voice files separation (no overlap)
parser.add_argument('--hop_length_frame', default=8064, type=int)
# hop length for noise files to blend (noise is splitted into several windows)
parser.add_argument('--hop_length_frame_noise', default=4000, type=int) #5000
# Choosing n_fft and hop_length_fft to have squared spectrograms
parser.add_argument('--n_fft', default=255, type=int)

parser.add_argument('--hop_length_fft', default=63, type=int)
