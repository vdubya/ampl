from dataclasses import dataclass

from ampl.state import State
from ampl.decision_tree.model_build import PipelineModelBuild
from ampl.decision_tree.model_ensemble import PipelineModelEnsemble
from ampl.decision_tree.model_eval import PipelineModelEval
from ampl.decision_tree.optuna import PipelineOptuna



@dataclass
class Pipeline():
    """
    Pipeline class which runs PipelineSteps.run()
    """
    state: State
    optuna: PipelineOptuna = None
    build: PipelineModelBuild = None
    eval: PipelineModelEval = None
    ensemble: PipelineModelEnsemble = None

    def run_all(self):
        if self.optuna:
            self.optuna.run()
        if self.build:
            self.build.run()
        if self.eval:
            self.eval.run()
        if self.ensemble:
            self.ensemble.run()
