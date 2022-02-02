import argparse
from pathlib import PurePath
import tabulate

class cli:
    def tabulate(self,data):
        return
    
    def createcsv(self):
        return

    def cleancopy(self):
        return

    def __init__(self) -> None:
        parser = argparse.ArgumentParser(
            description = "CLI application for viewing metadata of images and saving them, and creating clean copies."
            )
        parser.add_argument(
                            "--file","-f",
                            nargs=1,
                            type=str,
                            help = "file path of image"
                           )
        
        parser.add_argument(
                            "--directory","-dir",
                            nargs=1,
                            type=str,
                            help = "directory of images"
                           )
        
        parser.add_argument(
                            "--savecsv","-csv",
                            action="store_true",
                            help = "Save image metadata as a csv file "
                           )
        
        parser.add_argument(
                            "--view","-v",
                            action="store_true",
                            help = "View metadata of image(s) [table]"
                           )

        args = parser.parse_args()

        if args.file and args.directory:
            raise ValueError("Error: Use only 1 command => --file / --directory")

        image_list = []

        if args.file:
            suffix = str(PurePath(args.file[0]).suffix)
            if suffix not in [".jpg",".jpeg",".png",".raw",".dng"]:
                raise ValueError("Error: Invalid filetype")
            
            image_list.append(args.file[0])

        print(image_list)
    


if __name__ == "__main__":
    x = cli()