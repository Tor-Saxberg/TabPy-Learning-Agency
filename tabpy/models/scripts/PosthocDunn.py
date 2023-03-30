import scikit_posthocs as posthocs
from tabpy.models.utils import setup_utils


def posthoc_dunn(_arg1, _arg2, _arg3):
    """
    Dunn is a statistical hypothesis test that is used to compare
    two group means for equality.
    _arg1 must be a 2d array, 1d for each group compared.
    """
    groups = [_arg1, _arg2, _arg3]
    p_values = posthocs.posthoc_dunn(groups)
    a=p_values[1][2].tolist()
    b=p_values[1][3].tolist()
    c=p_values[2][3].tolist()
    return a,b,c,


if __name__ == "__main__":
    setup_utils.deploy_model("posthoc_dunn", posthoc_dunn, "Returns the adjusted p-value for the Dunn post hoc pairwise test")
