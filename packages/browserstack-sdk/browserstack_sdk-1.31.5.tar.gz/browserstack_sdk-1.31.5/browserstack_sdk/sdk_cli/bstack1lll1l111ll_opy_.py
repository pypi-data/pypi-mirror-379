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
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1lllll11111_opy_ import (
    bstack1llll1lllll_opy_,
    bstack1llllll1lll_opy_,
    bstack1llll1llll1_opy_,
    bstack1lllll11l11_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1l1l1lllll1_opy_, bstack111l1111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll111l11l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_, bstack1ll1lllll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1111l_opy_ import bstack1llll1l111l_opy_
from browserstack_sdk.sdk_cli.bstack1l1lllll1l1_opy_ import bstack1l1lll1llll_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack11llllll1_opy_ import bstack1ll111111_opy_, bstack1l11111l_opy_, bstack1l1l1ll111_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll111ll11_opy_(bstack1l1lll1llll_opy_):
    bstack1l11lll1ll1_opy_ = bstack1l11l11_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡷ࡯ࡶࡦࡴࡶࠦጛ")
    bstack1l1l1lll1ll_opy_ = bstack1l11l11_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧጜ")
    bstack1l1l111111l_opy_ = bstack1l11l11_opy_ (u"ࠢ࡯ࡱࡱࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤጝ")
    bstack1l1l1111l1l_opy_ = bstack1l11l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣጞ")
    bstack1l1l11111l1_opy_ = bstack1l11l11_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡠࡴࡨࡪࡸࠨጟ")
    bstack1l1l1llll1l_opy_ = bstack1l11l11_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡥࡵࡩࡦࡺࡥࡥࠤጠ")
    bstack1l11lllll1l_opy_ = bstack1l11l11_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡱࡥࡲ࡫ࠢጡ")
    bstack1l11lllll11_opy_ = bstack1l11l11_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡷࡹࡧࡴࡶࡵࠥጢ")
    def __init__(self):
        super().__init__(bstack1l1lll1lll1_opy_=self.bstack1l11lll1ll1_opy_, frameworks=[bstack1lll111l11l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1ll111l11ll_opy_((bstack1llll11ll11_opy_.BEFORE_EACH, bstack1ll1ll11111_opy_.POST), self.bstack1l11llll1l1_opy_)
        if bstack111l1111_opy_():
            TestFramework.bstack1ll111l11ll_opy_((bstack1llll11ll11_opy_.TEST, bstack1ll1ll11111_opy_.POST), self.bstack1ll1111lll1_opy_)
        else:
            TestFramework.bstack1ll111l11ll_opy_((bstack1llll11ll11_opy_.TEST, bstack1ll1ll11111_opy_.PRE), self.bstack1ll1111lll1_opy_)
        TestFramework.bstack1ll111l11ll_opy_((bstack1llll11ll11_opy_.TEST, bstack1ll1ll11111_opy_.POST), self.bstack1ll111l111l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11llll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1ll1lllll11_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs,
    ):
        bstack1l11lll1lll_opy_ = self.bstack1l11lllllll_opy_(instance.context)
        if not bstack1l11lll1lll_opy_:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡴࡦ࡭ࡥ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦጣ") + str(bstack1lllllll1l1_opy_) + bstack1l11l11_opy_ (u"ࠢࠣጤ"))
            return
        f.bstack1lllll1l1l1_opy_(instance, bstack1lll111ll11_opy_.bstack1l1l1lll1ll_opy_, bstack1l11lll1lll_opy_)
    def bstack1l11lllllll_opy_(self, context: bstack1lllll11l11_opy_, bstack1l1l1111l11_opy_= True):
        if bstack1l1l1111l11_opy_:
            bstack1l11lll1lll_opy_ = self.bstack1l1llll1111_opy_(context, reverse=True)
        else:
            bstack1l11lll1lll_opy_ = self.bstack1l1llll1lll_opy_(context, reverse=True)
        return [f for f in bstack1l11lll1lll_opy_ if f[1].state != bstack1llll1lllll_opy_.QUIT]
    def bstack1ll1111lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1ll1lllll11_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11llll1l1_opy_(f, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
        if not bstack1l1l1lllll1_opy_:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦጥ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠤࠥጦ"))
            return
        bstack1l11lll1lll_opy_ = f.bstack1llllll1l1l_opy_(instance, bstack1lll111ll11_opy_.bstack1l1l1lll1ll_opy_, [])
        if not bstack1l11lll1lll_opy_:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨጧ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠦࠧጨ"))
            return
        if len(bstack1l11lll1lll_opy_) > 1:
            self.logger.debug(
                bstack1ll1llll1ll_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢጩ"))
        bstack1l11lll1l1l_opy_, bstack1l1l1l111ll_opy_ = bstack1l11lll1lll_opy_[0]
        page = bstack1l11lll1l1l_opy_()
        if not page:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨጪ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠢࠣጫ"))
            return
        bstack1l1ll11l_opy_ = getattr(args[0], bstack1l11l11_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣጬ"), None)
        try:
            page.evaluate(bstack1l11l11_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥጭ"),
                        bstack1l11l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠧጮ") + json.dumps(
                            bstack1l1ll11l_opy_) + bstack1l11l11_opy_ (u"ࠦࢂࢃࠢጯ"))
        except Exception as e:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡼࡿࠥጰ"), e)
    def bstack1ll111l111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1ll1lllll11_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11llll1l1_opy_(f, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
        if not bstack1l1l1lllll1_opy_:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤጱ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠢࠣጲ"))
            return
        bstack1l11lll1lll_opy_ = f.bstack1llllll1l1l_opy_(instance, bstack1lll111ll11_opy_.bstack1l1l1lll1ll_opy_, [])
        if not bstack1l11lll1lll_opy_:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦጳ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠤࠥጴ"))
            return
        if len(bstack1l11lll1lll_opy_) > 1:
            self.logger.debug(
                bstack1ll1llll1ll_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡴࡦ࡭ࡥࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧጵ"))
        bstack1l11lll1l1l_opy_, bstack1l1l1l111ll_opy_ = bstack1l11lll1lll_opy_[0]
        page = bstack1l11lll1l1l_opy_()
        if not page:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦጶ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠧࠨጷ"))
            return
        status = f.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1l11llll11l_opy_, None)
        if not status:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠨ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤጸ") + str(bstack1lllllll1l1_opy_) + bstack1l11l11_opy_ (u"ࠢࠣጹ"))
            return
        bstack1l11llll111_opy_ = {bstack1l11l11_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣጺ"): status.lower()}
        bstack1l1l1111ll1_opy_ = f.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1l11llll1ll_opy_, None)
        if status.lower() == bstack1l11l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩጻ") and bstack1l1l1111ll1_opy_ is not None:
            bstack1l11llll111_opy_[bstack1l11l11_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪጼ")] = bstack1l1l1111ll1_opy_[0][bstack1l11l11_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧጽ")][0] if isinstance(bstack1l1l1111ll1_opy_, list) else str(bstack1l1l1111ll1_opy_)
        try:
              page.evaluate(
                    bstack1l11l11_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨጾ"),
                    bstack1l11l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࠫጿ")
                    + json.dumps(bstack1l11llll111_opy_)
                    + bstack1l11l11_opy_ (u"ࠢࡾࠤፀ")
                )
        except Exception as e:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥࢁࡽࠣፁ"), e)
    def bstack1l1ll1ll111_opy_(
        self,
        instance: bstack1ll1lllll11_opy_,
        f: TestFramework,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11llll1l1_opy_(f, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
        if not bstack1l1l1lllll1_opy_:
            self.logger.debug(
                bstack1ll1llll1ll_opy_ (u"ࠤࡰࡥࡷࡱ࡟ࡰ࠳࠴ࡽࡤࡹࡹ࡯ࡥ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥፂ"))
            return
        bstack1l11lll1lll_opy_ = f.bstack1llllll1l1l_opy_(instance, bstack1lll111ll11_opy_.bstack1l1l1lll1ll_opy_, [])
        if not bstack1l11lll1lll_opy_:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨፃ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠦࠧፄ"))
            return
        if len(bstack1l11lll1lll_opy_) > 1:
            self.logger.debug(
                bstack1ll1llll1ll_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢፅ"))
        bstack1l11lll1l1l_opy_, bstack1l1l1l111ll_opy_ = bstack1l11lll1lll_opy_[0]
        page = bstack1l11lll1l1l_opy_()
        if not page:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠨ࡭ࡢࡴ࡮ࡣࡴ࠷࠱ࡺࡡࡶࡽࡳࡩ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨፆ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠢࠣፇ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1l11l11_opy_ (u"ࠣࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡔࡻࡱࡧ࠿ࠨፈ") + str(timestamp)
        try:
            page.evaluate(
                bstack1l11l11_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥፉ"),
                bstack1l11l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨፊ").format(
                    json.dumps(
                        {
                            bstack1l11l11_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦፋ"): bstack1l11l11_opy_ (u"ࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢፌ"),
                            bstack1l11l11_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤፍ"): {
                                bstack1l11l11_opy_ (u"ࠢࡵࡻࡳࡩࠧፎ"): bstack1l11l11_opy_ (u"ࠣࡃࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠧፏ"),
                                bstack1l11l11_opy_ (u"ࠤࡧࡥࡹࡧࠢፐ"): data,
                                bstack1l11l11_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࠤፑ"): bstack1l11l11_opy_ (u"ࠦࡩ࡫ࡢࡶࡩࠥፒ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡱ࠴࠵ࡾࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࢀࢃࠢፓ"), e)
    def bstack1l1l1ll1ll1_opy_(
        self,
        instance: bstack1ll1lllll11_opy_,
        f: TestFramework,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11llll1l1_opy_(f, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
        if f.bstack1llllll1l1l_opy_(instance, bstack1lll111ll11_opy_.bstack1l1l1llll1l_opy_, False):
            return
        self.bstack1ll111l1111_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1ll11ll111l_opy_)
        req.test_framework_name = TestFramework.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1ll11l1l1ll_opy_)
        req.test_framework_version = TestFramework.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1l1l1ll1lll_opy_)
        req.test_framework_state = bstack1lllllll1l1_opy_[0].name
        req.test_hook_state = bstack1lllllll1l1_opy_[1].name
        req.test_uuid = TestFramework.bstack1llllll1l1l_opy_(instance, TestFramework.bstack1ll111ll1ll_opy_)
        for bstack1l11llllll1_opy_ in bstack1llll1l111l_opy_.bstack1lllll1111l_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1l11l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠧፔ")
                if bstack1l1l1lllll1_opy_
                else bstack1l11l11_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩࠨፕ")
            )
            session.ref = bstack1l11llllll1_opy_.ref()
            session.hub_url = bstack1llll1l111l_opy_.bstack1llllll1l1l_opy_(bstack1l11llllll1_opy_, bstack1llll1l111l_opy_.bstack1l1l111l1ll_opy_, bstack1l11l11_opy_ (u"ࠣࠤፖ"))
            session.framework_name = bstack1l11llllll1_opy_.framework_name
            session.framework_version = bstack1l11llllll1_opy_.framework_version
            session.framework_session_id = bstack1llll1l111l_opy_.bstack1llllll1l1l_opy_(bstack1l11llllll1_opy_, bstack1llll1l111l_opy_.bstack1l1l11l11l1_opy_, bstack1l11l11_opy_ (u"ࠤࠥፗ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1ll11111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1ll1lllll11_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs
    ):
        bstack1l11lll1lll_opy_ = f.bstack1llllll1l1l_opy_(instance, bstack1lll111ll11_opy_.bstack1l1l1lll1ll_opy_, [])
        if not bstack1l11lll1lll_opy_:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦፘ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠦࠧፙ"))
            return
        if len(bstack1l11lll1lll_opy_) > 1:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨፚ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠨࠢ፛"))
        bstack1l11lll1l1l_opy_, bstack1l1l1l111ll_opy_ = bstack1l11lll1lll_opy_[0]
        page = bstack1l11lll1l1l_opy_()
        if not page:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢ፜") + str(kwargs) + bstack1l11l11_opy_ (u"ࠣࠤ፝"))
            return
        return page
    def bstack1ll1111llll_opy_(
        self,
        f: TestFramework,
        instance: bstack1ll1lllll11_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1l1l11111ll_opy_ = {}
        for bstack1l11llllll1_opy_ in bstack1llll1l111l_opy_.bstack1lllll1111l_opy_.values():
            caps = bstack1llll1l111l_opy_.bstack1llllll1l1l_opy_(bstack1l11llllll1_opy_, bstack1llll1l111l_opy_.bstack1l1l11l1ll1_opy_, bstack1l11l11_opy_ (u"ࠤࠥ፞"))
        bstack1l1l11111ll_opy_[bstack1l11l11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣ፟")] = caps.get(bstack1l11l11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧ፠"), bstack1l11l11_opy_ (u"ࠧࠨ፡"))
        bstack1l1l11111ll_opy_[bstack1l11l11_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ።")] = caps.get(bstack1l11l11_opy_ (u"ࠢࡰࡵࠥ፣"), bstack1l11l11_opy_ (u"ࠣࠤ፤"))
        bstack1l1l11111ll_opy_[bstack1l11l11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ፥")] = caps.get(bstack1l11l11_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ፦"), bstack1l11l11_opy_ (u"ࠦࠧ፧"))
        bstack1l1l11111ll_opy_[bstack1l11l11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨ፨")] = caps.get(bstack1l11l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ፩"), bstack1l11l11_opy_ (u"ࠢࠣ፪"))
        return bstack1l1l11111ll_opy_
    def bstack1ll1l111l1l_opy_(self, page: object, bstack1ll111l1l1l_opy_, args={}):
        try:
            bstack1l1l1111111_opy_ = bstack1l11l11_opy_ (u"ࠣࠤࠥࠬ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࠨ࠯࠰࠱ࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵࠬࠤࢀࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡱࡩࡼࠦࡐࡳࡱࡰ࡭ࡸ࡫ࠨࠩࡴࡨࡷࡴࡲࡶࡦ࠮ࠣࡶࡪࡰࡥࡤࡶࠬࠤࡂࡄࠠࡼࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡷࡹࡧࡣ࡬ࡕࡧ࡯ࡆࡸࡧࡴ࠰ࡳࡹࡸ࡮ࠨࡳࡧࡶࡳࡱࡼࡥࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡾࡪࡳࡥࡢࡰࡦࡼࢁࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࡿࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࢂ࠯ࠨࡼࡣࡵ࡫ࡤࡰࡳࡰࡰࢀ࠭ࠧࠨࠢ፫")
            bstack1ll111l1l1l_opy_ = bstack1ll111l1l1l_opy_.replace(bstack1l11l11_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧ፬"), bstack1l11l11_opy_ (u"ࠥࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵࠥ፭"))
            script = bstack1l1l1111111_opy_.format(fn_body=bstack1ll111l1l1l_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1l11l11_opy_ (u"ࠦࡦ࠷࠱ࡺࡡࡶࡧࡷ࡯ࡰࡵࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡊࡸࡲࡰࡴࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡥ࠶࠷ࡹࠡࡵࡦࡶ࡮ࡶࡴ࠭ࠢࠥ፮") + str(e) + bstack1l11l11_opy_ (u"ࠧࠨ፯"))