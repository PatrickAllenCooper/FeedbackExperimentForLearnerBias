#########################
# patient recieving
# some medication
# at a fixed dose
#########################

from scipy.stats import gamma

class Patient:
    def __init__(self):
        self.DRUG_IMMUNITY = "gamma"


    def define_meta_variables(self):
        if self.DRUG_IMMUNITY is "gamma":
