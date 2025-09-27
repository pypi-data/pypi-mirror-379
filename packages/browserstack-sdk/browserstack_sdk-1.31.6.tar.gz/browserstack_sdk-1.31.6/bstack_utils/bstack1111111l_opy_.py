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
from bstack_utils.constants import bstack11ll11l1111_opy_
def bstack11lllll1ll_opy_(bstack11ll11l111l_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack1l1lll11ll_opy_
    host = bstack1l1lll11ll_opy_(cli.config, [bstack1l1l11_opy_ (u"ࠦࡦࡶࡩࡴࠤᝳ"), bstack1l1l11_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢ᝴"), bstack1l1l11_opy_ (u"ࠨࡡࡱ࡫ࠥ᝵")], bstack11ll11l1111_opy_)
    return bstack1l1l11_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭᝶").format(host, bstack11ll11l111l_opy_)