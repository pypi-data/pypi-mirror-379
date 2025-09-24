from importlib import resources
from qtpy import QtWidgets, uic
from qtpy.QtCore import Slot
import numpy as np
import refnx.reflect._app


UI_LOCATION = resources.files(refnx.reflect._app) / "ui"


class OptimisationParameterView(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = uic.loadUi(UI_LOCATION / "optimisation.ui", self)

    def parameters(self, method):
        """
        Parameters
        ----------
        method : {'differential_evolution'}
            The fit method

        Returns
        -------
        opt_par : dict
            Options for fitting algorithm.
        """
        kws = {}
        if method == "DE":
            kws["strategy"] = self.ui.de_strategy.currentText()
            kws["maxiter"] = self.ui.de_maxiter.value()
            kws["popsize"] = self.ui.de_popsize.value()
            kws["tol"] = self.ui.de_tol.value()
            kws["atol"] = self.ui.de_atol.value()
            kws["init"] = self.ui.de_initialisation.currentText()
            kws["recombination"] = self.ui.de_recombination.value()
            mutation_lb = self.ui.de_mutation_lb.value()
            mutation_ub = self.ui.de_mutation_ub.value()
            kws["mutation"] = (
                min(mutation_lb, mutation_ub),
                max(mutation_lb, mutation_ub),
            )
            target = self.ui.de_target.currentText()
            if target == "log-posterior":
                target = "nlpost"
            else:
                target = "nll"
            kws["target"] = target
        elif method == "dual_annealing":
            kws["maxiter"] = self.ui.da_maxiter.value()
            kws["initial_temp"] = self.ui.da_initial_temp.value()
            kws["restart_temp_ratio"] = self.ui.da_restart_temp.value()
            kws["visit"] = self.ui.da_visit.value()
            kws["accept"] = self.ui.da_accept.value()
            kws["no_local_search"] = (
                self.ui.da_no_local_search.isChecked() is True
            )

            target = self.ui.de_target.currentText()
            if target == "log-posterior":
                target = "nlpost"
            else:
                target = "nll"
            kws["target"] = target
        elif method == "L-BFGS-B":
            kws["maxiter"] = self.ui.lbfgsb_maxiter.value()
            target = self.ui.lbfgsb_target.currentText()
            if target == "log-posterior":
                target = "nlpost"
            else:
                target = "nll"
            kws["target"] = target
        elif method == "SHGO":
            target = self.ui.shgo_target.currentText()
            kws["n"] = self.ui.shgo_n.value()
            kws["iters"] = self.ui.shgo_iters.value()
            if target == "log-posterior":
                target = "nlpost"
            else:
                target = "nll"
            kws["target"] = target

        return kws
