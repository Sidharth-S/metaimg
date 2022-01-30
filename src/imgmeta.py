from PIL import Image
from PIL.ExifTags import TAGS

class metaimg:
    def __init__(self,image) -> None:
        self.image = image

        u_image = Image.open(self.image)
        exifdata = u_image.getexif()

        self.meta = []

        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)

            self.meta.append([tag,data])
        
        if len(self.meta) == 0:
            self.meta = None
    
    def cleanimage(self):
        return 


        
if __name__ == "__main__":
    test_images = ["./test_images/5.jpg",
                   "./test_images/1.jpg",
                    ]

    for i in test_images:
        x = metaimg(image = i)
        print(x.meta)
        print("")
