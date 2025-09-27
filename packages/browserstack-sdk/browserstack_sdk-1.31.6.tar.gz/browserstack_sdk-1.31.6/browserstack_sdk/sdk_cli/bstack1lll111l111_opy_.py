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
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1111111ll1_opy_ import bstack11111111ll_opy_
class bstack1llll11lll1_opy_(abc.ABC):
    bin_session_id: str
    bstack1111111ll1_opy_: bstack11111111ll_opy_
    def __init__(self):
        self.bstack1lll11111l1_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1111111ll1_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1llll1l111l_opy_(self):
        return (self.bstack1lll11111l1_opy_ != None and self.bin_session_id != None and self.bstack1111111ll1_opy_ != None)
    def configure(self, bstack1lll11111l1_opy_, config, bin_session_id: str, bstack1111111ll1_opy_: bstack11111111ll_opy_):
        self.bstack1lll11111l1_opy_ = bstack1lll11111l1_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1111111ll1_opy_ = bstack1111111ll1_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡦࡦࠣࡱࡴࡪࡵ࡭ࡧࠣࡿࡸ࡫࡬ࡧ࠰ࡢࡣࡨࡲࡡࡴࡵࡢࡣ࠳ࡥ࡟࡯ࡣࡰࡩࡤࡥࡽ࠻ࠢࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࡀࠦቒ") + str(self.bin_session_id) + bstack1l1l11_opy_ (u"ࠣࠤቓ"))
    def bstack1ll1111ll11_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1l1l11_opy_ (u"ࠤࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠣࡧࡦࡴ࡮ࡰࡶࠣࡦࡪࠦࡎࡰࡰࡨࠦቔ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False