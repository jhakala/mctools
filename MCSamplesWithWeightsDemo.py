from calcweights import *

mcMap = MCSamplesWeightsMap(209, "qcdsamples.tx")
#mcMap.showMap()

mapArray = mcMap.getMap()
for mapRow in mapArray:
    print str(mapRow[1]) + ", " + str(mapRow[2])
