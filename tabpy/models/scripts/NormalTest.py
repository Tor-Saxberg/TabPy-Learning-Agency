import scipy.stats as stats
from tabpy.models.utils import setup_utils


def normaltest(_arg1):
    """
    ANOVA is a statistical hypothesis test that is used to compare
    two or more group means for equality.For more information on
    the function and how to use it please refer to tabpy-tools.md
    """
    cols = [_arg1]
    for col in cols:
        if not isinstance(col[0], (int, float)):
            print("values must be numeric")
            raise ValueError
    _, p_value = stats.normaltest(_arg1)
    return p_value


if __name__ == "__main__":
    setup_utils.deploy_model("normaltest", normaltest, "Returns the p-value for scipy's normal test")
