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
from bstack_utils.bstack1l1lllll1l_opy_ import bstack1lll11lll11_opy_
from bstack_utils.constants import EVENTS
class bstack1lll111l11l_opy_(bstack1llllll11ll_opy_):
    bstack1l11l111l1l_opy_ = bstack1l11l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠦᖂ")
    NAME = bstack1l11l11_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢᖃ")
    bstack1l1l111l1ll_opy_ = bstack1l11l11_opy_ (u"ࠨࡨࡶࡤࡢࡹࡷࡲࠢᖄ")
    bstack1l1l11l11l1_opy_ = bstack1l11l11_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢᖅ")
    bstack11llll11l11_opy_ = bstack1l11l11_opy_ (u"ࠣ࡫ࡱࡴࡺࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᖆ")
    bstack1l1l11l1ll1_opy_ = bstack1l11l11_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᖇ")
    bstack1l11l11ll11_opy_ = bstack1l11l11_opy_ (u"ࠥ࡭ࡸࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡮ࡵࡣࠤᖈ")
    bstack11llll1111l_opy_ = bstack1l11l11_opy_ (u"ࠦࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᖉ")
    bstack11llll11111_opy_ = bstack1l11l11_opy_ (u"ࠧ࡫࡮ࡥࡧࡧࡣࡦࡺࠢᖊ")
    bstack1ll11ll111l_opy_ = bstack1l11l11_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࠢᖋ")
    bstack1l11ll11l11_opy_ = bstack1l11l11_opy_ (u"ࠢ࡯ࡧࡺࡷࡪࡹࡳࡪࡱࡱࠦᖌ")
    bstack11llll111ll_opy_ = bstack1l11l11_opy_ (u"ࠣࡩࡨࡸࠧᖍ")
    bstack1l1ll11l111_opy_ = bstack1l11l11_opy_ (u"ࠤࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨᖎ")
    bstack1l11l111ll1_opy_ = bstack1l11l11_opy_ (u"ࠥࡻ࠸ࡩࡥࡹࡧࡦࡹࡹ࡫ࡳࡤࡴ࡬ࡴࡹࠨᖏ")
    bstack1l11l111lll_opy_ = bstack1l11l11_opy_ (u"ࠦࡼ࠹ࡣࡦࡺࡨࡧࡺࡺࡥࡴࡥࡵ࡭ࡵࡺࡡࡴࡻࡱࡧࠧᖐ")
    bstack11llll1l11l_opy_ = bstack1l11l11_opy_ (u"ࠧࡷࡵࡪࡶࠥᖑ")
    bstack11llll111l1_opy_: Dict[str, List[Callable]] = dict()
    bstack1l11ll1ll11_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lll1l11ll1_opy_: Any
    bstack1l11l1111ll_opy_: Dict
    def __init__(
        self,
        bstack1l11ll1ll11_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1lll1l11ll1_opy_: Dict[str, Any],
        methods=[bstack1l11l11_opy_ (u"ࠨ࡟ࡠ࡫ࡱ࡭ࡹࡥ࡟ࠣᖒ"), bstack1l11l11_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࠢᖓ"), bstack1l11l11_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᖔ"), bstack1l11l11_opy_ (u"ࠤࡴࡹ࡮ࡺࠢᖕ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1l11ll1ll11_opy_ = bstack1l11ll1ll11_opy_
        self.platform_index = platform_index
        self.bstack1llllll11l1_opy_(methods)
        self.bstack1lll1l11ll1_opy_ = bstack1lll1l11ll1_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1llllll11ll_opy_.get_data(bstack1lll111l11l_opy_.bstack1l1l11l11l1_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1llllll11ll_opy_.get_data(bstack1lll111l11l_opy_.bstack1l1l111l1ll_opy_, target, strict)
    @staticmethod
    def bstack11llll11ll1_opy_(target: object, strict=True):
        return bstack1llllll11ll_opy_.get_data(bstack1lll111l11l_opy_.bstack11llll11l11_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1llllll11ll_opy_.get_data(bstack1lll111l11l_opy_.bstack1l1l11l1ll1_opy_, target, strict)
    @staticmethod
    def bstack1l1lllll11l_opy_(instance: bstack1llll1llll1_opy_) -> bool:
        return bstack1llllll11ll_opy_.bstack1llllll1l1l_opy_(instance, bstack1lll111l11l_opy_.bstack1l11l11ll11_opy_, False)
    @staticmethod
    def bstack1ll11l1111l_opy_(instance: bstack1llll1llll1_opy_, default_value=None):
        return bstack1llllll11ll_opy_.bstack1llllll1l1l_opy_(instance, bstack1lll111l11l_opy_.bstack1l1l111l1ll_opy_, default_value)
    @staticmethod
    def bstack1ll1l111ll1_opy_(instance: bstack1llll1llll1_opy_, default_value=None):
        return bstack1llllll11ll_opy_.bstack1llllll1l1l_opy_(instance, bstack1lll111l11l_opy_.bstack1l1l11l1ll1_opy_, default_value)
    @staticmethod
    def bstack1l1lllllll1_opy_(hub_url: str, bstack11llll11lll_opy_=bstack1l11l11_opy_ (u"ࠥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠢᖖ")):
        try:
            bstack11llll11l1l_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11llll11l1l_opy_.endswith(bstack11llll11lll_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1ll11l111l1_opy_(method_name: str):
        return method_name == bstack1l11l11_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᖗ")
    @staticmethod
    def bstack1ll111lll1l_opy_(method_name: str, *args):
        return (
            bstack1lll111l11l_opy_.bstack1ll11l111l1_opy_(method_name)
            and bstack1lll111l11l_opy_.bstack1l11ll111ll_opy_(*args) == bstack1lll111l11l_opy_.bstack1l11ll11l11_opy_
        )
    @staticmethod
    def bstack1ll11llll1l_opy_(method_name: str, *args):
        if not bstack1lll111l11l_opy_.bstack1ll11l111l1_opy_(method_name):
            return False
        if not bstack1lll111l11l_opy_.bstack1l11l111ll1_opy_ in bstack1lll111l11l_opy_.bstack1l11ll111ll_opy_(*args):
            return False
        bstack1ll111111ll_opy_ = bstack1lll111l11l_opy_.bstack1l1llllll1l_opy_(*args)
        return bstack1ll111111ll_opy_ and bstack1l11l11_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᖘ") in bstack1ll111111ll_opy_ and bstack1l11l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᖙ") in bstack1ll111111ll_opy_[bstack1l11l11_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᖚ")]
    @staticmethod
    def bstack1ll111llll1_opy_(method_name: str, *args):
        if not bstack1lll111l11l_opy_.bstack1ll11l111l1_opy_(method_name):
            return False
        if not bstack1lll111l11l_opy_.bstack1l11l111ll1_opy_ in bstack1lll111l11l_opy_.bstack1l11ll111ll_opy_(*args):
            return False
        bstack1ll111111ll_opy_ = bstack1lll111l11l_opy_.bstack1l1llllll1l_opy_(*args)
        return (
            bstack1ll111111ll_opy_
            and bstack1l11l11_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣᖛ") in bstack1ll111111ll_opy_
            and bstack1l11l11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡣࡳ࡫ࡳࡸࠧᖜ") in bstack1ll111111ll_opy_[bstack1l11l11_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥᖝ")]
        )
    @staticmethod
    def bstack1l11ll111ll_opy_(*args):
        return str(bstack1lll111l11l_opy_.bstack1ll1l111111_opy_(*args)).lower()
    @staticmethod
    def bstack1ll1l111111_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1llllll1l_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack11l1111ll1_opy_(driver):
        command_executor = getattr(driver, bstack1l11l11_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᖞ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1l11l11_opy_ (u"ࠧࡥࡵࡳ࡮ࠥᖟ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1l11l11_opy_ (u"ࠨ࡟ࡤ࡮࡬ࡩࡳࡺ࡟ࡤࡱࡱࡪ࡮࡭ࠢᖠ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1l11l11_opy_ (u"ࠢࡳࡧࡰࡳࡹ࡫࡟ࡴࡧࡵࡺࡪࡸ࡟ࡢࡦࡧࡶࠧᖡ"), None)
        return hub_url
    def bstack1l11l1lllll_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1l11l11_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᖢ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1l11l11_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧᖣ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1l11l11_opy_ (u"ࠥࡣࡺࡸ࡬ࠣᖤ")):
                setattr(command_executor, bstack1l11l11_opy_ (u"ࠦࡤࡻࡲ࡭ࠤᖥ"), hub_url)
                result = True
        if result:
            self.bstack1l11ll1ll11_opy_ = hub_url
            bstack1lll111l11l_opy_.bstack1lllll1l1l1_opy_(instance, bstack1lll111l11l_opy_.bstack1l1l111l1ll_opy_, hub_url)
            bstack1lll111l11l_opy_.bstack1lllll1l1l1_opy_(
                instance, bstack1lll111l11l_opy_.bstack1l11l11ll11_opy_, bstack1lll111l11l_opy_.bstack1l1lllllll1_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l11l11l11l_opy_(bstack1lllllll1l1_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llllll1lll_opy_]):
        return bstack1l11l11_opy_ (u"ࠧࡀࠢᖦ").join((bstack1llll1lllll_opy_(bstack1lllllll1l1_opy_[0]).name, bstack1llllll1lll_opy_(bstack1lllllll1l1_opy_[1]).name))
    @staticmethod
    def bstack1ll111l11ll_opy_(bstack1lllllll1l1_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llllll1lll_opy_], callback: Callable):
        bstack1l11l111l11_opy_ = bstack1lll111l11l_opy_.bstack1l11l11l11l_opy_(bstack1lllllll1l1_opy_)
        if not bstack1l11l111l11_opy_ in bstack1lll111l11l_opy_.bstack11llll111l1_opy_:
            bstack1lll111l11l_opy_.bstack11llll111l1_opy_[bstack1l11l111l11_opy_] = []
        bstack1lll111l11l_opy_.bstack11llll111l1_opy_[bstack1l11l111l11_opy_].append(callback)
    def bstack1lllll11l1l_opy_(self, instance: bstack1llll1llll1_opy_, method_name: str, bstack1llllllll1l_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1l11l11_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᖧ")):
            return
        cmd = args[0] if method_name == bstack1l11l11_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣᖨ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11llll1l111_opy_ = bstack1l11l11_opy_ (u"ࠣ࠼ࠥᖩ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1llll111l_opy_(bstack1l11l11_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳ࠼ࠥᖪ") + bstack11llll1l111_opy_, bstack1llllllll1l_opy_)
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
        bstack1l11l111l11_opy_ = bstack1lll111l11l_opy_.bstack1l11l11l11l_opy_(bstack1lllllll1l1_opy_)
        self.logger.debug(bstack1l11l11_opy_ (u"ࠥࡳࡳࡥࡨࡰࡱ࡮࠾ࠥࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࡀࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᖫ") + str(kwargs) + bstack1l11l11_opy_ (u"ࠦࠧᖬ"))
        if bstack1llllllll11_opy_ == bstack1llll1lllll_opy_.QUIT:
            if bstack1l11l1111l1_opy_ == bstack1llllll1lll_opy_.PRE:
                bstack1ll11lll1l1_opy_ = bstack1lll11lll11_opy_.bstack1ll111lll11_opy_(EVENTS.bstack1ll1l1ll1_opy_.value)
                bstack1llllll11ll_opy_.bstack1lllll1l1l1_opy_(instance, EVENTS.bstack1ll1l1ll1_opy_.value, bstack1ll11lll1l1_opy_)
                self.logger.debug(bstack1l11l11_opy_ (u"ࠧ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼࡿࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࡽࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡾࠢ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡾࠤᖭ").format(instance, method_name, bstack1llllllll11_opy_, bstack1l11l1111l1_opy_))
        if bstack1llllllll11_opy_ == bstack1llll1lllll_opy_.bstack1llll1lll1l_opy_:
            if bstack1l11l1111l1_opy_ == bstack1llllll1lll_opy_.POST and not bstack1lll111l11l_opy_.bstack1l1l11l11l1_opy_ in instance.data:
                session_id = getattr(target, bstack1l11l11_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᖮ"), None)
                if session_id:
                    instance.data[bstack1lll111l11l_opy_.bstack1l1l11l11l1_opy_] = session_id
        elif (
            bstack1llllllll11_opy_ == bstack1llll1lllll_opy_.bstack1lllll1ll11_opy_
            and bstack1lll111l11l_opy_.bstack1l11ll111ll_opy_(*args) == bstack1lll111l11l_opy_.bstack1l11ll11l11_opy_
        ):
            if bstack1l11l1111l1_opy_ == bstack1llllll1lll_opy_.PRE:
                hub_url = bstack1lll111l11l_opy_.bstack11l1111ll1_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lll111l11l_opy_.bstack1l1l111l1ll_opy_: hub_url,
                            bstack1lll111l11l_opy_.bstack1l11l11ll11_opy_: bstack1lll111l11l_opy_.bstack1l1lllllll1_opy_(hub_url),
                            bstack1lll111l11l_opy_.bstack1ll11ll111l_opy_: int(
                                os.environ.get(bstack1l11l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢᖯ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1ll111111ll_opy_ = bstack1lll111l11l_opy_.bstack1l1llllll1l_opy_(*args)
                bstack11llll11ll1_opy_ = bstack1ll111111ll_opy_.get(bstack1l11l11_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᖰ"), None) if bstack1ll111111ll_opy_ else None
                if isinstance(bstack11llll11ll1_opy_, dict):
                    instance.data[bstack1lll111l11l_opy_.bstack11llll11l11_opy_] = copy.deepcopy(bstack11llll11ll1_opy_)
                    instance.data[bstack1lll111l11l_opy_.bstack1l1l11l1ll1_opy_] = bstack11llll11ll1_opy_
            elif bstack1l11l1111l1_opy_ == bstack1llllll1lll_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1l11l11_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣᖱ"), dict()).get(bstack1l11l11_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡍࡩࠨᖲ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lll111l11l_opy_.bstack1l1l11l11l1_opy_: framework_session_id,
                                bstack1lll111l11l_opy_.bstack11llll1111l_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1llllllll11_opy_ == bstack1llll1lllll_opy_.bstack1lllll1ll11_opy_
            and bstack1lll111l11l_opy_.bstack1l11ll111ll_opy_(*args) == bstack1lll111l11l_opy_.bstack11llll1l11l_opy_
            and bstack1l11l1111l1_opy_ == bstack1llllll1lll_opy_.POST
        ):
            instance.data[bstack1lll111l11l_opy_.bstack11llll11111_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l11l111l11_opy_ in bstack1lll111l11l_opy_.bstack11llll111l1_opy_:
            bstack1l11l11l1l1_opy_ = None
            for callback in bstack1lll111l11l_opy_.bstack11llll111l1_opy_[bstack1l11l111l11_opy_]:
                try:
                    bstack1l11l11l111_opy_ = callback(self, target, exec, bstack1lllllll1l1_opy_, result, *args, **kwargs)
                    if bstack1l11l11l1l1_opy_ == None:
                        bstack1l11l11l1l1_opy_ = bstack1l11l11l111_opy_
                except Exception as e:
                    self.logger.error(bstack1l11l11_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࠤᖳ") + str(e) + bstack1l11l11_opy_ (u"ࠧࠨᖴ"))
                    traceback.print_exc()
            if bstack1llllllll11_opy_ == bstack1llll1lllll_opy_.QUIT:
                if bstack1l11l1111l1_opy_ == bstack1llllll1lll_opy_.POST:
                    bstack1ll11lll1l1_opy_ = bstack1llllll11ll_opy_.bstack1llllll1l1l_opy_(instance, EVENTS.bstack1ll1l1ll1_opy_.value)
                    if bstack1ll11lll1l1_opy_!=None:
                        bstack1lll11lll11_opy_.end(EVENTS.bstack1ll1l1ll1_opy_.value, bstack1ll11lll1l1_opy_+bstack1l11l11_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᖵ"), bstack1ll11lll1l1_opy_+bstack1l11l11_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᖶ"), True, None)
            if bstack1l11l1111l1_opy_ == bstack1llllll1lll_opy_.PRE and callable(bstack1l11l11l1l1_opy_):
                return bstack1l11l11l1l1_opy_
            elif bstack1l11l1111l1_opy_ == bstack1llllll1lll_opy_.POST and bstack1l11l11l1l1_opy_:
                return bstack1l11l11l1l1_opy_
    def bstack1lllll11ll1_opy_(
        self, method_name, previous_state: bstack1llll1lllll_opy_, *args, **kwargs
    ) -> bstack1llll1lllll_opy_:
        if method_name == bstack1l11l11_opy_ (u"ࠣࡡࡢ࡭ࡳ࡯ࡴࡠࡡࠥᖷ") or method_name == bstack1l11l11_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᖸ"):
            return bstack1llll1lllll_opy_.bstack1llll1lll1l_opy_
        if method_name == bstack1l11l11_opy_ (u"ࠥࡵࡺ࡯ࡴࠣᖹ"):
            return bstack1llll1lllll_opy_.QUIT
        if method_name == bstack1l11l11_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᖺ"):
            if previous_state != bstack1llll1lllll_opy_.NONE:
                command_name = bstack1lll111l11l_opy_.bstack1l11ll111ll_opy_(*args)
                if command_name == bstack1lll111l11l_opy_.bstack1l11ll11l11_opy_:
                    return bstack1llll1lllll_opy_.bstack1llll1lll1l_opy_
            return bstack1llll1lllll_opy_.bstack1lllll1ll11_opy_
        return bstack1llll1lllll_opy_.NONE