# coding: UTF-8
import sys
bstack1l11l1_opy_ = sys.version_info [0] == 2
bstack11llll_opy_ = 2048
bstack1l111ll_opy_ = 7
def bstack1l11l11_opy_ (bstack1l11_opy_):
    global bstack1lll11_opy_
    bstack11l11ll_opy_ = ord (bstack1l11_opy_ [-1])
    bstack1ll11_opy_ = bstack1l11_opy_ [:-1]
    bstack1llllll_opy_ = bstack11l11ll_opy_ % len (bstack1ll11_opy_)
    bstack1l1l1l_opy_ = bstack1ll11_opy_ [:bstack1llllll_opy_] + bstack1ll11_opy_ [bstack1llllll_opy_:]
    if bstack1l11l1_opy_:
        bstack11ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11llll_opy_ - (bstack11ll1l1_opy_ + bstack11l11ll_opy_) % bstack1l111ll_opy_) for bstack11ll1l1_opy_, char in enumerate (bstack1l1l1l_opy_)])
    else:
        bstack11ll_opy_ = str () .join ([chr (ord (char) - bstack11llll_opy_ - (bstack11ll1l1_opy_ + bstack11l11ll_opy_) % bstack1l111ll_opy_) for bstack11ll1l1_opy_, char in enumerate (bstack1l1l1l_opy_)])
    return eval (bstack11ll_opy_)
from collections import defaultdict
from threading import Lock
from dataclasses import dataclass
import logging
import traceback
from typing import List, Dict, Any
import os
@dataclass
class bstack1l1ll1ll1l_opy_:
    sdk_version: str
    path_config: str
    path_project: str
    test_framework: str
    frameworks: List[str]
    framework_versions: Dict[str, str]
    bs_config: Dict[str, Any]
@dataclass
class bstack11l1ll1111_opy_:
    pass
class bstack1111l11ll_opy_:
    bstack1ll1l11ll1_opy_ = bstack1l11l11_opy_ (u"ࠨࡢࡰࡱࡷࡷࡹࡸࡡࡱࠤᅱ")
    CONNECT = bstack1l11l11_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࠣᅲ")
    bstack11ll1l1ll_opy_ = bstack1l11l11_opy_ (u"ࠣࡵ࡫ࡹࡹࡪ࡯ࡸࡰࠥᅳ")
    CONFIG = bstack1l11l11_opy_ (u"ࠤࡦࡳࡳ࡬ࡩࡨࠤᅴ")
    bstack1ll1l11l11l_opy_ = bstack1l11l11_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡹࠢᅵ")
    bstack1l11l1ll1_opy_ = bstack1l11l11_opy_ (u"ࠦࡪࡾࡩࡵࠤᅶ")
class bstack1ll1l11l1l1_opy_:
    bstack1ll1l11l111_opy_ = bstack1l11l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡸࡺࡡࡳࡶࡨࡨࠧᅷ")
    FINISHED = bstack1l11l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᅸ")
class bstack1ll1l11llll_opy_:
    bstack1ll1l11l111_opy_ = bstack1l11l11_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡶࡸࡦࡸࡴࡦࡦࠥᅹ")
    FINISHED = bstack1l11l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧᅺ")
class bstack1ll1l11lll1_opy_:
    bstack1ll1l11l111_opy_ = bstack1l11l11_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡸࡺࡡࡳࡶࡨࡨࠧᅻ")
    FINISHED = bstack1l11l11_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᅼ")
class bstack1ll1l11l1ll_opy_:
    bstack1ll1l11ll1l_opy_ = bstack1l11l11_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡦࡶࡪࡧࡴࡦࡦࠥᅽ")
class bstack1ll1l11ll11_opy_:
    _1ll1ll1l11l_opy_ = None
    def __new__(cls):
        if not cls._1ll1ll1l11l_opy_:
            cls._1ll1ll1l11l_opy_ = super(bstack1ll1l11ll11_opy_, cls).__new__(cls)
        return cls._1ll1ll1l11l_opy_
    def __init__(self):
        self._hooks = defaultdict(lambda: defaultdict(list))
        self._lock = Lock()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def clear(self):
        with self._lock:
            self._hooks = defaultdict(list)
    def register(self, event_name, callback):
        with self._lock:
            if not callable(callback):
                raise ValueError(bstack1l11l11_opy_ (u"ࠧࡉࡡ࡭࡮ࡥࡥࡨࡱࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡥࡤࡰࡱࡧࡢ࡭ࡧࠣࡪࡴࡸࠠࠣᅾ") + event_name)
            pid = os.getpid()
            self.logger.debug(bstack1l11l11_opy_ (u"ࠨࡒࡦࡩ࡬ࡷࡹ࡫ࡲࡪࡰࡪࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࠢࠪࡿࡪࡼࡥ࡯ࡶࡢࡲࡦࡳࡥࡾࠩࠣࡻ࡮ࡺࡨࠡࡲ࡬ࡨࠥࠨᅿ") + str(pid) + bstack1l11l11_opy_ (u"ࠢࠣᆀ"))
            self._hooks[event_name][pid].append(callback)
    def invoke(self, event_name, *args, **kwargs):
        with self._lock:
            pid = os.getpid()
            callbacks = self._hooks.get(event_name, {}).get(pid, [])
            if not callbacks:
                self.logger.warning(bstack1l11l11_opy_ (u"ࠣࡐࡲࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࡹࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࠣࠫࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠪࠤࡼ࡯ࡴࡩࠢࡳ࡭ࡩࠦࠢᆁ") + str(pid) + bstack1l11l11_opy_ (u"ࠤࠥᆂ"))
                return
            self.logger.debug(bstack1l11l11_opy_ (u"ࠥࡍࡳࡼ࡯࡬࡫ࡱ࡫ࠥࢁ࡬ࡦࡰࠫࡧࡦࡲ࡬ࡣࡣࡦ࡯ࡸ࠯ࡽࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࡶࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺࠠࠨࡽࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࢃࠧࠡࡹ࡬ࡸ࡭ࠦࡰࡪࡦࠣࠦᆃ") + str(pid) + bstack1l11l11_opy_ (u"ࠦࠧᆄ"))
            for callback in callbacks:
                try:
                    self.logger.debug(bstack1l11l11_opy_ (u"ࠧࡏ࡮ࡷࡱ࡮ࡩࡩࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࠤࠬࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠫࠥࡽࡩࡵࡪࠣࡴ࡮ࡪࠠࠣᆅ") + str(pid) + bstack1l11l11_opy_ (u"ࠨࠢᆆ"))
                    callback(event_name, *args, **kwargs)
                except Exception as e:
                    self.logger.error(bstack1l11l11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࠦࠧࡼࡧࡹࡩࡳࡺ࡟࡯ࡣࡰࡩࢂ࠭ࠠࡸ࡫ࡷ࡬ࠥࡶࡩࡥࠢࡾࡴ࡮ࡪࡽ࠻ࠢࠥᆇ") + str(e) + bstack1l11l11_opy_ (u"ࠣࠤᆈ"))
                    traceback.print_exc()
bstack11lllll111_opy_ = bstack1ll1l11ll11_opy_()