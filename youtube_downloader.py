# first install the library pytube
from pytube import YouTube


link='https://www.youtube.com/watch?v=KC7WGe3kFc4'

my_video=YouTube(link)

print("********************* Video Title **********************")

print(my_video.title)
print("********************** Video Thumbnail *************************************")
print(my_video.thumbnail_url)

print("********************** Video  Streaming********************")

video=my_video.streams.all()

# for only audio
#video=my_video.streams.filter(only_audio=True)

vid=list(enumerate(video))
for i in vid:
    print(i)

strm=int(input("Enter:"))
video[strm].download
print("Successfully download")    




