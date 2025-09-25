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
from bstack_utils.constants import bstack11ll11l1111_opy_
def bstack1111lll11_opy_(bstack11ll11l111l_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack1l1l1llll_opy_
    host = bstack1l1l1llll_opy_(cli.config, [bstack1l11l11_opy_ (u"ࠦࡦࡶࡩࡴࠤᝳ"), bstack1l11l11_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢ᝴"), bstack1l11l11_opy_ (u"ࠨࡡࡱ࡫ࠥ᝵")], bstack11ll11l1111_opy_)
    return bstack1l11l11_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭᝶").format(host, bstack11ll11l111l_opy_)