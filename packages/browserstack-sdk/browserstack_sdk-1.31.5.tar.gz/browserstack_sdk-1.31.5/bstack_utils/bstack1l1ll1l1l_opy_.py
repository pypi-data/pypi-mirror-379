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
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack11ll1ll1l1l_opy_, bstack1ll11l11ll_opy_, get_host_info, bstack111lll1l111_opy_, \
 bstack11l1l1ll1l_opy_, bstack1lll1lll11_opy_, error_handler, bstack11l11111ll1_opy_, bstack111l11l11_opy_
import bstack_utils.accessibility as bstack1lll1l1ll1_opy_
from bstack_utils.bstack1l1l1l111_opy_ import bstack1l111lll_opy_
from bstack_utils.bstack111l1lllll_opy_ import bstack1ll1l1l111_opy_
from bstack_utils.percy import bstack11111l111_opy_
from bstack_utils.config import Config
bstack11ll1111ll_opy_ = Config.bstack1lllll1ll1_opy_()
logger = logging.getLogger(__name__)
percy = bstack11111l111_opy_()
@error_handler(class_method=False)
def bstack1llll1ll1l1l_opy_(bs_config, bstack1lll111l11_opy_):
  try:
    data = {
        bstack1l11l11_opy_ (u"࠭ࡦࡰࡴࡰࡥࡹ࠭↡"): bstack1l11l11_opy_ (u"ࠧ࡫ࡵࡲࡲࠬ↢"),
        bstack1l11l11_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡡࡱࡥࡲ࡫ࠧ↣"): bs_config.get(bstack1l11l11_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ↤"), bstack1l11l11_opy_ (u"ࠪࠫ↥")),
        bstack1l11l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ↦"): bs_config.get(bstack1l11l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ↧"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1l11l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ↨"): bs_config.get(bstack1l11l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ↩")),
        bstack1l11l11_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭↪"): bs_config.get(bstack1l11l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ↫"), bstack1l11l11_opy_ (u"ࠪࠫ↬")),
        bstack1l11l11_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ↭"): bstack111l11l11_opy_(),
        bstack1l11l11_opy_ (u"ࠬࡺࡡࡨࡵࠪ↮"): bstack111lll1l111_opy_(bs_config),
        bstack1l11l11_opy_ (u"࠭ࡨࡰࡵࡷࡣ࡮ࡴࡦࡰࠩ↯"): get_host_info(),
        bstack1l11l11_opy_ (u"ࠧࡤ࡫ࡢ࡭ࡳ࡬࡯ࠨ↰"): bstack1ll11l11ll_opy_(),
        bstack1l11l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡳࡷࡱࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ↱"): os.environ.get(bstack1l11l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨ↲")),
        bstack1l11l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡵࡩࡷࡻ࡮ࠨ↳"): os.environ.get(bstack1l11l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩ↴"), False),
        bstack1l11l11_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡥࡣࡰࡰࡷࡶࡴࡲࠧ↵"): bstack11ll1ll1l1l_opy_(),
        bstack1l11l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭↶"): bstack1llll111llll_opy_(bs_config),
        bstack1l11l11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡨࡪࡺࡡࡪ࡮ࡶࠫ↷"): bstack1llll11l1111_opy_(bstack1lll111l11_opy_),
        bstack1l11l11_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭↸"): bstack1llll11l11l1_opy_(bs_config, bstack1lll111l11_opy_.get(bstack1l11l11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪ↹"), bstack1l11l11_opy_ (u"ࠪࠫ↺"))),
        bstack1l11l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭↻"): bstack11l1l1ll1l_opy_(bs_config),
        bstack1l11l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠪ↼"): bstack1llll11ll111_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack1l11l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡴࡦࡿ࡬ࡰࡣࡧࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࠤࢀࢃࠢ↽").format(str(error)))
    return None
def bstack1llll11l1111_opy_(framework):
  return {
    bstack1l11l11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡑࡥࡲ࡫ࠧ↾"): framework.get(bstack1l11l11_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩ↿"), bstack1l11l11_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩ⇀")),
    bstack1l11l11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⇁"): framework.get(bstack1l11l11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ⇂")),
    bstack1l11l11_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ⇃"): framework.get(bstack1l11l11_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫ⇄")),
    bstack1l11l11_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩ⇅"): bstack1l11l11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ⇆"),
    bstack1l11l11_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ⇇"): framework.get(bstack1l11l11_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ⇈"))
  }
def bstack1llll11ll111_opy_(bs_config):
  bstack1l11l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡳࡵࡣࡵࡸ࠳ࠐࠠࠡࠤࠥࠦ⇉")
  if not bs_config:
    return {}
  bstack111l1111lll_opy_ = bstack1l111lll_opy_(bs_config).bstack1111lllll1l_opy_(bs_config)
  return bstack111l1111lll_opy_
def bstack11111ll11_opy_(bs_config, framework):
  bstack11l1l1l11l_opy_ = False
  bstack11lll11l1_opy_ = False
  bstack1llll11l1l11_opy_ = False
  if bstack1l11l11_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ⇊") in bs_config:
    bstack1llll11l1l11_opy_ = True
  elif bstack1l11l11_opy_ (u"࠭ࡡࡱࡲࠪ⇋") in bs_config:
    bstack11l1l1l11l_opy_ = True
  else:
    bstack11lll11l1_opy_ = True
  bstack1l1l1ll1ll_opy_ = {
    bstack1l11l11_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ⇌"): bstack1ll1l1l111_opy_.bstack1llll11ll1ll_opy_(bs_config, framework),
    bstack1l11l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⇍"): bstack1lll1l1ll1_opy_.bstack1lllll11l_opy_(bs_config),
    bstack1l11l11_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ⇎"): bs_config.get(bstack1l11l11_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ⇏"), False),
    bstack1l11l11_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭⇐"): bstack11lll11l1_opy_,
    bstack1l11l11_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ⇑"): bstack11l1l1l11l_opy_,
    bstack1l11l11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪ⇒"): bstack1llll11l1l11_opy_
  }
  return bstack1l1l1ll1ll_opy_
@error_handler(class_method=False)
def bstack1llll111llll_opy_(bs_config):
  try:
    bstack1llll11l1lll_opy_ = json.loads(os.getenv(bstack1l11l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ⇓"), bstack1l11l11_opy_ (u"ࠨࡽࢀࠫ⇔")))
    bstack1llll11l1lll_opy_ = bstack1llll11l1ll1_opy_(bs_config, bstack1llll11l1lll_opy_)
    return {
        bstack1l11l11_opy_ (u"ࠩࡶࡩࡹࡺࡩ࡯ࡩࡶࠫ⇕"): bstack1llll11l1lll_opy_
    }
  except Exception as error:
    logger.error(bstack1l11l11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࠦࡻࡾࠤ⇖").format(str(error)))
    return {}
def bstack1llll11l1ll1_opy_(bs_config, bstack1llll11l1lll_opy_):
  if ((bstack1l11l11_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ⇗") in bs_config or not bstack11l1l1ll1l_opy_(bs_config)) and bstack1lll1l1ll1_opy_.bstack1lllll11l_opy_(bs_config)):
    bstack1llll11l1lll_opy_[bstack1l11l11_opy_ (u"ࠧ࡯࡮ࡤ࡮ࡸࡨࡪࡋ࡮ࡤࡱࡧࡩࡩࡋࡸࡵࡧࡱࡷ࡮ࡵ࡮ࠣ⇘")] = True
  return bstack1llll11l1lll_opy_
def bstack1llll1ll1111_opy_(array, bstack1llll11ll11l_opy_, bstack1llll11l1l1l_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll11ll11l_opy_]
    result[key] = o[bstack1llll11l1l1l_opy_]
  return result
def bstack1llll1l1ll1l_opy_(bstack11lllll1_opy_=bstack1l11l11_opy_ (u"࠭ࠧ⇙")):
  bstack1llll11l11ll_opy_ = bstack1lll1l1ll1_opy_.on()
  bstack1llll11l111l_opy_ = bstack1ll1l1l111_opy_.on()
  bstack1llll11ll1l1_opy_ = percy.bstack1l1llll1l1_opy_()
  if bstack1llll11ll1l1_opy_ and not bstack1llll11l111l_opy_ and not bstack1llll11l11ll_opy_:
    return bstack11lllll1_opy_ not in [bstack1l11l11_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫ⇚"), bstack1l11l11_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ⇛")]
  elif bstack1llll11l11ll_opy_ and not bstack1llll11l111l_opy_:
    return bstack11lllll1_opy_ not in [bstack1l11l11_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ⇜"), bstack1l11l11_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ⇝"), bstack1l11l11_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ⇞")]
  return bstack1llll11l11ll_opy_ or bstack1llll11l111l_opy_ or bstack1llll11ll1l1_opy_
@error_handler(class_method=False)
def bstack1llll1l111l1_opy_(bstack11lllll1_opy_, test=None):
  bstack1llll111lll1_opy_ = bstack1lll1l1ll1_opy_.on()
  if not bstack1llll111lll1_opy_ or bstack11lllll1_opy_ not in [bstack1l11l11_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⇟")] or test == None:
    return None
  return {
    bstack1l11l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⇠"): bstack1llll111lll1_opy_ and bstack1lll1lll11_opy_(threading.current_thread(), bstack1l11l11_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭⇡"), None) == True and bstack1lll1l1ll1_opy_.bstack1l11ll111l_opy_(test[bstack1l11l11_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭⇢")])
  }
def bstack1llll11l11l1_opy_(bs_config, framework):
  bstack11l1l1l11l_opy_ = False
  bstack11lll11l1_opy_ = False
  bstack1llll11l1l11_opy_ = False
  if bstack1l11l11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⇣") in bs_config:
    bstack1llll11l1l11_opy_ = True
  elif bstack1l11l11_opy_ (u"ࠪࡥࡵࡶࠧ⇤") in bs_config:
    bstack11l1l1l11l_opy_ = True
  else:
    bstack11lll11l1_opy_ = True
  bstack1l1l1ll1ll_opy_ = {
    bstack1l11l11_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⇥"): bstack1ll1l1l111_opy_.bstack1llll11ll1ll_opy_(bs_config, framework),
    bstack1l11l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⇦"): bstack1lll1l1ll1_opy_.bstack111111ll1_opy_(bs_config),
    bstack1l11l11_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ⇧"): bs_config.get(bstack1l11l11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭⇨"), False),
    bstack1l11l11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪ⇩"): bstack11lll11l1_opy_,
    bstack1l11l11_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ⇪"): bstack11l1l1l11l_opy_,
    bstack1l11l11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧ⇫"): bstack1llll11l1l11_opy_
  }
  return bstack1l1l1ll1ll_opy_