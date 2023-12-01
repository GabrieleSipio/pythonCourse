import os
import json
import csv
import pandas as pd
import zlib
import zipfile
import smtplib
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import MIMETextimport as smtplibdef 

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

    def __writeJson(self,inputValue):
        with open(self.path + "/DictToJson.json", "w+", encoding="utf-8") as jsonFile:
            jsonFile.write(json.dumps(inputValue, indent=4))
            
    def __writeCsv(self, inputValue):
        with open(self.path + "/DictToCsv.csv" , 'w', encoding="utf-8") as csvfile:
            w = csv.DictWriter(csvfile, inputValue.keys())
            w.writeheader()
            w.writerow(inputValue)
            
    def __writeXlsx(self, inputValue):
        df = pd.DataFrame(data=inputValue, index=[0])
        df = (df.T)
        print (df)
        df.to_excel(self.path + "/dictToXlsx.xlsx")
    
    def WriteDictIntoFile (self, inputValue):
        print ("Writing dict to json")
        self.__writeJson(inputValue)
        print ("Writing dict to Csv")
        self.__writeCsv(inputValue)
        print ("Writing dict to Xlsx")
        self.__writeXlsx(inputValue)
        
        
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
                zf.write(self.path + "/" + file_name, file_name, compress_type=compression)

        except FileNotFoundError:
            print("An error occurred")
        finally:
            # Don't forget to close the file!
            zf.close()


    def send_file_zipped(self, the_file, recipients, sender='you@you.com'):
        # Create a multipart message
        msg = MIMEMultipart()
        body_part = MIMEText("messaggio inviato tramite python, you nigga!", 'plain')
        msg['Subject'] = "tst"
        msg['From'] = sender
        msg['To'] = "giacomo.difino89@gmail.com"
        # Add body to email
        msg.attach(body_part)
        # open and read the file in binary
        with open(self.path + "/RAWs.zip",'rb') as file:
        # Attach the file with filename to the email
            msg.attach(MIMEApplication(file.read(), Name='RAWs.zip'))
        # Create SMTP object    smtp_obj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # Login to the server    smtp_obj.login(SMTP_USERNAME, SMTP_PASSWORD)
        # Convert the message to a string and send it
        smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
        smtp_obj.quit()
        