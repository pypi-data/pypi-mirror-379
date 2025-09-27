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
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll111l11l_opy_ import bstack11ll111l1ll_opy_
from bstack_utils.constants import *
import json
class bstack1l1111lll_opy_:
    def __init__(self, bstack11111l11_opy_, bstack11ll111l111_opy_):
        self.bstack11111l11_opy_ = bstack11111l11_opy_
        self.bstack11ll111l111_opy_ = bstack11ll111l111_opy_
        self.bstack11ll111lll1_opy_ = None
    def __call__(self):
        bstack11ll111l1l1_opy_ = {}
        while True:
            self.bstack11ll111lll1_opy_ = bstack11ll111l1l1_opy_.get(
                bstack1l1l11_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩ᝷"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll1111lll_opy_ = self.bstack11ll111lll1_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll1111lll_opy_ > 0:
                sleep(bstack11ll1111lll_opy_ / 1000)
            params = {
                bstack1l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᝸"): self.bstack11111l11_opy_,
                bstack1l1l11_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭᝹"): int(datetime.now().timestamp() * 1000)
            }
            bstack11ll111ll1l_opy_ = bstack1l1l11_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨ᝺") + bstack11ll111llll_opy_ + bstack1l1l11_opy_ (u"ࠧ࠵ࡡࡶࡶࡲࡱࡦࡺࡥ࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࠤ᝻")
            if self.bstack11ll111l111_opy_.lower() == bstack1l1l11_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹࡹࠢ᝼"):
                bstack11ll111l1l1_opy_ = bstack11ll111l1ll_opy_.results(bstack11ll111ll1l_opy_, params)
            else:
                bstack11ll111l1l1_opy_ = bstack11ll111l1ll_opy_.bstack11ll111ll11_opy_(bstack11ll111ll1l_opy_, params)
            if str(bstack11ll111l1l1_opy_.get(bstack1l1l11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ᝽"), bstack1l1l11_opy_ (u"ࠨ࠴࠳࠴ࠬ᝾"))) != bstack1l1l11_opy_ (u"ࠩ࠷࠴࠹࠭᝿"):
                break
        return bstack11ll111l1l1_opy_.get(bstack1l1l11_opy_ (u"ࠪࡨࡦࡺࡡࠨក"), bstack11ll111l1l1_opy_)