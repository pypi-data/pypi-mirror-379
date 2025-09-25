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
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack111l11l1l11_opy_ import bstack111l11l1lll_opy_
from bstack_utils.bstack1l1l1l111_opy_ import bstack1l111lll_opy_
from bstack_utils.helper import bstack11l111lll_opy_
class bstack11lll11l11_opy_:
    _1ll1ll1l11l_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack111l11ll1ll_opy_ = bstack111l11l1lll_opy_(self.config, logger)
        self.bstack1l1l1l111_opy_ = bstack1l111lll_opy_.bstack1lllll1ll1_opy_(config=self.config)
        self.bstack111l11lll1l_opy_ = {}
        self.bstack11111l1l1l_opy_ = False
        self.bstack111l11ll11l_opy_ = (
            self.__111l11ll111_opy_()
            and self.bstack1l1l1l111_opy_ is not None
            and self.bstack1l1l1l111_opy_.bstack111111ll_opy_()
            and config.get(bstack1l11l11_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧḹ"), None) is not None
            and config.get(bstack1l11l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭Ḻ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1lllll1ll1_opy_(cls, config, logger):
        if cls._1ll1ll1l11l_opy_ is None and config is not None:
            cls._1ll1ll1l11l_opy_ = bstack11lll11l11_opy_(config, logger)
        return cls._1ll1ll1l11l_opy_
    def bstack111111ll_opy_(self):
        bstack1l11l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡆࡲࠤࡳࡵࡴࠡࡣࡳࡴࡱࡿࠠࡵࡧࡶࡸࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡸࡪࡨࡲ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡔ࠷࠱ࡺࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡑࡵࡨࡪࡸࡩ࡯ࡩࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠠࡪࡵࠣࡒࡴࡴࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠢ࡬ࡷࠥࡔ࡯࡯ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢḻ")
        return self.bstack111l11ll11l_opy_ and self.bstack111l11lll11_opy_()
    def bstack111l11lll11_opy_(self):
        return self.config.get(bstack1l11l11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨḼ"), None) in bstack11l1ll1ll1l_opy_
    def __111l11ll111_opy_(self):
        bstack11l1llllll1_opy_ = False
        for fw in bstack11l1lll1ll1_opy_:
            if fw in self.config.get(bstack1l11l11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩḽ"), bstack1l11l11_opy_ (u"ࠧࠨḾ")):
                bstack11l1llllll1_opy_ = True
        return bstack11l111lll_opy_(self.config.get(bstack1l11l11_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬḿ"), bstack11l1llllll1_opy_))
    def bstack111l111lll1_opy_(self):
        return (not self.bstack111111ll_opy_() and
                self.bstack1l1l1l111_opy_ is not None and self.bstack1l1l1l111_opy_.bstack111111ll_opy_())
    def bstack111l111llll_opy_(self):
        if not self.bstack111l111lll1_opy_():
            return
        if self.config.get(bstack1l11l11_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧṀ"), None) is None or self.config.get(bstack1l11l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ṁ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack1l11l11_opy_ (u"࡙ࠦ࡫ࡳࡵࠢࡕࡩࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡣࡢࡰࠪࡸࠥࡽ࡯ࡳ࡭ࠣࡥࡸࠦࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠢࡲࡶࠥࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠣ࡭ࡸࠦ࡮ࡶ࡮࡯࠲ࠥࡖ࡬ࡦࡣࡶࡩࠥࡹࡥࡵࠢࡤࠤࡳࡵ࡮࠮ࡰࡸࡰࡱࠦࡶࡢ࡮ࡸࡩ࠳ࠨṂ"))
        if not self.__111l11ll111_opy_():
            self.logger.info(bstack1l11l11_opy_ (u"࡚ࠧࡥࡴࡶࠣࡖࡪࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡤࡣࡱࠫࡹࠦࡷࡰࡴ࡮ࠤࡦࡹࠠࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡨ࡮ࡹࡡࡣ࡮ࡨࡨ࠳ࠦࡐ࡭ࡧࡤࡷࡪࠦࡥ࡯ࡣࡥࡰࡪࠦࡩࡵࠢࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠣࡪ࡮ࡲࡥ࠯ࠤṃ"))
    def bstack111l11l1l1l_opy_(self):
        return self.bstack11111l1l1l_opy_
    def bstack111111llll_opy_(self, bstack111l11l11ll_opy_):
        self.bstack11111l1l1l_opy_ = bstack111l11l11ll_opy_
        self.bstack1111l1111l_opy_(bstack1l11l11_opy_ (u"ࠨࡡࡱࡲ࡯࡭ࡪࡪࠢṄ"), bstack111l11l11ll_opy_)
    def bstack11111lllll_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack1l11l11_opy_ (u"ࠢ࡜ࡴࡨࡳࡷࡪࡥࡳࡡࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࡣࠠࡏࡱࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡱࡴࡲࡺ࡮ࡪࡥࡥࠢࡩࡳࡷࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧ࠯ࠤṅ"))
                return None
            orchestration_strategy = None
            bstack111l11l1ll1_opy_ = self.bstack1l1l1l111_opy_.bstack111l11l11l1_opy_()
            if self.bstack1l1l1l111_opy_ is not None:
                orchestration_strategy = self.bstack1l1l1l111_opy_.bstack1l11ll1ll1_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack1l11l11_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡷࡶࡦࡺࡥࡨࡻࠣ࡭ࡸࠦࡎࡰࡰࡨ࠲ࠥࡉࡡ࡯ࡰࡲࡸࠥࡶࡲࡰࡥࡨࡩࡩࠦࡷࡪࡶ࡫ࠤࡹ࡫ࡳࡵࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠱ࠦṆ"))
                return None
            self.logger.info(bstack1l11l11_opy_ (u"ࠤࡕࡩࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡻ࡮ࡺࡨࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡷࡶࡦࡺࡥࡨࡻ࠽ࠤࢀࢃࠢṇ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack1l11l11_opy_ (u"࡙ࠥࡸ࡯࡮ࡨࠢࡆࡐࡎࠦࡦ࡭ࡱࡺࠤ࡫ࡵࡲࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨṈ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy)
            else:
                self.logger.debug(bstack1l11l11_opy_ (u"࡚ࠦࡹࡩ࡯ࡩࠣࡷࡩࡱࠠࡧ࡮ࡲࡻࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠴ࠢṉ"))
                self.bstack111l11ll1ll_opy_.bstack111l11ll1l1_opy_(test_files, orchestration_strategy, bstack111l11l1ll1_opy_)
                ordered_test_files = self.bstack111l11ll1ll_opy_.bstack111l11l111l_opy_()
            if not ordered_test_files:
                return None
            self.bstack1111l1111l_opy_(bstack1l11l11_opy_ (u"ࠧࡻࡰ࡭ࡱࡤࡨࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴࡅࡲࡹࡳࡺࠢṊ"), len(test_files))
            self.bstack1111l1111l_opy_(bstack1l11l11_opy_ (u"ࠨ࡮ࡰࡦࡨࡍࡳࡪࡥࡹࠤṋ"), int(os.environ.get(bstack1l11l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥṌ")) or bstack1l11l11_opy_ (u"ࠣ࠲ࠥṍ")))
            self.bstack1111l1111l_opy_(bstack1l11l11_opy_ (u"ࠤࡷࡳࡹࡧ࡬ࡏࡱࡧࡩࡸࠨṎ"), int(os.environ.get(bstack1l11l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡄࡑࡘࡒ࡙ࠨṏ")) or bstack1l11l11_opy_ (u"ࠦ࠶ࠨṐ")))
            self.bstack1111l1111l_opy_(bstack1l11l11_opy_ (u"ࠧࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡇࡴࡻ࡮ࡵࠤṑ"), len(ordered_test_files))
            self.bstack1111l1111l_opy_(bstack1l11l11_opy_ (u"ࠨࡳࡱ࡮࡬ࡸ࡙࡫ࡳࡵࡵࡄࡔࡎࡉࡡ࡭࡮ࡆࡳࡺࡴࡴࠣṒ"), self.bstack111l11ll1ll_opy_.bstack111l11l1111_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠢ࡜ࡴࡨࡳࡷࡪࡥࡳࡡࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࡣࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡦࡰࡦࡹࡳࡦࡵ࠽ࠤࢀࢃࠢṓ").format(e))
        return None
    def bstack1111l1111l_opy_(self, key, value):
        self.bstack111l11lll1l_opy_[key] = value
    def bstack1l11lll1ll_opy_(self):
        return self.bstack111l11lll1l_opy_