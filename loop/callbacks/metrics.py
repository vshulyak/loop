from collections import defaultdict

from .base import Callback
from ..metrics import accuracy


class Accuracy(Callback):

    def training_started(self, **kwargs):
        self._init()

    def epoch_started(self, **kwargs):
        self._init()

    def batch_ended(self, phase, output, target, **kwargs):
        acc = accuracy(output, target).detach().item()
        self.counts[phase.name] += target.size(0)
        self.values[phase.name] += target.size(0) * acc

    def epoch_ended(self, phases, **kwargs):
        for phase in phases:
            metric = self.values[phase.name] / self.counts[phase.name]
            phase.update_metric('accuracy', metric)

    def _init(self):
        self.values = defaultdict(int)
        self.counts = defaultdict(int)
