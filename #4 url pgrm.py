#python program to read a url and display the content in terminal
#module
import requests
#taking input from user
url =str(input("enter url here including http:"))
#from http sending a request of url
url1=requests.get(url)
print(url1)
print(url1.content)



