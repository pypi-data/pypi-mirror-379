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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llllllll1l_opy_,
    bstack1lllll11lll_opy_,
    bstack1llll1lllll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll11111ll_opy_ import bstack1ll1ll111ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_, bstack1lll1l11l11_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1ll1ll1l_opy_ import bstack1ll1ll1111l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1l1lll_opy_ import bstack1lll1llll11_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1l11l1_opy_ import bstack1lll1ll1111_opy_
from bstack_utils.helper import bstack1ll11l11l11_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack111l11ll_opy_ import bstack1lll111lll1_opy_
import grpc
import traceback
import json
class bstack1llll111lll_opy_(bstack1llll11lll1_opy_):
    bstack1ll111l1l11_opy_ = False
    bstack1ll111ll1l1_opy_ = bstack1l1l11_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸࠢᆉ")
    bstack1ll1l111ll1_opy_ = bstack1l1l11_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧ࠱ࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࠨᆊ")
    bstack1ll1l111111_opy_ = bstack1l1l11_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣ࡮ࡴࡩࡵࠤᆋ")
    bstack1ll11lll1l1_opy_ = bstack1l1l11_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤ࡯ࡳࡠࡵࡦࡥࡳࡴࡩ࡯ࡩࠥᆌ")
    bstack1ll11llll1l_opy_ = bstack1l1l11_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡥࡨࡢࡵࡢࡹࡷࡲࠢᆍ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1lll11lllll_opy_, bstack1ll1l1lll11_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1ll11l1l111_opy_ = False
        self.bstack1ll111l1l1l_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1ll11111lll_opy_ = bstack1ll1l1lll11_opy_
        bstack1lll11lllll_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1lllll1ll1l_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1ll1111ll1l_opy_)
        TestFramework.bstack1ll111l11l1_opy_((bstack1lll1ll1ll1_opy_.TEST, bstack1lll1l1l1l1_opy_.PRE), self.bstack1ll111l1111_opy_)
        TestFramework.bstack1ll111l11l1_opy_((bstack1lll1ll1ll1_opy_.TEST, bstack1lll1l1l1l1_opy_.POST), self.bstack1ll111l1lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll111l1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1ll11lll11l_opy_(instance, args)
        test_framework = f.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1ll1111l11l_opy_)
        if self.bstack1ll11l1l111_opy_:
            self.bstack1ll111l1l1l_opy_[bstack1l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠢᆎ")] = f.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1ll11ll1lll_opy_)
        if bstack1l1l11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᆏ") in instance.bstack1ll1l111l1l_opy_:
            platform_index = f.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1ll1l1111l1_opy_)
            self.accessibility = self.bstack1ll11llll11_opy_(tags, self.config[bstack1l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᆐ")][platform_index])
        else:
            capabilities = self.bstack1ll11111lll_opy_.bstack1ll1111llll_opy_(f, instance, bstack1lllll11ll1_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡧࡱࡸࡲࡩࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᆑ") + str(kwargs) + bstack1l1l11_opy_ (u"ࠦࠧᆒ"))
                return
            self.accessibility = self.bstack1ll11llll11_opy_(tags, capabilities)
        if self.bstack1ll11111lll_opy_.pages and self.bstack1ll11111lll_opy_.pages.values():
            bstack1ll11l1l1l1_opy_ = list(self.bstack1ll11111lll_opy_.pages.values())
            if bstack1ll11l1l1l1_opy_ and isinstance(bstack1ll11l1l1l1_opy_[0], (list, tuple)) and bstack1ll11l1l1l1_opy_[0]:
                bstack1ll11lllll1_opy_ = bstack1ll11l1l1l1_opy_[0][0]
                if callable(bstack1ll11lllll1_opy_):
                    page = bstack1ll11lllll1_opy_()
                    def bstack1ll1l11ll_opy_():
                        self.get_accessibility_results(page, bstack1l1l11_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤᆓ"))
                    def bstack1ll11l1111l_opy_():
                        self.get_accessibility_results_summary(page, bstack1l1l11_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥᆔ"))
                    setattr(page, bstack1l1l11_opy_ (u"ࠢࡨࡧࡷࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡕࡩࡸࡻ࡬ࡵࡵࠥᆕ"), bstack1ll1l11ll_opy_)
                    setattr(page, bstack1l1l11_opy_ (u"ࠣࡩࡨࡸࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡖࡪࡹࡵ࡭ࡶࡖࡹࡲࡳࡡࡳࡻࠥᆖ"), bstack1ll11l1111l_opy_)
        self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡶ࡬ࡴࡻ࡬ࡥࠢࡵࡹࡳࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡶࡢ࡮ࡸࡩࡂࠨᆗ") + str(self.accessibility) + bstack1l1l11_opy_ (u"ࠥࠦᆘ"))
    def bstack1ll1111ll1l_opy_(
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
            bstack11l1ll1111_opy_ = datetime.now()
            self.bstack1ll1111l111_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼࡬ࡲ࡮ࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡤࡱࡱࡪ࡮࡭ࠢᆙ"), datetime.now() - bstack11l1ll1111_opy_)
            if (
                not f.bstack1ll11ll1l1l_opy_(method_name)
                or f.bstack1ll111l11ll_opy_(method_name, *args)
                or f.bstack1ll11l11l1l_opy_(method_name, *args)
            ):
                return
            if not f.bstack1lllll1l1l1_opy_(instance, bstack1llll111lll_opy_.bstack1ll1l111111_opy_, False):
                if not bstack1llll111lll_opy_.bstack1ll111l1l11_opy_:
                    self.logger.warning(bstack1l1l11_opy_ (u"ࠧࡡࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࠣᆚ") + str(f.platform_index) + bstack1l1l11_opy_ (u"ࠨ࡝ࠡࡣ࠴࠵ࡾࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥ࡮ࡡࡷࡧࠣࡲࡴࡺࠠࡣࡧࡨࡲࠥࡹࡥࡵࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᆛ"))
                    bstack1llll111lll_opy_.bstack1ll111l1l11_opy_ = True
                return
            bstack1ll11l1l1ll_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1ll11l1l1ll_opy_:
                platform_index = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll111ll_opy_.bstack1ll1l1111l1_opy_, 0)
                self.logger.debug(bstack1l1l11_opy_ (u"ࠢ࡯ࡱࠣࡥ࠶࠷ࡹࠡࡵࡦࡶ࡮ࡶࡴࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࡼࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧᆜ") + str(f.framework_name) + bstack1l1l11_opy_ (u"ࠣࠤᆝ"))
                return
            command_name = f.bstack1ll111l1ll1_opy_(*args)
            if not command_name:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࡀࠦᆞ") + str(method_name) + bstack1l1l11_opy_ (u"ࠥࠦᆟ"))
                return
            bstack1ll111lll11_opy_ = f.bstack1lllll1l1l1_opy_(instance, bstack1llll111lll_opy_.bstack1ll11llll1l_opy_, False)
            if command_name == bstack1l1l11_opy_ (u"ࠦ࡬࡫ࡴࠣᆠ") and not bstack1ll111lll11_opy_:
                f.bstack1llll1l1ll1_opy_(instance, bstack1llll111lll_opy_.bstack1ll11llll1l_opy_, True)
                bstack1ll111lll11_opy_ = True
            if not bstack1ll111lll11_opy_ and not self.bstack1ll11l1l111_opy_:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡴ࡯ࠡࡗࡕࡐࠥࡲ࡯ࡢࡦࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࡀࠦᆡ") + str(command_name) + bstack1l1l11_opy_ (u"ࠨࠢᆢ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠢ࡯ࡱࠣࡥ࠶࠷ࡹࠡࡵࡦࡶ࡮ࡶࡴࡴࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࡁࠧᆣ") + str(command_name) + bstack1l1l11_opy_ (u"ࠣࠤᆤ"))
                return
            self.logger.info(bstack1l1l11_opy_ (u"ࠤࡵࡹࡳࡴࡩ࡯ࡩࠣࡿࡱ࡫࡮ࠩࡵࡦࡶ࡮ࡶࡴࡴࡡࡷࡳࡤࡸࡵ࡯ࠫࢀࠤࡸࡩࡲࡪࡲࡷࡷࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࡀࠦᆥ") + str(command_name) + bstack1l1l11_opy_ (u"ࠥࠦᆦ"))
            scripts = [(s, bstack1ll11l1l1ll_opy_[s]) for s in scripts_to_run if s in bstack1ll11l1l1ll_opy_]
            for script_name, bstack1ll1l11111l_opy_ in scripts:
                try:
                    bstack11l1ll1111_opy_ = datetime.now()
                    if script_name == bstack1l1l11_opy_ (u"ࠦࡸࡩࡡ࡯ࠤᆧ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽ࠦᆨ") + script_name, datetime.now() - bstack11l1ll1111_opy_)
                    if isinstance(result, dict) and not result.get(bstack1l1l11_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹࠢᆩ"), True):
                        self.logger.warning(bstack1l1l11_opy_ (u"ࠢࡴ࡭࡬ࡴࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡴࡧࠡࡴࡨࡱࡦ࡯࡮ࡪࡰࡪࠤࡸࡩࡲࡪࡲࡷࡷ࠿ࠦࠢᆪ") + str(result) + bstack1l1l11_opy_ (u"ࠣࠤᆫ"))
                        break
                except Exception as e:
                    self.logger.error(bstack1l1l11_opy_ (u"ࠤࡨࡶࡷࡵࡲࠡࡧࡻࡩࡨࡻࡴࡪࡰࡪࠤࡸࡩࡲࡪࡲࡷࡁࢀࡹࡣࡳ࡫ࡳࡸࡤࡴࡡ࡮ࡧࢀࠤࡪࡸࡲࡰࡴࡀࠦᆬ") + str(e) + bstack1l1l11_opy_ (u"ࠥࠦᆭ"))
        except Exception as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥࠡࡧࡵࡶࡴࡸ࠽ࠣᆮ") + str(e) + bstack1l1l11_opy_ (u"ࠧࠨᆯ"))
    def bstack1ll111l1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll11ll1_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll1l1l1l1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1ll11lll11l_opy_(instance, args)
        capabilities = self.bstack1ll11111lll_opy_.bstack1ll1111llll_opy_(f, instance, bstack1lllll11ll1_opy_, *args, **kwargs)
        self.accessibility = self.bstack1ll11llll11_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠥᆰ"))
            return
        driver = self.bstack1ll11111lll_opy_.bstack1ll11l11ll1_opy_(f, instance, bstack1lllll11ll1_opy_, *args, **kwargs)
        test_name = f.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1ll11lll1ll_opy_)
        if not test_name:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡯ࡣࡰࡩࠧᆱ"))
            return
        test_uuid = f.bstack1lllll1l1l1_opy_(instance, TestFramework.bstack1ll11ll1lll_opy_)
        if not test_uuid:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡷࡸ࡭ࡩࠨᆲ"))
            return
        if isinstance(self.bstack1ll11111lll_opy_, bstack1lll1llll11_opy_):
            framework_name = bstack1l1l11_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᆳ")
        else:
            framework_name = bstack1l1l11_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬᆴ")
        self.bstack1111ll1l1_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll11ll11l1_opy_ = bstack1lll111lll1_opy_.bstack1ll11ll1l11_opy_(EVENTS.bstack1llll1ll_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࠧᆵ"))
            return
        bstack11l1ll1111_opy_ = datetime.now()
        bstack1ll1l11111l_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1l11_opy_ (u"ࠧࡹࡣࡢࡰࠥᆶ"), None)
        if not bstack1ll1l11111l_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡵࡦࡥࡳ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᆷ") + str(framework_name) + bstack1l1l11_opy_ (u"ࠢࠡࠤᆸ"))
            return
        if self.bstack1ll11l1l111_opy_:
            arg = dict()
            arg[bstack1l1l11_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࠣᆹ")] = method if method else bstack1l1l11_opy_ (u"ࠤࠥᆺ")
            arg[bstack1l1l11_opy_ (u"ࠥࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠥᆻ")] = self.bstack1ll111l1l1l_opy_[bstack1l1l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠦᆼ")]
            arg[bstack1l1l11_opy_ (u"ࠧࡺࡨࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠥᆽ")] = self.bstack1ll111l1l1l_opy_[bstack1l1l11_opy_ (u"ࠨࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡣࡷ࡬ࡰࡩࡥࡵࡶ࡫ࡧࠦᆾ")]
            arg[bstack1l1l11_opy_ (u"ࠢࡢࡷࡷ࡬ࡍ࡫ࡡࡥࡧࡵࠦᆿ")] = self.bstack1ll111l1l1l_opy_[bstack1l1l11_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳࠨᇀ")]
            arg[bstack1l1l11_opy_ (u"ࠤࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳࠨᇁ")] = self.bstack1ll111l1l1l_opy_[bstack1l1l11_opy_ (u"ࠥࡸ࡭ࡥࡪࡸࡶࡢࡸࡴࡱࡥ࡯ࠤᇂ")]
            arg[bstack1l1l11_opy_ (u"ࠦࡸࡩࡡ࡯ࡖ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠦᇃ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1ll11l11lll_opy_ = bstack1ll1l11111l_opy_ % json.dumps(arg)
            driver.execute_script(bstack1ll11l11lll_opy_)
            return
        instance = bstack1lllll11lll_opy_.bstack1llll1ll1l1_opy_(driver)
        if instance:
            if not bstack1lllll11lll_opy_.bstack1lllll1l1l1_opy_(instance, bstack1llll111lll_opy_.bstack1ll11lll1l1_opy_, False):
                bstack1lllll11lll_opy_.bstack1llll1l1ll1_opy_(instance, bstack1llll111lll_opy_.bstack1ll11lll1l1_opy_, True)
            else:
                self.logger.info(bstack1l1l11_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡩ࡯ࠢࡳࡶࡴ࡭ࡲࡦࡵࡶࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡ࡯ࡨࡸ࡭ࡵࡤ࠾ࠤᇄ") + str(method) + bstack1l1l11_opy_ (u"ࠨࠢᇅ"))
                return
        self.logger.info(bstack1l1l11_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡲ࡫ࡴࡩࡱࡧࡁࠧᇆ") + str(method) + bstack1l1l11_opy_ (u"ࠣࠤᇇ"))
        if framework_name == bstack1l1l11_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᇈ"):
            result = self.bstack1ll11111lll_opy_.bstack1ll11ll111l_opy_(driver, bstack1ll1l11111l_opy_)
        else:
            result = driver.execute_async_script(bstack1ll1l11111l_opy_, {bstack1l1l11_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠥᇉ"): method if method else bstack1l1l11_opy_ (u"ࠦࠧᇊ")})
        bstack1lll111lll1_opy_.end(EVENTS.bstack1llll1ll_opy_.value, bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᇋ"), bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᇌ"), True, None, command=method)
        if instance:
            bstack1lllll11lll_opy_.bstack1llll1l1ll1_opy_(instance, bstack1llll111lll_opy_.bstack1ll11lll1l1_opy_, False)
            instance.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿ࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱࠦᇍ"), datetime.now() - bstack11l1ll1111_opy_)
        return result
        def bstack1ll111l111l_opy_(self, driver: object, framework_name, bstack11lll11lll_opy_: str):
            self.bstack1ll1111ll11_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1ll11l11111_opy_ = self.bstack1ll111l1l1l_opy_[bstack1l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠣᇎ")]
            req.bstack11lll11lll_opy_ = bstack11lll11lll_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1lll11111l1_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦᇏ") + str(r) + bstack1l1l11_opy_ (u"ࠥࠦᇐ"))
                else:
                    bstack1ll111ll11l_opy_ = json.loads(r.bstack1ll11l1ll11_opy_.decode(bstack1l1l11_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᇑ")))
                    if bstack11lll11lll_opy_ == bstack1l1l11_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩᇒ"):
                        return bstack1ll111ll11l_opy_.get(bstack1l1l11_opy_ (u"ࠨࡤࡢࡶࡤࠦᇓ"), [])
                    else:
                        return bstack1ll111ll11l_opy_.get(bstack1l1l11_opy_ (u"ࠢࡥࡣࡷࡥࠧᇔ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack1l1l11_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡥࡵࡡࡤࡴࡵࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࠦࡦࡳࡱࡰࠤࡨࡲࡩ࠻ࠢࠥᇕ") + str(e) + bstack1l1l11_opy_ (u"ࠤࠥᇖ"))
    @measure(event_name=EVENTS.bstack1l1l1ll1l1_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠧᇗ"))
            return
        if self.bstack1ll11l1l111_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡥࡵࡶࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᇘ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1ll111l111l_opy_(driver, framework_name, bstack1l1l11_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠤᇙ"))
        bstack1ll1l11111l_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1l11_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠥᇚ"), None)
        if not bstack1ll1l11111l_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠢ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᇛ") + str(framework_name) + bstack1l1l11_opy_ (u"ࠣࠤᇜ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11l1ll1111_opy_ = datetime.now()
        if framework_name == bstack1l1l11_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᇝ"):
            result = self.bstack1ll11111lll_opy_.bstack1ll11ll111l_opy_(driver, bstack1ll1l11111l_opy_)
        else:
            result = driver.execute_async_script(bstack1ll1l11111l_opy_)
        instance = bstack1lllll11lll_opy_.bstack1llll1ll1l1_opy_(driver)
        if instance:
            instance.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࠨᇞ"), datetime.now() - bstack11l1ll1111_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l1ll111ll_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࡡࡶࡹࡲࡳࡡࡳࡻ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢᇟ"))
            return
        if self.bstack1ll11l1l111_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1ll111l111l_opy_(driver, framework_name, bstack1l1l11_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠩᇠ"))
        bstack1ll1l11111l_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1l11_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠥᇡ"), None)
        if not bstack1ll1l11111l_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠢ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᇢ") + str(framework_name) + bstack1l1l11_opy_ (u"ࠣࠤᇣ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11l1ll1111_opy_ = datetime.now()
        if framework_name == bstack1l1l11_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᇤ"):
            result = self.bstack1ll11111lll_opy_.bstack1ll11ll111l_opy_(driver, bstack1ll1l11111l_opy_)
        else:
            result = driver.execute_async_script(bstack1ll1l11111l_opy_)
        instance = bstack1lllll11lll_opy_.bstack1llll1ll1l1_opy_(driver)
        if instance:
            instance.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࡥࡳࡶ࡯ࡰࡥࡷࡿࠢᇥ"), datetime.now() - bstack11l1ll1111_opy_)
        return result
    @measure(event_name=EVENTS.bstack1ll111ll1ll_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def bstack1ll11l111l1_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1ll1111ll11_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1lll11111l1_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᇦ") + str(r) + bstack1l1l11_opy_ (u"ࠧࠨᇧ"))
            else:
                self.bstack1ll11lll111_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᇨ") + str(e) + bstack1l1l11_opy_ (u"ࠢࠣᇩ"))
            traceback.print_exc()
            raise e
    def bstack1ll11lll111_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠣ࡮ࡲࡥࡩࡥࡣࡰࡰࡩ࡭࡬ࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣᇪ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1ll11l1l111_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1ll111l1l1l_opy_[bstack1l1l11_opy_ (u"ࠤࡷࡩࡸࡺࡨࡶࡤࡢࡦࡺ࡯࡬ࡥࡡࡸࡹ࡮ࡪࠢᇫ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1ll111l1l1l_opy_[bstack1l1l11_opy_ (u"ࠥࡸ࡭ࡥࡪࡸࡶࡢࡸࡴࡱࡥ࡯ࠤᇬ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1ll111l1l1l_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1ll1111lll1_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1ll111ll1l1_opy_ and command.module == self.bstack1ll1l111ll1_opy_:
                        if command.method and not command.method in bstack1ll1111lll1_opy_:
                            bstack1ll1111lll1_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1ll1111lll1_opy_[command.method]:
                            bstack1ll1111lll1_opy_[command.method][command.name] = list()
                        bstack1ll1111lll1_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1ll1111lll1_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1ll1111l111_opy_(
        self,
        f: bstack1ll1ll111ll_opy_,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1ll11111lll_opy_, bstack1lll1llll11_opy_) and method_name != bstack1l1l11_opy_ (u"ࠫࡨࡵ࡮࡯ࡧࡦࡸࠬᇭ"):
            return
        if bstack1lllll11lll_opy_.bstack1llllll111l_opy_(instance, bstack1llll111lll_opy_.bstack1ll1l111111_opy_):
            return
        if f.bstack1ll11l111ll_opy_(method_name, *args):
            bstack1ll1111l1l1_opy_ = False
            desired_capabilities = f.bstack1ll111lllll_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1ll11ll1111_opy_(instance)
                platform_index = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll111ll_opy_.bstack1ll1l1111l1_opy_, 0)
                bstack1ll11l1lll1_opy_ = datetime.now()
                r = self.bstack1ll11l111l1_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡧࡴࡴࡦࡪࡩࠥᇮ"), datetime.now() - bstack1ll11l1lll1_opy_)
                bstack1ll1111l1l1_opy_ = r.success
            else:
                self.logger.error(bstack1l1l11_opy_ (u"ࠨ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡥࡧࡶ࡭ࡷ࡫ࡤࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠽ࠣᇯ") + str(desired_capabilities) + bstack1l1l11_opy_ (u"ࠢࠣᇰ"))
            f.bstack1llll1l1ll1_opy_(instance, bstack1llll111lll_opy_.bstack1ll1l111111_opy_, bstack1ll1111l1l1_opy_)
    def bstack1l1lll111l_opy_(self, test_tags):
        bstack1ll11l111l1_opy_ = self.config.get(bstack1l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᇱ"))
        if not bstack1ll11l111l1_opy_:
            return True
        try:
            include_tags = bstack1ll11l111l1_opy_[bstack1l1l11_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᇲ")] if bstack1l1l11_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᇳ") in bstack1ll11l111l1_opy_ and isinstance(bstack1ll11l111l1_opy_[bstack1l1l11_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᇴ")], list) else []
            exclude_tags = bstack1ll11l111l1_opy_[bstack1l1l11_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᇵ")] if bstack1l1l11_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᇶ") in bstack1ll11l111l1_opy_ and isinstance(bstack1ll11l111l1_opy_[bstack1l1l11_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᇷ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡶࡢ࡮࡬ࡨࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡨࡧ࡮࡯࡫ࡱ࡫࠳ࠦࡅࡳࡴࡲࡶࠥࡀࠠࠣᇸ") + str(error))
        return False
    def bstack11l11llll_opy_(self, caps):
        try:
            if self.bstack1ll11l1l111_opy_:
                bstack1ll111llll1_opy_ = caps.get(bstack1l1l11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣᇹ"))
                if bstack1ll111llll1_opy_ is not None and str(bstack1ll111llll1_opy_).lower() == bstack1l1l11_opy_ (u"ࠥࡥࡳࡪࡲࡰ࡫ࡧࠦᇺ"):
                    bstack1ll11ll1ll1_opy_ = caps.get(bstack1l1l11_opy_ (u"ࠦࡦࡶࡰࡪࡷࡰ࠾ࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨᇻ")) or caps.get(bstack1l1l11_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢᇼ"))
                    if bstack1ll11ll1ll1_opy_ is not None and int(bstack1ll11ll1ll1_opy_) < 11:
                        self.logger.warning(bstack1l1l11_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡁ࡯ࡦࡵࡳ࡮ࡪࠠ࠲࠳ࠣࡥࡳࡪࠠࡢࡤࡲࡺࡪ࠴ࠠࡄࡷࡵࡶࡪࡴࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡺࡪࡸࡳࡪࡱࡱࠤࡂࠨᇽ") + str(bstack1ll11ll1ll1_opy_) + bstack1l1l11_opy_ (u"ࠢࠣᇾ"))
                        return False
                return True
            bstack1ll1l1111ll_opy_ = caps.get(bstack1l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᇿ"), {}).get(bstack1l1l11_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ሀ"), caps.get(bstack1l1l11_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪሁ"), bstack1l1l11_opy_ (u"ࠫࠬሂ")))
            if bstack1ll1l1111ll_opy_:
                self.logger.warning(bstack1l1l11_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡊࡥࡴ࡭ࡷࡳࡵࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤሃ"))
                return False
            browser = caps.get(bstack1l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫሄ"), bstack1l1l11_opy_ (u"ࠧࠨህ")).lower()
            if browser != bstack1l1l11_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨሆ"):
                self.logger.warning(bstack1l1l11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧሇ"))
                return False
            bstack1ll111lll1l_opy_ = bstack1ll1111l1ll_opy_
            if not self.config.get(bstack1l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬለ")) or self.config.get(bstack1l1l11_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨሉ")):
                bstack1ll111lll1l_opy_ = bstack1ll11l1llll_opy_
            browser_version = caps.get(bstack1l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ሊ"))
            if not browser_version:
                browser_version = caps.get(bstack1l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧላ"), {}).get(bstack1l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨሌ"), bstack1l1l11_opy_ (u"ࠨࠩል"))
            if browser_version and browser_version != bstack1l1l11_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩሎ") and int(browser_version.split(bstack1l1l11_opy_ (u"ࠪ࠲ࠬሏ"))[0]) <= bstack1ll111lll1l_opy_:
                self.logger.warning(bstack1l1l11_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡧࡳࡧࡤࡸࡪࡸࠠࡵࡪࡤࡲࠥࠨሐ") + str(bstack1ll111lll1l_opy_) + bstack1l1l11_opy_ (u"ࠧ࠴ࠢሑ"))
                return False
            bstack1ll111ll111_opy_ = caps.get(bstack1l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧሒ"), {}).get(bstack1l1l11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧሓ"))
            if not bstack1ll111ll111_opy_:
                bstack1ll111ll111_opy_ = caps.get(bstack1l1l11_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ሔ"), {})
            if bstack1ll111ll111_opy_ and bstack1l1l11_opy_ (u"ࠩ࠰࠱࡭࡫ࡡࡥ࡮ࡨࡷࡸ࠭ሕ") in bstack1ll111ll111_opy_.get(bstack1l1l11_opy_ (u"ࠪࡥࡷ࡭ࡳࠨሖ"), []):
                self.logger.warning(bstack1l1l11_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡰࡰࠣࡰࡪ࡭ࡡࡤࡻࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠤࡘࡽࡩࡵࡥ࡫ࠤࡹࡵࠠ࡯ࡧࡺࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨࠤࡴࡸࠠࡢࡸࡲ࡭ࡩࠦࡵࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠨሗ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡻࡧ࡬ࡪࡦࡤࡸࡪࠦࡡ࠲࠳ࡼࠤࡸࡻࡰࡱࡱࡵࡸࠥࡀࠢመ") + str(error))
            return False
    def bstack1ll1l111lll_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1ll11llllll_opy_ = {
            bstack1l1l11_opy_ (u"࠭ࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩ࠭ሙ"): test_uuid,
        }
        bstack1ll11ll11ll_opy_ = {}
        if result.success:
            bstack1ll11ll11ll_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1ll11l11l11_opy_(bstack1ll11llllll_opy_, bstack1ll11ll11ll_opy_)
    def bstack1111ll1l1_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll11ll11l1_opy_ = None
        try:
            self.bstack1ll1111ll11_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack1l1l11_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢሚ")
            req.script_name = bstack1l1l11_opy_ (u"ࠣࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸࠨማ")
            r = self.bstack1lll11111l1_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤࡩࡸࡩࡷࡧࡵࠤࡪࡾࡥࡤࡷࡷࡩࠥࡶࡡࡳࡣࡰࡷࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧሜ") + str(r.error) + bstack1l1l11_opy_ (u"ࠥࠦም"))
            else:
                bstack1ll11llllll_opy_ = self.bstack1ll1l111lll_opy_(test_uuid, r)
                bstack1ll1l11111l_opy_ = r.script
            self.logger.debug(bstack1l1l11_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡢࡸ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧሞ") + str(bstack1ll11llllll_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1ll1l11111l_opy_:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧሟ") + str(framework_name) + bstack1l1l11_opy_ (u"ࠨࠠࠣሠ"))
                return
            bstack1ll11ll11l1_opy_ = bstack1lll111lll1_opy_.bstack1ll11ll1l11_opy_(EVENTS.bstack1ll11l1l11l_opy_.value)
            self.bstack1ll1l111l11_opy_(driver, bstack1ll1l11111l_opy_, bstack1ll11llllll_opy_, framework_name)
            self.logger.info(bstack1l1l11_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠥሡ"))
            bstack1lll111lll1_opy_.end(EVENTS.bstack1ll11l1l11l_opy_.value, bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣሢ"), bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠤ࠽ࡩࡳࡪࠢሣ"), True, None, command=bstack1l1l11_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨሤ"),test_name=name)
        except Exception as bstack1ll11l1ll1l_opy_:
            self.logger.error(bstack1l1l11_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨሥ") + bstack1l1l11_opy_ (u"ࠧࡹࡴࡳࠪࡳࡥࡹ࡮ࠩࠣሦ") + bstack1l1l11_opy_ (u"ࠨࠠࡆࡴࡵࡳࡷࠦ࠺ࠣሧ") + str(bstack1ll11l1ll1l_opy_))
            bstack1lll111lll1_opy_.end(EVENTS.bstack1ll11l1l11l_opy_.value, bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢረ"), bstack1ll11ll11l1_opy_+bstack1l1l11_opy_ (u"ࠣ࠼ࡨࡲࡩࠨሩ"), False, bstack1ll11l1ll1l_opy_, command=bstack1l1l11_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧሪ"),test_name=name)
    def bstack1ll1l111l11_opy_(self, driver, bstack1ll1l11111l_opy_, bstack1ll11llllll_opy_, framework_name):
        if framework_name == bstack1l1l11_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧራ"):
            self.bstack1ll11111lll_opy_.bstack1ll11ll111l_opy_(driver, bstack1ll1l11111l_opy_, bstack1ll11llllll_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1ll1l11111l_opy_, bstack1ll11llllll_opy_))
    def _1ll11lll11l_opy_(self, instance: bstack1lll1l11l11_opy_, args: Tuple) -> list:
        bstack1l1l11_opy_ (u"ࠦࠧࠨࡅࡹࡶࡵࡥࡨࡺࠠࡵࡣࡪࡷࠥࡨࡡࡴࡧࡧࠤࡴࡴࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯࠳ࠨࠢࠣሬ")
        if bstack1l1l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩር") in instance.bstack1ll1l111l1l_opy_:
            return args[2].tags if hasattr(args[2], bstack1l1l11_opy_ (u"࠭ࡴࡢࡩࡶࠫሮ")) else []
        if hasattr(args[0], bstack1l1l11_opy_ (u"ࠧࡰࡹࡱࡣࡲࡧࡲ࡬ࡧࡵࡷࠬሯ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1ll11llll11_opy_(self, tags, capabilities):
        return self.bstack1l1lll111l_opy_(tags) and self.bstack11l11llll_opy_(capabilities)