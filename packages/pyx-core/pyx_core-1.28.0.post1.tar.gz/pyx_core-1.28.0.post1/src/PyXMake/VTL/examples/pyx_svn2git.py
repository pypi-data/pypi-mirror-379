# -*- coding: utf-8 -*-
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %           PyXMake - Build environment for PyXMake            %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
Translate a given SVN repository to a GIT repository.

@version:  1.0    
----------------------------------------------------------------------------------------------
@requires:
       - git and svn executables

@change: 
       -    
   
@author: garb_ma                                                     [DLR-SY,STM Braunschweig]
----------------------------------------------------------------------------------------------
"""

import os, sys
import git
import glob
import time
import shlex
import shutil
import argparse
import subprocess

try:
    import PyXMake as _ #@UnusedImport
except ImportError:
    # Script is executed as a plug-in
    sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
finally:
    # Import all module dependencies
    from PyXMake.Tools import Utility
    from PyXMake.VTL import Scratch
    from PyXMake.Build.Make import AllowDefaultMakeOption

def main(git_repo, svn_repo, output=os.getcwd(), **kwargs):
    """
    Main function to execute the script.
    """
    # Do not attempt global import of SVN due to deprecation
    import svn.remote
    # Some local variables
    __maxTimeout = 10; numAttempts = __maxTimeout
    # Operate in a full temporary directory
    with Utility.ChangedWorkingDirectory(Scratch):
        # Create a temporary source code folder.
        __temp_path = os.path.join(os.getcwd(),Utility.GetTemporaryFileName(extension=""))
        # Print an informative message
        print("==================================")    
        print("Processing %s" % git_repo.upper())
        print("==================================")
        svn.remote.RemoteClient(svn_repo).checkout(__temp_path)
        with Utility.ChangedWorkingDirectory(__temp_path):
            # Get current bash executable from local GIT installation
            found, bash = Utility.GetExecutable("bash",get_path=True)
            if not found and Utility.GetPlatform() in ["windows"]:
                bash = os.path.join(os.path.dirname(os.path.dirname(Utility.GetExecutable(git.Git.GIT_PYTHON_GIT_EXECUTABLE, get_path=True)[-1])),"bin","bash.exe") #@UndefinedVariable
            # Search for all authors who contributed to this path
            command = "svn log -q | awk -F"+" '|' '/^r/ "+'{sub("^ ", "", $2); sub(" $", "", $2); ' + 'print $2" = "$2" <"$2">"}'+"' | sort -u > authors-git.txt"
            with open("authors.sh","w") as script: script.write(command)
            command = " ".join(['"'+bash+'"',"-c","./authors.sh"])
            # Create a bash script to execute a bash command with both types of quotation
            if Utility.GetPlatform() in ["linux"]: subprocess.run(['chmod', 'u+x', 'authors.sh'])
            subprocess.call(command, shell=True);
            while True:
                # Attempt to rename result. Avoid race condition
                if numAttempts <= 0: break
                if os.path.exists(os.path.join(os.getcwd(),"authors-git.txt")): 
                    shutil.move(os.path.join(os.getcwd(),"authors-git.txt"),os.path.join(Scratch,"authors-git.txt"))
                    break
                else: numAttempts -= 1
        # Again, avoid race condition. If it is still happening, retry again until success.
        numAttempts = 0
        while True:
            time.sleep(1)
            if numAttempts >= __maxTimeout: break
            try: Utility.DeleteRedundantFolders(__temp_path, ignore_readonly=True); break
            except: numAttempts += 1
        source = os.path.dirname(svn_repo)
        trunk = Utility.PathLeaf(svn_repo)

        # Create a new local repository
        g = git.Repo.init(os.path.join(os.getcwd(),git_repo)) #@UndefinedVariable
        if Utility.GetPlatform() == "windows": g.git.execute("git config --global core.longpaths true")

        # Assemble GIT command
        command = "git svn clone "+source+" --no-metadata --no-minimize-url -T "+trunk+" --authors-file="+str(os.path.join('"'+os.getcwd(),"authors-git.txt"+'"'))+" "+"."

        # Never surrender to GIT. Wait until the requested repository is non-empty
        while not glob.glob(os.path.join(os.getcwd(),git_repo, '*')):
            try:
                time.sleep(0.2) # Again, avoid race conditions
                g.git.execute(shlex.split(command,posix=not os.name.lower() in ["nt"]))
            except Exception as e:
                # Present exception error
                print(e)
                # Issue a notification
                print("==================================")
                print("This error is deemed non-critical. Ignoring")
                print("==================================")      
                pass
            
        # Delete files with no further use
        Utility.DeleteFilesbyEnding("authors-git.txt")
        if os.getcwd() != output: Utility.MoveIO(git_repo, os.path.join(output,git_repo))
    
if __name__ == '__main__':
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                  Access command line inputs                  %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    parser = argparse.ArgumentParser(description="Translate a given SVN repository to a GIT repository.")
    parser.add_argument('name', type=str, nargs=1, help="Name of the new GIT repository.")
    parser.add_argument('source', type=str, nargs=1, help="URL to source SVN repository.")
    parser.add_argument("--output", type=str, nargs=1, help="Absolute path to output directory. Defaults to the current workspace.")
    # Check all options or run unit tests in default mode
    try:
        # Check CLI options
        _ = sys.argv[1]
        args, _ = parser.parse_known_args()  
        # Project name is mandatory
        project = args.name[0] ; 
        # SVN repository URL is mandatory
        source = args.source[0] ; 
        # Optional non-default output directory
        try: output = args.output[0]
        except: output = os.path.abspath(os.getcwd())
    # Use an exception to allow help message to be printed.
    except Exception as _:
        # Run default function call for unit test coverage
        if AllowDefaultMakeOption: main("ccaudio", "http://svn.savannah.gnu.org/svn/ccaudio/trunk");
    # Execute command with user defined input
    else: main(project,source,output)
    # Finish translation job
    print("==================================")    
    print("Finished translation")
    print("==================================")    
    sys.exit()