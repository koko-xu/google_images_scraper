# google_images_scraper
Selenium scraper to download google images to local disk

# Set Up
install selenium and pyautogui
```
pip install selenium
pip install pyautogui
```

# Google_Image_Scraper.py
This script prints links to images from Google Images to the consol. First navigate to images.google.com, then search for the images you want. After you hit search, click on the first image that comes up and copy the link. Paste the link to
```
driver.get("your link)
```
This is your starting page. Adjust how many images you want to search for in
```
for i in range(your number):
```
and run the script. After the script is done scraping, open the consol and copy all links. Paste the links to a Google Sheets. If you're using this for a ML model, add labels to the scraped images. Export the Google Sheets to a csv file. 

# Download_Images.py
Copy the file path of your csv file and paste it in
```
df = pd.read_csv("your path")
```
If you're using this for a ML model, create approapriate folders based on your categorical labels. Run the script and the images linked in the csv file will be downloaded to your indicated location. 
