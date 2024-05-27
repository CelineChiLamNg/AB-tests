import numpy as np
import scipy.stats as stats

def ci_mean_analytical(data, confidence=0.95):
    mean = np.mean(data)
    sem = stats.sem(data)
    margin = sem * stats.t.ppf((1 + confidence) / 2., len(data)-1)
    return (mean, mean - margin, mean + margin)


def ci_bootstrap(data, num_boots=1000, confidence=0.95):
    boots = [np.mean(np.random.choice(data, replace=True, size=len(data))) for _ in range(num_boots)]
    mean = np.mean(boots)
    lower, upper = np.percentile(boots, [(1-confidence)/2*100, (1 + confidence)/2*100])
    return (mean, lower, upper)


