import sys
import traceback
from queue import Empty, Queue, ShutDown
from threading import Thread
from typing import Callable

import pandas as pd

if "ipykernel" in sys.modules:
    from tqdm.notebook import tqdm
else:
    from tqdm import tqdm


class Run:
    def __init__(self, fn, inputs, *, concurrency):
        if not callable(fn):
            raise TypeError("fn must be a callable")
        self.fn = fn

        if isinstance(inputs, pd.Series):
            self.index = inputs.index
            self.inputs = inputs.tolist()
        elif isinstance(inputs, pd.DataFrame):
            self.index = inputs.index
            self.inputs = inputs.to_dict(orient="records")
        elif isinstance(inputs, pd.Index):
            self.index = inputs
            self.inputs = range(len(inputs))
        elif isinstance(inputs, list):
            self.index = None
            self.inputs = inputs
        else:
            raise TypeError("inputs must be a list, Series, DataFrame, or Index")
        self.total = len(self.inputs)

        if not isinstance(concurrency, int) or concurrency <= 0:
            raise ValueError("concurrency must be a positive integer")
        self.concurrency = concurrency

        self.q_input = Queue()
        self.q_output = Queue()

    def worker(self):
        while True:
            try:
                idx = self.q_input.get_nowait()
            except (Empty, ShutDown):
                break

            try:
                input_ = self.inputs[idx]
                result = self.fn(input_)
                self.q_output.put((idx, result, None))
            except Exception:
                err = traceback.format_exc()
                self.q_output.put((idx, None, err))
                break

    def start(self):
        # enqueue all inputs
        for idx in range(self.total):
            self.q_input.put(idx)

        # We manage threads manually instead of using ThreadPoolExecutor.
        # map() is often used in Jupyter notebooks. When users interrupt
        # the kernel, it sends exceptions to the main thread but doesn't
        # stop worker threads. Uncaught exceptions in the main thread
        # also don't stop worker threads.

        # start workers
        nworkers = min(self.concurrency, self.total)
        for _ in range(nworkers):
            Thread(target=self.worker).start()

        # collect results
        results = [None] * self.total
        try:
            for _ in tqdm(range(self.total), mininterval=0, maxinterval=0.1):
                idx, result, err = self.q_output.get()
                if err is not None:
                    raise RuntimeError(err)
                results[idx] = result
        finally:
            # when user presses ctrl+c or user interrupts the kernel, queue.get() raises InterruptedError
            self.q_input.shutdown(immediate=True)  # signal workers to stop

        if self.index is not None:
            return pd.Series(results, index=self.index)
        return results


def map2(
    fn: Callable,
    inputs: list | pd.Series | pd.DataFrame | pd.Index,
    *,
    concurrency: int = 1,
) -> list | pd.Series:
    """
    Apply fn to each item in inputs using threads and a progress bar.

    inputs may be a list, pandas Series, DataFrame, or Index.
    Preserves index for Series/DataFrame/Index. Returns a list, or a Series if
    inputs had an index. concurrency controls number of worker threads.
    """

    return Run(fn, inputs, concurrency=concurrency).start()
