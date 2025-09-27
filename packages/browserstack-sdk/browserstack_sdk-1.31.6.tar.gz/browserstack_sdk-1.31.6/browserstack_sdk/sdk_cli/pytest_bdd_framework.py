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
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1llll1l1l1l_opy_ import bstack1111111111_opy_
from browserstack_sdk.sdk_cli.utils.bstack11111ll11_opy_ import bstack11llllll11l_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1ll1ll1_opy_,
    bstack1lll1l11l11_opy_,
    bstack1lll1l1l1l1_opy_,
    bstack1l111111l11_opy_,
    bstack1lll111llll_opy_,
)
import traceback
from bstack_utils.helper import bstack1l1lll1l111_opy_
from bstack_utils.bstack111l11ll_opy_ import bstack1lll111lll1_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1lll1111l11_opy_ import bstack1lll1ll11ll_opy_
from browserstack_sdk.sdk_cli.bstack1111111ll1_opy_ import bstack11111111ll_opy_
bstack1l1ll11111l_opy_ = bstack1l1lll1l111_opy_()
bstack1l1l1l1ll1l_opy_ = bstack1l1l11_opy_ (u"ࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨᐴ")
bstack11lllll111l_opy_ = bstack1l1l11_opy_ (u"ࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠥᐵ")
bstack1l111l111ll_opy_ = bstack1l1l11_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠢᐶ")
bstack1l11l111111_opy_ = 1.0
_1l1l1lll1l1_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1l111lll1l1_opy_ = bstack1l1l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤᐷ")
    bstack1l111llll11_opy_ = bstack1l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠣᐸ")
    bstack1l1111ll11l_opy_ = bstack1l1l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࠥᐹ")
    bstack1l111l1ll11_opy_ = bstack1l1l11_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠ࡮ࡤࡷࡹࡥࡳࡵࡣࡵࡸࡪࡪࠢᐺ")
    bstack1l11111ll11_opy_ = bstack1l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡ࡯ࡥࡸࡺ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤᐻ")
    bstack11lllll11ll_opy_: bool
    bstack1111111ll1_opy_: bstack11111111ll_opy_  = None
    bstack1l111l11lll_opy_ = [
        bstack1lll1ll1ll1_opy_.BEFORE_ALL,
        bstack1lll1ll1ll1_opy_.AFTER_ALL,
        bstack1lll1ll1ll1_opy_.BEFORE_EACH,
        bstack1lll1ll1ll1_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1l11111l1l1_opy_: Dict[str, str],
        bstack1ll1l111l1l_opy_: List[str]=[bstack1l1l11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᐼ")],
        bstack1111111ll1_opy_: bstack11111111ll_opy_ = None,
        bstack1lll11111l1_opy_=None
    ):
        super().__init__(bstack1ll1l111l1l_opy_, bstack1l11111l1l1_opy_, bstack1111111ll1_opy_)
        self.bstack11lllll11ll_opy_ = any(bstack1l1l11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᐽ") in item.lower() for item in bstack1ll1l111l1l_opy_)
        self.bstack1lll11111l1_opy_ = bstack1lll11111l1_opy_
    def track_event(
        self,
        context: bstack1l111111l11_opy_,
        test_framework_state: bstack1lll1ll1ll1_opy_,
        test_hook_state: bstack1lll1l1l1l1_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1ll1ll1_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1l111l11lll_opy_:
            bstack11llllll11l_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1ll1ll1_opy_.NONE:
            self.logger.warning(bstack1l1l11_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦࡦࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࠥᐾ") + str(test_hook_state) + bstack1l1l11_opy_ (u"ࠥࠦᐿ"))
            return
        if not self.bstack11lllll11ll_opy_:
            self.logger.warning(bstack1l1l11_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡁࠧᑀ") + str(str(self.bstack1ll1l111l1l_opy_)) + bstack1l1l11_opy_ (u"ࠧࠨᑁ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l1l11_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᑂ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠢࠣᑃ"))
            return
        instance = self.__1l111l1llll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡣࡵ࡫ࡸࡃࠢᑄ") + str(args) + bstack1l1l11_opy_ (u"ࠤࠥᑅ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l111l11lll_opy_ and test_hook_state == bstack1lll1l1l1l1_opy_.PRE:
                bstack1ll11ll11l1_opy_ = bstack1lll111lll1_opy_.bstack1ll11ll1l11_opy_(EVENTS.bstack1l1ll1111l_opy_.value)
                name = str(EVENTS.bstack1l1ll1111l_opy_.name)+bstack1l1l11_opy_ (u"ࠥ࠾ࠧᑆ")+str(test_framework_state.name)
                TestFramework.bstack1l1111111ll_opy_(instance, name, bstack1ll11ll11l1_opy_)
        except Exception as e:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࠡࡧࡵࡶࡴࡸࠠࡱࡴࡨ࠾ࠥࢁࡽࠣᑇ").format(e))
        try:
            if test_framework_state == bstack1lll1ll1ll1_opy_.TEST:
                if not TestFramework.bstack1llllll111l_opy_(instance, TestFramework.bstack1l111l1l1l1_opy_) and test_hook_state == bstack1lll1l1l1l1_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1l111ll1ll1_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡲ࡯ࡢࡦࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧᑈ") + str(test_hook_state) + bstack1l1l11_opy_ (u"ࠨࠢᑉ"))
                if test_hook_state == bstack1lll1l1l1l1_opy_.PRE and not TestFramework.bstack1llllll111l_opy_(instance, TestFramework.bstack1l1ll1l1111_opy_):
                    TestFramework.bstack1llll1l1ll1_opy_(instance, TestFramework.bstack1l1ll1l1111_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1l111ll11ll_opy_(instance, args)
                    self.logger.debug(bstack1l1l11_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡶࡸࡦࡸࡴࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧᑊ") + str(test_hook_state) + bstack1l1l11_opy_ (u"ࠣࠤᑋ"))
                elif test_hook_state == bstack1lll1l1l1l1_opy_.POST and not TestFramework.bstack1llllll111l_opy_(instance, TestFramework.bstack1l1ll1l1l11_opy_):
                    TestFramework.bstack1llll1l1ll1_opy_(instance, TestFramework.bstack1l1ll1l1l11_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡶࡩࡹࠦࡴࡦࡵࡷ࠱ࡪࡴࡤࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧᑌ") + str(test_hook_state) + bstack1l1l11_opy_ (u"ࠥࠦᑍ"))
            elif test_framework_state == bstack1lll1ll1ll1_opy_.STEP:
                if test_hook_state == bstack1lll1l1l1l1_opy_.PRE:
                    PytestBDDFramework.__1l111ll1lll_opy_(instance, args)
                elif test_hook_state == bstack1lll1l1l1l1_opy_.POST:
                    PytestBDDFramework.__11llllll1l1_opy_(instance, args)
            elif test_framework_state == bstack1lll1ll1ll1_opy_.LOG and test_hook_state == bstack1lll1l1l1l1_opy_.POST:
                PytestBDDFramework.__11lllll1ll1_opy_(instance, *args)
            elif test_framework_state == bstack1lll1ll1ll1_opy_.LOG_REPORT and test_hook_state == bstack1lll1l1l1l1_opy_.POST:
                self.__1l11111ll1l_opy_(instance, *args)
                self.__1l1111l1lll_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1l111l11lll_opy_:
                self.__1l1111l11ll_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᑎ") + str(instance.ref()) + bstack1l1l11_opy_ (u"ࠧࠨᑏ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1l1111lll1l_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l111l11lll_opy_ and test_hook_state == bstack1lll1l1l1l1_opy_.POST:
                name = str(EVENTS.bstack1l1ll1111l_opy_.name)+bstack1l1l11_opy_ (u"ࠨ࠺ࠣᑐ")+str(test_framework_state.name)
                bstack1ll11ll11l1_opy_ = TestFramework.bstack11lllll11l1_opy_(instance, name)
                bstack1lll111lll1_opy_.end(EVENTS.bstack1l1ll1111l_opy_.value, bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᑑ"), bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᑒ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤᑓ").format(e))
    def bstack1l1ll111lll_opy_(self):
        return self.bstack11lllll11ll_opy_
    def __1l11111l11l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l1l11_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢᑔ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1l1ll1lll11_opy_(rep, [bstack1l1l11_opy_ (u"ࠦࡼ࡮ࡥ࡯ࠤᑕ"), bstack1l1l11_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨᑖ"), bstack1l1l11_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨᑗ"), bstack1l1l11_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢᑘ"), bstack1l1l11_opy_ (u"ࠣࡵ࡮࡭ࡵࡶࡥࡥࠤᑙ"), bstack1l1l11_opy_ (u"ࠤ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠣᑚ")])
        return None
    def __1l11111ll1l_opy_(self, instance: bstack1lll1l11l11_opy_, *args):
        result = self.__1l11111l11l_opy_(*args)
        if not result:
            return
        failure = None
        bstack111111l11l_opy_ = None
        if result.get(bstack1l1l11_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᑛ"), None) == bstack1l1l11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᑜ") and len(args) > 1 and getattr(args[1], bstack1l1l11_opy_ (u"ࠧ࡫ࡸࡤ࡫ࡱࡪࡴࠨᑝ"), None) is not None:
            failure = [{bstack1l1l11_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᑞ"): [args[1].excinfo.exconly(), result.get(bstack1l1l11_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨᑟ"), None)]}]
            bstack111111l11l_opy_ = bstack1l1l11_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤᑠ") if bstack1l1l11_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧᑡ") in getattr(args[1].excinfo, bstack1l1l11_opy_ (u"ࠥࡸࡾࡶࡥ࡯ࡣࡰࡩࠧᑢ"), bstack1l1l11_opy_ (u"ࠦࠧᑣ")) else bstack1l1l11_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨᑤ")
        bstack1l1111llll1_opy_ = result.get(bstack1l1l11_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢᑥ"), TestFramework.bstack1l11111111l_opy_)
        if bstack1l1111llll1_opy_ != TestFramework.bstack1l11111111l_opy_:
            TestFramework.bstack1llll1l1ll1_opy_(instance, TestFramework.bstack1l1ll1111l1_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1l111ll11l1_opy_(instance, {
            TestFramework.bstack1l1l1111l11_opy_: failure,
            TestFramework.bstack1l111111lll_opy_: bstack111111l11l_opy_,
            TestFramework.bstack1l1l1111111_opy_: bstack1l1111llll1_opy_,
        })
    def __1l111l1llll_opy_(
        self,
        context: bstack1l111111l11_opy_,
        test_framework_state: bstack1lll1ll1ll1_opy_,
        test_hook_state: bstack1lll1l1l1l1_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1ll1ll1_opy_.SETUP_FIXTURE:
            instance = self.__1l111111l1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1l1111ll1l1_opy_ bstack1l111111111_opy_ this to be bstack1l1l11_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᑦ")
            if test_framework_state == bstack1lll1ll1ll1_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1l111l11l1l_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1ll1ll1_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l1l11_opy_ (u"ࠣࡰࡲࡨࡪࠨᑧ"), None), bstack1l1l11_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᑨ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l1l11_opy_ (u"ࠥࡲࡴࡪࡥࠣᑩ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack1l1l11_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᑪ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1llll1ll1l1_opy_(target) if target else None
        return instance
    def __1l1111l11ll_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        test_framework_state: bstack1lll1ll1ll1_opy_,
        test_hook_state: bstack1lll1l1l1l1_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1l1111111l1_opy_ = TestFramework.bstack1lllll1l1l1_opy_(instance, PytestBDDFramework.bstack1l111llll11_opy_, {})
        if not key in bstack1l1111111l1_opy_:
            bstack1l1111111l1_opy_[key] = []
        bstack1l111lll111_opy_ = TestFramework.bstack1lllll1l1l1_opy_(instance, PytestBDDFramework.bstack1l1111ll11l_opy_, {})
        if not key in bstack1l111lll111_opy_:
            bstack1l111lll111_opy_[key] = []
        bstack1l111l1l11l_opy_ = {
            PytestBDDFramework.bstack1l111llll11_opy_: bstack1l1111111l1_opy_,
            PytestBDDFramework.bstack1l1111ll11l_opy_: bstack1l111lll111_opy_,
        }
        if test_hook_state == bstack1lll1l1l1l1_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack1l1l11_opy_ (u"ࠧࡱࡥࡺࠤᑫ"): key,
                TestFramework.bstack1l1111l1ll1_opy_: uuid4().__str__(),
                TestFramework.bstack11llllll1ll_opy_: TestFramework.bstack11lllll1lll_opy_,
                TestFramework.bstack1l1111ll111_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1l1111l11l1_opy_: [],
                TestFramework.bstack1l111111ll1_opy_: hook_name,
                TestFramework.bstack1l11111llll_opy_: bstack1lll1ll11ll_opy_.bstack1l111ll1111_opy_()
            }
            bstack1l1111111l1_opy_[key].append(hook)
            bstack1l111l1l11l_opy_[PytestBDDFramework.bstack1l111l1ll11_opy_] = key
        elif test_hook_state == bstack1lll1l1l1l1_opy_.POST:
            bstack1l1111lllll_opy_ = bstack1l1111111l1_opy_.get(key, [])
            hook = bstack1l1111lllll_opy_.pop() if bstack1l1111lllll_opy_ else None
            if hook:
                result = self.__1l11111l11l_opy_(*args)
                if result:
                    bstack1l1111l1l11_opy_ = result.get(bstack1l1l11_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢᑬ"), TestFramework.bstack11lllll1lll_opy_)
                    if bstack1l1111l1l11_opy_ != TestFramework.bstack11lllll1lll_opy_:
                        hook[TestFramework.bstack11llllll1ll_opy_] = bstack1l1111l1l11_opy_
                hook[TestFramework.bstack1l111lllll1_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1l11111llll_opy_] = bstack1lll1ll11ll_opy_.bstack1l111ll1111_opy_()
                self.bstack1l111l111l1_opy_(hook)
                logs = hook.get(TestFramework.bstack11lllllll11_opy_, [])
                self.bstack1l1ll11l1ll_opy_(instance, logs)
                bstack1l111lll111_opy_[key].append(hook)
                bstack1l111l1l11l_opy_[PytestBDDFramework.bstack1l11111ll11_opy_] = key
        TestFramework.bstack1l111ll11l1_opy_(instance, bstack1l111l1l11l_opy_)
        self.logger.debug(bstack1l1l11_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡨࡰࡱ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻ࡬ࡧࡼࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥ࠿ࡾ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࢀࠤ࡭ࡵ࡯࡬ࡵࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࡂࠨᑭ") + str(bstack1l111lll111_opy_) + bstack1l1l11_opy_ (u"ࠣࠤᑮ"))
    def __1l111111l1l_opy_(
        self,
        context: bstack1l111111l11_opy_,
        test_framework_state: bstack1lll1ll1ll1_opy_,
        test_hook_state: bstack1lll1l1l1l1_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1l1ll1lll11_opy_(args[0], [bstack1l1l11_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣᑯ"), bstack1l1l11_opy_ (u"ࠥࡥࡷ࡭࡮ࡢ࡯ࡨࠦᑰ"), bstack1l1l11_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦᑱ"), bstack1l1l11_opy_ (u"ࠧ࡯ࡤࡴࠤᑲ"), bstack1l1l11_opy_ (u"ࠨࡵ࡯࡫ࡷࡸࡪࡹࡴࠣᑳ"), bstack1l1l11_opy_ (u"ࠢࡣࡣࡶࡩ࡮ࡪࠢᑴ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack1l1l11_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᑵ")) else fixturedef.get(bstack1l1l11_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣᑶ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l1l11_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࠣᑷ")) else None
        node = request.node if hasattr(request, bstack1l1l11_opy_ (u"ࠦࡳࡵࡤࡦࠤᑸ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l1l11_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᑹ")) else None
        baseid = fixturedef.get(bstack1l1l11_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨᑺ"), None) or bstack1l1l11_opy_ (u"ࠢࠣᑻ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l1l11_opy_ (u"ࠣࡡࡳࡽ࡫ࡻ࡮ࡤ࡫ࡷࡩࡲࠨᑼ")):
            target = PytestBDDFramework.__11lllll1l11_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l1l11_opy_ (u"ࠤ࡯ࡳࡨࡧࡴࡪࡱࡱࠦᑽ")) else None
            if target and not TestFramework.bstack1llll1ll1l1_opy_(target):
                self.__1l111l11l1l_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l1l11_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡴ࡯ࡥࡧࡀࡿࡳࡵࡤࡦࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧᑾ") + str(test_hook_state) + bstack1l1l11_opy_ (u"ࠦࠧᑿ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l1l11_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫ࡤࡦࡨࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥᒀ") + str(target) + bstack1l1l11_opy_ (u"ࠨࠢᒁ"))
            return None
        instance = TestFramework.bstack1llll1ll1l1_opy_(target)
        if not instance:
            self.logger.warning(bstack1l1l11_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡢࡢࡵࡨ࡭ࡩࡃࡻࡣࡣࡶࡩ࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤᒂ") + str(target) + bstack1l1l11_opy_ (u"ࠣࠤᒃ"))
            return None
        bstack1l111l1l1ll_opy_ = TestFramework.bstack1lllll1l1l1_opy_(instance, PytestBDDFramework.bstack1l111lll1l1_opy_, {})
        if os.getenv(bstack1l1l11_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡈࡌ࡜࡙࡛ࡒࡆࡕࠥᒄ"), bstack1l1l11_opy_ (u"ࠥ࠵ࠧᒅ")) == bstack1l1l11_opy_ (u"ࠦ࠶ࠨᒆ"):
            bstack1l111ll111l_opy_ = bstack1l1l11_opy_ (u"ࠧࡀࠢᒇ").join((scope, fixturename))
            bstack1l111llll1l_opy_ = datetime.now(tz=timezone.utc)
            bstack1l1111l1111_opy_ = {
                bstack1l1l11_opy_ (u"ࠨ࡫ࡦࡻࠥᒈ"): bstack1l111ll111l_opy_,
                bstack1l1l11_opy_ (u"ࠢࡵࡣࡪࡷࠧᒉ"): PytestBDDFramework.__1l111l1lll1_opy_(request.node, scenario),
                bstack1l1l11_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࠤᒊ"): fixturedef,
                bstack1l1l11_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣᒋ"): scope,
                bstack1l1l11_opy_ (u"ࠥࡸࡾࡶࡥࠣᒌ"): None,
            }
            try:
                if test_hook_state == bstack1lll1l1l1l1_opy_.POST and callable(getattr(args[-1], bstack1l1l11_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡷࡺࡲࡴࠣᒍ"), None)):
                    bstack1l1111l1111_opy_[bstack1l1l11_opy_ (u"ࠧࡺࡹࡱࡧࠥᒎ")] = TestFramework.bstack1l1ll11ll1l_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1l1l1l1_opy_.PRE:
                bstack1l1111l1111_opy_[bstack1l1l11_opy_ (u"ࠨࡵࡶ࡫ࡧࠦᒏ")] = uuid4().__str__()
                bstack1l1111l1111_opy_[PytestBDDFramework.bstack1l1111ll111_opy_] = bstack1l111llll1l_opy_
            elif test_hook_state == bstack1lll1l1l1l1_opy_.POST:
                bstack1l1111l1111_opy_[PytestBDDFramework.bstack1l111lllll1_opy_] = bstack1l111llll1l_opy_
            if bstack1l111ll111l_opy_ in bstack1l111l1l1ll_opy_:
                bstack1l111l1l1ll_opy_[bstack1l111ll111l_opy_].update(bstack1l1111l1111_opy_)
                self.logger.debug(bstack1l1l11_opy_ (u"ࠢࡶࡲࡧࡥࡹ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࠣᒐ") + str(bstack1l111l1l1ll_opy_[bstack1l111ll111l_opy_]) + bstack1l1l11_opy_ (u"ࠣࠤᒑ"))
            else:
                bstack1l111l1l1ll_opy_[bstack1l111ll111l_opy_] = bstack1l1111l1111_opy_
                self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡽࠡࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࠧᒒ") + str(len(bstack1l111l1l1ll_opy_)) + bstack1l1l11_opy_ (u"ࠥࠦᒓ"))
        TestFramework.bstack1llll1l1ll1_opy_(instance, PytestBDDFramework.bstack1l111lll1l1_opy_, bstack1l111l1l1ll_opy_)
        self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡷࡂࢁ࡬ࡦࡰࠫࡸࡷࡧࡣ࡬ࡧࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࡸ࠯ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᒔ") + str(instance.ref()) + bstack1l1l11_opy_ (u"ࠧࠨᒕ"))
        return instance
    def __1l111l11l1l_opy_(
        self,
        context: bstack1l111111l11_opy_,
        test_framework_state: bstack1lll1ll1ll1_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1111111111_opy_.create_context(target)
        ob = bstack1lll1l11l11_opy_(ctx, self.bstack1ll1l111l1l_opy_, self.bstack1l11111l1l1_opy_, test_framework_state)
        TestFramework.bstack1l111ll11l1_opy_(ob, {
            TestFramework.bstack1ll1111l11l_opy_: context.test_framework_name,
            TestFramework.bstack1l1l1ll11ll_opy_: context.test_framework_version,
            TestFramework.bstack1l111ll1l1l_opy_: [],
            PytestBDDFramework.bstack1l111lll1l1_opy_: {},
            PytestBDDFramework.bstack1l1111ll11l_opy_: {},
            PytestBDDFramework.bstack1l111llll11_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1l1ll1_opy_(ob, TestFramework.bstack11lllllllll_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1l1ll1_opy_(ob, TestFramework.bstack1ll1l1111l1_opy_, context.platform_index)
        TestFramework.bstack1lllllllll1_opy_[ctx.id] = ob
        self.logger.debug(bstack1l1l11_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡤࡶࡻ࠲࡮ࡪ࠽ࡼࡥࡷࡼ࠳࡯ࡤࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨᒖ") + str(TestFramework.bstack1lllllllll1_opy_.keys()) + bstack1l1l11_opy_ (u"ࠢࠣᒗ"))
        return ob
    @staticmethod
    def __1l111ll11ll_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l1l11_opy_ (u"ࠨ࡫ࡧࠫᒘ"): id(step),
                bstack1l1l11_opy_ (u"ࠩࡷࡩࡽࡺࠧᒙ"): step.name,
                bstack1l1l11_opy_ (u"ࠪ࡯ࡪࡿࡷࡰࡴࡧࠫᒚ"): step.keyword,
            })
        meta = {
            bstack1l1l11_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࠬᒛ"): {
                bstack1l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᒜ"): feature.name,
                bstack1l1l11_opy_ (u"࠭ࡰࡢࡶ࡫ࠫᒝ"): feature.filename,
                bstack1l1l11_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬᒞ"): feature.description
            },
            bstack1l1l11_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪᒟ"): {
                bstack1l1l11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᒠ"): scenario.name
            },
            bstack1l1l11_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᒡ"): steps,
            bstack1l1l11_opy_ (u"ࠫࡪࡾࡡ࡮ࡲ࡯ࡩࡸ࠭ᒢ"): PytestBDDFramework.__11lllll1111_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1l1111lll11_opy_: meta
            }
        )
    def bstack1l111l111l1_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡷ࡮ࡳࡩ࡭ࡣࡵࠤࡹࡵࠠࡵࡪࡨࠤࡏࡧࡶࡢࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡪࡵࠣࡱࡪࡺࡨࡰࡦ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡆ࡬ࡪࡩ࡫ࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡯࡮ࡴ࡫ࡧࡩࠥࢄ࠯࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠯ࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡪࡲࡳࡰࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠰ࠥࡸࡥࡱ࡮ࡤࡧࡪࡹࠠࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢࠡ࡫ࡱࠤ࡮ࡺࡳࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡏࡦࠡࡣࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤࡹ࡮ࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡲࡧࡴࡤࡪࡨࡷࠥࡧࠠ࡮ࡱࡧ࡭࡫࡯ࡥࡥࠢ࡫ࡳࡴࡱ࠭࡭ࡧࡹࡩࡱࠦࡦࡪ࡮ࡨ࠰ࠥ࡯ࡴࠡࡥࡵࡩࡦࡺࡥࡴࠢࡤࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡷࡪࡶ࡫ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡕ࡬ࡱ࡮ࡲࡡࡳ࡮ࡼ࠰ࠥ࡯ࡴࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦ࡬ࡰࡥࡤࡸࡪࡪࠠࡪࡰࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱ࠵ࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡨࡹࠡࡴࡨࡴࡱࡧࡣࡪࡰࡪࠤࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤ࡙࡮ࡥࠡࡥࡵࡩࡦࡺࡥࡥࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࡷࠥࡧࡲࡦࠢࡤࡨࡩ࡫ࡤࠡࡶࡲࠤࡹ࡮ࡥࠡࡪࡲࡳࡰ࠭ࡳࠡࠤ࡯ࡳ࡬ࡹࠢࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭࠽ࠤ࡙࡮ࡥࠡࡧࡹࡩࡳࡺࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴ࡭ࡳࠡࡣࡱࡨࠥ࡮࡯ࡰ࡭ࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡖࡡࡵࡪࠣࡳࡧࡰࡥࡤࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡵࡪ࡮ࡧࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᒣ")
        global _1l1l1lll1l1_opy_
        platform_index = os.environ[bstack1l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᒤ")]
        bstack1l1ll111ll1_opy_ = os.path.join(bstack1l1ll11111l_opy_, (bstack1l1l1l1ll1l_opy_ + str(platform_index)), bstack11lllll111l_opy_)
        if not os.path.exists(bstack1l1ll111ll1_opy_) or not os.path.isdir(bstack1l1ll111ll1_opy_):
            return
        logs = hook.get(bstack1l1l11_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᒥ"), [])
        with os.scandir(bstack1l1ll111ll1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1l1l1lll1l1_opy_:
                    self.logger.info(bstack1l1l11_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨᒦ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1l1l11_opy_ (u"ࠤࠥᒧ")
                    log_entry = bstack1lll111llll_opy_(
                        kind=bstack1l1l11_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᒨ"),
                        message=bstack1l1l11_opy_ (u"ࠦࠧᒩ"),
                        level=bstack1l1l11_opy_ (u"ࠧࠨᒪ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1l1ll11l1_opy_=entry.stat().st_size,
                        bstack1l1ll1l1lll_opy_=bstack1l1l11_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨᒫ"),
                        bstack1111l_opy_=os.path.abspath(entry.path),
                        bstack1l111l11l11_opy_=hook.get(TestFramework.bstack1l1111l1ll1_opy_)
                    )
                    logs.append(log_entry)
                    _1l1l1lll1l1_opy_.add(abs_path)
        platform_index = os.environ[bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᒬ")]
        bstack1l111lll11l_opy_ = os.path.join(bstack1l1ll11111l_opy_, (bstack1l1l1l1ll1l_opy_ + str(platform_index)), bstack11lllll111l_opy_, bstack1l111l111ll_opy_)
        if not os.path.exists(bstack1l111lll11l_opy_) or not os.path.isdir(bstack1l111lll11l_opy_):
            self.logger.info(bstack1l1l11_opy_ (u"ࠣࡐࡲࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣࡥࡹࡀࠠࡼࡿࠥᒭ").format(bstack1l111lll11l_opy_))
        else:
            self.logger.info(bstack1l1l11_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡪࡷࡵ࡭ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠾ࠥࢁࡽࠣᒮ").format(bstack1l111lll11l_opy_))
            with os.scandir(bstack1l111lll11l_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1l1l1lll1l1_opy_:
                        self.logger.info(bstack1l1l11_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣᒯ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1l1l11_opy_ (u"ࠦࠧᒰ")
                        log_entry = bstack1lll111llll_opy_(
                            kind=bstack1l1l11_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᒱ"),
                            message=bstack1l1l11_opy_ (u"ࠨࠢᒲ"),
                            level=bstack1l1l11_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦᒳ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1l1ll11l1_opy_=entry.stat().st_size,
                            bstack1l1ll1l1lll_opy_=bstack1l1l11_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᒴ"),
                            bstack1111l_opy_=os.path.abspath(entry.path),
                            bstack1l1l1ll1l1l_opy_=hook.get(TestFramework.bstack1l1111l1ll1_opy_)
                        )
                        logs.append(log_entry)
                        _1l1l1lll1l1_opy_.add(abs_path)
        hook[bstack1l1l11_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᒵ")] = logs
    def bstack1l1ll11l1ll_opy_(
        self,
        bstack1l1ll1lll1l_opy_: bstack1lll1l11l11_opy_,
        entries: List[bstack1lll111llll_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡗࡊ࡙ࡓࡊࡑࡑࡣࡎࡊࠢᒶ"))
        req.platform_index = TestFramework.bstack1lllll1l1l1_opy_(bstack1l1ll1lll1l_opy_, TestFramework.bstack1ll1l1111l1_opy_)
        req.execution_context.hash = str(bstack1l1ll1lll1l_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1ll1lll1l_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1ll1lll1l_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.bstack1lllll1l1l1_opy_(bstack1l1ll1lll1l_opy_, TestFramework.bstack1ll1111l11l_opy_)
            log_entry.test_framework_version = TestFramework.bstack1lllll1l1l1_opy_(bstack1l1ll1lll1l_opy_, TestFramework.bstack1l1l1ll11ll_opy_)
            log_entry.uuid = entry.bstack1l111l11l11_opy_ if entry.bstack1l111l11l11_opy_ else TestFramework.bstack1lllll1l1l1_opy_(bstack1l1ll1lll1l_opy_, TestFramework.bstack1ll11ll1lll_opy_)
            log_entry.test_framework_state = bstack1l1ll1lll1l_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l1l11_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᒷ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1l1l11_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᒸ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1l1ll11l1_opy_
                log_entry.file_path = entry.bstack1111l_opy_
        def bstack1l1ll1ll1l1_opy_():
            bstack11l1ll1111_opy_ = datetime.now()
            try:
                self.bstack1lll11111l1_opy_.LogCreatedEvent(req)
                bstack1l1ll1lll1l_opy_.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠥᒹ"), datetime.now() - bstack11l1ll1111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1l11_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡿࢂࠨᒺ").format(str(e)))
                traceback.print_exc()
        self.bstack1111111ll1_opy_.enqueue(bstack1l1ll1ll1l1_opy_)
    def __1l1111l1lll_opy_(self, instance) -> None:
        bstack1l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡒ࡯ࡢࡦࡶࠤࡨࡻࡳࡵࡱࡰࠤࡹࡧࡧࡴࠢࡩࡳࡷࠦࡴࡩࡧࠣ࡫࡮ࡼࡥ࡯ࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡴࡨࡥࡹ࡫ࡳࠡࡣࠣࡨ࡮ࡩࡴࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡰࡪࡼࡥ࡭ࠢࡦࡹࡸࡺ࡯࡮ࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࡪࠠࡧࡴࡲࡱࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡶࡵࡷࡳࡲ࡚ࡡࡨࡏࡤࡲࡦ࡭ࡥࡳࠢࡤࡲࡩࠦࡵࡱࡦࡤࡸࡪࡹࠠࡵࡪࡨࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡳࡵࡣࡷࡩࠥࡻࡳࡪࡰࡪࠤࡸ࡫ࡴࡠࡵࡷࡥࡹ࡫࡟ࡦࡰࡷࡶ࡮࡫ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᒻ")
        bstack1l111l1l11l_opy_ = {bstack1l1l11_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡡࡰࡩࡹࡧࡤࡢࡶࡤࠦᒼ"): bstack1lll1ll11ll_opy_.bstack1l111ll1111_opy_()}
        TestFramework.bstack1l111ll11l1_opy_(instance, bstack1l111l1l11l_opy_)
    @staticmethod
    def __1l111ll1lll_opy_(instance, args):
        request, bstack11lllll1l1l_opy_ = args
        bstack1l11111lll1_opy_ = id(bstack11lllll1l1l_opy_)
        bstack1l111l11ll1_opy_ = instance.data[TestFramework.bstack1l1111lll11_opy_]
        step = next(filter(lambda st: st[bstack1l1l11_opy_ (u"ࠪ࡭ࡩ࠭ᒽ")] == bstack1l11111lll1_opy_, bstack1l111l11ll1_opy_[bstack1l1l11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᒾ")]), None)
        step.update({
            bstack1l1l11_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᒿ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1l111l11ll1_opy_[bstack1l1l11_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᓀ")]) if st[bstack1l1l11_opy_ (u"ࠧࡪࡦࠪᓁ")] == step[bstack1l1l11_opy_ (u"ࠨ࡫ࡧࠫᓂ")]), None)
        if index is not None:
            bstack1l111l11ll1_opy_[bstack1l1l11_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᓃ")][index] = step
        instance.data[TestFramework.bstack1l1111lll11_opy_] = bstack1l111l11ll1_opy_
    @staticmethod
    def __11llllll1l1_opy_(instance, args):
        bstack1l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡸࡪࡨࡲࠥࡲࡥ࡯ࠢࡤࡶ࡬ࡹࠠࡪࡵࠣ࠶࠱ࠦࡩࡵࠢࡶ࡭࡬ࡴࡩࡧ࡫ࡨࡷࠥࡺࡨࡦࡴࡨࠤ࡮ࡹࠠ࡯ࡱࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡦࡸࡧࡴࠢࡤࡶࡪࠦ࠭ࠡ࡝ࡵࡩࡶࡻࡥࡴࡶ࠯ࠤࡸࡺࡥࡱ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮࡬ࠠࡢࡴࡪࡷࠥࡧࡲࡦࠢ࠶ࠤࡹ࡮ࡥ࡯ࠢࡷ࡬ࡪࠦ࡬ࡢࡵࡷࠤࡻࡧ࡬ࡶࡧࠣ࡭ࡸࠦࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᓄ")
        bstack1l111l11111_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack11lllll1l1l_opy_ = args[1]
        bstack1l11111lll1_opy_ = id(bstack11lllll1l1l_opy_)
        bstack1l111l11ll1_opy_ = instance.data[TestFramework.bstack1l1111lll11_opy_]
        step = None
        if bstack1l11111lll1_opy_ is not None and bstack1l111l11ll1_opy_.get(bstack1l1l11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᓅ")):
            step = next(filter(lambda st: st[bstack1l1l11_opy_ (u"ࠬ࡯ࡤࠨᓆ")] == bstack1l11111lll1_opy_, bstack1l111l11ll1_opy_[bstack1l1l11_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᓇ")]), None)
            step.update({
                bstack1l1l11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᓈ"): bstack1l111l11111_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack1l1l11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᓉ"): bstack1l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᓊ"),
                bstack1l1l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᓋ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack1l1l11_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᓌ"): bstack1l1l11_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᓍ"),
                })
        index = next((i for i, st in enumerate(bstack1l111l11ll1_opy_[bstack1l1l11_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᓎ")]) if st[bstack1l1l11_opy_ (u"ࠧࡪࡦࠪᓏ")] == step[bstack1l1l11_opy_ (u"ࠨ࡫ࡧࠫᓐ")]), None)
        if index is not None:
            bstack1l111l11ll1_opy_[bstack1l1l11_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᓑ")][index] = step
        instance.data[TestFramework.bstack1l1111lll11_opy_] = bstack1l111l11ll1_opy_
    @staticmethod
    def __11lllll1111_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack1l1l11_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬᓒ")):
                examples = list(node.callspec.params[bstack1l1l11_opy_ (u"ࠫࡤࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡨࡼࡦࡳࡰ࡭ࡧࠪᓓ")].values())
            return examples
        except:
            return []
    def bstack1l1l1l1llll_opy_(self, instance: bstack1lll1l11l11_opy_, bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_]):
        bstack1l11l11111l_opy_ = (
            PytestBDDFramework.bstack1l111l1ll11_opy_
            if bstack1lllll11ll1_opy_[1] == bstack1lll1l1l1l1_opy_.PRE
            else PytestBDDFramework.bstack1l11111ll11_opy_
        )
        hook = PytestBDDFramework.bstack1l111l1l111_opy_(instance, bstack1l11l11111l_opy_)
        entries = hook.get(TestFramework.bstack1l1111l11l1_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1l111ll1l1l_opy_, []))
        return entries
    def bstack1l1ll11lll1_opy_(self, instance: bstack1lll1l11l11_opy_, bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_]):
        bstack1l11l11111l_opy_ = (
            PytestBDDFramework.bstack1l111l1ll11_opy_
            if bstack1lllll11ll1_opy_[1] == bstack1lll1l1l1l1_opy_.PRE
            else PytestBDDFramework.bstack1l11111ll11_opy_
        )
        PytestBDDFramework.bstack1l11111l111_opy_(instance, bstack1l11l11111l_opy_)
        TestFramework.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1l111ll1l1l_opy_, []).clear()
    @staticmethod
    def bstack1l111l1l111_opy_(instance: bstack1lll1l11l11_opy_, bstack1l11l11111l_opy_: str):
        bstack1l111l1111l_opy_ = (
            PytestBDDFramework.bstack1l1111ll11l_opy_
            if bstack1l11l11111l_opy_ == PytestBDDFramework.bstack1l11111ll11_opy_
            else PytestBDDFramework.bstack1l111llll11_opy_
        )
        bstack1l111lll1ll_opy_ = TestFramework.bstack1lllll1l1l1_opy_(instance, bstack1l11l11111l_opy_, None)
        bstack1l1111ll1ll_opy_ = TestFramework.bstack1lllll1l1l1_opy_(instance, bstack1l111l1111l_opy_, None) if bstack1l111lll1ll_opy_ else None
        return (
            bstack1l1111ll1ll_opy_[bstack1l111lll1ll_opy_][-1]
            if isinstance(bstack1l1111ll1ll_opy_, dict) and len(bstack1l1111ll1ll_opy_.get(bstack1l111lll1ll_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1l11111l111_opy_(instance: bstack1lll1l11l11_opy_, bstack1l11l11111l_opy_: str):
        hook = PytestBDDFramework.bstack1l111l1l111_opy_(instance, bstack1l11l11111l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1l1111l11l1_opy_, []).clear()
    @staticmethod
    def __11lllll1ll1_opy_(instance: bstack1lll1l11l11_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l1l11_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡨࡵࡲࡥࡵࠥᓔ"), None)):
            return
        if os.getenv(bstack1l1l11_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡒࡏࡈࡕࠥᓕ"), bstack1l1l11_opy_ (u"ࠢ࠲ࠤᓖ")) != bstack1l1l11_opy_ (u"ࠣ࠳ࠥᓗ"):
            PytestBDDFramework.logger.warning(bstack1l1l11_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡪࡰࡪࠤࡨࡧࡰ࡭ࡱࡪࠦᓘ"))
            return
        bstack1l1111l111l_opy_ = {
            bstack1l1l11_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤᓙ"): (PytestBDDFramework.bstack1l111l1ll11_opy_, PytestBDDFramework.bstack1l111llll11_opy_),
            bstack1l1l11_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᓚ"): (PytestBDDFramework.bstack1l11111ll11_opy_, PytestBDDFramework.bstack1l1111ll11l_opy_),
        }
        for when in (bstack1l1l11_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦᓛ"), bstack1l1l11_opy_ (u"ࠨࡣࡢ࡮࡯ࠦᓜ"), bstack1l1l11_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᓝ")):
            bstack11llllll111_opy_ = args[1].get_records(when)
            if not bstack11llllll111_opy_:
                continue
            records = [
                bstack1lll111llll_opy_(
                    kind=TestFramework.bstack1l1lll1ll1l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l1l11_opy_ (u"ࠣ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨࠦᓞ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l1l11_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࠥᓟ")) and r.created
                        else None
                    ),
                )
                for r in bstack11llllll111_opy_
                if isinstance(getattr(r, bstack1l1l11_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦᓠ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1l111l1ll1l_opy_, bstack1l111l1111l_opy_ = bstack1l1111l111l_opy_.get(when, (None, None))
            bstack1l111llllll_opy_ = TestFramework.bstack1lllll1l1l1_opy_(instance, bstack1l111l1ll1l_opy_, None) if bstack1l111l1ll1l_opy_ else None
            bstack1l1111ll1ll_opy_ = TestFramework.bstack1lllll1l1l1_opy_(instance, bstack1l111l1111l_opy_, None) if bstack1l111llllll_opy_ else None
            if isinstance(bstack1l1111ll1ll_opy_, dict) and len(bstack1l1111ll1ll_opy_.get(bstack1l111llllll_opy_, [])) > 0:
                hook = bstack1l1111ll1ll_opy_[bstack1l111llllll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1l1111l11l1_opy_ in hook:
                    hook[TestFramework.bstack1l1111l11l1_opy_].extend(records)
                    continue
            logs = TestFramework.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1l111ll1l1l_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1l111ll1ll1_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        bstack111l1l1l1_opy_ = request.node.nodeid
        test_name = PytestBDDFramework.__1l111ll1l11_opy_(request.node, scenario)
        bstack1l11111l1ll_opy_ = feature.filename
        if not bstack111l1l1l1_opy_ or not test_name or not bstack1l11111l1ll_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1ll11ll1lll_opy_: uuid4().__str__(),
            TestFramework.bstack1l111l1l1l1_opy_: bstack111l1l1l1_opy_,
            TestFramework.bstack1ll11lll1ll_opy_: test_name,
            TestFramework.bstack1l1l11lll1l_opy_: bstack111l1l1l1_opy_,
            TestFramework.bstack11llllllll1_opy_: bstack1l11111l1ll_opy_,
            TestFramework.bstack1l1111l1l1l_opy_: PytestBDDFramework.__1l111l1lll1_opy_(feature, scenario),
            TestFramework.bstack11lllllll1l_opy_: code,
            TestFramework.bstack1l1l1111111_opy_: TestFramework.bstack1l11111111l_opy_,
            TestFramework.bstack1l11l1l1l11_opy_: test_name
        }
    @staticmethod
    def __1l111ll1l11_opy_(node, scenario):
        if hasattr(node, bstack1l1l11_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭ᓡ")):
            parts = node.nodeid.rsplit(bstack1l1l11_opy_ (u"ࠧࡡࠢᓢ"))
            params = parts[-1]
            return bstack1l1l11_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨᓣ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1l111l1lll1_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack1l1l11_opy_ (u"ࠧࡵࡣࡪࡷࠬᓤ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack1l1l11_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᓥ")) else [])
    @staticmethod
    def __11lllll1l11_opy_(location):
        return bstack1l1l11_opy_ (u"ࠤ࠽࠾ࠧᓦ").join(filter(lambda x: isinstance(x, str), location))