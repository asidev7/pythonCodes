#bin/usr/python@augustin


from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Télécharger avec succès")


link = input("Entrez le lien de video Youtube ici : ")
Download(link)
