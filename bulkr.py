import os, sys, shutil,string

# ref:https://careerkarma.com/blog/python-rename-file/,https://discuss.python.org/t/adding-numbers-to-filenames/4419
# https://lerner.co.il/2019/03/04/understanding-python-slices/

        # test dir :"C://xampp/htdocs/Py/bulkrename/test/"
def main(): 
#   created new folder 'test' for testing
    # path2=getuserdir()  #https://www.geekpills.com/operating-system/linux/python-passing-variable-between-functions
    getuserinput()
    exit()
       

def getuserdir():
    value1 = input("Please enter directory of file you want to rename starting from drive name. Example->C://Downloads :\n")
    # value2 = input("Please enter ways you want to rename:\n")
    
    path = str(value1)
    return path

def getuserinput(): 
#  get get the number of files want to be named ,dir , wht wnt to be named,rename ways
   
    # file = str(value2)
    
    choice = input("Enter 1 for naming it by number (ex:file1,file2,file3).\nEnter 2 for naming by letters of alphabet (ex:fileA,fileB,etc).\n")
    choice = int(choice)
    
    if choice == 1:
        print(f'Naming by number')
        renamebynumbers()
    elif choice == 2:
        print(f'Naming by alphabet')
        renamebyletters()
    

def renamebyletters():  
    path2=getuserdir()  #is actually calling the function getuserdir() too
    list=[]
    for i in string.ascii_uppercase:    #to add alphabets to the list so tht it can be referenced by list[0] as a,etc
        list.append(i)
  
    for countstr,filename in enumerate(os.listdir(path2)): #because if no count then filename become tuple, not str
        # countstr=str(string.ascii_lowercase)
        # print(countstr)
        splicetext=os.path.splitext(path2+ filename)[0]  #get filename without extension included
        file_extension=os.path.splitext(path2+ filename)[1] #get only file extension
        dst =splicetext+ list[countstr]+ file_extension 
        print("new file:"+dst)
        src =path2+ filename
        os.rename(src, dst) 
      
        
def renamebynumbers():
    path2=getuserdir()

    for count, filename in enumerate(os.listdir(path2)): 
        splicetext=os.path.splitext(path2+ filename)[0]  #get filename without extension included
        file_extension=os.path.splitext(path2+ filename)[1] #get only file extension
        dst =splicetext+ str(count)+ file_extension #put str() to prevent duplicate file naming by only putting 'filename'
        src =path2+ filename
        # dst =path2+ dst 
        # print(splicetext)
    #    splitext() is to rename file without including the .png or whatever the file extension is to be renamed
    #    ref=https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python

        #NOTA:the reason why the splicetext=.. include [0] is because when use splitext(), it will divide the filename into two,
        # ex: ('my_file', '.txt') and we only need the first section, ex:'my_file', the[0] section of array for the splicetext process
        #for file_extension, we use '[1]' because we need the 2nd part of array, which is the '.txt' or the extension


        # rename() function will 
        # rename all the files 
        # shutil.move(src,dst)
        os.rename(src, dst) 
   

# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 


    # future ventures/other ways:
    # create getuserdir.py-to make path a global variable, then just import that to freely use 'path'