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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llllllll1l_opy_,
    bstack1llll1lllll_opy_,
)
from bstack_utils.helper import  bstack1l11111lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11111ll_opy_ import bstack1ll1ll111ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1ll1_opy_, bstack1lll1l11l11_opy_, bstack1lll1l1l1l1_opy_, bstack1lll111llll_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1l1l11lll1_opy_ import bstack1lll1111l1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1ll1ll1l_opy_ import bstack1ll1ll1111l_opy_
from bstack_utils.percy import bstack1111l11l_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1lll1111lll_opy_(bstack1llll11lll1_opy_):
    def __init__(self, bstack1l1l1l111ll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack1l1l1l111ll_opy_ = bstack1l1l1l111ll_opy_
        self.percy = bstack1111l11l_opy_()
        self.bstack11llll111_opy_ = bstack1lll1111l1_opy_()
        self.bstack1l1l11ll1ll_opy_()
        bstack1ll1ll111ll_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1lllll1ll1l_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1l1l1l1111l_opy_)
        TestFramework.bstack1ll111l11l1_opy_((bstack1lll1ll1ll1_opy_.TEST, bstack1lll1l1l1l1_opy_.POST), self.bstack1ll111l1lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1lll11l1l_opy_(self, instance: bstack1llll1lllll_opy_, driver: object):
        bstack1l1l1ll111l_opy_ = TestFramework.bstack1lllll1l1ll_opy_(instance.context)
        for t in bstack1l1l1ll111l_opy_:
            bstack1l1l1l1l11l_opy_ = TestFramework.bstack1lllll1l1l1_opy_(t, bstack1ll1ll1111l_opy_.bstack1l1l1lllll1_opy_, [])
            if any(instance is d[1] for d in bstack1l1l1l1l11l_opy_) or instance == driver:
                return t
    def bstack1l1l1l1111l_opy_(
        self,
        f: bstack1ll1ll111ll_opy_,
        driver: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1ll1ll111ll_opy_.bstack1ll11ll1l1l_opy_(method_name):
                return
            platform_index = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll111ll_opy_.bstack1ll1l1111l1_opy_, 0)
            bstack1l1ll1lll1l_opy_ = self.bstack1l1lll11l1l_opy_(instance, driver)
            bstack1l1l11lll11_opy_ = TestFramework.bstack1lllll1l1l1_opy_(bstack1l1ll1lll1l_opy_, TestFramework.bstack1l1l11lll1l_opy_, None)
            if not bstack1l1l11lll11_opy_:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠢࡰࡰࡢࡴࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡵࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥࡧࡳࠡࡵࡨࡷࡸ࡯࡯࡯ࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡼࡩࡹࠦࡳࡵࡣࡵࡸࡪࡪࠢዥ"))
                return
            driver_command = f.bstack1ll111l1ll1_opy_(*args)
            for command in bstack11lll111ll_opy_:
                if command == driver_command:
                    self.bstack11l11l1lll_opy_(driver, platform_index)
            bstack11llll1lll_opy_ = self.percy.bstack1l11lll1l1_opy_()
            if driver_command in bstack1l1l1l11l_opy_[bstack11llll1lll_opy_]:
                self.bstack11llll111_opy_.bstack1l11l1ll11_opy_(bstack1l1l11lll11_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠣࡱࡱࡣࡵࡸࡥࡠࡧࡻࡩࡨࡻࡴࡦ࠼ࠣࡩࡷࡸ࡯ࡳࠤዦ"), e)
    def bstack1ll111l1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111l11ll_opy_ import bstack1lll111lll1_opy_
        bstack1l1l1l1l11l_opy_ = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l1l1lllll1_opy_, [])
        if not bstack1l1l1l1l11l_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦዧ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠥࠦየ"))
            return
        if len(bstack1l1l1l1l11l_opy_) > 1:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨዩ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠧࠨዪ"))
        bstack1l1l1l11ll1_opy_, bstack1l1l1l11l11_opy_ = bstack1l1l1l1l11l_opy_[0]
        driver = bstack1l1l1l11ll1_opy_()
        if not driver:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢያ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠢࠣዬ"))
            return
        bstack1l1l11llll1_opy_ = {
            TestFramework.bstack1ll11lll1ll_opy_: bstack1l1l11_opy_ (u"ࠣࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦይ"),
            TestFramework.bstack1ll11ll1lll_opy_: bstack1l1l11_opy_ (u"ࠤࡷࡩࡸࡺࠠࡶࡷ࡬ࡨࠧዮ"),
            TestFramework.bstack1l1l11lll1l_opy_: bstack1l1l11_opy_ (u"ࠥࡸࡪࡹࡴࠡࡴࡨࡶࡺࡴࠠ࡯ࡣࡰࡩࠧዯ")
        }
        bstack1l1l1l11l1l_opy_ = { key: f.bstack1lllll1l1l1_opy_(instance, key) for key in bstack1l1l11llll1_opy_ }
        bstack1l1l11lllll_opy_ = [key for key, value in bstack1l1l1l11l1l_opy_.items() if not value]
        if bstack1l1l11lllll_opy_:
            for key in bstack1l1l11lllll_opy_:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠢደ") + str(key) + bstack1l1l11_opy_ (u"ࠧࠨዱ"))
            return
        platform_index = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll111ll_opy_.bstack1ll1l1111l1_opy_, 0)
        if self.bstack1l1l1l111ll_opy_.percy_capture_mode == bstack1l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣዲ"):
            bstack11l1l11lll_opy_ = bstack1l1l1l11l1l_opy_.get(TestFramework.bstack1l1l11lll1l_opy_) + bstack1l1l11_opy_ (u"ࠢ࠮ࡶࡨࡷࡹࡩࡡࡴࡧࠥዳ")
            bstack1ll11ll11l1_opy_ = bstack1lll111lll1_opy_.bstack1ll11ll1l11_opy_(EVENTS.bstack1l1l11ll1l1_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11l1l11lll_opy_,
                bstack1lll11llll_opy_=bstack1l1l1l11l1l_opy_[TestFramework.bstack1ll11lll1ll_opy_],
                bstack11l111l11l_opy_=bstack1l1l1l11l1l_opy_[TestFramework.bstack1ll11ll1lll_opy_],
                bstack11l1l1111_opy_=platform_index
            )
            bstack1lll111lll1_opy_.end(EVENTS.bstack1l1l11ll1l1_opy_.value, bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣዴ"), bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠤ࠽ࡩࡳࡪࠢድ"), True, None, None, None, None, test_name=bstack11l1l11lll_opy_)
    def bstack11l11l1lll_opy_(self, driver, platform_index):
        if self.bstack11llll111_opy_.bstack11llllll_opy_() is True or self.bstack11llll111_opy_.capturing() is True:
            return
        self.bstack11llll111_opy_.bstack111llll11_opy_()
        while not self.bstack11llll111_opy_.bstack11llllll_opy_():
            bstack1l1l11lll11_opy_ = self.bstack11llll111_opy_.bstack1l111lll1_opy_()
            self.bstack111ll11l_opy_(driver, bstack1l1l11lll11_opy_, platform_index)
        self.bstack11llll111_opy_.bstack1l11ll1l1_opy_()
    def bstack111ll11l_opy_(self, driver, bstack111llll11l_opy_, platform_index, test=None):
        from bstack_utils.bstack111l11ll_opy_ import bstack1lll111lll1_opy_
        bstack1ll11ll11l1_opy_ = bstack1lll111lll1_opy_.bstack1ll11ll1l11_opy_(EVENTS.bstack1l11ll1l11_opy_.value)
        if test != None:
            bstack1lll11llll_opy_ = getattr(test, bstack1l1l11_opy_ (u"ࠪࡲࡦࡳࡥࠨዶ"), None)
            bstack11l111l11l_opy_ = getattr(test, bstack1l1l11_opy_ (u"ࠫࡺࡻࡩࡥࠩዷ"), None)
            PercySDK.screenshot(driver, bstack111llll11l_opy_, bstack1lll11llll_opy_=bstack1lll11llll_opy_, bstack11l111l11l_opy_=bstack11l111l11l_opy_, bstack11l1l1111_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack111llll11l_opy_)
        bstack1lll111lll1_opy_.end(EVENTS.bstack1l11ll1l11_opy_.value, bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧዸ"), bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠨ࠺ࡦࡰࡧࠦዹ"), True, None, None, None, None, test_name=bstack111llll11l_opy_)
    def bstack1l1l11ll1ll_opy_(self):
        os.environ[bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬዺ")] = str(self.bstack1l1l1l111ll_opy_.success)
        os.environ[bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬዻ")] = str(self.bstack1l1l1l111ll_opy_.percy_capture_mode)
        self.percy.bstack1l1l1l111l1_opy_(self.bstack1l1l1l111ll_opy_.is_percy_auto_enabled)
        self.percy.bstack1l1l1l11111_opy_(self.bstack1l1l1l111ll_opy_.percy_build_id)