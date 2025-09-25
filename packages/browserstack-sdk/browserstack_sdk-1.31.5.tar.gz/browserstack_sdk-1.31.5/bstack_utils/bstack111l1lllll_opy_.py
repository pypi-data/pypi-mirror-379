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
import threading
from bstack_utils.helper import bstack11l111lll_opy_
from bstack_utils.constants import bstack11l1lll1ll1_opy_, EVENTS, STAGE
from bstack_utils.bstack1l1111ll1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll1l1l111_opy_:
    bstack1llllll1ll1l_opy_ = None
    @classmethod
    def bstack1l111ll11l_opy_(cls):
        if cls.on() and os.getenv(bstack1l11l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤ⇬")):
            logger.info(
                bstack1l11l11_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠬ⇭").format(os.getenv(bstack1l11l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦ⇮"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack1l11l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⇯"), None) is None or os.environ[bstack1l11l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ⇰")] == bstack1l11l11_opy_ (u"ࠤࡱࡹࡱࡲࠢ⇱"):
            return False
        return True
    @classmethod
    def bstack1llll11ll1ll_opy_(cls, bs_config, framework=bstack1l11l11_opy_ (u"ࠥࠦ⇲")):
        bstack11l1llllll1_opy_ = False
        for fw in bstack11l1lll1ll1_opy_:
            if fw in framework:
                bstack11l1llllll1_opy_ = True
        return bstack11l111lll_opy_(bs_config.get(bstack1l11l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⇳"), bstack11l1llllll1_opy_))
    @classmethod
    def bstack1llll111ll11_opy_(cls, framework):
        return framework in bstack11l1lll1ll1_opy_
    @classmethod
    def bstack1llll1ll11l1_opy_(cls, bs_config, framework):
        return cls.bstack1llll11ll1ll_opy_(bs_config, framework) is True and cls.bstack1llll111ll11_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1l11l11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⇴"), None)
    @staticmethod
    def bstack111ll111l1_opy_():
        if getattr(threading.current_thread(), bstack1l11l11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ⇵"), None):
            return {
                bstack1l11l11_opy_ (u"ࠧࡵࡻࡳࡩࠬ⇶"): bstack1l11l11_opy_ (u"ࠨࡶࡨࡷࡹ࠭⇷"),
                bstack1l11l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇸"): getattr(threading.current_thread(), bstack1l11l11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⇹"), None)
            }
        if getattr(threading.current_thread(), bstack1l11l11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ⇺"), None):
            return {
                bstack1l11l11_opy_ (u"ࠬࡺࡹࡱࡧࠪ⇻"): bstack1l11l11_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⇼"),
                bstack1l11l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇽"): getattr(threading.current_thread(), bstack1l11l11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ⇾"), None)
            }
        return None
    @staticmethod
    def bstack1llll111l11l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll1l1l111_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack111l11111l_opy_(test, hook_name=None):
        bstack1llll111ll1l_opy_ = test.parent
        if hook_name in [bstack1l11l11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ⇿"), bstack1l11l11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫ∀"), bstack1l11l11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪ∁"), bstack1l11l11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧ∂")]:
            bstack1llll111ll1l_opy_ = test
        scope = []
        while bstack1llll111ll1l_opy_ is not None:
            scope.append(bstack1llll111ll1l_opy_.name)
            bstack1llll111ll1l_opy_ = bstack1llll111ll1l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1llll111l1l1_opy_(hook_type):
        if hook_type == bstack1l11l11_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦ∃"):
            return bstack1l11l11_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦ∄")
        elif hook_type == bstack1l11l11_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧ∅"):
            return bstack1l11l11_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤ∆")
    @staticmethod
    def bstack1llll111l1ll_opy_(bstack1llllll1ll_opy_):
        try:
            if not bstack1ll1l1l111_opy_.on():
                return bstack1llllll1ll_opy_
            if os.environ.get(bstack1l11l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣ∇"), None) == bstack1l11l11_opy_ (u"ࠦࡹࡸࡵࡦࠤ∈"):
                tests = os.environ.get(bstack1l11l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤ∉"), None)
                if tests is None or tests == bstack1l11l11_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ∊"):
                    return bstack1llllll1ll_opy_
                bstack1llllll1ll_opy_ = tests.split(bstack1l11l11_opy_ (u"ࠧ࠭ࠩ∋"))
                return bstack1llllll1ll_opy_
        except Exception as exc:
            logger.debug(bstack1l11l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤ∌") + str(str(exc)) + bstack1l11l11_opy_ (u"ࠤࠥ∍"))
        return bstack1llllll1ll_opy_