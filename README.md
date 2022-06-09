# FixLoop-NSE
Adjust loop points in Nord Sample Editor from loop points in used wav files

# Getting it to work
- Install python 3: [python 3](https://www.python.org/downloads/)   
installation of Python is straight forward (make sure to include python to the Path, this is an option during installation)
- download wavfile (enhanced): [wavfile](https://gist.github.com/josephernest/3f22c5ed5dabf1815f16efa8fa53d476)
- in a terminal window install numpy: "pip install numpy"  
(run cmd for windows, terminal for MacOs)

- Create a simple project with Nord Sample editor:  
-> Import all samples  
-> Assign them to zones if not done already  
-> Select all zones and select Loop  
-> Save Project  

- put samples (wav files), projectfile (.nsmpproj), wavfile.py and fixloop.py in the same folder

- run application from terminal/: python fixloop.py  
This will open all project files in folder and tries to find matching .wav files and transfers it's loop points and sets crossfade to 0.

- a copy of the project file is written with a prefix "_"
- Open the new project file with the prefix, check the loops and generate the Nord Sample file and transfer. 
