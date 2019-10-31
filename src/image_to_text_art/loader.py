from cv2 import imread, COLOR_BGR2RGB, COLOR_BGR2GRAY, cvtColor
from os.path import exists, isfile


class Loader:
    """A wrapper for loading images
    """
    def load_image(self):
        """Loads source image
        
        Raises
        ------
        FileNotFoundError
            when the file does not exist
        ValueError
            when the loaded file is not an image
        """
        try:
            filename = self.args.image
            if not(exists(filename) and isfile(filename)):
                raise FileNotFoundError(f"File {filename} does not exist")
        
            self.image = imread(filename)
            if self.image is None:
                raise ValueError(f"File {filename} is not an image!")
            
            self.image = cvtColor(self.image, COLOR_BGR2RGB if self.args.color else COLOR_BGR2GRAY)
        except Exception as e:
            print(e)
            exit()
