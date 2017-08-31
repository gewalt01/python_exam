from PIL import Image

class GifImage:
    path = ""
    frameNum = 0
    image = None

    def __init__(self, path):
        self.loadImage(path)

    def loadImage(self, path):
        self.path = path
        self.image = Image.open(path)
        self.analyseImage(path)

    def analyseImage(self, path):
        n = 0
        try:
            while True:
                n += 1
                self.image.seek(self.image.tell() + 1)
        except EOFError:
            self.imageRewind()
            self.frameNum = n
    
    def imageRewind(self):
        self.image.seek(0)

    def getFrame(self, num):
        try:
            frame = Image.new('RGBA', self.image.size)

            for x in xrange(0, num + 1):
                self.image.seek(x)
                frame.paste(self.image, (0,0), self.image.convert('RGBA'))
            self.image.seek(num)
            frame.paste(self.image, (0,0), self.image.convert('RGBA'))
        

        except:
            frame = None
        
        self.imageRewind()

        return frame


if __name__ == "__main__":
    name = "image.gif"

    im = GifImage(name)
    for frame_no in range(0, im.frameNum):
        out = "out-%d.png" % frame_no
        im.getFrame(frame_no).save(out)
