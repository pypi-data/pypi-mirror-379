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
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llllllll1l_opy_,
    bstack1lllll11lll_opy_,
    bstack1llll1lllll_opy_,
    bstack1llll1llll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll11111ll_opy_ import bstack1ll1ll111ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_, bstack1lll1l11l11_opy_
from browserstack_sdk.sdk_cli.bstack1l1lllll1ll_opy_ import bstack1l1llll11ll_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1l1ll1l11ll_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1ll1ll1111l_opy_(bstack1l1llll11ll_opy_):
    bstack1l11lllll1l_opy_ = bstack1l1l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡴ࡬ࡺࡪࡸࡳࠣᏇ")
    bstack1l1l1lllll1_opy_ = bstack1l1l11_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᏈ")
    bstack1l1l11111l1_opy_ = bstack1l1l11_opy_ (u"ࠦࡳࡵ࡮ࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᏉ")
    bstack1l11lll1lll_opy_ = bstack1l1l11_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᏊ")
    bstack1l11llll11l_opy_ = bstack1l1l11_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡤࡸࡥࡧࡵࠥᏋ")
    bstack1l1lll1l1l1_opy_ = bstack1l1l11_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡩࡲࡦࡣࡷࡩࡩࠨᏌ")
    bstack1l11llll1l1_opy_ = bstack1l1l11_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦᏍ")
    bstack1l11llll1ll_opy_ = bstack1l1l11_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡴࡶࡤࡸࡺࡹࠢᏎ")
    def __init__(self):
        super().__init__(bstack1l1lllll111_opy_=self.bstack1l11lllll1l_opy_, frameworks=[bstack1ll1ll111ll_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1ll111l11l1_opy_((bstack1lll1ll1ll1_opy_.BEFORE_EACH, bstack1lll1l1l1l1_opy_.POST), self.bstack1l11l1l11ll_opy_)
        TestFramework.bstack1ll111l11l1_opy_((bstack1lll1ll1ll1_opy_.TEST, bstack1lll1l1l1l1_opy_.PRE), self.bstack1ll111l1111_opy_)
        TestFramework.bstack1ll111l11l1_opy_((bstack1lll1ll1ll1_opy_.TEST, bstack1lll1l1l1l1_opy_.POST), self.bstack1ll111l1lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1l11ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1l1l1l11l_opy_ = self.bstack1l11l11ll1l_opy_(instance.context)
        if not bstack1l1l1l1l11l_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᏏ") + str(bstack1lllll11ll1_opy_) + bstack1l1l11_opy_ (u"ࠦࠧᏐ"))
        f.bstack1llll1l1ll1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l1l1lllll1_opy_, bstack1l1l1l1l11l_opy_)
        bstack1l11l1l1111_opy_ = self.bstack1l11l11ll1l_opy_(instance.context, bstack1l11l11llll_opy_=False)
        f.bstack1llll1l1ll1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l1l11111l1_opy_, bstack1l11l1l1111_opy_)
    def bstack1ll111l1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11l1l11ll_opy_(f, instance, bstack1lllll11ll1_opy_, *args, **kwargs)
        if not f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l11llll1l1_opy_, False):
            self.__1l11l1l111l_opy_(f,instance,bstack1lllll11ll1_opy_)
    def bstack1ll111l1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11l1l11ll_opy_(f, instance, bstack1lllll11ll1_opy_, *args, **kwargs)
        if not f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l11llll1l1_opy_, False):
            self.__1l11l1l111l_opy_(f, instance, bstack1lllll11ll1_opy_)
        if not f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l11llll1ll_opy_, False):
            self.__1l11l1l1ll1_opy_(f, instance, bstack1lllll11ll1_opy_)
    def bstack1l11l1l11l1_opy_(
        self,
        f: bstack1ll1ll111ll_opy_,
        driver: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1l1llll1l11_opy_(instance):
            return
        if f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l11llll1ll_opy_, False):
            return
        driver.execute_script(
            bstack1l1l11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᏑ").format(
                json.dumps(
                    {
                        bstack1l1l11_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᏒ"): bstack1l1l11_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᏓ"),
                        bstack1l1l11_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᏔ"): {bstack1l1l11_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᏕ"): result},
                    }
                )
            )
        )
        f.bstack1llll1l1ll1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l11llll1ll_opy_, True)
    def bstack1l11l11ll1l_opy_(self, context: bstack1llll1llll1_opy_, bstack1l11l11llll_opy_= True):
        if bstack1l11l11llll_opy_:
            bstack1l1l1l1l11l_opy_ = self.bstack1l1lllll1l1_opy_(context, reverse=True)
        else:
            bstack1l1l1l1l11l_opy_ = self.bstack1l1lll1lll1_opy_(context, reverse=True)
        return [f for f in bstack1l1l1l1l11l_opy_ if f[1].state != bstack1lllll1lll1_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1l11l111ll_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def __1l11l1l1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᏖ")).get(bstack1l1l11_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᏗ")):
            bstack1l1l1l1l11l_opy_ = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l1l1lllll1_opy_, [])
            if not bstack1l1l1l1l11l_opy_:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᏘ") + str(bstack1lllll11ll1_opy_) + bstack1l1l11_opy_ (u"ࠨࠢᏙ"))
                return
            driver = bstack1l1l1l1l11l_opy_[0][0]()
            status = f.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1l1l1111111_opy_, None)
            if not status:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᏚ") + str(bstack1lllll11ll1_opy_) + bstack1l1l11_opy_ (u"ࠣࠤᏛ"))
                return
            bstack1l11lll1l1l_opy_ = {bstack1l1l11_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᏜ"): status.lower()}
            bstack1l11llllll1_opy_ = f.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1l1l1111l11_opy_, None)
            if status.lower() == bstack1l1l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᏝ") and bstack1l11llllll1_opy_ is not None:
                bstack1l11lll1l1l_opy_[bstack1l1l11_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᏞ")] = bstack1l11llllll1_opy_[0][bstack1l1l11_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᏟ")][0] if isinstance(bstack1l11llllll1_opy_, list) else str(bstack1l11llllll1_opy_)
            driver.execute_script(
                bstack1l1l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᏠ").format(
                    json.dumps(
                        {
                            bstack1l1l11_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᏡ"): bstack1l1l11_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᏢ"),
                            bstack1l1l11_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᏣ"): bstack1l11lll1l1l_opy_,
                        }
                    )
                )
            )
            f.bstack1llll1l1ll1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l11llll1ll_opy_, True)
    @measure(event_name=EVENTS.bstack1l1l1l1lll_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def __1l11l1l111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᏤ")).get(bstack1l1l11_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨᏥ")):
            test_name = f.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1l11l1l1l11_opy_, None)
            if not test_name:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦᏦ"))
                return
            bstack1l1l1l1l11l_opy_ = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l1l1lllll1_opy_, [])
            if not bstack1l1l1l1l11l_opy_:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᏧ") + str(bstack1lllll11ll1_opy_) + bstack1l1l11_opy_ (u"ࠢࠣᏨ"))
                return
            for bstack1l1l1l11ll1_opy_, bstack1l11l11ll11_opy_ in bstack1l1l1l1l11l_opy_:
                if not bstack1ll1ll111ll_opy_.bstack1l1llll1l11_opy_(bstack1l11l11ll11_opy_):
                    continue
                driver = bstack1l1l1l11ll1_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack1l1l11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᏩ").format(
                        json.dumps(
                            {
                                bstack1l1l11_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᏪ"): bstack1l1l11_opy_ (u"ࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᏫ"),
                                bstack1l1l11_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᏬ"): {bstack1l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᏭ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llll1l1ll1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l11llll1l1_opy_, True)
    def bstack1l1ll11l111_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        f: TestFramework,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11l1l11ll_opy_(f, instance, bstack1lllll11ll1_opy_, *args, **kwargs)
        bstack1l1l1l1l11l_opy_ = [d for d, _ in f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l1l1lllll1_opy_, [])]
        if not bstack1l1l1l1l11l_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥࡺ࡯ࠡ࡮࡬ࡲࡰࠨᏮ"))
            return
        if not bstack1l1ll1l11ll_opy_():
            self.logger.debug(bstack1l1l11_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᏯ"))
            return
        for bstack1l11l1ll111_opy_ in bstack1l1l1l1l11l_opy_:
            driver = bstack1l11l1ll111_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1l1l11_opy_ (u"ࠣࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡔࡻࡱࡧ࠿ࠨᏰ") + str(timestamp)
            driver.execute_script(
                bstack1l1l11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᏱ").format(
                    json.dumps(
                        {
                            bstack1l1l11_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᏲ"): bstack1l1l11_opy_ (u"ࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨᏳ"),
                            bstack1l1l11_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᏴ"): {
                                bstack1l1l11_opy_ (u"ࠨࡴࡺࡲࡨࠦᏵ"): bstack1l1l11_opy_ (u"ࠢࡂࡰࡱࡳࡹࡧࡴࡪࡱࡱࠦ᏶"),
                                bstack1l1l11_opy_ (u"ࠣࡦࡤࡸࡦࠨ᏷"): data,
                                bstack1l1l11_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬ࠣᏸ"): bstack1l1l11_opy_ (u"ࠥࡨࡪࡨࡵࡨࠤᏹ")
                            }
                        }
                    )
                )
            )
    def bstack1l1ll111l11_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        f: TestFramework,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11l1l11ll_opy_(f, instance, bstack1lllll11ll1_opy_, *args, **kwargs)
        keys = [
            bstack1ll1ll1111l_opy_.bstack1l1l1lllll1_opy_,
            bstack1ll1ll1111l_opy_.bstack1l1l11111l1_opy_,
        ]
        bstack1l1l1l1l11l_opy_ = []
        for key in keys:
            bstack1l1l1l1l11l_opy_.extend(f.bstack1lllll1l1l1_opy_(instance, key, []))
        if not bstack1l1l1l1l11l_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡡ࡯ࡻࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥࡺ࡯ࠡ࡮࡬ࡲࡰࠨᏺ"))
            return
        if f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l1lll1l1l1_opy_, False):
            self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡃࡃࡖࠣࡥࡱࡸࡥࡢࡦࡼࠤࡨࡸࡥࡢࡶࡨࡨࠧᏻ"))
            return
        self.bstack1ll1111ll11_opy_()
        bstack11l1ll1111_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1ll1l1111l1_opy_)
        req.test_framework_name = TestFramework.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1ll1111l11l_opy_)
        req.test_framework_version = TestFramework.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1l1l1ll11ll_opy_)
        req.test_framework_state = bstack1lllll11ll1_opy_[0].name
        req.test_hook_state = bstack1lllll11ll1_opy_[1].name
        req.test_uuid = TestFramework.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1ll11ll1lll_opy_)
        for bstack1l1l1l11ll1_opy_, driver in bstack1l1l1l1l11l_opy_:
            try:
                webdriver = bstack1l1l1l11ll1_opy_()
                if webdriver is None:
                    self.logger.debug(bstack1l1l11_opy_ (u"ࠨࡗࡦࡤࡇࡶ࡮ࡼࡥࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠥ࠮ࡲࡦࡨࡨࡶࡪࡴࡣࡦࠢࡨࡼࡵ࡯ࡲࡦࡦࠬࠦᏼ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack1l1l11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨᏽ")
                    if bstack1ll1ll111ll_opy_.bstack1lllll1l1l1_opy_(driver, bstack1ll1ll111ll_opy_.bstack1l11l1l1l1l_opy_, False)
                    else bstack1l1l11_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠢ᏾")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1ll1ll111ll_opy_.bstack1lllll1l1l1_opy_(driver, bstack1ll1ll111ll_opy_.bstack1l1l111l1l1_opy_, bstack1l1l11_opy_ (u"ࠤࠥ᏿"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1ll1ll111ll_opy_.bstack1lllll1l1l1_opy_(driver, bstack1ll1ll111ll_opy_.bstack1l1l111llll_opy_, bstack1l1l11_opy_ (u"ࠥࠦ᐀"))
                caps = None
                if hasattr(webdriver, bstack1l1l11_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᐁ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack1l1l11_opy_ (u"࡙ࠧࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࡪࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡤࡪࡴࡨࡧࡹࡲࡹࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷ࠴ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᐂ"))
                    except Exception as e:
                        self.logger.debug(bstack1l1l11_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡪࡩࡹࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥ࡬ࡲࡰ࡯ࠣࡨࡷ࡯ࡶࡦࡴ࠱ࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠼ࠣࠦᐃ") + str(e) + bstack1l1l11_opy_ (u"ࠢࠣᐄ"))
                try:
                    bstack1l11l1l1lll_opy_ = json.dumps(caps).encode(bstack1l1l11_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᐅ")) if caps else bstack1l11l11lll1_opy_ (u"ࠤࡾࢁࠧᐆ")
                    req.capabilities = bstack1l11l1l1lll_opy_
                except Exception as e:
                    self.logger.debug(bstack1l1l11_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡤࡤࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡱࡨࠥࡹࡥࡳ࡫ࡤࡰ࡮ࢀࡥࠡࡥࡤࡴࡸࠦࡦࡰࡴࠣࡶࡪࡷࡵࡦࡵࡷ࠾ࠥࠨᐇ") + str(e) + bstack1l1l11_opy_ (u"ࠦࠧᐈ"))
            except Exception as e:
                self.logger.error(bstack1l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡷࡩࡲࡀࠠࠣᐉ") + str(str(e)) + bstack1l1l11_opy_ (u"ࠨࠢᐊ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1ll1111llll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_],
        *args,
        **kwargs
    ):
        bstack1l1l1l1l11l_opy_ = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l1l1lllll1_opy_, [])
        if not bstack1l1ll1l11ll_opy_() and len(bstack1l1l1l1l11l_opy_) == 0:
            bstack1l1l1l1l11l_opy_ = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l1l11111l1_opy_, [])
        if not bstack1l1l1l1l11l_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᐋ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠣࠤᐌ"))
            return {}
        if len(bstack1l1l1l1l11l_opy_) > 1:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᐍ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠥࠦᐎ"))
            return {}
        bstack1l1l1l11ll1_opy_, bstack1l1l1l11l11_opy_ = bstack1l1l1l1l11l_opy_[0]
        driver = bstack1l1l1l11ll1_opy_()
        if not driver:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᐏ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠧࠨᐐ"))
            return {}
        capabilities = f.bstack1lllll1l1l1_opy_(bstack1l1l1l11l11_opy_, bstack1ll1ll111ll_opy_.bstack1l1l1111lll_opy_)
        if not capabilities:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡪࡴࡻ࡮ࡥࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᐑ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠢࠣᐒ"))
            return {}
        return capabilities.get(bstack1l1l11_opy_ (u"ࠣࡣ࡯ࡻࡦࡿࡳࡎࡣࡷࡧ࡭ࠨᐓ"), {})
    def bstack1ll11l11ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_],
        *args,
        **kwargs
    ):
        bstack1l1l1l1l11l_opy_ = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l1l1lllll1_opy_, [])
        if not bstack1l1ll1l11ll_opy_() and len(bstack1l1l1l1l11l_opy_) == 0:
            bstack1l1l1l1l11l_opy_ = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll1111l_opy_.bstack1l1l11111l1_opy_, [])
        if not bstack1l1l1l1l11l_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᐔ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠥࠦᐕ"))
            return
        if len(bstack1l1l1l1l11l_opy_) > 1:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࡭ࡧࡱࠬࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᐖ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠧࠨᐗ"))
        bstack1l1l1l11ll1_opy_, bstack1l1l1l11l11_opy_ = bstack1l1l1l1l11l_opy_[0]
        driver = bstack1l1l1l11ll1_opy_()
        if not driver:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᐘ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠢࠣᐙ"))
            return
        return driver