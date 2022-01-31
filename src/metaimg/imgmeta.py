from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import  PurePath

class metaimg:
    def __init__(self,image_path) :
        self.image = image_path

        u_image = Image.open(self.image)
        exifdata = u_image.getexif()

        self.meta = []

        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            self.meta.append([tag,data])

        if len(self.meta) == 0:
            self.meta = None
    
    def cleanimage(self,replace = False):
        im1 = Image.open(self.image)
        im2 = im1.copy()
        
        fp = PurePath(self.image)

        if replace == True :
            im2.save(str(fp))
            return

        directory = fp.parent
        fname = f"Clean - {fp.name}"
        new_path = str(directory.joinpath(fname))
        im2.save(new_path)
        return 

    def metacsv(self):
        return


        
if __name__ == "__main__":
    test_images = [ 
                    PurePath('./test_images/1.jpg'),
                    PurePath('./test_images/5.jpg'),
                  ]

    for i in test_images:
        x = metaimg(image_path = str(i))
        print(x.meta)
        #x.cleanimage(replace=True)
        print("")
