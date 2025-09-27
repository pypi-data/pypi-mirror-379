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
import os
import threading
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack1llll1llll1_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack1111111111_opy_:
    bstack11lll1llll1_opy_ = bstack1l1l11_opy_ (u"ࠤࡥࡩࡳࡩࡨ࡮ࡣࡵ࡯ࠧᗩ")
    context: bstack1llll1llll1_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack1llll1llll1_opy_):
        self.context = context
        self.data = dict({bstack1111111111_opy_.bstack11lll1llll1_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack1l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᗪ"), bstack1l1l11_opy_ (u"ࠫ࠵࠭ᗫ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1llll1lll11_opy_(self, target: object):
        return bstack1111111111_opy_.create_context(target) == self.context
    def bstack1l1llll1111_opy_(self, context: bstack1llll1llll1_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack11ll1l1ll1_opy_(self, key: str, value: timedelta):
        self.data[bstack1111111111_opy_.bstack11lll1llll1_opy_][key] += value
    def bstack1ll1ll111l1_opy_(self) -> dict:
        return self.data[bstack1111111111_opy_.bstack11lll1llll1_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack1llll1llll1_opy_(
            id=hash(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=target,
        )