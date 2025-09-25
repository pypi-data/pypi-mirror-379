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
import threading
import logging
import bstack_utils.accessibility as bstack1lll1l1ll1_opy_
from bstack_utils.helper import bstack1lll1lll11_opy_
logger = logging.getLogger(__name__)
def bstack1lllll1l11_opy_(bstack11111ll1_opy_):
  return True if bstack11111ll1_opy_ in threading.current_thread().__dict__.keys() else False
def bstack111ll111_opy_(context, *args):
    tags = getattr(args[0], bstack1l11l11_opy_ (u"ࠫࡹࡧࡧࡴࠩខ"), [])
    bstack1ll111lll1_opy_ = bstack1lll1l1ll1_opy_.bstack1l11ll111l_opy_(tags)
    threading.current_thread().isA11yTest = bstack1ll111lll1_opy_
    try:
      bstack111llllll_opy_ = threading.current_thread().bstackSessionDriver if bstack1lllll1l11_opy_(bstack1l11l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫគ")) else context.browser
      if bstack111llllll_opy_ and bstack111llllll_opy_.session_id and bstack1ll111lll1_opy_ and bstack1lll1lll11_opy_(
              threading.current_thread(), bstack1l11l11_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬឃ"), None):
          threading.current_thread().isA11yTest = bstack1lll1l1ll1_opy_.bstack1l1lll11l_opy_(bstack111llllll_opy_, bstack1ll111lll1_opy_)
    except Exception as e:
       logger.debug(bstack1l11l11_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡤ࠵࠶ࡿࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧ࠽ࠤࢀࢃࠧង").format(str(e)))
def bstack11l111l1ll_opy_(bstack111llllll_opy_):
    if bstack1lll1lll11_opy_(threading.current_thread(), bstack1l11l11_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬច"), None) and bstack1lll1lll11_opy_(
      threading.current_thread(), bstack1l11l11_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨឆ"), None) and not bstack1lll1lll11_opy_(threading.current_thread(), bstack1l11l11_opy_ (u"ࠪࡥ࠶࠷ࡹࡠࡵࡷࡳࡵ࠭ជ"), False):
      threading.current_thread().a11y_stop = True
      bstack1lll1l1ll1_opy_.bstack11llll11l1_opy_(bstack111llllll_opy_, name=bstack1l11l11_opy_ (u"ࠦࠧឈ"), path=bstack1l11l11_opy_ (u"ࠧࠨញ"))