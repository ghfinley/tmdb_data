

#api_key = "6eafcd32a8ce19930bf33f3b6a37af29" #use the api key from the website, unique to you 

#The problem with this is that this code will be able to be seen by anyone who views your code in github, therefore you need to go about it another way 
#Generate a new file called api_key and place in the same folder as you main project fodler and only place the api key in there 

f = open("api_key","r",)  # open the api_key file and "r" is for read, in variable f
api_key = f.read()
f.close()

print(api_key)

# To hide the file, place the api_key file in the .gitifnore file

#Make a git repo 
# 1. in the folder on terminal use commmand git init 
# 2. use command ls -la to see hidden files and verify that you are in a git repo




