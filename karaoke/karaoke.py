import tkinter as tk
import sounddevice as sd
import soundfile as sf
import threading
import pygame

fs = 44100  
seconds = 3
filename = "voice_record.wav"
minus_track = "minus.wav"  

def record_voice():
    print("Запис")
    data = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    sf.write(filename, data, fs)
    print("Запис готов!", filename)

def start_recording():
    
    pygame.mixer.music.load(minus_track)
    pygame.mixer.music.play()

    threading.Thread(target=record_voice).start()

def play_result():
    
    pygame.mixer.music.load(minus_track)
    pygame.mixer.music.play()

    data, fs = sf.read(filename, dtype='int16')
    sd.play(data, fs)


root = tk.Tk()
root.title("Караоке")
root.geometry("300x200")

pygame.mixer.init()

record = tk.Button(root, text="Записати", command=start_recording, font=("Arial", 14))
record.pack(pady=20)

play = tk.Button(root, text="Відтворити", command=play_result, font=("Arial", 14))
play.pack(pady=20)

root.mainloop()
