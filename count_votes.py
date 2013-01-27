# Filename: count_votes.py
# Author: Koh Hui Qi
# Date created: 24 Jan 2013
# Description: Count the number and percentage of votes garnered by each party
#              in VOTES.TXT

try:
    dfile = open("VOTES.TXT", 'r')
    lines = dfile.readlines()
    
    # initiate vote counts for each party
    pap = 0
    wp = 0
    rp = 0
    sda = 0
    invalid = 0

    # start counting votes
    for line in lines:
        if line == "PAP,1\n":
            pap = pap + 1
        elif line == "WP,1\n":
            wp = wp + 1
        elif line == "RP,1\n":
            rp = rp + 1
        elif line == "SDA,1\n":
            sda = sda + 1
        else:
            invalid = invalid + 1

    # calculate total number of votes
    total = pap + wp + rp + sda + invalid
    print(total)

    # calculate percentage
    ppap = (pap / total) * 100
    pwp = (wp / total) * 100
    prp = (rp / total) * 100
    psda = (sda / total) * 100
    pinvalid = (invalid / total) * 100

    # print results
    print("PAP:", pap,"votes,", ppap, "%")
    print("WP:", wp,"votes,", pwp, "%")
    print("RP:", rp,"votes,", prp, "%")
    print("SDA:", sda,"votes,", psda, "%")
    print("Invalid votes:", invalid,"votes,", pinvalid, "%")




except IOError:
    print("Error! Cannot read file VOTES.TXT")
