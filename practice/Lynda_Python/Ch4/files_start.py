#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # w - write access to the file, "+" - to create file if it doesn't exist
  #f = open("textfile.txt","w+")


  # Open the file for appending text to the end
  f = open("textfile.txt","r")

  # write some lines of data to the file
  # for i in range(10):
  #   f.write("This is line " + str(i) + "\r\n")
  
  # close the file when done
  # f.close()
  
   #Open the file back up and read the contents
   #reason for the following block is to make sure that
   #file is opend in read mode
  if f.mode=='r':
    #contents = f.read()
    #readline() - to read the first line of the file
    #readlines() - to read the file line by line
    fl = f.readlines()
    for x in fl:
      print(x)
    # print(contents)
    
if __name__ == "__main__":
  main()
