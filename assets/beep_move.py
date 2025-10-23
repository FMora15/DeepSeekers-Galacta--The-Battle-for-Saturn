import wave, struct, math

def write_beep_wav(path, freq=880.0, duration_ms=80, volume=0.2, framerate=44100):
    nframes = int(framerate * duration_ms / 1000.0)
    with wave.open(path, 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2)  # 16-bit
        w.setframerate(framerate)
        for i in range(nframes):
            t = float(i) / framerate
            sample = int(volume * 32767 * math.sin(2.0 * math.pi * freq * t))
            w.writeframesraw(struct.pack('<h', sample))
        w.writeframes(b'')
