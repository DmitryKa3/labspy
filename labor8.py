from PIL import Image
import os


def convert_images(directory, extensions):
    for name in os.listdir(directory):
        lowername = name.lower()
        if any(lowername.endswith(ext.lower()) for ext in extensions):
            path = os.path.join(directory, name)
            img = Image.open(path)
            if img.mode == 'P':
                img = img.convert('RGB')
            elif img.mode == 'RGBA':
                img = img.convert('RGB')

            for ext in extensions:
                if lowername.endswith(ext.lower()):
                    img.save(os.path.join(directory, name))
                else:
                    newfilename = os.path.splitext(name)[0] + ext.lower()
                    newdirectory = os.path.join(directory, ext.lstrip('.'))
                    if not os.path.exists(newdirectory):
                        os.makedirs(newdirectory)
                    img.save(os.path.join(newdirectory, newfilename))

            img.close()

directory = "C:/Users/Asus/Desktop/papk"
extensions = [".png", ".jpg", ".ico", '.gif']
convert_images(directory, extensions)
