from collections import OrderedDict
import re


def default(x, fallback=None):
    return x if x is not None else fallback


def merge_dicts(ds):
    merged = OrderedDict()
    for d in ds:
        for k, v in d.items():
            merged[k] = v
    return merged


def to_snake_case(string):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()



# from pathlib import Path
#
# from .callbacks import History, Logger, CSVLogger, Checkpoint
# from .schedule import Scheduler, CosineAnnealingSchedule
#
#
# def wdefault_callbacks(workdir=None):
#     """Returns a list with commonly used callbacks."""
#
#     workdir = Path(workdir) if workdir else Path.cwd()
#     return [
#         History(),
#         Logger(),
#         CSVLogger(filename=workdir/'history.csv'),
#         Checkpoint(folder=workdir),
#         Scheduler(CosineAnnealingSchedule(), mode='batch')
#     ]