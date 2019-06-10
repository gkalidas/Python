# 
# Example file for retrieving data from the internet
#
import urllib.request

def main():
  weburl = urllib.request.urlopen("https://www.google.com")
  print("result code "+ str(weburl.getcode()))
  data = weburl.read()
  print(data)
  #200 - ok
  #404 - file not found

if __name__ == "__main__":
  main()
