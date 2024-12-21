import os
import librosa
import numpy as np
from scipy.io.wavfile import write
from data_tools import audio_files_to_numpy, blend_noise_randomly, numpy_audio_to_matrix_spectrogram

def create_data(noise_dir, voice_dir, path_save_time_serie, path_save_sound, path_save_spectrogram, sample_rate,
                min_duration, frame_length, hop_length_frame, hop_length_frame_noise, nb_samples, n_fft, hop_length_fft):
    list_noise_files = os.listdir(noise_dir)
    list_voice_files = os.listdir(voice_dir)

    list_noise_files = [f for f in list_noise_files if not f.startswith('.')]  # Removes any hidden files
    list_voice_files = [f for f in list_voice_files if not f.startswith('.')]

    # Convert audio files to numpy arrays
    noise = audio_files_to_numpy(noise_dir, list_noise_files, sample_rate, frame_length, hop_length_frame_noise, min_duration)
    voice = audio_files_to_numpy(voice_dir, list_voice_files, sample_rate, frame_length, hop_length_frame, min_duration)

    # Blend clean voice and noise
    prod_voice, prod_noise, prod_noisy_voice = blend_noise_randomly(voice, noise, nb_samples, frame_length)

    # Save blended audio to disk
    noisy_voice_long = prod_noisy_voice.reshape(1, nb_samples * frame_length)
    write(os.path.join(path_save_sound, 'noisy_voice_long.wav'), sample_rate, (noisy_voice_long[0, :] * 32767).astype(np.int16))

    voice_long = prod_voice.reshape(1, nb_samples * frame_length)
    write(os.path.join(path_save_sound, 'voice_long.wav'), sample_rate, (voice_long[0, :] * 32767).astype(np.int16))

    noise_long = prod_noise.reshape(1, nb_samples * frame_length)
    write(os.path.join(path_save_sound, 'noise_long.wav'), sample_rate, (noise_long[0, :] * 32767).astype(np.int16))

    # Create spectrograms
    dim_square_spec = int(n_fft / 2) + 1
    m_amp_db_voice, m_pha_voice = numpy_audio_to_matrix_spectrogram(prod_voice, dim_square_spec, n_fft, hop_length_fft)
    m_amp_db_noise, m_pha_noise = numpy_audio_to_matrix_spectrogram(prod_noise, dim_square_spec, n_fft, hop_length_fft)
    m_amp_db_noisy_voice, m_pha_noisy_voice = numpy_audio_to_matrix_spectrogram(prod_noisy_voice, dim_square_spec, n_fft, hop_length_fft)

    # Save data to disk for further processing
    np.save(os.path.join(path_save_time_serie, 'voice_timeserie.npy'), prod_voice)
    np.save(os.path.join(path_save_time_serie, 'noise_timeserie.npy'), prod_noise)
    np.save(os.path.join(path_save_time_serie, 'noisy_voice_timeserie.npy'), prod_noisy_voice)

    np.save(os.path.join(path_save_spectrogram, 'voice_amp_db.npy'), m_amp_db_voice)
    np.save(os.path.join(path_save_spectrogram, 'noise_amp_db.npy'), m_amp_db_noise)
    np.save(os.path.join(path_save_spectrogram, 'noisy_voice_amp_db.npy'), m_amp_db_noisy_voice)

    np.save(os.path.join(path_save_spectrogram, 'voice_pha_db.npy'), m_pha_voice)
    np.save(os.path.join(path_save_spectrogram, 'noise_pha_db.npy'), m_pha_noise)
    np.save(os.path.join(path_save_spectrogram, 'noisy_voice_pha_db.npy'), m_pha_noisy_voice)
