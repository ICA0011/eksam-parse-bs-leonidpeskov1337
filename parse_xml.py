from bs4 import BeautifulSoup
import requests
import lxml

def parse_xml():
  url = "http://upload.itcollege.ee/~aleksei/test.xml"
  xml_content = requests.get(url).content
  soup = BeautifulSoup(xml_content,'xml')
  
  result = soup.find("data").contents
  stripted = result[0].strip()
  result = stripted
  return result
  
