# Filename: generate_votes.py
# Author: Koh Hui Qi
# Date Created: 24 Jan 2013
# Description: Generate a suitable delimited file VOTES.DAT containing a 
#              reasonable number of records

import random

try:
    # open VOTES.DAT file
    dfile = open("VOTES.TXT", "w")

    for i in range(1,34001):
        v = random.randint(1, 102)
        # PAP vote
        if v <= 52:
            dfile.write("PAP,1")
            dfile.write("\n")
        # WP vote
        if (52 < v <94):
            dfile.write("WP,1")
            dfile.write("\n")
        # SDA vote
        if (93 < v < 99):
            dfile.write("SDA,1")
            dfile.write("\n")
        # RP vote
        if (98 < v < 101):
            dfile.write("RP,1")
            dfile.write("\n")
        # invalid vote
        elif v > 100:
            a = random.randint(1,100)
            # PAP vote
            if a <= 52:
                dfile.write("PAP,0")
                dfile.write("\n")
            # WP vote
            if (52 < a <94):
                dfile.write("WP,0")
                dfile.write("\n")
            # SDA vote
            if (93 < a < 99):
                dfile.write("SDA,0")
                dfile.write("\n")
            # RP vote
            elif (98 < a < 101):
                dfile.write("RP,0")
                dfile.write("\n")

    # close VOTES.DAT file
    dfile.close()
    
except IOError:
    print("Error. Cannot open VOTES.TXT")
