from pathlib import Path
import logging
import inspect
from uuid import uuid4


logger = logging.getLogger(__file__)
open_ = open


def open(file, mode='r', buffering=-1, encoding=None,
         errors=None, newline=None, closefd=True, opener=None):

    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    kwargs = {k: values[k] for k in args}

    if 'w' in mode:
        path = Path(file)
        kwargs['file'] = path
        if path.exists():
            newpath = path.parent / (path.name+'.'+uuid4().hex)
            logger.warning(
                f'Path {path} exists! Creating new filepath {newpath}.',
            )
            kwargs['file'] = newpath
            return open(**kwargs)
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            logger.warning(
                f'Directory path {path.parent} does not exist!'
                f' Creating new directory (including parents) {path.parent}.'
            )
        return open_(**kwargs)
    return open_(**kwargs)
