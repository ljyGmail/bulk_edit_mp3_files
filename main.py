import re
import os
import mutagen
from mutagen.easyid3 import EasyID3


# audio = EasyID3('src/20120107晚清有个李鸿章.mp3')
# print(len(audio.keys()))
# for key in audio.keys():
#     print(key, '-->', audio[key])


def getTitleFromFileName(filename):
    filenameRegex = re.compile(r'(.*).mp3', re.IGNORECASE)
    mo = filenameRegex.search(filename)
    if mo == None:
        return None
    titleName = mo.group(1)
    return titleName


folder_path = 'C:/Users/liang/Documents/压缩版/《2010年老梁说天下88集MP3》'
album_name = folder_path.rsplit('/', 1)[1]
print(album_name)
album_name = '2010年老梁说天下88集MP3'
print(album_name)

file_list = os.listdir(folder_path)
for index, f in enumerate(file_list):
    title_name = getTitleFromFileName(f)
    if title_name == None:
        continue
    print('###', index + 1)
    print(f, '-->', title_name)
    file_full_path = folder_path + '/' + f
    try:
        audio = EasyID3(file_full_path)
    except mutagen.id3.ID3NoHeaderError:
        audio = mutagen.File(file_full_path, easy=True)
        audio.add_tags()
    audio['title'] = title_name  # 제목
    audio['artist'] = '老梁'  # 참여 음악가
    audio['album'] = album_name  # 앨범
    audio['version'] = ''  # 자막
    audio['albumartist'] = ''  # 앨앰 음악가
    audio['composer'] = ''  # 작곡가
    audio['conductor'] = ''  # 지휘자
    audio['grouping'] = ''  # 그룹 설명
    audio['discnumber'] = ''  # 집합의 일부
    audio['lyricist'] = ''  # 작사가
    audio['genre'] = '时评'  # 장르
    audio['date'] = '2010'  # 연도
    audio.save()
