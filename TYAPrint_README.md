This python program will run minimized. Everytime an ALT+P is pressed it will print a PDF file with SumatraPDF viewer to the default printer. It will also check for a lockfile.lck at a location, if that file is found. It will restart itself. 

This code was created for the purpose of running in tandum with another program. The other program also sent jobs to a printer, but after the job was sent. It made the python code break. Restarting the program solved the issue. 
