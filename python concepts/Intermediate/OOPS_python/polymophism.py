class AudioFile():
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Invalid file format')

        self.filename = filename

class Mp3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print(f'playing mp3: {self.filename}')

class WavFile(AudioFile):
    ext = 'wav'
    def play(self):
        print(f'playing wav: {self.filename}')

class AacFile(AudioFile):
    ext = 'aac'
    def play(self):
        print(f'playing aac: {self.filename}')

a = Mp3File('sing.mp3')
b = WavFile('sang.wav')
c = AacFile('song.aac')

a.play()
b.play()
c.play()