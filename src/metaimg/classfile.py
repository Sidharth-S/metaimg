from logging import exception
from xml.dom import ValidationErr
from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import  PurePath
import csv

class metaimg:
    def __init__(self,image_path) :

        self.image = PurePath(image_path)

        if self.image.suffix not in [".jpg",".jpeg",".png",".raw",".dng"]:
            raise ValueError("Error: File not an image format")


        u_image = Image.open(str(self.image))
        exifdata = u_image.getexif()

        # List storing the metadata of the image (self.image)
        self.meta = []

        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            self.meta.append([tag,data])

        if len(self.meta) == 0:
            self.meta = None
    
    def cleanimage(self,replace = False,fp = None):
        im1 = Image.open(str(self.image))
        im2 = im1.copy()
        

        temp_fp = self.image

        if replace == True :
            im2.save(str(temp_fp))
            return

        directory = temp_fp.parent
        fname = f"Clean - {temp_fp.name}"
        save_path = str(directory.joinpath(fname))

        # If fp has been provided
        if fp : save_path = fp

        im2.save(save_path)

        return 

    def metacsv(self, fp = None):
        fields = ["Tag" , "Value"]
        rows = self.meta
        
        directory = self.image.parent
        filename = f"csv {self.image.stem}.csv"
        filename = str(directory.joinpath(filename))

        if fp:
            filename = fp

        try:
            with open(filename, 'w') as csvfile: 
                csvwriter = csv.writer(csvfile) 
                csvwriter.writerow(fields) 
                csvwriter.writerows(rows)
        except  exception as e :
            raise RuntimeError("Error. Unable to create csv")

        return


        
if __name__ == "__main__":
    test_images = [ 
                    PurePath('src/metaimg/1.jpg'),
                  ]

    for i in test_images:
        x = metaimg(image_path = str(i))
        #x.metacsv(fp="tests/123.csv")
        x.cleanimage(replace=True)
        print("")
