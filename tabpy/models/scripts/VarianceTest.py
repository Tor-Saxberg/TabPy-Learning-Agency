import scipy.stats as stats
from tabpy.models.utils import setup_utils


def variancetest(_arg1, _arg2, *_argN):
    """
    ANOVA is a statistical hypothesis test that is used to compare
    two or more group means for equality.For more information on
    the function and how to use it please refer to tabpy-tools.md
    """

    cols = [_arg1, _arg2] + list(_argN)
    for col in cols:
        if not isinstance(col[0], (int, float)):
            print("values must be numeric")
            raise ValueError
    _, p_value = stats.levene(_arg1, _arg2, *_argN)
    print("\n\np_value:", p_value, "\n\n")
    return p_value


if __name__ == "__main__":
    setup_utils.deploy_model("variancetest", variancetest, "Returns the p-value form an ANOVA test")
