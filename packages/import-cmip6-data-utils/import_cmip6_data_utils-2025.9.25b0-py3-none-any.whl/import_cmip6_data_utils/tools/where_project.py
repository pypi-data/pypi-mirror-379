#!/usr/bin/env python3

"""This script contains a function to locate the project absolute path.

Functions :

get_project_absolute_path : Finds the absolute path of the project root.

Author : GIBONI Lucas

Feel free to copy, adapt and modify it under the provided license.
"""

##################################
### IMPORTATION OF THE MODULES ###
##################################

from pathlib import Path  # It is used to know the absolute path of this script.

###################################
### DEFINITION OF THE FUNCTIONS ###
###################################

#################################
### GET_PROJECT_ABSOLUTE_PATH ###
#################################


def get_project_absolute_path():
    """Finds the absolute path of the project root.

    Returns
    -------
    project_absolute_path : str

        The path of the project root.


    """

    ### GET THIS SCRIPT'S ABSOLUTE PATH ###

    script_absolute_path = Path(__file__).parent.resolve()

    ### GET THE PROJECT ROOT'S ABSOLUTE PATH ###

    project_absolute_path = script_absolute_path.parent.parent

    ### CONVERT IT TO STR ###

    project_absolute_path = str(project_absolute_path)

    return project_absolute_path


######################
### USED FOR TESTS ###
######################

if __name__ == "__main__":
    pass
