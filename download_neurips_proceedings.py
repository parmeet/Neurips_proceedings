from bs4 import BeautifulSoup
import urllib.request
import requests,os

#funtion to donwload PDF
def downloadPDF(url,file_name):
    myfile = requests.get(url)
    with open(file_name,'wb') as f: f.write(myfile.content)

#set-up
neurips_url = 'https://papers.nips.cc/book/advances-in-neural-information-processing-systems-32-2019'
base_url    = 'https://papers.nips.cc'
download_folder = r'D:\'
destination_folder = os.path.join(download_folder,'NeurIPS2019')
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

#query URL
resp = urllib.request.urlopen(neurips_url)
soup = BeautifulSoup(resp)

all_paper_links = [base_url+l['href']+'.pdf' for l in soup.find_all('a',href=True) if '/paper/' in l['href']]
print("Total number of papers to download:{}".format(len(all_paper_links)))

#download PDFs
for l in all_paper_links:
    paper_name = l.split('/')[-1]
    print("Downloading paper:{}".format(paper_name))
    downloadPDF(l,os.path.join(destination_folder,paper_name))
