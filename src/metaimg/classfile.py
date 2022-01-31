from tkinter.tix import DirSelectBox
from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import  PurePath
import csv

class metaimg:
    def __init__(self,image_path) :

        self.image = PurePath(image_path)

        u_image = Image.open(str(self.image))
        exifdata = u_image.getexif()

        self.meta = []

        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            self.meta.append([tag,data])

        if len(self.meta) == 0:
            self.meta = None
    
    def cleanimage(self,replace = False):
        im1 = Image.open(str(self.image))
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
        fields = ["Tag" , "Value"]
        rows = self.meta
        
        directory = self.image.parent
        filename = f"csv {self.image.stem}.csv"
        filename = str(directory.joinpath(filename))

        with open(filename, 'w') as csvfile: 
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(fields) 
            csvwriter.writerows(rows)
        
        return


        
if __name__ == "__main__":
    test_images = [ 
                    PurePath('src/metaimg/1.jpg'),
                    #PurePath('./test_images/5.jpg'),
                  ]

    for i in test_images:
        x = metaimg(image_path = str(i))
        x.metacsv()
        #x.cleanimage(replace=True)
        print("")
