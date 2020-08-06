import pickle
import requests

url = "https://www.youtube.com/redirect?redir_token=D4-2OLto10Bo5GbIjaRdU2Aaa398MTU5MjgyNDI1M0AxNTkyNzM3ODUz&q=https%3A%2F%2Farchive.ics.uci.edu%2Fml%2Fmachine-learning-databases%2Firis%2Firis.data%27&event=comments&stzid=UgwQC4KdLMe50PCvl554AaABAg"

responce = requests.get(url).text
data = responce.splitlines()
red = [[i]for i in data]
print(red)

fileobj = open("iris.pkl","wb")
pickle.dump(red,fileobj)
fileobj.close()

fileobj = open("iris.pkl","rb")
data = pickle.load(fileobj)
print(data)