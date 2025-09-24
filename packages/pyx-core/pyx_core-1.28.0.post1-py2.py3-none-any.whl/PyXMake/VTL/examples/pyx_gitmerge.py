# -*- coding: utf-8 -*-
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                                                         PyXMake - Build environment for PyXMake                                                         %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
Triple-use minimum working example for PyXMake. This script can be
executed in three different ways in varying levels of accessibility
 
@note: Merge multiple git repositories into a single entity
Created on 17.06.2021

@version:  1.0    
----------------------------------------------------------------------------------------------
@requires:
       - git

@change: 
       -
   
@author: garb_ma                                                                          [DLR-SY,STM Braunschweig]
----------------------------------------------------------------------------------------------
"""
import os, sys
import argparse

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

def main(
    BuildID, 
    # Resource paths
    source=[],
    # Define output path
    output=os.getcwd(),
    # Additional keyword arguments
    **kwargs):
    """
    Main function to execute the script.
    """   
    # Create an archive from the given path.
    Utility.GetMergedRepositories(BuildID, source, output=output, **kwargs)
    pass
    
if __name__ == "__main__":
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                                                                         Access command line inputs                                                                  %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Process all known arguments
    parser = argparse.ArgumentParser(description='CLI wrapper options for  repository merger (GIT).')
    parser.add_argument('name', type=str, nargs=1, help="Name of the new repository.")
    parser.add_argument('source', type=Utility.GetIterable, nargs="+", help="List of URLs pointing to existing repositories with optionally checkout and branch names.")
    parser.add_argument("--keep", type=Utility.GetIterable, nargs="+", help="List of boolean values representing the merge operation. Source URLs with custom checkouts are kept as is, all other as solely kept as branches.")
    parser.add_argument("--output", type=str, nargs=1, help="Absolute path to output directory. Defaults to the current workspace.")
    # Check all options or run unit tests in default mode   
    try:
        # Check CLI options
        _ = sys.argv[1]
        args, _ = parser.parse_known_args()  
        # Archive output name is mandatory
        project = args.name[0] ; 
        # Source specification is mandatory
        source = [(x[0],"") if not isinstance(x, tuple) or x[0] == x[-1] else x for x in  args.source[0] ]
        # Optional non-default output directory
        try: output = args.output[0]
        except: output = os.path.abspath(os.getcwd())
        # Optional non-default mapping to keep certain folders as defined.
        try: keep = [Utility.GetBoolean(x) for x in Utility.ArbitraryFlattening(args.keep[0]) if Utility.IsNotEmpty(x)]
        except: keep = []
        # Create a dictionary combining all settings
        settings = {"output":output, "keep_subfolder":keep}
    # Use an exception to allow help message to be printed.
    except Exception as _:
        # Run default function call for unit test coverage
        if AllowDefaultMakeOption: main("dlr", 
                                                                    source=["https://gitlab.com/dlr-sy/beos.git#beos_core",
                                                                                  ("https://gitlab.com/dlr-sy/micofam.git","mico"),
                                                                                  ("https://gitlab.com/dlr-sy/displam.git","displam")], 
                                                                    output=Scratch, keep_subfolder=[False,False,True])
    # Execute valid CLI command
    else: main(project, source, **settings)
    # Finish 
    print("==================================")
    print("Finished merging repositories")
    print("==================================")   