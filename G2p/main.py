from g2p_en import G2p

texts = ["In our continued efforts to make findings about the amazing and fulfilled lifetime of Austrian Nigerian artist , Susan Wenger who abandoned the comfort of family and luxury of home country to live in a developing town to graciously make Osun , the goddess of fertility a cynosure of all eyes , WITHIN NIGERIA extended its wings of investigation to examine and expose the meaningful contributions of the Osun White Priestess to the upliftment of Osun sacred grove among others . Osun Osogbo Sacred Grove had greatly suffered depreciation owing to commercial interests and termites destroying shrine facilities , sacred sculptures and carvings . The sacred grove was gradually diminishing in values and on its way to extinction following the personalities and characters of early custodians who were major driven by interests which affected the sacred grove . But Austrian Nigerian artist teamed up with the Public Works Department and many local artists in the town to eradicate the termites and redevelop the carvings and buildings within the shrine using both woods and cements. " # number -> spell-out
        #  "popular pets, e.g. cats and dogs", # e.g. -> for example
        #  "I refuse to collect the refuse around here.", # homograph
        #  "I'm an activationist."] # newly coined word
        ]
g2p = G2p()
for text in texts:
    out = g2p(text)
    print(out)