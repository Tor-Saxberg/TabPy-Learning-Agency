import scipy.stats as stats
from tabpy.models.utils import setup_utils


def kruskal(_arg1, _arg2, *_argN):
    """
    Kruskal is a statistical hypothesis test that is used to compare
    two or more group means for equality.For more information on
    the function and how to use it please refer to tabpy-tools.md
    """

    cols = [_arg1, _arg2] + list(_argN)
    for col in cols:
        if not isinstance(col[0], (int, float)):
            print("values must be numeric")
            raise ValueError
    _, p_value = stats.kruskal(_arg1, _arg2, *_argN)
    return p_value


if __name__ == "__main__":
    setup_utils.deploy_model("kruskal", kruskal, "Returns the p-value form the kruskal test")
