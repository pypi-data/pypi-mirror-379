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
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllll11111_opy_ import (
    bstack1llllll11ll_opy_,
    bstack1llll1llll1_opy_,
    bstack1llll1lllll_opy_,
    bstack1llllll1lll_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1llll1l111l_opy_(bstack1llllll11ll_opy_):
    bstack1l11l111l1l_opy_ = bstack1l11l11_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠣᐚ")
    bstack1l1l11l11l1_opy_ = bstack1l11l11_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤᐛ")
    bstack1l1l111l1ll_opy_ = bstack1l11l11_opy_ (u"ࠥ࡬ࡺࡨ࡟ࡶࡴ࡯ࠦᐜ")
    bstack1l1l11l1ll1_opy_ = bstack1l11l11_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᐝ")
    bstack1l11l111ll1_opy_ = bstack1l11l11_opy_ (u"ࠧࡽ࠳ࡤࡧࡻࡩࡨࡻࡴࡦࡵࡦࡶ࡮ࡶࡴࠣᐞ")
    bstack1l11l111lll_opy_ = bstack1l11l11_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࡣࡶࡽࡳࡩࠢᐟ")
    NAME = bstack1l11l11_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦᐠ")
    bstack1l11l11l1ll_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lll1l11ll1_opy_: Any
    bstack1l11l1111ll_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack1l11l11_opy_ (u"ࠣ࡮ࡤࡹࡳࡩࡨࠣᐡ"), bstack1l11l11_opy_ (u"ࠤࡦࡳࡳࡴࡥࡤࡶࠥᐢ"), bstack1l11l11_opy_ (u"ࠥࡲࡪࡽ࡟ࡱࡣࡪࡩࠧᐣ"), bstack1l11l11_opy_ (u"ࠦࡨࡲ࡯ࡴࡧࠥᐤ"), bstack1l11l11_opy_ (u"ࠧࡪࡩࡴࡲࡤࡸࡨ࡮ࠢᐥ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1llllll11l1_opy_(methods)
    def bstack1lllll11l1l_opy_(self, instance: bstack1llll1llll1_opy_, method_name: str, bstack1llllllll1l_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1lllll1l1ll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llllll1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1llllllll11_opy_, bstack1l11l1111l1_opy_ = bstack1lllllll1l1_opy_
        bstack1l11l111l11_opy_ = bstack1llll1l111l_opy_.bstack1l11l11l11l_opy_(bstack1lllllll1l1_opy_)
        if bstack1l11l111l11_opy_ in bstack1llll1l111l_opy_.bstack1l11l11l1ll_opy_:
            bstack1l11l11l1l1_opy_ = None
            for callback in bstack1llll1l111l_opy_.bstack1l11l11l1ll_opy_[bstack1l11l111l11_opy_]:
                try:
                    bstack1l11l11l111_opy_ = callback(self, target, exec, bstack1lllllll1l1_opy_, result, *args, **kwargs)
                    if bstack1l11l11l1l1_opy_ == None:
                        bstack1l11l11l1l1_opy_ = bstack1l11l11l111_opy_
                except Exception as e:
                    self.logger.error(bstack1l11l11_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࠦᐦ") + str(e) + bstack1l11l11_opy_ (u"ࠢࠣᐧ"))
                    traceback.print_exc()
            if bstack1l11l1111l1_opy_ == bstack1llllll1lll_opy_.PRE and callable(bstack1l11l11l1l1_opy_):
                return bstack1l11l11l1l1_opy_
            elif bstack1l11l1111l1_opy_ == bstack1llllll1lll_opy_.POST and bstack1l11l11l1l1_opy_:
                return bstack1l11l11l1l1_opy_
    def bstack1lllll11ll1_opy_(
        self, method_name, previous_state: bstack1llll1lllll_opy_, *args, **kwargs
    ) -> bstack1llll1lllll_opy_:
        if method_name == bstack1l11l11_opy_ (u"ࠨ࡮ࡤࡹࡳࡩࡨࠨᐨ") or method_name == bstack1l11l11_opy_ (u"ࠩࡦࡳࡳࡴࡥࡤࡶࠪᐩ") or method_name == bstack1l11l11_opy_ (u"ࠪࡲࡪࡽ࡟ࡱࡣࡪࡩࠬᐪ"):
            return bstack1llll1lllll_opy_.bstack1llll1lll1l_opy_
        if method_name == bstack1l11l11_opy_ (u"ࠫࡩ࡯ࡳࡱࡣࡷࡧ࡭࠭ᐫ"):
            return bstack1llll1lllll_opy_.bstack1lllllllll1_opy_
        if method_name == bstack1l11l11_opy_ (u"ࠬࡩ࡬ࡰࡵࡨࠫᐬ"):
            return bstack1llll1lllll_opy_.QUIT
        return bstack1llll1lllll_opy_.NONE
    @staticmethod
    def bstack1l11l11l11l_opy_(bstack1lllllll1l1_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llllll1lll_opy_]):
        return bstack1l11l11_opy_ (u"ࠨ࠺ࠣᐭ").join((bstack1llll1lllll_opy_(bstack1lllllll1l1_opy_[0]).name, bstack1llllll1lll_opy_(bstack1lllllll1l1_opy_[1]).name))
    @staticmethod
    def bstack1ll111l11ll_opy_(bstack1lllllll1l1_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llllll1lll_opy_], callback: Callable):
        bstack1l11l111l11_opy_ = bstack1llll1l111l_opy_.bstack1l11l11l11l_opy_(bstack1lllllll1l1_opy_)
        if not bstack1l11l111l11_opy_ in bstack1llll1l111l_opy_.bstack1l11l11l1ll_opy_:
            bstack1llll1l111l_opy_.bstack1l11l11l1ll_opy_[bstack1l11l111l11_opy_] = []
        bstack1llll1l111l_opy_.bstack1l11l11l1ll_opy_[bstack1l11l111l11_opy_].append(callback)
    @staticmethod
    def bstack1ll11l111l1_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1ll111lll1l_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1ll1l111ll1_opy_(instance: bstack1llll1llll1_opy_, default_value=None):
        return bstack1llllll11ll_opy_.bstack1llllll1l1l_opy_(instance, bstack1llll1l111l_opy_.bstack1l1l11l1ll1_opy_, default_value)
    @staticmethod
    def bstack1l1lllll11l_opy_(instance: bstack1llll1llll1_opy_) -> bool:
        return True
    @staticmethod
    def bstack1ll11l1111l_opy_(instance: bstack1llll1llll1_opy_, default_value=None):
        return bstack1llllll11ll_opy_.bstack1llllll1l1l_opy_(instance, bstack1llll1l111l_opy_.bstack1l1l111l1ll_opy_, default_value)
    @staticmethod
    def bstack1ll1l111111_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1ll11llll1l_opy_(method_name: str, *args):
        if not bstack1llll1l111l_opy_.bstack1ll11l111l1_opy_(method_name):
            return False
        if not bstack1llll1l111l_opy_.bstack1l11l111ll1_opy_ in bstack1llll1l111l_opy_.bstack1l11ll111ll_opy_(*args):
            return False
        bstack1ll111111ll_opy_ = bstack1llll1l111l_opy_.bstack1l1llllll1l_opy_(*args)
        return bstack1ll111111ll_opy_ and bstack1l11l11_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᐮ") in bstack1ll111111ll_opy_ and bstack1l11l11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᐯ") in bstack1ll111111ll_opy_[bstack1l11l11_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤᐰ")]
    @staticmethod
    def bstack1ll111llll1_opy_(method_name: str, *args):
        if not bstack1llll1l111l_opy_.bstack1ll11l111l1_opy_(method_name):
            return False
        if not bstack1llll1l111l_opy_.bstack1l11l111ll1_opy_ in bstack1llll1l111l_opy_.bstack1l11ll111ll_opy_(*args):
            return False
        bstack1ll111111ll_opy_ = bstack1llll1l111l_opy_.bstack1l1llllll1l_opy_(*args)
        return (
            bstack1ll111111ll_opy_
            and bstack1l11l11_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥᐱ") in bstack1ll111111ll_opy_
            and bstack1l11l11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡥࡵ࡭ࡵࡺࠢᐲ") in bstack1ll111111ll_opy_[bstack1l11l11_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᐳ")]
        )
    @staticmethod
    def bstack1l11ll111ll_opy_(*args):
        return str(bstack1llll1l111l_opy_.bstack1ll1l111111_opy_(*args)).lower()