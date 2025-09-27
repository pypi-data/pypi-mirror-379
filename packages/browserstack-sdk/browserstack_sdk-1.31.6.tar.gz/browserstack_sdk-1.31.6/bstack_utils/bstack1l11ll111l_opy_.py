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
import threading
import logging
import bstack_utils.accessibility as bstack1ll11l111l_opy_
from bstack_utils.helper import bstack1l11111lll_opy_
logger = logging.getLogger(__name__)
def bstack11l11111l1_opy_(bstack11ll11ll1l_opy_):
  return True if bstack11ll11ll1l_opy_ in threading.current_thread().__dict__.keys() else False
def bstack11l111l1l_opy_(context, *args):
    tags = getattr(args[0], bstack1l1l11_opy_ (u"ࠫࡹࡧࡧࡴࠩខ"), [])
    bstack1l111llll1_opy_ = bstack1ll11l111l_opy_.bstack1l1lll111l_opy_(tags)
    threading.current_thread().isA11yTest = bstack1l111llll1_opy_
    try:
      bstack1l1l111l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack11l11111l1_opy_(bstack1l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫគ")) else context.browser
      if bstack1l1l111l1l_opy_ and bstack1l1l111l1l_opy_.session_id and bstack1l111llll1_opy_ and bstack1l11111lll_opy_(
              threading.current_thread(), bstack1l1l11_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬឃ"), None):
          threading.current_thread().isA11yTest = bstack1ll11l111l_opy_.bstack1l1l1l1l_opy_(bstack1l1l111l1l_opy_, bstack1l111llll1_opy_)
    except Exception as e:
       logger.debug(bstack1l1l11_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡤ࠵࠶ࡿࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧ࠽ࠤࢀࢃࠧង").format(str(e)))
def bstack1l1ll111l1_opy_(bstack1l1l111l1l_opy_):
    if bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬច"), None) and bstack1l11111lll_opy_(
      threading.current_thread(), bstack1l1l11_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨឆ"), None) and not bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠪࡥ࠶࠷ࡹࡠࡵࡷࡳࡵ࠭ជ"), False):
      threading.current_thread().a11y_stop = True
      bstack1ll11l111l_opy_.bstack1111ll1l1_opy_(bstack1l1l111l1l_opy_, name=bstack1l1l11_opy_ (u"ࠦࠧឈ"), path=bstack1l1l11_opy_ (u"ࠧࠨញ"))