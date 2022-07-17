import pytube
import os
import datetime

def main():


    url = input('Введите ссылку на видео: ')
    today = datetime.datetime.today()
    newName = f'{today.strftime(f"%Y-%m-%d-%H.%M.%S")}'
    if not os.path.isdir('Video'):
        os.mkdir('Video')
    path = f'{os.getcwd()}\Video\{newName}'
    try:
        yt = pytube.YouTube(url)
    except Exception as error:
        print(error)
    stream = yt.streams.get_by_itag(22)
    stream.download(output_path=path, filename=newName+'.mp4')
    print('Готово')

if __name__ == '__main__':
    main()
