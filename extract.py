from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.amazon.in/gp/product/B0794JD9JS/ref=s9_acss_bw_cg_famcat1_3a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=DT9XVBR7CAEHX2W2S4ND&pf_rd_t=101&pf_rd_p=014d2fb9-0a03-415a-8da8-feb434b3d68f&pf_rd_i=14156834031"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
title = soup.title      # extracting the title of the product
print(title)
print("\n")

links = soup.find_all("a")      # extracting the links related to the product
for link in links:
    print(link.get("href"))
print("\n")

images = soup.find_all("img")   # extracting the images of the product
for image in images:
    print(image.get("src"))
print("\n")

text = soup.get_text()          # extracting the text
print(text)

