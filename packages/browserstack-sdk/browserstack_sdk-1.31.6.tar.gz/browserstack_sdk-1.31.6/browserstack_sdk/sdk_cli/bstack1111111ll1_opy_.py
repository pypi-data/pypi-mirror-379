# coding: UTF-8
import sys
bstack1l111l1_opy_ = sys.version_info [0] == 2
bstack11l111l_opy_ = 2048
bstack111_opy_ = 7
def bstack1l1l11_opy_ (bstack1111ll1_opy_):
    global bstack1l1l11l_opy_
    bstack111ll_opy_ = ord (bstack1111ll1_opy_ [-1])
    bstack11l1l11_opy_ = bstack1111ll1_opy_ [:-1]
    bstack1l11_opy_ = bstack111ll_opy_ % len (bstack11l1l11_opy_)
    bstack1ll1l1l_opy_ = bstack11l1l11_opy_ [:bstack1l11_opy_] + bstack11l1l11_opy_ [bstack1l11_opy_:]
    if bstack1l111l1_opy_:
        bstack1ll11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111l_opy_ - (bstack111l1l1_opy_ + bstack111ll_opy_) % bstack111_opy_) for bstack111l1l1_opy_, char in enumerate (bstack1ll1l1l_opy_)])
    else:
        bstack1ll11l_opy_ = str () .join ([chr (ord (char) - bstack11l111l_opy_ - (bstack111l1l1_opy_ + bstack111ll_opy_) % bstack111_opy_) for bstack111l1l1_opy_, char in enumerate (bstack1ll1l1l_opy_)])
    return eval (bstack1ll11l_opy_)
import threading
import queue
from typing import Callable, Union
class bstack11111111ll_opy_:
    timeout: int
    bstack11111111l1_opy_: Union[None, Callable]
    bstack1111111l11_opy_: Union[None, Callable]
    def __init__(self, timeout=1, bstack1111111l1l_opy_=1, bstack11111111l1_opy_=None, bstack1111111l11_opy_=None):
        self.timeout = timeout
        self.bstack1111111l1l_opy_ = bstack1111111l1l_opy_
        self.bstack11111111l1_opy_ = bstack11111111l1_opy_
        self.bstack1111111l11_opy_ = bstack1111111l11_opy_
        self.queue = queue.Queue()
        self.bstack111111111l_opy_ = threading.Event()
        self.threads = []
    def enqueue(self, job: Callable):
        if not callable(job):
            raise ValueError(bstack1l1l11_opy_ (u"ࠦ࡮ࡴࡶࡢ࡮࡬ࡨࠥࡰ࡯ࡣ࠼ࠣࠦ႖") + type(job))
        self.queue.put(job)
    def start(self):
        if self.threads:
            return
        self.threads = [threading.Thread(target=self.worker, daemon=True) for _ in range(self.bstack1111111l1l_opy_)]
        for thread in self.threads:
            thread.start()
    def stop(self):
        if not self.threads:
            return
        if not self.queue.empty():
            self.queue.join()
        self.bstack111111111l_opy_.set()
        for _ in self.threads:
            self.queue.put(None)
        for thread in self.threads:
            thread.join()
        self.threads.clear()
    def worker(self):
        while not self.bstack111111111l_opy_.is_set():
            try:
                job = self.queue.get(block=True, timeout=self.timeout)
                if job is None:
                    break
                try:
                    job()
                except Exception as e:
                    if callable(self.bstack11111111l1_opy_):
                        self.bstack11111111l1_opy_(e, job)
                finally:
                    self.queue.task_done()
            except queue.Empty:
                pass
            except Exception as e:
                if callable(self.bstack1111111l11_opy_):
                    self.bstack1111111l11_opy_(e)