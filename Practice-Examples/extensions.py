#Program - 4  "extensions.py"

import itertools
import sys

w = {'UTSA':'www.utsa.edu','AMD':'www.amd.com','Intel':'www.intel.com','fake':'iamfake.net','google':'www.google.com','UTAustin':'www.utaustin.edu'}


n_w = {}
for key,val in w.items():
    n_w.update({key : val[-3:]})


new_dict = {}
for pair in n_w.items():
    if pair[1] not in new_dict.keys():
        new_dict[pair[1]] = []

    new_dict[pair[1]].append(pair[0])

print (new_dict)

