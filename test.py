# import moviepy.editor as mp
# video = mp.VideoFileClip(r"Sub-3_Video-Multi-UAV_Short_C.mp4")
# video.audio.write_audiofile(r"output.mp3")


import speech_recognition as sr
r = sr.Recognizer()                        #預設辨識英文
with sr.WavFile("output.wav") as source:    #讀取wav檔
    audio = r.record(source)
try:
    string =  r.recognize_google(audio,language="zh-TW")
    print("Transcription: " + string)  #使用Google的服務
    txt = 'output.txt'
    f = open(txt, 'w')
    f.writelines( string)

except LookupError:
    print("Could not understand audio")
