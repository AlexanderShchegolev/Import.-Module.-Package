import pytube


link = 'https://www.youtube.com/watch?v=OoRqKJJ_XAE&t=296s'
path = '/Users/alexshchegolev/Downloads'

YT_parser = pytube.YouTube(link)

highest_resolution_video = YT_parser.streams.get_highest_resolution()
highest_resolution_video.download(path)

