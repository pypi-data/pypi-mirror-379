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
import logging
import abc
from browserstack_sdk.sdk_cli.bstack111111111l_opy_ import bstack11111111l1_opy_
class bstack1lll1l11l1l_opy_(abc.ABC):
    bin_session_id: str
    bstack111111111l_opy_: bstack11111111l1_opy_
    def __init__(self):
        self.bstack1ll1ll1ll1l_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack111111111l_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1ll1l1lllll_opy_(self):
        return (self.bstack1ll1ll1ll1l_opy_ != None and self.bin_session_id != None and self.bstack111111111l_opy_ != None)
    def configure(self, bstack1ll1ll1ll1l_opy_, config, bin_session_id: str, bstack111111111l_opy_: bstack11111111l1_opy_):
        self.bstack1ll1ll1ll1l_opy_ = bstack1ll1ll1ll1l_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack111111111l_opy_ = bstack111111111l_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1l11l11_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡦࡦࠣࡱࡴࡪࡵ࡭ࡧࠣࡿࡸ࡫࡬ࡧ࠰ࡢࡣࡨࡲࡡࡴࡵࡢࡣ࠳ࡥ࡟࡯ࡣࡰࡩࡤࡥࡽ࠻ࠢࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࡀࠦቒ") + str(self.bin_session_id) + bstack1l11l11_opy_ (u"ࠣࠤቓ"))
    def bstack1ll111l1111_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1l11l11_opy_ (u"ࠤࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠣࡧࡦࡴ࡮ࡰࡶࠣࡦࡪࠦࡎࡰࡰࡨࠦቔ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False