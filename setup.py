import cx_Freeze
import sys



base= None

if sys.platform == 'win32':
    base = "Win32GUI"


executables = [cx_Freeze.Executable("Numerology-Softwere.py", base=base,icon='icon.ico')]
cx_Freeze.setup(
    name="Numerology-Softwere",
	version="0.01",
    description="create by Purnendu Das,(das888purnendu@gmail.com), it is made by many Astrological theories",
    options = {"build_exe":{"packages":["tkinter"],"include_files":["icon.ico","label-image1.gif","label-image2.gif",r"C:\Users\User\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll",r"C:\Users\User\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll"]}},
    executables=executables
    
    )
