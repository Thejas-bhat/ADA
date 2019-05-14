# ADA
Design and analysis of algorithms project

lev_ratio file uses a 2D array for the edit matrix of predefined size.

fuzz_complete file dynamically computes and allocates each row of the matrix with levenshtein distance of each letter of the word to be searched.

Damerau-levenshtein does the same but also takes into account transpositions

ui.py and ui_new.py are both terminal interfaces that function as a very rudimentary autocorrect/autocomplete system. (type start after the (cmd) prompt to start, and then enter your word and press tab to see a list of corrections. if there is only one possible correction, it is autocorrected to that)
