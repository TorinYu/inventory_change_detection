import numpy as np
import matplotlib.pyplot as plt
import math
from ratiosTest import ratios_unchanged, ratios_changed, changed_075, unchanged_075, changed_09, unchanged_09, changed, unchanged

num_bins = 10

def plot(changed, unchanged, bins, savepath):
    # width = 0.7 * (bins[1] - bins[0])
    # center = (bins[:-1] + bins[1:]) / 2
    plt.hist(changed, bins, alpha=0.5, label='changed')
    plt.hist(unchanged, bins, alpha=0.5, label='unchanged')
    plt.legend(loc='upper right')
    plt.savefig(savepath)
    plt.clf()

def calc_score_table(ratios_changed, ratios_unchanged):
    interval_min = min(min(ratios_changed), min(ratios_unchanged))
    interval_max = max(max(ratios_changed), max(ratios_unchanged))
    interval = (interval_min, interval_max)

    hist_changed, bins = np.histogram(ratios_changed, bins=num_bins, range=interval)
    hist_unchanged, bins = np.histogram(ratios_unchanged, bins=num_bins, range=interval)

    def cal_score(i):
        if hist_changed[i] == 0 and hist_unchanged[i] == 0:
            if i == 0:
                return 100
            if i == len(bins) - 1:
                return 0
            return (cal_score(i-1)+cal_score(i+1))/2
        return int(round(float(hist_changed[i])/float((hist_changed[i]+hist_unchanged[i]))*100))
    
    # bins is the end points of the intervals!
    scores = [-1] * (len(bins)-1)
    for i in range(len(bins)-1):
        scores[i] = cal_score(i)

    # make sure score is non-increasing
    for i in range(len(bins)-2):
        if scores[i+1] > scores[i]:
            if i == 0:
                scores[i] = (100 + scores[i])/2
            else:
                scores[i] = (scores[i+1] + scores[i-1])/2
    return scores, bins

def get_score(ratio, scores, bins):
    index = int(math.floor((ratio - bins[0])/(bins[1]-bins[0])))
    return scores[index]

if __name__ == "__main__":
    scores, bins = calc_score_table(ratios_changed, ratios_unchanged)
    print scores
    print bins
    print get_score(0.01, scores, bins)
    print get_score(0.11, scores, bins)
    print get_score(0.21, scores, bins)
    print get_score(0.31, scores, bins)
    print get_score(0.41, scores, bins)
    #plot(ratios_changed, ratios_unchanged, bins, "plot.png")
    #plot(changed_075, unchanged_075, bins, "plot075.png")
    #plot(changed_09, unchanged_09, bins, "plot090.png")
    plot(changed, unchanged, bins, "plot.png")
