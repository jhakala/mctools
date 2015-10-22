from calcweights import *

mcMap = MCSamplesWeightsMap(209, "demosamples.tx")
#mcMap.showMap()

mapArray = mcMap.getMap()
for mapRow in mapArray:
    print str(mapRow[1]) + ", " + str(mapRow[2])
