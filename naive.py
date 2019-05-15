from lev_ratio import *
import time
data = open("./data/google-10000-english.txt", "r")



start = time.time()
for line in data.readlines():
    words = line.split(" ")
    for i in range(len(words)):
        x = lev_ratio_and_dist(words[i], "wanger", True)
        if x[0] <= 3:
            print(words[i])
end = time.time()

print(end - start)