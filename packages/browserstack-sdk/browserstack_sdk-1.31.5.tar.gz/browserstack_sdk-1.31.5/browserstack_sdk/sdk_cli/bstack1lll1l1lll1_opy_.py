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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll1l11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11111_opy_ import (
    bstack1llll1lllll_opy_,
    bstack1llllll1lll_opy_,
    bstack1llll1llll1_opy_,
)
from bstack_utils.helper import  bstack1lll1lll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll111l11l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11ll11_opy_, bstack1ll1lllll11_opy_, bstack1ll1ll11111_opy_, bstack1lll1llll1l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11ll1l1l_opy_ import bstack11l11l111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1ll1_opy_ import bstack1ll1ll1llll_opy_
from bstack_utils.percy import bstack11111l111_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1lll1ll1lll_opy_(bstack1lll1l11l1l_opy_):
    def __init__(self, bstack1l1l1l1111l_opy_: Dict[str, str]):
        super().__init__()
        self.bstack1l1l1l1111l_opy_ = bstack1l1l1l1111l_opy_
        self.percy = bstack11111l111_opy_()
        self.bstack11l1l1lll1_opy_ = bstack11l11l111l_opy_()
        self.bstack1l1l11llll1_opy_()
        bstack1lll111l11l_opy_.bstack1ll111l11ll_opy_((bstack1llll1lllll_opy_.bstack1lllll1ll11_opy_, bstack1llllll1lll_opy_.PRE), self.bstack1l1l11ll1l1_opy_)
        TestFramework.bstack1ll111l11ll_opy_((bstack1llll11ll11_opy_.TEST, bstack1ll1ll11111_opy_.POST), self.bstack1ll111l111l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1ll1l1lll_opy_(self, instance: bstack1llll1llll1_opy_, driver: object):
        bstack1l1l1lll11l_opy_ = TestFramework.bstack1llll1l1lll_opy_(instance.context)
        for t in bstack1l1l1lll11l_opy_:
            bstack1l1ll1llll1_opy_ = TestFramework.bstack1llllll1l1l_opy_(t, bstack1ll1ll1llll_opy_.bstack1l1l1lll1ll_opy_, [])
            if any(instance is d[1] for d in bstack1l1ll1llll1_opy_) or instance == driver:
                return t
    def bstack1l1l11ll1l1_opy_(
        self,
        f: bstack1lll111l11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llllll1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lll111l11l_opy_.bstack1ll11l111l1_opy_(method_name):
                return
            platform_index = f.bstack1llllll1l1l_opy_(instance, bstack1lll111l11l_opy_.bstack1ll11ll111l_opy_, 0)
            bstack1l1ll1ll1l1_opy_ = self.bstack1l1ll1l1lll_opy_(instance, driver)
            bstack1l1l1l11l11_opy_ = TestFramework.bstack1llllll1l1l_opy_(bstack1l1ll1ll1l1_opy_, TestFramework.bstack1l1l11lllll_opy_, None)
            if not bstack1l1l1l11l11_opy_:
                self.logger.debug(bstack1l11l11_opy_ (u"ࠢࡰࡰࡢࡴࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡵࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥࡧࡳࠡࡵࡨࡷࡸ࡯࡯࡯ࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡼࡩࡹࠦࡳࡵࡣࡵࡸࡪࡪࠢዥ"))
                return
            driver_command = f.bstack1ll1l111111_opy_(*args)
            for command in bstack11111111_opy_:
                if command == driver_command:
                    self.bstack11l1l1l11_opy_(driver, platform_index)
            bstack1ll1l11l1_opy_ = self.percy.bstack1l11l1l11l_opy_()
            if driver_command in bstack1ll1lllll_opy_[bstack1ll1l11l1_opy_]:
                self.bstack11l1l1lll1_opy_.bstack1lll111l1_opy_(bstack1l1l1l11l11_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1l11l11_opy_ (u"ࠣࡱࡱࡣࡵࡸࡥࡠࡧࡻࡩࡨࡻࡴࡦ࠼ࠣࡩࡷࡸ࡯ࡳࠤዦ"), e)
    def bstack1ll111l111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1ll1lllll11_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1l1lllll1l_opy_ import bstack1lll11lll11_opy_
        bstack1l1ll1llll1_opy_ = f.bstack1llllll1l1l_opy_(instance, bstack1ll1ll1llll_opy_.bstack1l1l1lll1ll_opy_, [])
        if not bstack1l1ll1llll1_opy_:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦዧ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠥࠦየ"))
            return
        if len(bstack1l1ll1llll1_opy_) > 1:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨዩ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠧࠨዪ"))
        bstack1l1l1l11ll1_opy_, bstack1l1l1l111ll_opy_ = bstack1l1ll1llll1_opy_[0]
        driver = bstack1l1l1l11ll1_opy_()
        if not driver:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢያ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠢࠣዬ"))
            return
        bstack1l1l11ll1ll_opy_ = {
            TestFramework.bstack1ll1111ll1l_opy_: bstack1l11l11_opy_ (u"ࠣࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦይ"),
            TestFramework.bstack1ll111ll1ll_opy_: bstack1l11l11_opy_ (u"ࠤࡷࡩࡸࡺࠠࡶࡷ࡬ࡨࠧዮ"),
            TestFramework.bstack1l1l11lllll_opy_: bstack1l11l11_opy_ (u"ࠥࡸࡪࡹࡴࠡࡴࡨࡶࡺࡴࠠ࡯ࡣࡰࡩࠧዯ")
        }
        bstack1l1l1l111l1_opy_ = { key: f.bstack1llllll1l1l_opy_(instance, key) for key in bstack1l1l11ll1ll_opy_ }
        bstack1l1l1l11111_opy_ = [key for key, value in bstack1l1l1l111l1_opy_.items() if not value]
        if bstack1l1l1l11111_opy_:
            for key in bstack1l1l1l11111_opy_:
                self.logger.debug(bstack1l11l11_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠢደ") + str(key) + bstack1l11l11_opy_ (u"ࠧࠨዱ"))
            return
        platform_index = f.bstack1llllll1l1l_opy_(instance, bstack1lll111l11l_opy_.bstack1ll11ll111l_opy_, 0)
        if self.bstack1l1l1l1111l_opy_.percy_capture_mode == bstack1l11l11_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣዲ"):
            bstack11l1l111l1_opy_ = bstack1l1l1l111l1_opy_.get(TestFramework.bstack1l1l11lllll_opy_) + bstack1l11l11_opy_ (u"ࠢ࠮ࡶࡨࡷࡹࡩࡡࡴࡧࠥዳ")
            bstack1ll11lll1l1_opy_ = bstack1lll11lll11_opy_.bstack1ll111lll11_opy_(EVENTS.bstack1l1l11lll1l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11l1l111l1_opy_,
                bstack1l1111l11_opy_=bstack1l1l1l111l1_opy_[TestFramework.bstack1ll1111ll1l_opy_],
                bstack1ll11ll111_opy_=bstack1l1l1l111l1_opy_[TestFramework.bstack1ll111ll1ll_opy_],
                bstack11l1l11l_opy_=platform_index
            )
            bstack1lll11lll11_opy_.end(EVENTS.bstack1l1l11lll1l_opy_.value, bstack1ll11lll1l1_opy_+bstack1l11l11_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣዴ"), bstack1ll11lll1l1_opy_+bstack1l11l11_opy_ (u"ࠤ࠽ࡩࡳࡪࠢድ"), True, None, None, None, None, test_name=bstack11l1l111l1_opy_)
    def bstack11l1l1l11_opy_(self, driver, platform_index):
        if self.bstack11l1l1lll1_opy_.bstack1l11lll1l1_opy_() is True or self.bstack11l1l1lll1_opy_.capturing() is True:
            return
        self.bstack11l1l1lll1_opy_.bstack1lll1lll1_opy_()
        while not self.bstack11l1l1lll1_opy_.bstack1l11lll1l1_opy_():
            bstack1l1l1l11l11_opy_ = self.bstack11l1l1lll1_opy_.bstack11l111ll_opy_()
            self.bstack1l1ll11111_opy_(driver, bstack1l1l1l11l11_opy_, platform_index)
        self.bstack11l1l1lll1_opy_.bstack1lll11l1l_opy_()
    def bstack1l1ll11111_opy_(self, driver, bstack11llll1ll1_opy_, platform_index, test=None):
        from bstack_utils.bstack1l1lllll1l_opy_ import bstack1lll11lll11_opy_
        bstack1ll11lll1l1_opy_ = bstack1lll11lll11_opy_.bstack1ll111lll11_opy_(EVENTS.bstack1l1l1111_opy_.value)
        if test != None:
            bstack1l1111l11_opy_ = getattr(test, bstack1l11l11_opy_ (u"ࠪࡲࡦࡳࡥࠨዶ"), None)
            bstack1ll11ll111_opy_ = getattr(test, bstack1l11l11_opy_ (u"ࠫࡺࡻࡩࡥࠩዷ"), None)
            PercySDK.screenshot(driver, bstack11llll1ll1_opy_, bstack1l1111l11_opy_=bstack1l1111l11_opy_, bstack1ll11ll111_opy_=bstack1ll11ll111_opy_, bstack11l1l11l_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack11llll1ll1_opy_)
        bstack1lll11lll11_opy_.end(EVENTS.bstack1l1l1111_opy_.value, bstack1ll11lll1l1_opy_+bstack1l11l11_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧዸ"), bstack1ll11lll1l1_opy_+bstack1l11l11_opy_ (u"ࠨ࠺ࡦࡰࡧࠦዹ"), True, None, None, None, None, test_name=bstack11llll1ll1_opy_)
    def bstack1l1l11llll1_opy_(self):
        os.environ[bstack1l11l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬዺ")] = str(self.bstack1l1l1l1111l_opy_.success)
        os.environ[bstack1l11l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬዻ")] = str(self.bstack1l1l1l1111l_opy_.percy_capture_mode)
        self.percy.bstack1l1l11lll11_opy_(self.bstack1l1l1l1111l_opy_.is_percy_auto_enabled)
        self.percy.bstack1l1l1l11l1l_opy_(self.bstack1l1l1l1111l_opy_.percy_build_id)