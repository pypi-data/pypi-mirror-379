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
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1lllll11111_opy_ import bstack1llll1llll1_opy_, bstack1llll1lllll_opy_, bstack1llllll1lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll1l11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1ll1_opy_ import bstack1ll1ll1llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll111l11l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11ll11_opy_, bstack1ll1lllll11_opy_, bstack1ll1ll11111_opy_, bstack1lll1llll1l_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1l1l1lllll1_opy_, bstack1l1ll11111l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l1ll1l11ll_opy_ = [bstack1l11l11_opy_ (u"ࠥࡲࡦࡳࡥࠣባ"), bstack1l11l11_opy_ (u"ࠦࡵࡧࡲࡦࡰࡷࠦቤ"), bstack1l11l11_opy_ (u"ࠧࡩ࡯࡯ࡨ࡬࡫ࠧብ"), bstack1l11l11_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴࠢቦ"), bstack1l11l11_opy_ (u"ࠢࡱࡣࡷ࡬ࠧቧ")]
bstack1l1ll11llll_opy_ = bstack1l1ll11111l_opy_()
bstack1l1ll11l1ll_opy_ = bstack1l11l11_opy_ (u"ࠣࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠭ࠣቨ")
bstack1l1l1llll11_opy_ = {
    bstack1l11l11_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡌࡸࡪࡳࠢቩ"): bstack1l1ll1l11ll_opy_,
    bstack1l11l11_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡔࡦࡩ࡫ࡢࡩࡨࠦቪ"): bstack1l1ll1l11ll_opy_,
    bstack1l11l11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡒࡵࡤࡶ࡮ࡨࠦቫ"): bstack1l1ll1l11ll_opy_,
    bstack1l11l11_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡉ࡬ࡢࡵࡶࠦቬ"): bstack1l1ll1l11ll_opy_,
    bstack1l11l11_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡆࡶࡰࡦࡸ࡮ࡵ࡮ࠣቭ"): bstack1l1ll1l11ll_opy_
    + [
        bstack1l11l11_opy_ (u"ࠢࡰࡴ࡬࡫࡮ࡴࡡ࡭ࡰࡤࡱࡪࠨቮ"),
        bstack1l11l11_opy_ (u"ࠣ࡭ࡨࡽࡼࡵࡲࡥࡵࠥቯ"),
        bstack1l11l11_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧ࡬ࡲ࡫ࡵࠢተ"),
        bstack1l11l11_opy_ (u"ࠥ࡯ࡪࡿࡷࡰࡴࡧࡷࠧቱ"),
        bstack1l11l11_opy_ (u"ࠦࡨࡧ࡬࡭ࡵࡳࡩࡨࠨቲ"),
        bstack1l11l11_opy_ (u"ࠧࡩࡡ࡭࡮ࡲࡦ࡯ࠨታ"),
        bstack1l11l11_opy_ (u"ࠨࡳࡵࡣࡵࡸࠧቴ"),
        bstack1l11l11_opy_ (u"ࠢࡴࡶࡲࡴࠧት"),
        bstack1l11l11_opy_ (u"ࠣࡦࡸࡶࡦࡺࡩࡰࡰࠥቶ"),
        bstack1l11l11_opy_ (u"ࠤࡺ࡬ࡪࡴࠢቷ"),
    ],
    bstack1l11l11_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡱࡦ࡯࡮࠯ࡕࡨࡷࡸ࡯࡯࡯ࠤቸ"): [bstack1l11l11_opy_ (u"ࠦࡸࡺࡡࡳࡶࡳࡥࡹ࡮ࠢቹ"), bstack1l11l11_opy_ (u"ࠧࡺࡥࡴࡶࡶࡪࡦ࡯࡬ࡦࡦࠥቺ"), bstack1l11l11_opy_ (u"ࠨࡴࡦࡵࡷࡷࡨࡵ࡬࡭ࡧࡦࡸࡪࡪࠢቻ"), bstack1l11l11_opy_ (u"ࠢࡪࡶࡨࡱࡸࠨቼ")],
    bstack1l11l11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡥࡲࡲ࡫࡯ࡧ࠯ࡅࡲࡲ࡫࡯ࡧࠣች"): [bstack1l11l11_opy_ (u"ࠤ࡬ࡲࡻࡵࡣࡢࡶ࡬ࡳࡳࡥࡰࡢࡴࡤࡱࡸࠨቾ"), bstack1l11l11_opy_ (u"ࠥࡥࡷ࡭ࡳࠣቿ")],
    bstack1l11l11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲࡫࡯ࡸࡵࡷࡵࡩࡸ࠴ࡆࡪࡺࡷࡹࡷ࡫ࡄࡦࡨࠥኀ"): [bstack1l11l11_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦኁ"), bstack1l11l11_opy_ (u"ࠨࡡࡳࡩࡱࡥࡲ࡫ࠢኂ"), bstack1l11l11_opy_ (u"ࠢࡧࡷࡱࡧࠧኃ"), bstack1l11l11_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣኄ"), bstack1l11l11_opy_ (u"ࠤࡸࡲ࡮ࡺࡴࡦࡵࡷࠦኅ"), bstack1l11l11_opy_ (u"ࠥ࡭ࡩࡹࠢኆ")],
    bstack1l11l11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲࡫࡯ࡸࡵࡷࡵࡩࡸ࠴ࡓࡶࡤࡕࡩࡶࡻࡥࡴࡶࠥኇ"): [bstack1l11l11_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࠥኈ"), bstack1l11l11_opy_ (u"ࠨࡰࡢࡴࡤࡱࠧ኉"), bstack1l11l11_opy_ (u"ࠢࡱࡣࡵࡥࡲࡥࡩ࡯ࡦࡨࡼࠧኊ")],
    bstack1l11l11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡴࡸࡲࡳ࡫ࡲ࠯ࡅࡤࡰࡱࡏ࡮ࡧࡱࠥኋ"): [bstack1l11l11_opy_ (u"ࠤࡺ࡬ࡪࡴࠢኌ"), bstack1l11l11_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࠥኍ")],
    bstack1l11l11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡲ࡬࠰ࡶࡸࡷࡻࡣࡵࡷࡵࡩࡸ࠴ࡎࡰࡦࡨࡏࡪࡿࡷࡰࡴࡧࡷࠧ኎"): [bstack1l11l11_opy_ (u"ࠧࡴ࡯ࡥࡧࠥ኏"), bstack1l11l11_opy_ (u"ࠨࡰࡢࡴࡨࡲࡹࠨነ")],
    bstack1l11l11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮࡮ࡣࡵ࡯࠳ࡹࡴࡳࡷࡦࡸࡺࡸࡥࡴ࠰ࡐࡥࡷࡱࠢኑ"): [bstack1l11l11_opy_ (u"ࠣࡰࡤࡱࡪࠨኒ"), bstack1l11l11_opy_ (u"ࠤࡤࡶ࡬ࡹࠢና"), bstack1l11l11_opy_ (u"ࠥ࡯ࡼࡧࡲࡨࡵࠥኔ")],
}
_1l1ll11ll1l_opy_ = set()
class bstack1ll1l1llll1_opy_(bstack1lll1l11l1l_opy_):
    bstack1l1ll1l1l11_opy_ = bstack1l11l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡧࡩ࡫࡫ࡲࡳࡧࡧࠦን")
    bstack1l1ll111111_opy_ = bstack1l11l11_opy_ (u"ࠧࡏࡎࡇࡑࠥኖ")
    bstack1l1l1ll11l1_opy_ = bstack1l11l11_opy_ (u"ࠨࡅࡓࡔࡒࡖࠧኗ")
    bstack1l1l1l1l11l_opy_: Callable
    bstack1l1l1lll111_opy_: Callable
    def __init__(self, bstack1llll11ll1l_opy_, bstack1ll1ll111ll_opy_):
        super().__init__()
        self.bstack1ll11l1lll1_opy_ = bstack1ll1ll111ll_opy_
        if os.getenv(bstack1l11l11_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡏ࠲࠳࡜ࠦኘ"), bstack1l11l11_opy_ (u"ࠣ࠳ࠥኙ")) != bstack1l11l11_opy_ (u"ࠤ࠴ࠦኚ") or not self.is_enabled():
            self.logger.warning(bstack1l11l11_opy_ (u"ࠥࠦኛ") + str(self.__class__.__name__) + bstack1l11l11_opy_ (u"ࠦࠥࡪࡩࡴࡣࡥࡰࡪࡪࠢኜ"))
            return
        TestFramework.bstack1ll111l11ll_opy_((bstack1llll11ll11_opy_.TEST, bstack1ll1ll11111_opy_.PRE), self.bstack1ll1111lll1_opy_)
        TestFramework.bstack1ll111l11ll_opy_((bstack1llll11ll11_opy_.TEST, bstack1ll1ll11111_opy_.POST), self.bstack1ll111l111l_opy_)
        for event in bstack1llll11ll11_opy_:
            for state in bstack1ll1ll11111_opy_:
                TestFramework.bstack1ll111l11ll_opy_((event, state), self.bstack1l1ll1l11l1_opy_)
        bstack1llll11ll1l_opy_.bstack1ll111l11ll_opy_((bstack1llll1lllll_opy_.bstack1lllll1ll11_opy_, bstack1llllll1lll_opy_.POST), self.bstack1l1ll1lll11_opy_)
        self.bstack1l1l1l1l11l_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l1lll11ll1_opy_(bstack1ll1l1llll1_opy_.bstack1l1ll111111_opy_, self.bstack1l1l1l1l11l_opy_)
        self.bstack1l1l1lll111_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l1lll11ll1_opy_(bstack1ll1l1llll1_opy_.bstack1l1l1ll11l1_opy_, self.bstack1l1l1lll111_opy_)
        self.bstack1l1ll1l111l_opy_ = builtins.print
        builtins.print = self.bstack1l1ll1l1l1l_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l1ll1l11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1ll1lllll11_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1l1l1l1l111_opy_() and instance:
            bstack1l1ll111l11_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1lllllll1l1_opy_
            if test_framework_state == bstack1llll11ll11_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1llll11ll11_opy_.LOG:
                bstack1lll1lllll_opy_ = datetime.now()
                entries = f.bstack1l1lll1l1ll_opy_(instance, bstack1lllllll1l1_opy_)
                if entries:
                    self.bstack1l1l1l1l1l1_opy_(instance, entries)
                    instance.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࠧኝ"), datetime.now() - bstack1lll1lllll_opy_)
                    f.bstack1l1lll11111_opy_(instance, bstack1lllllll1l1_opy_)
                instance.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠨ࡯࠲࠳ࡼ࠾ࡴࡴ࡟ࡢ࡮࡯ࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴࡴࠤኞ"), datetime.now() - bstack1l1ll111l11_opy_)
                return # bstack1l1lll111l1_opy_ not send this event with the bstack1l1lll1l1l1_opy_ bstack1l1l1llllll_opy_
            elif (
                test_framework_state == bstack1llll11ll11_opy_.TEST
                and test_hook_state == bstack1ll1ll11111_opy_.POST
                and not f.bstack1lllll1l11l_opy_(instance, TestFramework.bstack1l1lll1ll11_opy_)
            ):
                self.logger.warning(bstack1l11l11_opy_ (u"ࠢࡥࡴࡲࡴࡵ࡯࡮ࡨࠢࡧࡹࡪࠦࡴࡰࠢ࡯ࡥࡨࡱࠠࡰࡨࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࠧኟ") + str(TestFramework.bstack1lllll1l11l_opy_(instance, TestFramework.bstack1l1lll1ll11_opy_)) + bstack1l11l11_opy_ (u"ࠣࠤአ"))
                f.bstack1lllll1l1l1_opy_(instance, bstack1ll1l1llll1_opy_.bstack1l1ll1l1l11_opy_, True)
                return # bstack1l1lll111l1_opy_ not send this event bstack1l1lll11l11_opy_ bstack1l1ll1l1ll1_opy_
            elif (
                f.bstack1llllll1l1l_opy_(instance, bstack1ll1l1llll1_opy_.bstack1l1ll1l1l11_opy_, False)
                and test_framework_state == bstack1llll11ll11_opy_.LOG_REPORT
                and test_hook_state == bstack1ll1ll11111_opy_.POST
                and f.bstack1lllll1l11l_opy_(instance, TestFramework.bstack1l1lll1ll11_opy_)
            ):
                self.logger.warning(bstack1l11l11_opy_ (u"ࠤ࡬ࡲ࡯࡫ࡣࡵ࡫ࡱ࡫࡚ࠥࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡵࡧ࠱ࡘࡊ࡙ࡔ࠭ࠢࡗࡩࡸࡺࡈࡰࡱ࡮ࡗࡹࡧࡴࡦ࠰ࡓࡓࡘ࡚ࠠࠣኡ") + str(TestFramework.bstack1lllll1l11l_opy_(instance, TestFramework.bstack1l1lll1ll11_opy_)) + bstack1l11l11_opy_ (u"ࠥࠦኢ"))
                self.bstack1l1ll1l11l1_opy_(f, instance, (bstack1llll11ll11_opy_.TEST, bstack1ll1ll11111_opy_.POST), *args, **kwargs)
            bstack1lll1lllll_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l1ll11l1l1_opy_ = sorted(
                filter(lambda x: x.get(bstack1l11l11_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢኣ"), None), data.pop(bstack1l11l11_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧኤ"), {}).values()),
                key=lambda x: x[bstack1l11l11_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤእ")],
            )
            if bstack1ll1ll1llll_opy_.bstack1l1l1lll1ll_opy_ in data:
                data.pop(bstack1ll1ll1llll_opy_.bstack1l1l1lll1ll_opy_)
            data.update({bstack1l11l11_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢኦ"): bstack1l1ll11l1l1_opy_})
            instance.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠣ࡬ࡶࡳࡳࡀࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨኧ"), datetime.now() - bstack1lll1lllll_opy_)
            bstack1lll1lllll_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l1l1ll1l11_opy_)
            instance.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠤ࡭ࡷࡴࡴ࠺ࡰࡰࡢࡥࡱࡲ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷࡷࠧከ"), datetime.now() - bstack1lll1lllll_opy_)
            self.bstack1l1l1llllll_opy_(instance, bstack1lllllll1l1_opy_, event_json=event_json)
            instance.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠥࡳ࠶࠷ࡹ࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨኩ"), datetime.now() - bstack1l1ll111l11_opy_)
    def bstack1ll1111lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1ll1lllll11_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1l1lllll1l_opy_ import bstack1lll11lll11_opy_
        bstack1ll11lll1l1_opy_ = bstack1lll11lll11_opy_.bstack1ll111lll11_opy_(EVENTS.bstack11ll1ll1l_opy_.value)
        self.bstack1ll11l1lll1_opy_.bstack1l1ll1ll111_opy_(instance, f, bstack1lllllll1l1_opy_, *args, **kwargs)
        bstack1lll11lll11_opy_.end(EVENTS.bstack11ll1ll1l_opy_.value, bstack1ll11lll1l1_opy_ + bstack1l11l11_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦኪ"), bstack1ll11lll1l1_opy_ + bstack1l11l11_opy_ (u"ࠧࡀࡥ࡯ࡦࠥካ"), status=True, failure=None, test_name=None)
    def bstack1ll111l111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1ll1lllll11_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1ll11l1lll1_opy_.bstack1l1l1ll1ll1_opy_(instance, f, bstack1lllllll1l1_opy_, *args, **kwargs)
        self.bstack1l1l1ll111l_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l1ll111ll1_opy_, stage=STAGE.bstack1lll1111l_opy_)
    def bstack1l1l1ll111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1ll1lllll11_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠨࡓ࡬࡫ࡳࡴ࡮ࡴࡧࠡࡖࡨࡷࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡋࡶࡦࡰࡷࠤ࡬ࡘࡐࡄࠢࡦࡥࡱࡲ࠺ࠡࡐࡲࠤࡻࡧ࡬ࡪࡦࠣࡶࡪࡷࡵࡦࡵࡷࠤࡩࡧࡴࡢࠤኬ"))
            return
        bstack1lll1lllll_opy_ = datetime.now()
        try:
            r = self.bstack1ll1ll1ll1l_opy_.TestSessionEvent(req)
            instance.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡸࡪࡹࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡨࡺࡪࡴࡴࠣክ"), datetime.now() - bstack1lll1lllll_opy_)
            f.bstack1lllll1l1l1_opy_(instance, self.bstack1ll11l1lll1_opy_.bstack1l1l1llll1l_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1l11l11_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥኮ") + str(r) + bstack1l11l11_opy_ (u"ࠤࠥኯ"))
        except grpc.RpcError as e:
            self.logger.error(bstack1l11l11_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣኰ") + str(e) + bstack1l11l11_opy_ (u"ࠦࠧ኱"))
            traceback.print_exc()
            raise e
    def bstack1l1ll1lll11_opy_(
        self,
        f: bstack1lll111l11l_opy_,
        _driver: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        _1l1ll11l11l_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llllll1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lll111l11l_opy_.bstack1ll11l111l1_opy_(method_name):
            return
        if f.bstack1ll1l111111_opy_(*args) == bstack1lll111l11l_opy_.bstack1l1ll11l111_opy_:
            bstack1l1ll111l11_opy_ = datetime.now()
            screenshot = result.get(bstack1l11l11_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦኲ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack1l11l11_opy_ (u"ࠨࡩ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠤ࡮ࡳࡡࡨࡧࠣࡦࡦࡹࡥ࠷࠶ࠣࡷࡹࡸࠢኳ"))
                return
            bstack1l1ll1ll1l1_opy_ = self.bstack1l1ll1l1lll_opy_(instance)
            if bstack1l1ll1ll1l1_opy_:
                entry = bstack1lll1llll1l_opy_(TestFramework.bstack1l1ll1lllll_opy_, screenshot)
                self.bstack1l1l1l1l1l1_opy_(bstack1l1ll1ll1l1_opy_, [entry])
                instance.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠢࡰ࠳࠴ࡽ࠿ࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡦࡺࡨࡧࡺࡺࡥࠣኴ"), datetime.now() - bstack1l1ll111l11_opy_)
            else:
                self.logger.warning(bstack1l11l11_opy_ (u"ࠣࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡵࡧࡶࡸࠥ࡬࡯ࡳࠢࡺ࡬࡮ࡩࡨࠡࡶ࡫࡭ࡸࠦࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠣࡻࡦࡹࠠࡵࡣ࡮ࡩࡳࠦࡢࡺࠢࡧࡶ࡮ࡼࡥࡳ࠿ࠣࡿࢂࠨኵ").format(instance.ref()))
        event = {}
        bstack1l1ll1ll1l1_opy_ = self.bstack1l1ll1l1lll_opy_(instance)
        if bstack1l1ll1ll1l1_opy_:
            self.bstack1l1lll111ll_opy_(event, bstack1l1ll1ll1l1_opy_)
            if event.get(bstack1l11l11_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢ኶")):
                self.bstack1l1l1l1l1l1_opy_(bstack1l1ll1ll1l1_opy_, event[bstack1l11l11_opy_ (u"ࠥࡰࡴ࡭ࡳࠣ኷")])
            else:
                self.logger.debug(bstack1l11l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡰࡴ࡭ࡳࠡࡨࡲࡶࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠢࡨࡺࡪࡴࡴࠣኸ"))
    @measure(event_name=EVENTS.bstack1l1lll1l11l_opy_, stage=STAGE.bstack1lll1111l_opy_)
    def bstack1l1l1l1l1l1_opy_(
        self,
        bstack1l1ll1ll1l1_opy_: bstack1ll1lllll11_opy_,
        entries: List[bstack1lll1llll1l_opy_],
    ):
        self.bstack1ll111l1111_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1llllll1l1l_opy_(bstack1l1ll1ll1l1_opy_, TestFramework.bstack1ll11ll111l_opy_)
        req.execution_context.hash = str(bstack1l1ll1ll1l1_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1ll1ll1l1_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1ll1ll1l1_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.bstack1llllll1l1l_opy_(bstack1l1ll1ll1l1_opy_, TestFramework.bstack1ll11l1l1ll_opy_)
            log_entry.test_framework_version = TestFramework.bstack1llllll1l1l_opy_(bstack1l1ll1ll1l1_opy_, TestFramework.bstack1l1l1ll1lll_opy_)
            log_entry.uuid = TestFramework.bstack1llllll1l1l_opy_(bstack1l1ll1ll1l1_opy_, TestFramework.bstack1ll111ll1ll_opy_)
            log_entry.test_framework_state = bstack1l1ll1ll1l1_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l11l11_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦኹ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1l11l11_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣኺ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1ll111l1l_opy_
                log_entry.file_path = entry.bstack1l1l1l1_opy_
        def bstack1l1ll1lll1l_opy_():
            bstack1lll1lllll_opy_ = datetime.now()
            try:
                self.bstack1ll1ll1ll1l_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l1ll1lllll_opy_:
                    bstack1l1ll1ll1l1_opy_.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦኻ"), datetime.now() - bstack1lll1lllll_opy_)
                elif entry.kind == TestFramework.bstack1l1l1l1ll1l_opy_:
                    bstack1l1ll1ll1l1_opy_.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧኼ"), datetime.now() - bstack1lll1lllll_opy_)
                else:
                    bstack1l1ll1ll1l1_opy_.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡ࡯ࡳ࡬ࠨኽ"), datetime.now() - bstack1lll1lllll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l11l11_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣኾ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack111111111l_opy_.enqueue(bstack1l1ll1lll1l_opy_)
    @measure(event_name=EVENTS.bstack1l1lll1ll1l_opy_, stage=STAGE.bstack1lll1111l_opy_)
    def bstack1l1l1llllll_opy_(
        self,
        instance: bstack1ll1lllll11_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        event_json=None,
    ):
        self.bstack1ll111l1111_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1ll11ll111l_opy_)
        req.test_framework_name = TestFramework.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1ll11l1l1ll_opy_)
        req.test_framework_version = TestFramework.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1l1l1ll1lll_opy_)
        req.test_framework_state = bstack1lllllll1l1_opy_[0].name
        req.test_hook_state = bstack1lllllll1l1_opy_[1].name
        started_at = TestFramework.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1l1l1l1l1ll_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1l1l1ll1111_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l1l1ll1l11_opy_)).encode(bstack1l11l11_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥ኿"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1l1ll1lll1l_opy_():
            bstack1lll1lllll_opy_ = datetime.now()
            try:
                self.bstack1ll1ll1ll1l_opy_.TestFrameworkEvent(req)
                instance.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡨࡺࡪࡴࡴࠣዀ"), datetime.now() - bstack1lll1lllll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l11l11_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦ዁") + str(e))
                traceback.print_exc()
                raise e
        self.bstack111111111l_opy_.enqueue(bstack1l1ll1lll1l_opy_)
    def bstack1l1ll1l1lll_opy_(self, instance: bstack1llll1llll1_opy_):
        bstack1l1l1lll11l_opy_ = TestFramework.bstack1llll1l1lll_opy_(instance.context)
        for t in bstack1l1l1lll11l_opy_:
            bstack1l1ll1llll1_opy_ = TestFramework.bstack1llllll1l1l_opy_(t, bstack1ll1ll1llll_opy_.bstack1l1l1lll1ll_opy_, [])
            if any(instance is d[1] for d in bstack1l1ll1llll1_opy_):
                return t
    def bstack1l1ll111lll_opy_(self, message):
        self.bstack1l1l1l1l11l_opy_(message + bstack1l11l11_opy_ (u"ࠢ࡝ࡰࠥዂ"))
    def log_error(self, message):
        self.bstack1l1l1lll111_opy_(message + bstack1l11l11_opy_ (u"ࠣ࡞ࡱࠦዃ"))
    def bstack1l1lll11ll1_opy_(self, level, original_func):
        def bstack1l1l1l1ll11_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack1l11l11_opy_ (u"ࠤࡈࡺࡪࡴࡴࡅ࡫ࡶࡴࡦࡺࡣࡩࡧࡵࡑࡴࡪࡵ࡭ࡧࠥዄ") in message or bstack1l11l11_opy_ (u"ࠥ࡟ࡘࡊࡋࡄࡎࡌࡡࠧዅ") in message or bstack1l11l11_opy_ (u"ࠦࡠ࡝ࡥࡣࡆࡵ࡭ࡻ࡫ࡲࡎࡱࡧࡹࡱ࡫࡝ࠣ዆") in message:
                return return_value
            bstack1l1l1lll11l_opy_ = TestFramework.bstack1l1ll11lll1_opy_()
            if not bstack1l1l1lll11l_opy_:
                return return_value
            bstack1l1ll1ll1l1_opy_ = next(
                (
                    instance
                    for instance in bstack1l1l1lll11l_opy_
                    if TestFramework.bstack1lllll1l11l_opy_(instance, TestFramework.bstack1ll111ll1ll_opy_)
                ),
                None,
            )
            if not bstack1l1ll1ll1l1_opy_:
                return return_value
            entry = bstack1lll1llll1l_opy_(TestFramework.bstack1l1l1l1lll1_opy_, message, level)
            self.bstack1l1l1l1l1l1_opy_(bstack1l1ll1ll1l1_opy_, [entry])
            return return_value
        return bstack1l1l1l1ll11_opy_
    def bstack1l1ll1l1l1l_opy_(self):
        def bstack1l1l1ll1l1l_opy_(*args, **kwargs):
            try:
                self.bstack1l1ll1l111l_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack1l11l11_opy_ (u"ࠬࠦࠧ዇").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack1l11l11_opy_ (u"ࠨࡅࡷࡧࡱࡸࡉ࡯ࡳࡱࡣࡷࡧ࡭࡫ࡲࡎࡱࡧࡹࡱ࡫ࠢወ") in message:
                    return
                bstack1l1l1lll11l_opy_ = TestFramework.bstack1l1ll11lll1_opy_()
                if not bstack1l1l1lll11l_opy_:
                    return
                bstack1l1ll1ll1l1_opy_ = next(
                    (
                        instance
                        for instance in bstack1l1l1lll11l_opy_
                        if TestFramework.bstack1lllll1l11l_opy_(instance, TestFramework.bstack1ll111ll1ll_opy_)
                    ),
                    None,
                )
                if not bstack1l1ll1ll1l1_opy_:
                    return
                entry = bstack1lll1llll1l_opy_(TestFramework.bstack1l1l1l1lll1_opy_, message, bstack1ll1l1llll1_opy_.bstack1l1ll111111_opy_)
                self.bstack1l1l1l1l1l1_opy_(bstack1l1ll1ll1l1_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l1ll1l111l_opy_(bstack1ll1llll1ll_opy_ (u"ࠢ࡜ࡇࡹࡩࡳࡺࡄࡪࡵࡳࡥࡹࡩࡨࡦࡴࡐࡳࡩࡻ࡬ࡦ࡟ࠣࡐࡴ࡭ࠠࡤࡣࡳࡸࡺࡸࡥࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࡨࢁࠧዉ"))
                except:
                    pass
        return bstack1l1l1ll1l1l_opy_
    def bstack1l1lll111ll_opy_(self, event: dict, instance=None) -> None:
        global _1l1ll11ll1l_opy_
        levels = [bstack1l11l11_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦዊ"), bstack1l11l11_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨዋ")]
        bstack1l1lll1111l_opy_ = bstack1l11l11_opy_ (u"ࠥࠦዌ")
        if instance is not None:
            try:
                bstack1l1lll1111l_opy_ = TestFramework.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1ll111ll1ll_opy_)
            except Exception as e:
                self.logger.warning(bstack1l11l11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡺࡻࡩࡥࠢࡩࡶࡴࡳࠠࡪࡰࡶࡸࡦࡴࡣࡦࠤው").format(e))
        bstack1l1l1ll11ll_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack1l11l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬዎ")]
                bstack1l1lll1l111_opy_ = os.path.join(bstack1l1ll11llll_opy_, (bstack1l1ll11l1ll_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1l1lll1l111_opy_):
                    self.logger.debug(bstack1l11l11_opy_ (u"ࠨࡄࡪࡴࡨࡧࡹࡵࡲࡺࠢࡱࡳࡹࠦࡰࡳࡧࡶࡩࡳࡺࠠࡧࡱࡵࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡖࡨࡷࡹࠦࡡ࡯ࡦࠣࡆࡺ࡯࡬ࡥࠢ࡯ࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡻࡾࠤዏ").format(bstack1l1lll1l111_opy_))
                    continue
                file_names = os.listdir(bstack1l1lll1l111_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1l1lll1l111_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1l1ll11ll1l_opy_:
                        self.logger.info(bstack1l11l11_opy_ (u"ࠢࡑࡣࡷ࡬ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡾࢁࠧዐ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l1l1lll1l1_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l1l1lll1l1_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack1l11l11_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦዑ"):
                                entry = bstack1lll1llll1l_opy_(
                                    kind=bstack1l11l11_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦዒ"),
                                    message=bstack1l11l11_opy_ (u"ࠥࠦዓ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1ll111l1l_opy_=file_size,
                                    bstack1l1l1l11lll_opy_=bstack1l11l11_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦዔ"),
                                    bstack1l1l1l1_opy_=os.path.abspath(file_path),
                                    bstack1lll111ll1_opy_=bstack1l1lll1111l_opy_
                                )
                            elif level == bstack1l11l11_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤዕ"):
                                entry = bstack1lll1llll1l_opy_(
                                    kind=bstack1l11l11_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣዖ"),
                                    message=bstack1l11l11_opy_ (u"ࠢࠣ዗"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1ll111l1l_opy_=file_size,
                                    bstack1l1l1l11lll_opy_=bstack1l11l11_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣዘ"),
                                    bstack1l1l1l1_opy_=os.path.abspath(file_path),
                                    bstack1l1ll11ll11_opy_=bstack1l1lll1111l_opy_
                                )
                            bstack1l1l1ll11ll_opy_.append(entry)
                            _1l1ll11ll1l_opy_.add(abs_path)
                        except Exception as bstack1l1ll1ll1ll_opy_:
                            self.logger.error(bstack1l11l11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡸࡡࡪࡵࡨࡨࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࢁࡽࠣዙ").format(bstack1l1ll1ll1ll_opy_))
        except Exception as e:
            self.logger.error(bstack1l11l11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡲࡢ࡫ࡶࡩࡩࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡻࡾࠤዚ").format(e))
        event[bstack1l11l11_opy_ (u"ࠦࡱࡵࡧࡴࠤዛ")] = bstack1l1l1ll11ll_opy_
class bstack1l1l1ll1l11_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l1l1l1llll_opy_ = set()
        kwargs[bstack1l11l11_opy_ (u"ࠧࡹ࡫ࡪࡲ࡮ࡩࡾࡹࠢዜ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l1lll11lll_opy_(obj, self.bstack1l1l1l1llll_opy_)
def bstack1l1ll1111l1_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l1lll11lll_opy_(obj, bstack1l1l1l1llll_opy_=None, max_depth=3):
    if bstack1l1l1l1llll_opy_ is None:
        bstack1l1l1l1llll_opy_ = set()
    if id(obj) in bstack1l1l1l1llll_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l1l1l1llll_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l1ll1111ll_opy_ = TestFramework.bstack1l1lll11l1l_opy_(obj)
    bstack1l1ll1ll11l_opy_ = next((k.lower() in bstack1l1ll1111ll_opy_.lower() for k in bstack1l1l1llll11_opy_.keys()), None)
    if bstack1l1ll1ll11l_opy_:
        obj = TestFramework.bstack1l1ll1l1111_opy_(obj, bstack1l1l1llll11_opy_[bstack1l1ll1ll11l_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1l11l11_opy_ (u"ࠨ࡟ࡠࡵ࡯ࡳࡹࡹ࡟ࡠࠤዝ")):
            keys = getattr(obj, bstack1l11l11_opy_ (u"ࠢࡠࡡࡶࡰࡴࡺࡳࡠࡡࠥዞ"), [])
        elif hasattr(obj, bstack1l11l11_opy_ (u"ࠣࡡࡢࡨ࡮ࡩࡴࡠࡡࠥዟ")):
            keys = getattr(obj, bstack1l11l11_opy_ (u"ࠤࡢࡣࡩ࡯ࡣࡵࡡࡢࠦዠ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1l11l11_opy_ (u"ࠥࡣࠧዡ"))}
        if not obj and bstack1l1ll1111ll_opy_ == bstack1l11l11_opy_ (u"ࠦࡵࡧࡴࡩ࡮࡬ࡦ࠳ࡖ࡯ࡴ࡫ࡻࡔࡦࡺࡨࠣዢ"):
            obj = {bstack1l11l11_opy_ (u"ࠧࡶࡡࡵࡪࠥዣ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l1ll1111l1_opy_(key) or str(key).startswith(bstack1l11l11_opy_ (u"ࠨ࡟ࠣዤ")):
            continue
        if value is not None and bstack1l1ll1111l1_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l1lll11lll_opy_(value, bstack1l1l1l1llll_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l1lll11lll_opy_(o, bstack1l1l1l1llll_opy_, max_depth) for o in value]))
    return result or None