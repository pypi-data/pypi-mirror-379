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
import time
from bstack_utils.bstack11ll111l11l_opy_ import bstack11ll111l1ll_opy_
from bstack_utils.constants import bstack11l1l1l1lll_opy_
from bstack_utils.helper import get_host_info, bstack11l1111llll_opy_
class bstack111l11ll1ll_opy_:
    bstack1l1l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡉࡣࡱࡨࡱ࡫ࡳࠡࡶࡨࡷࡹࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡸ࡭ࠦࡴࡩࡧࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡶࡩࡷࡼࡥࡳ࠰ࠍࠤࠥࠦࠠࠣࠤࠥ⁠")
    def __init__(self, config, logger):
        bstack1l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡤࡪࡥࡷ࠰ࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡧࡴࡴࡦࡪࡩࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡣࡸࡺࡲࡢࡶࡨ࡫ࡾࡀࠠࡴࡶࡵ࠰ࠥࡺࡥࡴࡶࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡹࡴࡳࡣࡷࡩ࡬ࡿࠠ࡯ࡣࡰࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ⁡")
        self.config = config
        self.logger = logger
        self.bstack1lllll1111ll_opy_ = bstack1l1l11_opy_ (u"ࠤࡷࡩࡸࡺ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡱ࡮࡬ࡸ࠲ࡺࡥࡴࡶࡶࠦ⁢")
        self.bstack1lllll11111l_opy_ = None
        self.bstack1lllll1111l1_opy_ = 60
        self.bstack1llll1lll11l_opy_ = 5
        self.bstack1llll1lllll1_opy_ = 0
    def bstack111l11l1111_opy_(self, test_files, orchestration_strategy, bstack111l111llll_opy_={}):
        bstack1l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡊࡰ࡬ࡸ࡮ࡧࡴࡦࡵࠣࡸ࡭࡫ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡲࡷࡨࡷࡹࠦࡡ࡯ࡦࠣࡷࡹࡵࡲࡦࡵࠣࡸ࡭࡫ࠠࡳࡧࡶࡴࡴࡴࡳࡦࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡵࡵ࡬࡭࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ⁣")
        self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡍࡳ࡯ࡴࡪࡣࡷ࡭ࡳ࡭ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡽࡩࡵࡪࠣࡷࡹࡸࡡࡵࡧࡪࡽ࠿ࠦࡻࡾࠤ⁤").format(orchestration_strategy))
        try:
            bstack1111ll1111l_opy_ = []
            if bstack111l111llll_opy_[bstack1l1l11_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫ⁥")].get(bstack1l1l11_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ⁦"), False): # check if bstack1lllll111111_opy_ bstack1llll1llll1l_opy_ is enabled
                bstack1111lll11ll_opy_ = bstack111l111llll_opy_[bstack1l1l11_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭⁧")].get(bstack1l1l11_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ⁨"), []) # for multi-repo
                bstack1111ll1111l_opy_ = bstack11l1111llll_opy_(bstack1111lll11ll_opy_) # bstack11l11ll1lll_opy_-repo is handled bstack1111lllllll_opy_
            payload = {
                bstack1l1l11_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣ⁩"): [{bstack1l1l11_opy_ (u"ࠥࡪ࡮ࡲࡥࡑࡣࡷ࡬ࠧ⁪"): f} for f in test_files],
                bstack1l1l11_opy_ (u"ࠦࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡗࡹࡸࡡࡵࡧࡪࡽࠧ⁫"): orchestration_strategy,
                bstack1l1l11_opy_ (u"ࠧࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡒ࡫ࡴࡢࡦࡤࡸࡦࠨ⁬"): bstack111l111llll_opy_,
                bstack1l1l11_opy_ (u"ࠨ࡮ࡰࡦࡨࡍࡳࡪࡥࡹࠤ⁭"): int(os.environ.get(bstack1l1l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥ⁮")) or bstack1l1l11_opy_ (u"ࠣ࠲ࠥ⁯")),
                bstack1l1l11_opy_ (u"ࠤࡷࡳࡹࡧ࡬ࡏࡱࡧࡩࡸࠨ⁰"): int(os.environ.get(bstack1l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡓ࡙ࡇࡌࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧⁱ")) or bstack1l1l11_opy_ (u"ࠦ࠶ࠨ⁲")),
                bstack1l1l11_opy_ (u"ࠧࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠥ⁳"): self.config.get(bstack1l1l11_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ⁴"), bstack1l1l11_opy_ (u"ࠧࠨ⁵")),
                bstack1l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠦ⁶"): self.config.get(bstack1l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ⁷"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ⁸"): self.config.get(bstack1l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭⁹"), bstack1l1l11_opy_ (u"ࠬ࠭⁺")),
                bstack1l1l11_opy_ (u"ࠨࡨࡰࡵࡷࡍࡳ࡬࡯ࠣ⁻"): get_host_info(),
                bstack1l1l11_opy_ (u"ࠢࡱࡴࡇࡩࡹࡧࡩ࡭ࡵࠥ⁼"): bstack1111ll1111l_opy_
            }
            self.logger.debug(bstack1l1l11_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷ࠿ࠦࡻࡾࠤ⁽").format(payload))
            response = bstack11ll111l1ll_opy_.bstack1llllll1111l_opy_(self.bstack1lllll1111ll_opy_, payload)
            if response:
                self.bstack1lllll11111l_opy_ = self._1llll1ll1ll1_opy_(response)
                self.logger.debug(bstack1l1l11_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡕࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧ⁾").format(self.bstack1lllll11111l_opy_))
            else:
                self.logger.error(bstack1l1l11_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠰ࠥⁿ"))
        except Exception as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡳࡪࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹ࠺࠻ࠢࡾࢁࠧ₀").format(e))
    def _1llll1ll1ll1_opy_(self, response):
        bstack1l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡂࡒࡌࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠦࡡ࡯ࡦࠣࡩࡽࡺࡲࡢࡥࡷࡷࠥࡸࡥ࡭ࡧࡹࡥࡳࡺࠠࡧ࡫ࡨࡰࡩࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ₁")
        bstack1ll1ll1ll1_opy_ = {}
        bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢ₂")] = response.get(bstack1l1l11_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣ₃"), self.bstack1lllll1111l1_opy_)
        bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥ₄")] = response.get(bstack1l1l11_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠦ₅"), self.bstack1llll1lll11l_opy_)
        bstack1lllll111l11_opy_ = response.get(bstack1l1l11_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨ₆"))
        bstack1llll1lll1l1_opy_ = response.get(bstack1l1l11_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣ₇"))
        if bstack1lllll111l11_opy_:
            bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸ࡚ࡸ࡬ࠣ₈")] = bstack1lllll111l11_opy_.split(bstack11l1l1l1lll_opy_ + bstack1l1l11_opy_ (u"ࠨ࠯ࠣ₉"))[1] if bstack11l1l1l1lll_opy_ + bstack1l1l11_opy_ (u"ࠢ࠰ࠤ₊") in bstack1lllll111l11_opy_ else bstack1lllll111l11_opy_
        else:
            bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦ₋")] = None
        if bstack1llll1lll1l1_opy_:
            bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨ₌")] = bstack1llll1lll1l1_opy_.split(bstack11l1l1l1lll_opy_ + bstack1l1l11_opy_ (u"ࠥ࠳ࠧ₍"))[1] if bstack11l1l1l1lll_opy_ + bstack1l1l11_opy_ (u"ࠦ࠴ࠨ₎") in bstack1llll1lll1l1_opy_ else bstack1llll1lll1l1_opy_
        else:
            bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤ₏")] = None
        if (
            response.get(bstack1l1l11_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢₐ")) is None or
            response.get(bstack1l1l11_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤₑ")) is None or
            response.get(bstack1l1l11_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧₒ")) is None or
            response.get(bstack1l1l11_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧₓ")) is None
        ):
            self.logger.debug(bstack1l1l11_opy_ (u"ࠥ࡟ࡵࡸ࡯ࡤࡧࡶࡷࡤࡹࡰ࡭࡫ࡷࡣࡹ࡫ࡳࡵࡵࡢࡶࡪࡹࡰࡰࡰࡶࡩࡢࠦࡒࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡰࡸࡰࡱࠦࡶࡢ࡮ࡸࡩ࠭ࡹࠩࠡࡨࡲࡶࠥࡹ࡯࡮ࡧࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࡹࠠࡪࡰࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡃࡓࡍࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢₔ"))
        return bstack1ll1ll1ll1_opy_
    def bstack111l11ll111_opy_(self):
        if not self.bstack1lllll11111l_opy_:
            self.logger.error(bstack1l1l11_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡔ࡯ࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡧࡥࡹࡧࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠱ࠦₕ"))
            return None
        bstack1llll1llllll_opy_ = None
        test_files = []
        bstack1llll1lll111_opy_ = int(time.time() * 1000) # bstack1llll1llll11_opy_ sec
        bstack1llll1ll1lll_opy_ = int(self.bstack1lllll11111l_opy_.get(bstack1l1l11_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢₖ"), self.bstack1llll1lll11l_opy_))
        bstack1llll1lll1ll_opy_ = int(self.bstack1lllll11111l_opy_.get(bstack1l1l11_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢₗ"), self.bstack1lllll1111l1_opy_)) * 1000
        bstack1llll1lll1l1_opy_ = self.bstack1lllll11111l_opy_.get(bstack1l1l11_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦₘ"), None)
        bstack1lllll111l11_opy_ = self.bstack1lllll11111l_opy_.get(bstack1l1l11_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦₙ"), None)
        if bstack1lllll111l11_opy_ is None and bstack1llll1lll1l1_opy_ is None:
            return None
        try:
            while bstack1lllll111l11_opy_ and (time.time() * 1000 - bstack1llll1lll111_opy_) < bstack1llll1lll1ll_opy_:
                response = bstack11ll111l1ll_opy_.bstack1llllll11111_opy_(bstack1lllll111l11_opy_, {})
                if response and response.get(bstack1l1l11_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣₚ")):
                    bstack1llll1llllll_opy_ = response.get(bstack1l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤₛ"))
                self.bstack1llll1lllll1_opy_ += 1
                if bstack1llll1llllll_opy_:
                    break
                time.sleep(bstack1llll1ll1lll_opy_)
                self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡌࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡰࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡧࡴࡲࡱࠥࡸࡥࡴࡷ࡯ࡸ࡛ࠥࡒࡍࠢࡤࡪࡹ࡫ࡲࠡࡹࡤ࡭ࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡻࡾࠢࡶࡩࡨࡵ࡮ࡥࡵ࠱ࠦₜ").format(bstack1llll1ll1lll_opy_))
            if bstack1llll1lll1l1_opy_ and not bstack1llll1llllll_opy_:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡆࡦࡶࡦ࡬࡮ࡴࡧࠡࡱࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࡳࠡࡨࡵࡳࡲࠦࡴࡪ࡯ࡨࡳࡺࡺࠠࡖࡔࡏࠦ₝"))
                response = bstack11ll111l1ll_opy_.bstack1llllll11111_opy_(bstack1llll1lll1l1_opy_, {})
                if response and response.get(bstack1l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧ₞")):
                    bstack1llll1llllll_opy_ = response.get(bstack1l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨ₟"))
            if bstack1llll1llllll_opy_ and len(bstack1llll1llllll_opy_) > 0:
                for bstack111ll1llll_opy_ in bstack1llll1llllll_opy_:
                    file_path = bstack111ll1llll_opy_.get(bstack1l1l11_opy_ (u"ࠣࡨ࡬ࡰࡪࡖࡡࡵࡪࠥ₠"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack1llll1llllll_opy_:
                return None
            self.logger.debug(bstack1l1l11_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡓࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡴࡨࡧࡪ࡯ࡶࡦࡦ࠽ࠤࢀࢃࠢ₡").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀࢃࠢ₢").format(e))
            return None
    def bstack111l11l11l1_opy_(self):
        bstack1l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡣࡰࡷࡱࡸࠥࡵࡦࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡧࡦࡲ࡬ࡴࠢࡰࡥࡩ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ₣")
        return self.bstack1llll1lllll1_opy_