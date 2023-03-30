import scipy.stats as stats
from tabpy.models.utils import setup_utils


def anova(_arg1, _arg2, *_argN):
    if _arg1[1] == "constr":
        _arg3 = _argN[0]
        labels = list(set(_arg3))
        groups = [ [] for _ in range(len(labels)) ]
        for i in range(len(_arg2)):
            label_index = labels.index(_arg3[i])
            groups[label_index].append(_arg2[i])
        #print("_arg1: \n\n",len(_arg1))
        #print("labels: \n\n",labels)
        #print("groups: \n\n ",[len(x) for x in groups])
        _, p_value = stats.f_oneway(*groups)
        print("\n\n", p_value, "\n\n")
        return p_value

    elif len(set(_arg2)) == 2:
        # each sample in _arg1 needs to have a corresponding classification
        # in _arg2
        if not (len(_arg1) == len(_arg2)):
            raise ValueError
        class1, class2 = set(_arg2)
        sample1 = []
        sample2 = []
        for i in range(len(_arg1)):
            if _arg2[i] == class1:
                sample1.append(_arg1[i])
            else:
                sample2.append(_arg1[i])
        test_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)
        return p_value

    else:
        print("\n\n", "simple anova", "\n\n")
        print(_arg1)
        cols = [_arg1, _arg2] + list(_argN)
        for col in cols:
            if not isinstance(col[0], (int, float)):
                print("values must be numeric")
                raise ValueError
        _, p_value = stats.f_oneway(_arg1, _arg2, *_argN)
        return p_value


if __name__ == "__main__":
    setup_utils.deploy_model("anova", anova, "Returns the p-value form an ANOVA test")
