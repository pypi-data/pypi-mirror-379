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
from collections import deque
from bstack_utils.constants import *
class bstack1lll1111l1_opy_:
    def __init__(self):
        self._111111ll111_opy_ = deque()
        self._111111ll1ll_opy_ = {}
        self._111111l1ll1_opy_ = False
        self._lock = threading.RLock()
    def bstack111111lll11_opy_(self, test_name, bstack111111ll1l1_opy_):
        with self._lock:
            bstack111111l11ll_opy_ = self._111111ll1ll_opy_.get(test_name, {})
            return bstack111111l11ll_opy_.get(bstack111111ll1l1_opy_, 0)
    def bstack111111l111l_opy_(self, test_name, bstack111111ll1l1_opy_):
        with self._lock:
            bstack111111l11l1_opy_ = self.bstack111111lll11_opy_(test_name, bstack111111ll1l1_opy_)
            self.bstack111111lll1l_opy_(test_name, bstack111111ll1l1_opy_)
            return bstack111111l11l1_opy_
    def bstack111111lll1l_opy_(self, test_name, bstack111111ll1l1_opy_):
        with self._lock:
            if test_name not in self._111111ll1ll_opy_:
                self._111111ll1ll_opy_[test_name] = {}
            bstack111111l11ll_opy_ = self._111111ll1ll_opy_[test_name]
            bstack111111l11l1_opy_ = bstack111111l11ll_opy_.get(bstack111111ll1l1_opy_, 0)
            bstack111111l11ll_opy_[bstack111111ll1l1_opy_] = bstack111111l11l1_opy_ + 1
    def bstack1l11l1ll11_opy_(self, bstack111111l1lll_opy_, bstack111111l1l11_opy_):
        bstack111111l1l1l_opy_ = self.bstack111111l111l_opy_(bstack111111l1lll_opy_, bstack111111l1l11_opy_)
        event_name = bstack11l1lll11l1_opy_[bstack111111l1l11_opy_]
        bstack1l1l11lll11_opy_ = bstack1l1l11_opy_ (u"ࠥࡿࢂ࠳ࡻࡾ࠯ࡾࢁࠧἨ").format(bstack111111l1lll_opy_, event_name, bstack111111l1l1l_opy_)
        with self._lock:
            self._111111ll111_opy_.append(bstack1l1l11lll11_opy_)
    def bstack11llllll_opy_(self):
        with self._lock:
            return len(self._111111ll111_opy_) == 0
    def bstack1l111lll1_opy_(self):
        with self._lock:
            if self._111111ll111_opy_:
                bstack111111ll11l_opy_ = self._111111ll111_opy_.popleft()
                return bstack111111ll11l_opy_
            return None
    def capturing(self):
        with self._lock:
            return self._111111l1ll1_opy_
    def bstack111llll11_opy_(self):
        with self._lock:
            self._111111l1ll1_opy_ = True
    def bstack1l11ll1l1_opy_(self):
        with self._lock:
            self._111111l1ll1_opy_ = False