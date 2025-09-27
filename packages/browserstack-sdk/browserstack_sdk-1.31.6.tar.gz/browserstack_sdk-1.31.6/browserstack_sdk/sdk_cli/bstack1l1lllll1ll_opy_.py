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
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llllllll1l_opy_,
    bstack1lllll11lll_opy_,
    bstack1llll1lllll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll11111ll_opy_ import bstack1ll1ll111ll_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1l11l1_opy_ import bstack1lll1ll1111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l1l_opy_ import bstack1llll1llll1_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1llll11lll1_opy_
import weakref
class bstack1l1llll11ll_opy_(bstack1llll11lll1_opy_):
    bstack1l1lllll111_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1llll1lllll_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1llll1lllll_opy_]]
    def __init__(self, bstack1l1lllll111_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1l1lll1llll_opy_ = dict()
        self.bstack1l1lllll111_opy_ = bstack1l1lllll111_opy_
        self.frameworks = frameworks
        bstack1lll1ll1111_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1llll1lll1l_opy_, bstack1llllllll1l_opy_.POST), self.__1l1lllll11l_opy_)
        if any(bstack1ll1ll111ll_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1ll1ll111ll_opy_.bstack1ll111l11l1_opy_(
                (bstack1lllll1lll1_opy_.bstack1lllll1ll1l_opy_, bstack1llllllll1l_opy_.PRE), self.__1l1llll1l1l_opy_
            )
            bstack1ll1ll111ll_opy_.bstack1ll111l11l1_opy_(
                (bstack1lllll1lll1_opy_.QUIT, bstack1llllllll1l_opy_.POST), self.__1l1llll1lll_opy_
            )
    def __1l1lllll11l_opy_(
        self,
        f: bstack1lll1ll1111_opy_,
        bstack1l1llll111l_opy_: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack1l1l11_opy_ (u"ࠥࡲࡪࡽ࡟ࡱࡣࡪࡩࠧቕ"):
                return
            contexts = bstack1l1llll111l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack1l1l11_opy_ (u"ࠦࡦࡨ࡯ࡶࡶ࠽ࡦࡱࡧ࡮࡬ࠤቖ") in page.url:
                                self.logger.debug(bstack1l1l11_opy_ (u"࡙ࠧࡴࡰࡴ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡲࡪࡽࠠࡱࡣࡪࡩࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠢ቗"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lllll11lll_opy_.bstack1llll1l1ll1_opy_(instance, self.bstack1l1lllll111_opy_, True)
                                self.logger.debug(bstack1l1l11_opy_ (u"ࠨ࡟ࡠࡱࡱࡣࡵࡧࡧࡦࡡ࡬ࡲ࡮ࡺ࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦቘ") + str(instance.ref()) + bstack1l1l11_opy_ (u"ࠢࠣ቙"))
        except Exception as e:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡲࡶ࡮ࡴࡧࠡࡰࡨࡻࠥࡶࡡࡨࡧࠣ࠾ࠧቚ"),e)
    def __1l1llll1l1l_opy_(
        self,
        f: bstack1ll1ll111ll_opy_,
        driver: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lllll11lll_opy_.bstack1lllll1l1l1_opy_(instance, self.bstack1l1lllll111_opy_, False):
            return
        if not f.bstack1ll1111111l_opy_(f.hub_url(driver)):
            self.bstack1l1lll1llll_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lllll11lll_opy_.bstack1llll1l1ll1_opy_(instance, self.bstack1l1lllll111_opy_, True)
            self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡢࡣࡴࡴ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡ࡬ࡲ࡮ࡺ࠺ࠡࡰࡲࡲࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡩࡸࡩࡷࡧࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢቛ") + str(instance.ref()) + bstack1l1l11_opy_ (u"ࠥࠦቜ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lllll11lll_opy_.bstack1llll1l1ll1_opy_(instance, self.bstack1l1lllll111_opy_, True)
        self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࡣ࡮ࡴࡩࡵ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨቝ") + str(instance.ref()) + bstack1l1l11_opy_ (u"ࠧࠨ቞"))
    def __1l1llll1lll_opy_(
        self,
        f: bstack1ll1ll111ll_opy_,
        driver: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1l1llll11l1_opy_(instance)
        self.logger.debug(bstack1l1l11_opy_ (u"ࠨ࡟ࡠࡱࡱࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡱࡶ࡫ࡷ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣ቟") + str(instance.ref()) + bstack1l1l11_opy_ (u"ࠢࠣበ"))
    def bstack1l1lllll1l1_opy_(self, context: bstack1llll1llll1_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll1lllll_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1l1llll1111_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1ll1ll111ll_opy_.bstack1l1llll1l11_opy_(data[1])
                    and data[1].bstack1l1llll1111_opy_(context)
                    and getattr(data[0](), bstack1l1l11_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠧቡ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lllll111l1_opy_, reverse=reverse)
    def bstack1l1lll1lll1_opy_(self, context: bstack1llll1llll1_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll1lllll_opy_]]:
        matches = []
        for data in self.bstack1l1lll1llll_opy_.values():
            if (
                data[1].bstack1l1llll1111_opy_(context)
                and getattr(data[0](), bstack1l1l11_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨቢ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lllll111l1_opy_, reverse=reverse)
    def bstack1l1llll1ll1_opy_(self, instance: bstack1llll1lllll_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1l1llll11l1_opy_(self, instance: bstack1llll1lllll_opy_) -> bool:
        if self.bstack1l1llll1ll1_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lllll11lll_opy_.bstack1llll1l1ll1_opy_(instance, self.bstack1l1lllll111_opy_, False)
            return True
        return False