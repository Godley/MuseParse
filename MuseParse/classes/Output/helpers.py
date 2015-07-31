import os
from sys import platform

def setup_lilypond(path_to_lilypond_folder="default"):
    '''
    Optional helper method which works out the platform and calls the relevant setup method

    * param path_to_lilypond_folder: the path where lilypond.exe or the lilypond runner tool in mac is located. Not needed if
    setup is default, or if using linux

    * :return: None
    '''
    options = {"win32" : setup_lilypond_windows, "darwin": setup_lilypond_osx}
    if platform.startswith("linux"):
        setup_lilypond_linux()
    else:
        options[platform](path_to_lilypond_folder)

def setup_lilypond_windows(path="default"):
    '''
    Optional helper method which does the environment setup for lilypond in windows. If you've ran this method, you do not need and should not provide
    a lyscript when you instantiate this class. As this method is static, you can run this method before you set up the LilypondRenderer
    instance.

    * parameter: path_to_lilypond is the path to the folder which contains the file "lilypond.exe". Usually ProgramFiles/Lilypond/usr/bin.
    Leave at default to set to this path.

    * returns: None
    '''
    default = "C:/Program Files (x86)/LilyPond/usr/bin"
    path_variable = os.environ['PATH'].split(";")
    if path == "default":
        path_variable.append(default)
    else:
        path_variable.append(path)
    os.environ['PATH'] = ";".join(path_variable)


def setup_lilypond_linux():
    '''
    Optional helper method which downloads and installs lilypond from apt-get.

    * return: None
    '''
    os.system("sudo apt-get install lilypond")


def setup_lilypond_osx(path="default"):
    '''
    Optional helper method which sets up the environment on osx.

    * parameter: path is the path to the file you are using as an lyscript. Please refer to the lilypond.org documentation for what this should contain

    * return: None
    '''

    default = "/Applications/LilyPond.app/Contents/Resources/bin"
    path_variable = os.environ['PATH'].split(":")
    if path == "default":
        path_variable.append(default)
    else:
        path_variable.append(path)
    os.environ['PATH'] = ":".join(path_variable)
