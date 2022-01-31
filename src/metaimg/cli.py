import argparse


import argparse
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
                            help = ""
                           )

        

        args = parser.parse_args()