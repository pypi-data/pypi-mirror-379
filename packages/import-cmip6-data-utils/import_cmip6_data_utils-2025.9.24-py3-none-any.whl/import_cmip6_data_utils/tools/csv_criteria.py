#!/usr/bin/env python3

"""This script contains functions used to read csv files and extracts the criteria to constrain the search of CMIP6 outputs.

Functions :
-----------

csv_to_dataframe : Reads the provided csv file and generates a panda dataframe from it.

extract_search_facets : Reads the provided csv file holding the search criteria and generates a dictionary of the search facets.

Author : GIBONI Lucas

Feel free to copy, adapt and modify it under the provided license.
"""

##################################
### IMPORTATION OF THE MODULES ###
##################################

### HANDLING PATHS ###
from os.path import (
    join,  # This allows to generate a path without caring about "/".
    isfile,  # We used it to check the existence of a given file.
)

from pathlib import Path  # It is used to check the .csv suffix of filenames.

### DATA OBJECTS AND ASSOCIATED COMPUTATION ###
import pandas as pd  # This is to read csv files.

### PROJECT MODULES ###

## Getting the absolute path of the root of the project ##

from import_cmip6_data_utils.tools.where_project import (
    get_project_absolute_path,  # It is used to get the absolute path of the root of the project.
)

###################################
### DEFINITION OF THE FUNCTIONS ###
###################################

########################
### CSV_TO_DATAFRAME ###
########################


def csv_to_dataframe(csv_filename: str) -> pd.DataFrame:
    """Reads the provided csv file and generates a panda dataframe from it.

    Parameters
    ----------
    csv_filename : str

        Name of the csv file to load into a Panda Dataframe.

    Returns
    -------
    criteria_dataframe : pd.DataFrame

        Panda DataFrame made out of the criteria contained in the csv file
    """

    ### TEST IF THE FILENAME IS DEFINED ###

    if csv_filename:  # We verify that the filename is defined.
        ### FILENAME DEFINED : INITIALISATION ###

        ## Adding the suffix .csv if not added by the user ##

        csv_filename = str(Path(csv_filename).with_suffix(".csv"))

        ## Generate the path of the csv file ##

        # Get the absolute path of the project root #

        project_absolute_path = get_project_absolute_path()

        # Generate the path of the criteria folder #

        criteria_folder_path = join(project_absolute_path, "criteria")

        # Generate the path of the csv file #

        full_path_criteria_csv = join(criteria_folder_path, csv_filename)

        ### TEST IF THE FILENAME EXISTS ###

        if isfile(full_path_criteria_csv):  # This verifies if the csv file exists.
            ### BOTH TEST PASSED : GENERATE A PANDA DATAFRAME FROM THE PROVIDED CSV FILE ###

            criteria_dataframe = pd.read_csv(full_path_criteria_csv, sep=";", dtype=str)

            return criteria_dataframe

        ### THE FILE DOES NOT EXISTS ###

        else:
            raise FileNotFoundError(
                "The file was not found at the path {}.".format(full_path_criteria_csv)
            )

    ### THE FILENAME IS NOT DEFINED ###

    else:
        raise FileNotFoundError("csv_filename is not defined.")


#############################
### EXTRACT_SEARCH_FACETS ###
#############################


def extract_search_facets(csv_filename: str) -> dict[str, list[str]]:
    """Reads the provided csv file holding the search criteria and generates a dictionary of the search facets.

    Parameters
    ----------
    csv_filename : str

        Name of the csv file used to define the search facets.

    Returns
    -------
    search_dict : dict[str, list[str]]

        Dictionary of the different search facets given in the csv file.
    """

    ### GENERATE A DICTIONARY FROM THE PROVIDED SEARCH FACETS ###

    ## Read the file ##

    criteria = csv_to_dataframe(csv_filename)

    ## Get the list of the search facets ##

    provided_facets_list = list(criteria.keys())

    ## Generate a dictionary from the provided search facets ##

    search_dict = {
        facet_name: list(criteria[facet_name]) for facet_name in provided_facets_list
    }

    return search_dict


######################
### USED FOR TESTS ###
######################

if __name__ == "__main__":
    pass
