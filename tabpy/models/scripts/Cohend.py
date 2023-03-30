import scipy.stats as stats
from statistics import mean, stdev
from math import sqrt
from tabpy.models.utils import setup_utils

def cohend(_arg1, _arg2, *_argN):
    labels = list(set(_arg2))
    labels.sort()
    print("_arg1: ",len(_arg1))
    print("_arg2: ",len(_arg2))
    print("\n\nlabels: ",labels)
    groups = [ [] for _ in range(len(labels)) ]
    for i in range(len(_arg1)):
        label_index = labels.index(_arg2[i])
        groups[label_index].append(_arg1[i])

    print("\n\ngroups: ",[len(x) for x in groups])

    n1,n2 = len(groups[0]), len(groups[1])
    u1,u2 = mean(groups[0]), mean(groups[1])
    sd1,sd2 = stdev(groups[0]), stdev(groups[1])
    s = sqrt( ((n1 - 1)*sd1 + (n2 - 1) * sd2) / (n1 + n2) )
    d = (u1 - u2) / s
    print("\n\n", d, "\n\n")
    return d

if __name__ == "__main__":
    setup_utils.deploy_model("cohend", cohend, "Returns the effect size b/t two groups")
