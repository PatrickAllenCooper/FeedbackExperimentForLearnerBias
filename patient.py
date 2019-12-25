#########################
# patient recieving
# some medication
# at a fixed dose
#########################

from scipy.stats import gamma
import seaborn as sns
import matplotlib.pyplot as plt


class Patient:

    def __init__(self):
        self.DRUG_IMMUNITY = "gamma"

    def define_meta_variables(self):
        data_gamma = gamma.rvs(a=5, size=10000)
        if self.DRUG_IMMUNITY is "gamma":
            ax = sns.distplot(data_gamma,
                              kde=True,
                              bins=100,
                              color='skyblue',
                              hist_kws={"linewidth": 15, 'alpha': 1})
            ax.set(xlabel='Gamma Distribution', ylabel='Frequency')

            plt.show()
