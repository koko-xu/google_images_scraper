""" Download Images """
import random
import urllib.request
from urllib.request import Request, urlopen
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/kokoxu/Downloads/Cattails.csv")

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Chrome/36.0.1941.0')]
urllib.request.install_opener(opener)

def download_image(folder, url, index):
    name = folder+str(index)+".jpg"
    urllib.request.urlretrieve(url, name)

cattails_folder = "/Users/kokoxu/Downloads/Cattails Dataset/Cattails/"
not_cattails_folder = "/Users/kokoxu/Downloads/Cattails Dataset/Not Cattails/"

for i in range(len(df)):
    url = df["Link"][i]
    if df["Type"][i] == "cattail":
        download_image(cattails_folder, url, i)
    else:
        download_image(not_cattails_folder, url, i)
