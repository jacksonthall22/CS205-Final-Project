"""
Put any helper/utility functions here that do not need to be attached to objects -JH

How To Use
----------
To use particular functions in another file (must be in the same directory, which they are 
for now (10/19/20)), use an `include` statement at the very top of the file (by convention)
to import the necessary functions separated by commas. Then you can use the functions
normally, as if they were written in the same file. 

Example
-------
    from utility import function_1, function_2

    x = function_1()
    y = function_2()
    etc.
    
"""

import re


def is_valid_filename(filename, valid_extensions):
    """
        Return True iff filename is a valid filename (using Windows standards) with no leading
        or trailing whitespace.
        
        valid_extensions: Iterable of all strings that are valid file extensions. Return False
                          if given extension is not in this list. Example:

                              valid_extensions = ['exe', 'txt', 'png', ...]
    """
    valid_windows_filename_regex = f'[^/\\*:?*<>|]*\.({"|".join(valid_extensions)})'

    # re.match produces a MatchObject if any matches are found, else None
    return re.match(valid_windows_filename_regex, filename) is not None
