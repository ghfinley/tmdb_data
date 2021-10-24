import urllib.request
import os 
import json
import time #you need to have time package imported so that the program does not run forver 


#api_key = "6eafcd32a8ce19930bf33f3b6a37af29" #use the api key from the website, unique to you 

#The problem with this is that this code will be able to be seen by anyone who views your code in github, therefore you need to go about it another way 
#Generate a new file called api_key and place in the same folder as you main project fodler and only place the api key in there 

f = open("api_key","r",)  # open the api_key file and "r" is for read, in variable f
api_key = f.read()
f.close()

#print(api_key)  use this to just verifty that you have teh key 

# To hide the file, place the api_key file in the .gitifnore file

#Make a git repo 
# 1. in the folder on terminal use commmand git init 
# 2. use command ls -la to see hidden files and verify that you are in a git repo
# 3. use git status to see what files can be uploaded, amke sure that the api_key file is not there 
# 4. git add . to add to the repo 
# 5. git commit -m"Short summary"
# 6. write code and then just commit when done 

#Next Step is to set up the git hub repo so that we have an interface to see 

# 1. Create new REpo
# 2. give it a name and make it public
# 3. Link to the git repo with the git remote add orgin command, copy and paste 
# 4. Use commnad git push origin master to upload the files to git hub 
# 5. yes to continue.. you can now view files on git hub 

#  Now we have the Api Key and we have set up the git Repo and GitHub Repo

if not os.path.exists("json_files"): # For loop to create the folder for the json files 
	os.mkdir("json_files")

#Request the latest movies from tmdb
response  = urllib.request.urlopen("https://api.themoviedb.org/3/movie/latest?api_key=" + api_key) 
json_response = json.load(response)  #save the json into a variable 
movie_end = int(json_response['id']) #To get the latest movie that was placed on the website and save as an integer, pulls the 'id' out of the json response 
print(movie_end)

movie_start = movie_end-10 #This way we only have the latest 10 additions to the website and not all of them 

#Now request the data from the website, each website has their own way to do it, look at example api request 

for movie_id in range(movie_start, movie_end): #choosing the range may be difficult, in this case we set up our own range variables 
	#movie_id = 550 #the movie Id will be unique for each movie so we will have a variable for them 
	response  = urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + api_key)  #the api key is at the end so you need to add the variable at the end 

	#print(response.read()) # this is just to make sure that the code works and it prints out what you wnat 

	json_response = json.load(response)  #save the json into a variable 

	f = open("json_files/tmdb" + str(movie_id) +".json","w")  #open and file to place the json and w for write
	f.write(json.dumps(json_response)) #write the json response to the json files folder 
	f.close()
	time.sleep(20) #program will sleep for 20 seconds before re running, usually you want to more

# Now add the For loop to download more 





