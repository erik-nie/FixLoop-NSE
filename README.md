# FixLoop-NSE
Adjust loop points in Nord Sample Editor from loop points in used wav files.

Some wav files have loop markers that can be inserted by loop editors or already in.  
The Nord Sample Editor does not read those loop markers. So you need to re-loop them in the Nord Sample editor.
Some external loop programs have better loop options, like different fade curves and smarter detection of loop points.
I'll recommend [Endless Wav](https://www.bjoernbojahr.de/) for this.

This Python script will search in the .nsmpproj file for the included wav files, will get the loop markers from that wav file and update the loop point in the .nsmpproj file.  

It is not fully tested, so please let me know if something goes wrong.


# Getting it to work
- Install python 3: [python 3](https://www.python.org/downloads/)   
installation of Python is straight forward (make sure to include python to the Path, this is an option during installation)  
- Download this fixloop.py
- Download wavfile.py from this repository  (based on enhanced version from Joseph Ernest: [wavfile.py](https://gist.github.com/josephernest/3f22c5ed5dabf1815f16efa8fa53d476))
- In a terminal window install numpy: "pip install numpy"  
(run cmd for windows, terminal for MacOs)

- Create a simple project with Nord Sample editor:  
-> Import all samples  
-> Assign them to zones if not done already  
-> Select all zones and select Loop  
-> Save Project  


- put samples (wav files), projectfile (.nsmpproj), wavfile.py and fixloop.py in the same folder or work from a consolodated project. Put the fixloop.py and wavefile.py file in the same folder as the projectfile

- run application from terminal/: python fixloop.py  
This will open all project files in folder and tries to find matching .wav files and transfers it's loop points and sets crossfade to 0.

- a copy of the project file is written with a prefix "_"
- Open the new project file with the prefix, check the loops and generate the Nord Sample file and transfer. 

# CheckLoopPoints
Is a simple tool to recursively traverses all folders from current folder and shows loop points if they can be found
The file wavfile.py from this repository is needed in the same folder.

# Experimental runtime version for Windows
No need to install Python.
Just create the project as described above, put wav files, projectfile and fixloop.exe in the same folder 
and run fixloop.exe by double clicking, or to run it from the commandline to see all output.
This version also scan the Media folder of a consolidated project
[fixloop.exe & checklooppoints.exe](https://qsheets.eriknie.synology.me/)
The files can be downloaded from on the bottom of that webpage 


