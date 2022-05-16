from pytube import YouTube
URL = input('Input your URL: ',)
Video = YouTube(URL)
res = input('What resolistion do u want(144,360,720,1080): ',)

try:
    Video.streams.filter(res= res+"p").first().download()
    print('Download done')
except:
    print('Failed')