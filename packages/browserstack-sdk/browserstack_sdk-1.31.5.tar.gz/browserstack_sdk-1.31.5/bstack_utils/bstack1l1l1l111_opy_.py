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
import tempfile
import math
from bstack_utils import bstack1l1111ll1l_opy_
from bstack_utils.constants import bstack1lll1111ll_opy_, bstack11l1ll1ll1l_opy_
from bstack_utils.helper import bstack11l11ll111l_opy_, get_host_info
from bstack_utils.bstack11ll111l1ll_opy_ import bstack11ll111lll1_opy_
bstack1111lll11l1_opy_ = bstack1l11l11_opy_ (u"ࠣࡴࡨࡸࡷࡿࡔࡦࡵࡷࡷࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠢṔ")
bstack1111lll1ll1_opy_ = bstack1l11l11_opy_ (u"ࠤࡤࡦࡴࡸࡴࡃࡷ࡬ࡰࡩࡕ࡮ࡇࡣ࡬ࡰࡺࡸࡥࠣṕ")
bstack1111ll1l11l_opy_ = bstack1l11l11_opy_ (u"ࠥࡶࡺࡴࡐࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡉࡥ࡮ࡲࡥࡥࡈ࡬ࡶࡸࡺࠢṖ")
bstack1111ll1lll1_opy_ = bstack1l11l11_opy_ (u"ࠦࡷ࡫ࡲࡶࡰࡓࡶࡪࡼࡩࡰࡷࡶࡰࡾࡌࡡࡪ࡮ࡨࡨࠧṗ")
bstack111l11111ll_opy_ = bstack1l11l11_opy_ (u"ࠧࡹ࡫ࡪࡲࡉࡰࡦࡱࡹࡢࡰࡧࡊࡦ࡯࡬ࡦࡦࠥṘ")
bstack1111lllll11_opy_ = bstack1l11l11_opy_ (u"ࠨࡲࡶࡰࡖࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࠥṙ")
bstack1111ll11l1l_opy_ = {
    bstack1111lll11l1_opy_,
    bstack1111lll1ll1_opy_,
    bstack1111ll1l11l_opy_,
    bstack1111ll1lll1_opy_,
    bstack111l11111ll_opy_,
    bstack1111lllll11_opy_
}
bstack111l111ll11_opy_ = {bstack1l11l11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧṚ")}
logger = bstack1l1111ll1l_opy_.get_logger(__name__, bstack1lll1111ll_opy_)
class bstack1111ll1llll_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack1111ll1111l_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1l111lll_opy_:
    _1ll1ll1l11l_opy_ = None
    def __init__(self, config):
        self.bstack1111ll11l11_opy_ = False
        self.bstack111l111l1l1_opy_ = False
        self.bstack1111ll111ll_opy_ = False
        self.bstack1111llll111_opy_ = False
        self.bstack111l111l1ll_opy_ = None
        self.bstack111l1111l1l_opy_ = bstack1111ll1llll_opy_()
        self.bstack111l11111l1_opy_ = None
        opts = config.get(bstack1l11l11_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬṛ"), {})
        bstack1111ll1ll11_opy_ = opts.get(bstack1111lllll11_opy_, {})
        self.__1111ll1l1l1_opy_(
            bstack1111ll1ll11_opy_.get(bstack1l11l11_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪṜ"), False),
            bstack1111ll1ll11_opy_.get(bstack1l11l11_opy_ (u"ࠪࡱࡴࡪࡥࠨṝ"), bstack1l11l11_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫṞ")),
            bstack1111ll1ll11_opy_.get(bstack1l11l11_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬṟ"), None)
        )
        self.__1111ll111l1_opy_(opts.get(bstack1111ll1l11l_opy_, False))
        self.__111l1111l11_opy_(opts.get(bstack1111ll1lll1_opy_, False))
        self.__1111lll1111_opy_(opts.get(bstack111l11111ll_opy_, False))
    @classmethod
    def bstack1lllll1ll1_opy_(cls, config=None):
        if cls._1ll1ll1l11l_opy_ is None and config is not None:
            cls._1ll1ll1l11l_opy_ = bstack1l111lll_opy_(config)
        return cls._1ll1ll1l11l_opy_
    @staticmethod
    def bstack1lllllll11_opy_(config: dict) -> bool:
        bstack1111ll11ll1_opy_ = config.get(bstack1l11l11_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪṠ"), {}).get(bstack1111lll11l1_opy_, {})
        return bstack1111ll11ll1_opy_.get(bstack1l11l11_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨṡ"), False)
    @staticmethod
    def bstack1ll11lllll_opy_(config: dict) -> int:
        bstack1111ll11ll1_opy_ = config.get(bstack1l11l11_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬṢ"), {}).get(bstack1111lll11l1_opy_, {})
        retries = 0
        if bstack1l111lll_opy_.bstack1lllllll11_opy_(config):
            retries = bstack1111ll11ll1_opy_.get(bstack1l11l11_opy_ (u"ࠩࡰࡥࡽࡘࡥࡵࡴ࡬ࡩࡸ࠭ṣ"), 1)
        return retries
    @staticmethod
    def bstack1l111l1l_opy_(config: dict) -> dict:
        bstack111l1111lll_opy_ = config.get(bstack1l11l11_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧṤ"), {})
        return {
            key: value for key, value in bstack111l1111lll_opy_.items() if key in bstack1111ll11l1l_opy_
        }
    @staticmethod
    def bstack111l1111ll1_opy_():
        bstack1l11l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅ࡫ࡩࡨࡱࠠࡪࡨࠣࡸ࡭࡫ࠠࡢࡤࡲࡶࡹࠦࡢࡶ࡫࡯ࡨࠥ࡬ࡩ࡭ࡧࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣṥ")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack1l11l11_opy_ (u"ࠧࡧࡢࡰࡴࡷࡣࡧࡻࡩ࡭ࡦࡢࡿࢂࠨṦ").format(os.getenv(bstack1l11l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦṧ")))))
    @staticmethod
    def bstack1111ll1l1ll_opy_(test_name: str):
        bstack1l11l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈ࡮ࡥࡤ࡭ࠣ࡭࡫ࠦࡴࡩࡧࠣࡥࡧࡵࡲࡵࠢࡥࡹ࡮ࡲࡤࠡࡨ࡬ࡰࡪࠦࡥࡹ࡫ࡶࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦṨ")
        bstack111l111l111_opy_ = os.path.join(tempfile.gettempdir(), bstack1l11l11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹ࡟ࡼࡿ࠱ࡸࡽࡺࠢṩ").format(os.getenv(bstack1l11l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢṪ"))))
        with open(bstack111l111l111_opy_, bstack1l11l11_opy_ (u"ࠪࡥࠬṫ")) as file:
            file.write(bstack1l11l11_opy_ (u"ࠦࢀࢃ࡜࡯ࠤṬ").format(test_name))
    @staticmethod
    def bstack111l111111l_opy_(framework: str) -> bool:
       return framework.lower() in bstack111l111ll11_opy_
    @staticmethod
    def bstack11l1l11llll_opy_(config: dict) -> bool:
        bstack1111llll11l_opy_ = config.get(bstack1l11l11_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩṭ"), {}).get(bstack1111lll1ll1_opy_, {})
        return bstack1111llll11l_opy_.get(bstack1l11l11_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧṮ"), False)
    @staticmethod
    def bstack11l1l111ll1_opy_(config: dict, bstack11l1l1l1l11_opy_: int = 0) -> int:
        bstack1l11l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡌ࡫ࡴࠡࡶ࡫ࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥ࠮ࠣࡻ࡭࡯ࡣࡩࠢࡦࡥࡳࠦࡢࡦࠢࡤࡲࠥࡧࡢࡴࡱ࡯ࡹࡹ࡫ࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡴࠣࡥࠥࡶࡥࡳࡥࡨࡲࡹࡧࡧࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡥࡲࡲ࡫࡯ࡧࠡࠪࡧ࡭ࡨࡺࠩ࠻ࠢࡗ࡬ࡪࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡳࡹࡧ࡬ࡠࡶࡨࡷࡹࡹࠠࠩ࡫ࡱࡸ࠮ࡀࠠࡕࡪࡨࠤࡹࡵࡴࡢ࡮ࠣࡲࡺࡳࡢࡦࡴࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥ࠮ࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡨࡲࡶࠥࡶࡥࡳࡥࡨࡲࡹࡧࡧࡦ࠯ࡥࡥࡸ࡫ࡤࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧࡷ࠮࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡱࡸ࠿ࠦࡔࡩࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧṯ")
        bstack1111llll11l_opy_ = config.get(bstack1l11l11_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬṰ"), {}).get(bstack1l11l11_opy_ (u"ࠩࡤࡦࡴࡸࡴࡃࡷ࡬ࡰࡩࡕ࡮ࡇࡣ࡬ࡰࡺࡸࡥࠨṱ"), {})
        bstack1111ll1ll1l_opy_ = 0
        bstack1111ll1l111_opy_ = 0
        if bstack1l111lll_opy_.bstack11l1l11llll_opy_(config):
            bstack1111ll1l111_opy_ = bstack1111llll11l_opy_.get(bstack1l11l11_opy_ (u"ࠪࡱࡦࡾࡆࡢ࡫࡯ࡹࡷ࡫ࡳࠨṲ"), 5)
            if isinstance(bstack1111ll1l111_opy_, str) and bstack1111ll1l111_opy_.endswith(bstack1l11l11_opy_ (u"ࠫࠪ࠭ṳ")):
                try:
                    percentage = int(bstack1111ll1l111_opy_.strip(bstack1l11l11_opy_ (u"ࠬࠫࠧṴ")))
                    if bstack11l1l1l1l11_opy_ > 0:
                        bstack1111ll1ll1l_opy_ = math.ceil((percentage * bstack11l1l1l1l11_opy_) / 100)
                    else:
                        raise ValueError(bstack1l11l11_opy_ (u"ࠨࡔࡰࡶࡤࡰࠥࡺࡥࡴࡶࡶࠤࡲࡻࡳࡵࠢࡥࡩࠥࡶࡲࡰࡸ࡬ࡨࡪࡪࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠮ࡤࡤࡷࡪࡪࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦࡶ࠲ࠧṵ"))
                except ValueError as e:
                    raise ValueError(bstack1l11l11_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩࠥࡼࡡ࡭ࡷࡨࠤ࡫ࡵࡲࠡ࡯ࡤࡼࡋࡧࡩ࡭ࡷࡵࡩࡸࡀࠠࡼࡿࠥṶ").format(bstack1111ll1l111_opy_)) from e
            else:
                bstack1111ll1ll1l_opy_ = int(bstack1111ll1l111_opy_)
        logger.info(bstack1l11l11_opy_ (u"ࠣࡏࡤࡼࠥ࡬ࡡࡪ࡮ࡸࡶࡪࡹࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦࠣࡷࡪࡺࠠࡵࡱ࠽ࠤࢀࢃࠠࠩࡨࡵࡳࡲࠦࡣࡰࡰࡩ࡭࡬ࡀࠠࡼࡿࠬࠦṷ").format(bstack1111ll1ll1l_opy_, bstack1111ll1l111_opy_))
        return bstack1111ll1ll1l_opy_
    def bstack1111lllllll_opy_(self):
        return self.bstack1111llll111_opy_
    def bstack1111ll11lll_opy_(self):
        return self.bstack111l111l1ll_opy_
    def bstack111l1111111_opy_(self):
        return self.bstack111l11111l1_opy_
    def __1111ll1l1l1_opy_(self, enabled, mode, source=None):
        try:
            self.bstack1111llll111_opy_ = bool(enabled)
            self.bstack111l111l1ll_opy_ = mode
            if source is None:
                self.bstack111l11111l1_opy_ = []
            elif isinstance(source, list):
                self.bstack111l11111l1_opy_ = source
            self.__1111llll1ll_opy_()
        except Exception as e:
            logger.error(bstack1l11l11_opy_ (u"ࠤ࡞ࡣࡤࡹࡥࡵࡡࡵࡹࡳࡥࡳ࡮ࡣࡵࡸࡤࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮࡞ࠢࠣࡿࢂࠨṸ").format(e))
    def bstack111l111ll1l_opy_(self):
        return self.bstack1111ll11l11_opy_
    def __1111ll111l1_opy_(self, value):
        self.bstack1111ll11l11_opy_ = bool(value)
        self.__1111llll1ll_opy_()
    def bstack1111llllll1_opy_(self):
        return self.bstack111l111l1l1_opy_
    def __111l1111l11_opy_(self, value):
        self.bstack111l111l1l1_opy_ = bool(value)
        self.__1111llll1ll_opy_()
    def bstack1111lll1l11_opy_(self):
        return self.bstack1111ll111ll_opy_
    def __1111lll1111_opy_(self, value):
        self.bstack1111ll111ll_opy_ = bool(value)
        self.__1111llll1ll_opy_()
    def __1111llll1ll_opy_(self):
        if self.bstack1111llll111_opy_:
            self.bstack1111ll11l11_opy_ = False
            self.bstack111l111l1l1_opy_ = False
            self.bstack1111ll111ll_opy_ = False
            self.bstack111l1111l1l_opy_.enable(bstack1111lllll11_opy_)
        elif self.bstack1111ll11l11_opy_:
            self.bstack111l111l1l1_opy_ = False
            self.bstack1111ll111ll_opy_ = False
            self.bstack1111llll111_opy_ = False
            self.bstack111l1111l1l_opy_.enable(bstack1111ll1l11l_opy_)
        elif self.bstack111l111l1l1_opy_:
            self.bstack1111ll11l11_opy_ = False
            self.bstack1111ll111ll_opy_ = False
            self.bstack1111llll111_opy_ = False
            self.bstack111l1111l1l_opy_.enable(bstack1111ll1lll1_opy_)
        elif self.bstack1111ll111ll_opy_:
            self.bstack1111ll11l11_opy_ = False
            self.bstack111l111l1l1_opy_ = False
            self.bstack1111llll111_opy_ = False
            self.bstack111l1111l1l_opy_.enable(bstack111l11111ll_opy_)
        else:
            self.bstack111l1111l1l_opy_.disable()
    def bstack111111ll_opy_(self):
        return self.bstack111l1111l1l_opy_.bstack1111ll1111l_opy_()
    def bstack1l11ll1ll1_opy_(self):
        if self.bstack111l1111l1l_opy_.bstack1111ll1111l_opy_():
            return self.bstack111l1111l1l_opy_.get_name()
        return None
    def bstack111l11l11l1_opy_(self):
        data = {
            bstack1l11l11_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩṹ"): {
                bstack1l11l11_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬṺ"): self.bstack1111lllllll_opy_(),
                bstack1l11l11_opy_ (u"ࠬࡳ࡯ࡥࡧࠪṻ"): self.bstack1111ll11lll_opy_(),
                bstack1l11l11_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭Ṽ"): self.bstack111l1111111_opy_()
            }
        }
        return data
    def bstack1111lllll1l_opy_(self, config):
        bstack1111lll1lll_opy_ = {}
        bstack1111lll1lll_opy_[bstack1l11l11_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ṽ")] = {
            bstack1l11l11_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩṾ"): self.bstack1111lllllll_opy_(),
            bstack1l11l11_opy_ (u"ࠩࡰࡳࡩ࡫ࠧṿ"): self.bstack1111ll11lll_opy_()
        }
        bstack1111lll1lll_opy_[bstack1l11l11_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡳࡶࡪࡼࡩࡰࡷࡶࡰࡾࡥࡦࡢ࡫࡯ࡩࡩ࠭Ẁ")] = {
            bstack1l11l11_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬẁ"): self.bstack1111llllll1_opy_()
        }
        bstack1111lll1lll_opy_[bstack1l11l11_opy_ (u"ࠬࡸࡵ࡯ࡡࡳࡶࡪࡼࡩࡰࡷࡶࡰࡾࡥࡦࡢ࡫࡯ࡩࡩࡥࡦࡪࡴࡶࡸࠬẂ")] = {
            bstack1l11l11_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧẃ"): self.bstack111l111ll1l_opy_()
        }
        bstack1111lll1lll_opy_[bstack1l11l11_opy_ (u"ࠧࡴ࡭࡬ࡴࡤ࡬ࡡࡪ࡮࡬ࡲ࡬ࡥࡡ࡯ࡦࡢࡪࡱࡧ࡫ࡺࠩẄ")] = {
            bstack1l11l11_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩẅ"): self.bstack1111lll1l11_opy_()
        }
        if self.bstack1lllllll11_opy_(config):
            bstack1111lll1lll_opy_[bstack1l11l11_opy_ (u"ࠩࡵࡩࡹࡸࡹࡠࡶࡨࡷࡹࡹ࡟ࡰࡰࡢࡪࡦ࡯࡬ࡶࡴࡨࠫẆ")] = {
                bstack1l11l11_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫẇ"): True,
                bstack1l11l11_opy_ (u"ࠫࡲࡧࡸࡠࡴࡨࡸࡷ࡯ࡥࡴࠩẈ"): self.bstack1ll11lllll_opy_(config)
            }
        if self.bstack11l1l11llll_opy_(config):
            bstack1111lll1lll_opy_[bstack1l11l11_opy_ (u"ࠬࡧࡢࡰࡴࡷࡣࡧࡻࡩ࡭ࡦࡢࡳࡳࡥࡦࡢ࡫࡯ࡹࡷ࡫ࠧẉ")] = {
                bstack1l11l11_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧẊ"): True,
                bstack1l11l11_opy_ (u"ࠧ࡮ࡣࡻࡣ࡫ࡧࡩ࡭ࡷࡵࡩࡸ࠭ẋ"): self.bstack11l1l111ll1_opy_(config)
            }
        return bstack1111lll1lll_opy_
    def bstack1lll11l1_opy_(self, config):
        bstack1l11l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉ࡯࡭࡮ࡨࡧࡹࡹࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤࡧࡿࠠ࡮ࡣ࡮࡭ࡳ࡭ࠠࡢࠢࡦࡥࡱࡲࠠࡵࡱࠣࡸ࡭࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠣࠬࡸࡺࡲࠪ࠼ࠣࡘ࡭࡫ࠠࡖࡗࡌࡈࠥࡵࡦࠡࡶ࡫ࡩࠥࡨࡵࡪ࡮ࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡦࡤࡸࡦࠦࡦࡰࡴ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡩࡤࡶ࠽ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡥࡹ࡮ࡲࡤ࠮ࡦࡤࡸࡦࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴ࠭ࠢࡲࡶࠥࡔ࡯࡯ࡧࠣ࡭࡫ࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦẌ")
        if not (config.get(bstack1l11l11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬẍ"), None) in bstack11l1ll1ll1l_opy_ and self.bstack1111lllllll_opy_()):
            return None
        bstack1111lll1l1l_opy_ = os.environ.get(bstack1l11l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨẎ"), None)
        logger.debug(bstack1l11l11_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡆࡳࡱࡲࡥࡤࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇ࠾ࠥࢁࡽࠣẏ").format(bstack1111lll1l1l_opy_))
        try:
            bstack11ll11l111l_opy_ = bstack1l11l11_opy_ (u"ࠧࡺࡥࡴࡶࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠱ࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠥẐ").format(bstack1111lll1l1l_opy_)
            bstack1111llll1l1_opy_ = self.bstack111l1111111_opy_() or [] # for multi-repo
            bstack1111lll11ll_opy_ = bstack11l11ll111l_opy_(bstack1111llll1l1_opy_) # bstack111llll11ll_opy_-repo is handled bstack1111lll111l_opy_
            payload = {
                bstack1l11l11_opy_ (u"ࠨࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠦẑ"): config.get(bstack1l11l11_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬẒ"), bstack1l11l11_opy_ (u"ࠨࠩẓ")),
                bstack1l11l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠧẔ"): config.get(bstack1l11l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ẕ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1l11l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡕࡹࡳࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤẖ"): config.get(bstack1l11l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧẗ"), bstack1l11l11_opy_ (u"࠭ࠧẘ")),
                bstack1l11l11_opy_ (u"ࠢ࡯ࡱࡧࡩࡎࡴࡤࡦࡺࠥẙ"): int(os.environ.get(bstack1l11l11_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦẚ")) or bstack1l11l11_opy_ (u"ࠤ࠳ࠦẛ")),
                bstack1l11l11_opy_ (u"ࠥࡸࡴࡺࡡ࡭ࡐࡲࡨࡪࡹࠢẜ"): int(os.environ.get(bstack1l11l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡔ࡚ࡁࡍࡡࡑࡓࡉࡋ࡟ࡄࡑࡘࡒ࡙ࠨẝ")) or bstack1l11l11_opy_ (u"ࠧ࠷ࠢẞ")),
                bstack1l11l11_opy_ (u"ࠨࡨࡰࡵࡷࡍࡳ࡬࡯ࠣẟ"): get_host_info(),
                bstack1l11l11_opy_ (u"ࠢࡱࡴࡇࡩࡹࡧࡩ࡭ࡵࠥẠ"): bstack1111lll11ll_opy_
            }
            logger.debug(bstack1l11l11_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡓࡦࡰࡧ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤࡵࡧࡹ࡭ࡱࡤࡨ࠿ࠦࡻࡾࠤạ").format(payload))
            response = bstack11ll111lll1_opy_.bstack111l111l11l_opy_(bstack11ll11l111l_opy_, payload)
            if response:
                logger.debug(bstack1l11l11_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡃࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢẢ").format(response))
                return response
            else:
                logger.error(bstack1l11l11_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡨࡵ࡬࡭ࡧࡦࡸࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨ࡛ࠥࡕࡊࡆ࠽ࠤࢀࢃࠢả").format(bstack1111lll1l1l_opy_))
                return None
        except Exception as e:
            logger.error(bstack1l11l11_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨ࡛ࠥࡕࡊࡆࠣࡿࢂࡀࠠࡼࡿࠥẤ").format(bstack1111lll1l1l_opy_, e))
            return None