# Filename: by_election.py
# Author: Koh Hui Qi
# Date Created: 27 Jan 2013
# Description: Display election result in specified format

import datetime

# read from VOTES.TXT
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

    # calculate percentage
    ppap = (pap / total) * 100
    pwp = (wp / total) * 100
    prp = (rp / total) * 100
    psda = (sda / total) * 100
    pinvalid = (invalid / total) * 100


except IOError:
    print("Error! Cannot read file VOTES.TXT")

# output to RESULTS.TXT
try:
    # open file
    outfile = open("RESULTS.TXT", "w")
    
    date = datetime.date.today()

    # format time
    time = datetime.datetime.now()
    time = time.strftime("%H:%M")
    if int(time[0:2]) > 12:
        time = str(int(time[0:2]) - 12) + time[2:] + " PM"
    else:
        time = str(time) + " AM"

    # determine winner
    array = [pap, wp, rp, sda]
    if max(array) == pap:
        winner = "PAP"
    elif max(array) == wp:
        winner = "WP"
    elif max(array) == rp:
        winner = "RP"
    else:
        winner = "SDA"

    # write to output file
    outfile.write("DATE: " + date.strftime("%d/%m/%Y") + " "*19)
    outfile.write("TIME: " + format(time))
    outfile.write("\n")
    outfile.write("RESULTS OF THE 2013 PUNGGOL EAST SMC BY ELECTION" + "\n")
    outfile.write("WARD                PARTY     #VOTES    %VOTES" + "\n")
    outfile.write("--------------------------------------------------" + "\n")
    outfile.write("PUNGGOL EAST SMC    PAP        " + "{0:>5s}".format(str(pap))
                  + "    " + "{0:.2f}".format(ppap) + "%" + "\n")
    outfile.write("                    RP         " + "{0:>5s}".format(str(rp))
                  + "    " + "{0:.2f}".format(prp) + "%" + "\n")
    outfile.write("                    SDA        " + "{0:>5s}".format(str(sda))
                  + "    " + "{0:.2f}".format(psda) + "%" + "\n")
    outfile.write("                    WP         " + "{0:>5s}".format(str(wp))
                  + "    " + "{0:.2f}".format(pwp) + "%" + "\n")
    outfile.write("--------------------------------------------------" + "\n")
    outfile.write("WINNER: " + winner + "\n")
    outfile.write("TOTAL VOTES: " + str(total) + "\n")
    outfile.write("#SPOILT VOTES: " + str(invalid) + "\n")
    outfile.write("%SPOILT VOTES: " + str(pinvalid))


    # close file
    outfile.close()

except IOError:
    print("Error! Cannot write file RESULTS.TXT")
