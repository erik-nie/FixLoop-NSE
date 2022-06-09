# fixloop.py
#
# install python 3
# download wavfile (enhanced) #https://gist.github.com/josephernest/3f22c5ed5dabf1815f16efa8fa53d476
# pip install numpy
# create a simple project with Nord Sample editor: import all samples and assign them to zones if not done already
# put samples, projectfile, wavfile.py and fixloop.py in the same folder
# python fixloop.py -> will open all project files in folder and tries to find matching .wav files and transfers it's loop points and sets crossfade to 0.
# a copy of the project file is written with a prefix "_"

import wavfile 
import glob
import re

for p in glob.glob("*.nsmpproj"):
    if p[0]=="_":
        continue
    print("=============[ "+p+" ]=============")
    
    proj_file = open(p, "r")
    ll = proj_file.readlines()

    # for all wav files get loop points and inject them into the nsmpproj file
    for filename in glob.glob("*.wav"):
        try:
            r = wavfile.read(filename,readloops=True)
            start = r[3][0][0]
            end = r[3][0][1]
        except:
            print(filename+" has no loops")
            continue
        
        
        #Search ID of filename
        id=""
        for i in range(len(ll)):
            if ll[i].find(filename) > -1:
                id = re.findall('[0-9]+', ll[i-1])[0]
                break
        if id=="":
            continue
        
        #Replace loop points        
        foundZone = False
        for i in range(len(ll)):
            if ll[i].find("m_fileID = "+id+"\n") > -1:
                foundZone = True
            if foundZone:
                if ll[i].find("m_loopStart = ") > -1:
                    ll[i] = "      m_loopStart = "+str(start)+".00000\n"
                if ll[i].find("m_loopLengthLong = ") > -1:
                    ll[i] = "      m_loopLengthLong = "+str(end-start)+".00000\n"
                if ll[i].find("m_loopXFadeLengthLong = ") > -1:
                    ll[i] = "      m_loopXFadeLengthLong = 0.00000\n"
                if ll[i].find("}") > -1:
                    print(filename + "ID:"+id+" start:", str(start), " end:" + str(end) + " len:", str(end-start))
                    #foundZone=False
                    break
                        
        if  not foundZone or id=="-":                
            print(filename + " NOT FOUND in " + p)
                    
    #write file with "_" prefix    
    proj_file = open("_"+p, "w")
    proj_file.writelines(ll)
    proj_file.close()
        

