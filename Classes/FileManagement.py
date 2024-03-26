import os
import json
import csv
import pandas as pd
import zlib
import zipfile
import smtplib
import zipfile


class FileManagement:
    def __init__(self, path):
        self.path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        if not os.path.isdir(value):
            raise ValueError("Path is not valid")
        self.__path = value

    def __writeJson(self, inputValue, name):
        with open(self.path + f"/{name}DictToJson.json", "w+", encoding="utf-8") as jsonFile:
            jsonFile.write(json.dumps(inputValue, indent=4))

    def __writeCsv(self, inputValue, name):
        with open(self.path + f"/{name}DictToCsv.csv", 'w', encoding="utf-8") as csvfile:
            w = csv.DictWriter(csvfile, inputValue.keys())
            w.writeheader()
            w.writerow(inputValue)

    def __writeXlsx(self, inputValue, name):
        df = pd.DataFrame(data=inputValue, index=[0])
        df = (df.T)
        print(df)
        df.to_excel(self.path + f"/{name}dictToXlsx.xlsx")

    def WriteDictIntoFile(self, inputValue, name):
        print("Writing dict to json")
        self.__writeJson(inputValue, name)
        print("Writing dict to Csv")
        self.__writeCsv(inputValue, name)
        print("Writing dict to Xlsx")
        self.__writeXlsx(inputValue, name)

    def WriteDictToJsonFile(self, inputValue, name):
        print("Writing dict to json")
        self.__writeJson(inputValue, name)
    def CreateZip(self):
        file_names = os.listdir(path="Files/FileManagement")
        print("File Paths:")
        print(file_names)

        # Select the compression mode ZIP_DEFLATED for compression
        # or zipfile.ZIP_STORED to just store the file
        compression = zipfile.ZIP_DEFLATED

        # create the zip file first parameter path/name, second mode
        zf = zipfile.ZipFile(self.path + "/RAWs.zip", mode="w")
        try:
            for file_name in file_names:
                # Add file to the zip file
                # first parameter file to zip, second filename in zip
                zf.write(self.path + "/" + file_name,
                         file_name, compress_type=compression)

        except FileNotFoundError:
            print("An error occurred")
        finally:
            # Don't forget to close the file!
            zf.close()
