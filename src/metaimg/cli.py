import argparse


import argparse
from msilib.schema import Error
from parso import parse
import tabulate

class cli:
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
        


        

        args = parser.parse_args()

        if args.file and args.directory:
            raise ValueError("Error: Use only 1 command => --file / --directory")

if __name__ == "__main__":
    x = cli()