#mean median mode standard deviation
import numpy as np

scores = [72, 85, 90, 68, 75, 85, 92, 78, 85, 70,
          88, 76, 95, 82, 85, 73, 90, 67, 80, 85]
print("Scores:", scores)
print("Mean:", np.mean(scores))
print("Standard Deviation:", np.std(scores))
print("Median:", np.median(scores))
print("Mode:", np.bincount(scores).argmax())