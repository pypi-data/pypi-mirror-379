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
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack11ll11l1lll_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11ll11lllll_opy_ as bstack11ll1ll1111_opy_, EVENTS
from bstack_utils.bstack11l1111ll1_opy_ import bstack11l1111ll1_opy_
from bstack_utils.helper import bstack11llll11_opy_, bstack1111ll1lll_opy_, bstack1l11111ll1_opy_, bstack11ll1l11l1l_opy_, \
  bstack11ll11ll111_opy_, bstack1l1111l11l_opy_, get_host_info, bstack11ll1l11111_opy_, bstack1lll1ll1l_opy_, error_handler, bstack11ll1ll111l_opy_, bstack11ll1lll1l1_opy_, bstack1l11111lll_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack11lll1llll_opy_ import get_logger
from bstack_utils.bstack111l11ll_opy_ import bstack1lll111lll1_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack111l11ll_opy_ = bstack1lll111lll1_opy_()
@error_handler(class_method=False)
def _11ll1llll1l_opy_(driver, bstack11111l111l_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1l1l11_opy_ (u"ࠨࡱࡶࡣࡳࡧ࡭ࡦࠩᘠ"): caps.get(bstack1l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨᘡ"), None),
        bstack1l1l11_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᘢ"): bstack11111l111l_opy_.get(bstack1l1l11_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧᘣ"), None),
        bstack1l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫᘤ"): caps.get(bstack1l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᘥ"), None),
        bstack1l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᘦ"): caps.get(bstack1l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᘧ"), None)
    }
  except Exception as error:
    logger.debug(bstack1l1l11_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡥࡵࡣ࡬ࡰࡸࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭ᘨ") + str(error))
  return response
def on():
    if os.environ.get(bstack1l1l11_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᘩ"), None) is None or os.environ[bstack1l1l11_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᘪ")] == bstack1l1l11_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᘫ"):
        return False
    return True
def bstack11llll1ll1_opy_(config):
  return config.get(bstack1l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᘬ"), False) or any([p.get(bstack1l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᘭ"), False) == True for p in config.get(bstack1l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᘮ"), [])])
def bstack1ll1l1ll11_opy_(config, bstack1lll11lll_opy_):
  try:
    bstack11ll1l11lll_opy_ = config.get(bstack1l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᘯ"), False)
    if int(bstack1lll11lll_opy_) < len(config.get(bstack1l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᘰ"), [])) and config[bstack1l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᘱ")][bstack1lll11lll_opy_]:
      bstack11ll11ll1ll_opy_ = config[bstack1l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᘲ")][bstack1lll11lll_opy_].get(bstack1l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᘳ"), None)
    else:
      bstack11ll11ll1ll_opy_ = config.get(bstack1l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᘴ"), None)
    if bstack11ll11ll1ll_opy_ != None:
      bstack11ll1l11lll_opy_ = bstack11ll11ll1ll_opy_
    bstack11ll11lll11_opy_ = os.getenv(bstack1l1l11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᘵ")) is not None and len(os.getenv(bstack1l1l11_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᘶ"))) > 0 and os.getenv(bstack1l1l11_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᘷ")) != bstack1l1l11_opy_ (u"ࠫࡳࡻ࡬࡭ࠩᘸ")
    return bstack11ll1l11lll_opy_ and bstack11ll11lll11_opy_
  except Exception as error:
    logger.debug(bstack1l1l11_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡻ࡫ࡲࡪࡨࡼ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬᘹ") + str(error))
  return False
def bstack1l1lll111l_opy_(test_tags):
  bstack1ll11l111l1_opy_ = os.getenv(bstack1l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧᘺ"))
  if bstack1ll11l111l1_opy_ is None:
    return True
  bstack1ll11l111l1_opy_ = json.loads(bstack1ll11l111l1_opy_)
  try:
    include_tags = bstack1ll11l111l1_opy_[bstack1l1l11_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᘻ")] if bstack1l1l11_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᘼ") in bstack1ll11l111l1_opy_ and isinstance(bstack1ll11l111l1_opy_[bstack1l1l11_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᘽ")], list) else []
    exclude_tags = bstack1ll11l111l1_opy_[bstack1l1l11_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᘾ")] if bstack1l1l11_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᘿ") in bstack1ll11l111l1_opy_ and isinstance(bstack1ll11l111l1_opy_[bstack1l1l11_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᙀ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1l1l11_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡻࡧ࡬ࡪࡦࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡥࡳࡴࡩ࡯ࡩ࠱ࠤࡊࡸࡲࡰࡴࠣ࠾ࠥࠨᙁ") + str(error))
  return False
def bstack11ll1l111ll_opy_(config, bstack11ll11ll1l1_opy_, bstack11ll1l1l11l_opy_, bstack11lll11111l_opy_):
  bstack11ll1ll1ll1_opy_ = bstack11ll1l11l1l_opy_(config)
  bstack11ll1llll11_opy_ = bstack11ll11ll111_opy_(config)
  if bstack11ll1ll1ll1_opy_ is None or bstack11ll1llll11_opy_ is None:
    logger.error(bstack1l1l11_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡯࡯࡯ࠢࡷࡳࡰ࡫࡮ࠨᙂ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩᙃ"), bstack1l1l11_opy_ (u"ࠩࡾࢁࠬᙄ")))
    data = {
        bstack1l1l11_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᙅ"): config[bstack1l1l11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᙆ")],
        bstack1l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᙇ"): config.get(bstack1l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩᙈ"), os.path.basename(os.getcwd())),
        bstack1l1l11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡚ࡩ࡮ࡧࠪᙉ"): bstack11llll11_opy_(),
        bstack1l1l11_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ᙊ"): config.get(bstack1l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬᙋ"), bstack1l1l11_opy_ (u"ࠪࠫᙌ")),
        bstack1l1l11_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᙍ"): {
            bstack1l1l11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬᙎ"): bstack11ll11ll1l1_opy_,
            bstack1l1l11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩᙏ"): bstack11ll1l1l11l_opy_,
            bstack1l1l11_opy_ (u"ࠧࡴࡦ࡮࡚ࡪࡸࡳࡪࡱࡱࠫᙐ"): __version__,
            bstack1l1l11_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪᙑ"): bstack1l1l11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩᙒ"),
            bstack1l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᙓ"): bstack1l1l11_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ᙔ"),
            bstack1l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬᙕ"): bstack11lll11111l_opy_
        },
        bstack1l1l11_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨᙖ"): settings,
        bstack1l1l11_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࡄࡱࡱࡸࡷࡵ࡬ࠨᙗ"): bstack11ll1l11111_opy_(),
        bstack1l1l11_opy_ (u"ࠨࡥ࡬ࡍࡳ࡬࡯ࠨᙘ"): bstack1l1111l11l_opy_(),
        bstack1l1l11_opy_ (u"ࠩ࡫ࡳࡸࡺࡉ࡯ࡨࡲࠫᙙ"): get_host_info(),
        bstack1l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᙚ"): bstack1l11111ll1_opy_(config)
    }
    headers = {
        bstack1l1l11_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᙛ"): bstack1l1l11_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᙜ"),
    }
    config = {
        bstack1l1l11_opy_ (u"࠭ࡡࡶࡶ࡫ࠫᙝ"): (bstack11ll1ll1ll1_opy_, bstack11ll1llll11_opy_),
        bstack1l1l11_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᙞ"): headers
    }
    response = bstack1lll1ll1l_opy_(bstack1l1l11_opy_ (u"ࠨࡒࡒࡗ࡙࠭ᙟ"), bstack11ll1ll1111_opy_ + bstack1l1l11_opy_ (u"ࠩ࠲ࡺ࠷࠵ࡴࡦࡵࡷࡣࡷࡻ࡮ࡴࠩᙠ"), data, config)
    bstack11lll111111_opy_ = response.json()
    if bstack11lll111111_opy_[bstack1l1l11_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫᙡ")]:
      parsed = json.loads(os.getenv(bstack1l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬᙢ"), bstack1l1l11_opy_ (u"ࠬࢁࡽࠨᙣ")))
      parsed[bstack1l1l11_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᙤ")] = bstack11lll111111_opy_[bstack1l1l11_opy_ (u"ࠧࡥࡣࡷࡥࠬᙥ")][bstack1l1l11_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᙦ")]
      os.environ[bstack1l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪᙧ")] = json.dumps(parsed)
      bstack11l1111ll1_opy_.bstack1ll11l11ll_opy_(bstack11lll111111_opy_[bstack1l1l11_opy_ (u"ࠪࡨࡦࡺࡡࠨᙨ")][bstack1l1l11_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬᙩ")])
      bstack11l1111ll1_opy_.bstack11ll1ll1l1l_opy_(bstack11lll111111_opy_[bstack1l1l11_opy_ (u"ࠬࡪࡡࡵࡣࠪᙪ")][bstack1l1l11_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨᙫ")])
      bstack11l1111ll1_opy_.store()
      return bstack11lll111111_opy_[bstack1l1l11_opy_ (u"ࠧࡥࡣࡷࡥࠬᙬ")][bstack1l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳ࠭᙭")], bstack11lll111111_opy_[bstack1l1l11_opy_ (u"ࠩࡧࡥࡹࡧࠧ᙮")][bstack1l1l11_opy_ (u"ࠪ࡭ࡩ࠭ᙯ")]
    else:
      logger.error(bstack1l1l11_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠬᙰ") + bstack11lll111111_opy_[bstack1l1l11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᙱ")])
      if bstack11lll111111_opy_[bstack1l1l11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᙲ")] == bstack1l1l11_opy_ (u"ࠧࡊࡰࡹࡥࡱ࡯ࡤࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡲࡤࡷࡸ࡫ࡤ࠯ࠩᙳ"):
        for bstack11ll1ll1l11_opy_ in bstack11lll111111_opy_[bstack1l1l11_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨᙴ")]:
          logger.error(bstack11ll1ll1l11_opy_[bstack1l1l11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᙵ")])
      return None, None
  except Exception as error:
    logger.error(bstack1l1l11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡸࡵ࡯ࠢࡩࡳࡷࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠦᙶ") +  str(error))
    return None, None
def bstack11ll1l1llll_opy_():
  if os.getenv(bstack1l1l11_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᙷ")) is None:
    return {
        bstack1l1l11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᙸ"): bstack1l1l11_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᙹ"),
        bstack1l1l11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᙺ"): bstack1l1l11_opy_ (u"ࠨࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢ࡫ࡥࡩࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠧᙻ")
    }
  data = {bstack1l1l11_opy_ (u"ࠩࡨࡲࡩ࡚ࡩ࡮ࡧࠪᙼ"): bstack11llll11_opy_()}
  headers = {
      bstack1l1l11_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᙽ"): bstack1l1l11_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࠬᙾ") + os.getenv(bstack1l1l11_opy_ (u"ࠧࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠥᙿ")),
      bstack1l1l11_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ "): bstack1l1l11_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᚁ")
  }
  response = bstack1lll1ll1l_opy_(bstack1l1l11_opy_ (u"ࠨࡒࡘࡘࠬᚂ"), bstack11ll1ll1111_opy_ + bstack1l1l11_opy_ (u"ࠩ࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠵ࡳࡵࡱࡳࠫᚃ"), data, { bstack1l1l11_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫᚄ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1l1l11_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯ࠢࡰࡥࡷࡱࡥࡥࠢࡤࡷࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠡࡣࡷࠤࠧᚅ") + bstack1111ll1lll_opy_().isoformat() + bstack1l1l11_opy_ (u"ࠬࡠࠧᚆ"))
      return {bstack1l1l11_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᚇ"): bstack1l1l11_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨᚈ"), bstack1l1l11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᚉ"): bstack1l1l11_opy_ (u"ࠩࠪᚊ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1l1l11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡣࡰ࡯ࡳࡰࡪࡺࡩࡰࡰࠣࡳ࡫ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡗࡩࡸࡺࠠࡓࡷࡱ࠾ࠥࠨᚋ") + str(error))
    return {
        bstack1l1l11_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᚌ"): bstack1l1l11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᚍ"),
        bstack1l1l11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᚎ"): str(error)
    }
def bstack11ll1l1ll11_opy_(bstack11ll1lll11l_opy_):
    return re.match(bstack1l1l11_opy_ (u"ࡲࠨࡠ࡟ࡨ࠰࠮࡜࠯࡞ࡧ࠯࠮ࡅࠤࠨᚏ"), bstack11ll1lll11l_opy_.strip()) is not None
def bstack11l11llll_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack11ll1l11l11_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack11ll1l11l11_opy_ = desired_capabilities
        else:
          bstack11ll1l11l11_opy_ = {}
        bstack1ll111llll1_opy_ = (bstack11ll1l11l11_opy_.get(bstack1l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧᚐ"), bstack1l1l11_opy_ (u"ࠩࠪᚑ")).lower() or caps.get(bstack1l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩᚒ"), bstack1l1l11_opy_ (u"ࠫࠬᚓ")).lower())
        if bstack1ll111llll1_opy_ == bstack1l1l11_opy_ (u"ࠬ࡯࡯ࡴࠩᚔ"):
            return True
        if bstack1ll111llll1_opy_ == bstack1l1l11_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࠧᚕ"):
            bstack1ll11ll1ll1_opy_ = str(float(caps.get(bstack1l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩᚖ")) or bstack11ll1l11l11_opy_.get(bstack1l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᚗ"), {}).get(bstack1l1l11_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬᚘ"),bstack1l1l11_opy_ (u"ࠪࠫᚙ"))))
            if bstack1ll111llll1_opy_ == bstack1l1l11_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࠬᚚ") and int(bstack1ll11ll1ll1_opy_.split(bstack1l1l11_opy_ (u"ࠬ࠴ࠧ᚛"))[0]) < float(bstack11ll1l1l111_opy_):
                logger.warning(str(bstack11ll1l1ll1l_opy_))
                return False
            return True
        bstack1ll1l1111ll_opy_ = caps.get(bstack1l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᚜"), {}).get(bstack1l1l11_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ᚝"), caps.get(bstack1l1l11_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ᚞"), bstack1l1l11_opy_ (u"ࠩࠪ᚟")))
        if bstack1ll1l1111ll_opy_:
            logger.warning(bstack1l1l11_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡈࡪࡹ࡫ࡵࡱࡳࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢᚠ"))
            return False
        browser = caps.get(bstack1l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᚡ"), bstack1l1l11_opy_ (u"ࠬ࠭ᚢ")).lower() or bstack11ll1l11l11_opy_.get(bstack1l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᚣ"), bstack1l1l11_opy_ (u"ࠧࠨᚤ")).lower()
        if browser != bstack1l1l11_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨᚥ"):
            logger.warning(bstack1l1l11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧᚦ"))
            return False
        browser_version = caps.get(bstack1l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᚧ")) or caps.get(bstack1l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᚨ")) or bstack11ll1l11l11_opy_.get(bstack1l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᚩ")) or bstack11ll1l11l11_opy_.get(bstack1l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᚪ"), {}).get(bstack1l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᚫ")) or bstack11ll1l11l11_opy_.get(bstack1l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᚬ"), {}).get(bstack1l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫᚭ"))
        bstack1ll111lll1l_opy_ = bstack11ll11l1lll_opy_.bstack1ll1111l1ll_opy_
        bstack11ll1lll111_opy_ = False
        if config is not None:
          bstack11ll1lll111_opy_ = bstack1l1l11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧᚮ") in config and str(config[bstack1l1l11_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨᚯ")]).lower() != bstack1l1l11_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫᚰ")
        if os.environ.get(bstack1l1l11_opy_ (u"࠭ࡉࡔࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗࡊ࡙ࡓࡊࡑࡑࠫᚱ"), bstack1l1l11_opy_ (u"ࠧࠨᚲ")).lower() == bstack1l1l11_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᚳ") or bstack11ll1lll111_opy_:
          bstack1ll111lll1l_opy_ = bstack11ll11l1lll_opy_.bstack1ll11l1llll_opy_
        if browser_version and browser_version != bstack1l1l11_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩᚴ") and int(browser_version.split(bstack1l1l11_opy_ (u"ࠪ࠲ࠬᚵ"))[0]) <= bstack1ll111lll1l_opy_:
          logger.warning(bstack1lll11llll1_opy_ (u"ࠫࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡧࡳࡧࡤࡸࡪࡸࠠࡵࡪࡤࡲࠥࢁ࡭ࡪࡰࡢࡥ࠶࠷ࡹࡠࡵࡸࡴࡵࡵࡲࡵࡧࡧࡣࡨ࡮ࡲࡰ࡯ࡨࡣࡻ࡫ࡲࡴ࡫ࡲࡲࢂ࠴ࠧᚶ"))
          return False
        if not options:
          bstack1ll111ll111_opy_ = caps.get(bstack1l1l11_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᚷ")) or bstack11ll1l11l11_opy_.get(bstack1l1l11_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᚸ"), {})
          if bstack1l1l11_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫᚹ") in bstack1ll111ll111_opy_.get(bstack1l1l11_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ᚺ"), []):
              logger.warning(bstack1l1l11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦᚻ"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack1l1l11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡥࡱ࡯ࡤࡢࡶࡨࠤࡦ࠷࠱ࡺࠢࡶࡹࡵࡶ࡯ࡳࡶࠣ࠾ࠧᚼ") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1lll1llll1l_opy_ = config.get(bstack1l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᚽ"), {})
    bstack1lll1llll1l_opy_[bstack1l1l11_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨᚾ")] = os.getenv(bstack1l1l11_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫᚿ"))
    bstack11ll1ll1lll_opy_ = json.loads(os.getenv(bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨᛀ"), bstack1l1l11_opy_ (u"ࠨࡽࢀࠫᛁ"))).get(bstack1l1l11_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᛂ"))
    if not config[bstack1l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬᛃ")].get(bstack1l1l11_opy_ (u"ࠦࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠥᛄ")):
      if bstack1l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᛅ") in caps:
        caps[bstack1l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᛆ")][bstack1l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᛇ")] = bstack1lll1llll1l_opy_
        caps[bstack1l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᛈ")][bstack1l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᛉ")][bstack1l1l11_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᛊ")] = bstack11ll1ll1lll_opy_
      else:
        caps[bstack1l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᛋ")] = bstack1lll1llll1l_opy_
        caps[bstack1l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᛌ")][bstack1l1l11_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᛍ")] = bstack11ll1ll1lll_opy_
  except Exception as error:
    logger.debug(bstack1l1l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠴ࠠࡆࡴࡵࡳࡷࡀࠠࠣᛎ") +  str(error))
def bstack1l1l1l1l_opy_(driver, bstack11ll11llll1_opy_):
  try:
    setattr(driver, bstack1l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨᛏ"), True)
    session = driver.session_id
    if session:
      bstack11ll1ll11ll_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack11ll1ll11ll_opy_ = False
      bstack11ll1ll11ll_opy_ = url.scheme in [bstack1l1l11_opy_ (u"ࠤ࡫ࡸࡹࡶࠢᛐ"), bstack1l1l11_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤᛑ")]
      if bstack11ll1ll11ll_opy_:
        if bstack11ll11llll1_opy_:
          logger.info(bstack1l1l11_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣࡪࡴࡸࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡪࡤࡷࠥࡹࡴࡢࡴࡷࡩࡩ࠴ࠠࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡢࡦࡩ࡬ࡲࠥࡳ࡯࡮ࡧࡱࡸࡦࡸࡩ࡭ࡻ࠱ࠦᛒ"))
      return bstack11ll11llll1_opy_
  except Exception as e:
    logger.error(bstack1l1l11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣᛓ") + str(e))
    return False
def bstack1111ll1l1_opy_(driver, name, path):
  try:
    bstack1ll11llllll_opy_ = {
        bstack1l1l11_opy_ (u"࠭ࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩ࠭ᛔ"): threading.current_thread().current_test_uuid,
        bstack1l1l11_opy_ (u"ࠧࡵࡪࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᛕ"): os.environ.get(bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᛖ"), bstack1l1l11_opy_ (u"ࠩࠪᛗ")),
        bstack1l1l11_opy_ (u"ࠪࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴࠧᛘ"): os.environ.get(bstack1l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᛙ"), bstack1l1l11_opy_ (u"ࠬ࠭ᛚ"))
    }
    bstack1ll11ll11l1_opy_ = bstack111l11ll_opy_.bstack1ll11ll1l11_opy_(EVENTS.bstack1llll1ll_opy_.value)
    logger.debug(bstack1l1l11_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩᛛ"))
    try:
      if (bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧᛜ"), None) and bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᛝ"), None)):
        scripts = {bstack1l1l11_opy_ (u"ࠩࡶࡧࡦࡴࠧᛞ"): bstack11l1111ll1_opy_.perform_scan}
        bstack11ll1lllll1_opy_ = json.loads(scripts[bstack1l1l11_opy_ (u"ࠥࡷࡨࡧ࡮ࠣᛟ")].replace(bstack1l1l11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢᛠ"), bstack1l1l11_opy_ (u"ࠧࠨᛡ")))
        bstack11ll1lllll1_opy_[bstack1l1l11_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᛢ")][bstack1l1l11_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪࠧᛣ")] = None
        scripts[bstack1l1l11_opy_ (u"ࠣࡵࡦࡥࡳࠨᛤ")] = bstack1l1l11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࠧᛥ") + json.dumps(bstack11ll1lllll1_opy_)
        bstack11l1111ll1_opy_.bstack1ll11l11ll_opy_(scripts)
        bstack11l1111ll1_opy_.store()
        logger.debug(driver.execute_script(bstack11l1111ll1_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l1111ll1_opy_.perform_scan, {bstack1l1l11_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠥᛦ"): name}))
      bstack111l11ll_opy_.end(EVENTS.bstack1llll1ll_opy_.value, bstack1ll11ll11l1_opy_ + bstack1l1l11_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᛧ"), bstack1ll11ll11l1_opy_ + bstack1l1l11_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᛨ"), True, None)
    except Exception as error:
      bstack111l11ll_opy_.end(EVENTS.bstack1llll1ll_opy_.value, bstack1ll11ll11l1_opy_ + bstack1l1l11_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᛩ"), bstack1ll11ll11l1_opy_ + bstack1l1l11_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᛪ"), False, str(error))
    bstack1ll11ll11l1_opy_ = bstack111l11ll_opy_.bstack11ll1l11ll1_opy_(EVENTS.bstack1ll11l1l11l_opy_.value)
    bstack111l11ll_opy_.mark(bstack1ll11ll11l1_opy_ + bstack1l1l11_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ᛫"))
    try:
      if (bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ᛬"), None) and bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ᛭"), None)):
        scripts = {bstack1l1l11_opy_ (u"ࠫࡸࡩࡡ࡯ࠩᛮ"): bstack11l1111ll1_opy_.perform_scan}
        bstack11ll1lllll1_opy_ = json.loads(scripts[bstack1l1l11_opy_ (u"ࠧࡹࡣࡢࡰࠥᛯ")].replace(bstack1l1l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࠤᛰ"), bstack1l1l11_opy_ (u"ࠢࠣᛱ")))
        bstack11ll1lllll1_opy_[bstack1l1l11_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᛲ")][bstack1l1l11_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩᛳ")] = None
        scripts[bstack1l1l11_opy_ (u"ࠥࡷࡨࡧ࡮ࠣᛴ")] = bstack1l1l11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢᛵ") + json.dumps(bstack11ll1lllll1_opy_)
        bstack11l1111ll1_opy_.bstack1ll11l11ll_opy_(scripts)
        bstack11l1111ll1_opy_.store()
        logger.debug(driver.execute_script(bstack11l1111ll1_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l1111ll1_opy_.bstack11ll1l1111l_opy_, bstack1ll11llllll_opy_))
      bstack111l11ll_opy_.end(bstack1ll11ll11l1_opy_, bstack1ll11ll11l1_opy_ + bstack1l1l11_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᛶ"), bstack1ll11ll11l1_opy_ + bstack1l1l11_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᛷ"),True, None)
    except Exception as error:
      bstack111l11ll_opy_.end(bstack1ll11ll11l1_opy_, bstack1ll11ll11l1_opy_ + bstack1l1l11_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᛸ"), bstack1ll11ll11l1_opy_ + bstack1l1l11_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ᛹"),False, str(error))
    logger.info(bstack1l1l11_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠧ᛺"))
  except Exception as bstack1ll11l1ll1l_opy_:
    logger.error(bstack1l1l11_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧ࠽ࠤࠧ᛻") + str(path) + bstack1l1l11_opy_ (u"ࠦࠥࡋࡲࡳࡱࡵࠤ࠿ࠨ᛼") + str(bstack1ll11l1ll1l_opy_))
def bstack11ll1lll1ll_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack1l1l11_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ᛽")) and str(caps.get(bstack1l1l11_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ᛾"))).lower() == bstack1l1l11_opy_ (u"ࠢࡢࡰࡧࡶࡴ࡯ࡤࠣ᛿"):
        bstack1ll11ll1ll1_opy_ = caps.get(bstack1l1l11_opy_ (u"ࠣࡣࡳࡴ࡮ࡻ࡭࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥᜀ")) or caps.get(bstack1l1l11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦᜁ"))
        if bstack1ll11ll1ll1_opy_ and int(str(bstack1ll11ll1ll1_opy_)) < bstack11ll1l1l111_opy_:
            return False
    return True
def bstack11l11l11l_opy_(config):
  if bstack1l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᜂ") in config:
        return config[bstack1l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᜃ")]
  for platform in config.get(bstack1l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᜄ"), []):
      if bstack1l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᜅ") in platform:
          return platform[bstack1l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᜆ")]
  return None
def bstack11l111lll_opy_(bstack1lll111l11_opy_):
  try:
    browser_name = bstack1lll111l11_opy_[bstack1l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧᜇ")]
    browser_version = bstack1lll111l11_opy_[bstack1l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫᜈ")]
    chrome_options = bstack1lll111l11_opy_[bstack1l1l11_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡢࡳࡵࡺࡩࡰࡰࡶࠫᜉ")]
    try:
        bstack11ll11ll11l_opy_ = int(browser_version.split(bstack1l1l11_opy_ (u"ࠫ࠳࠭ᜊ"))[0])
    except ValueError as e:
        logger.error(bstack1l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡴࡴࡶࡦࡴࡷ࡭ࡳ࡭ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡸࡨࡶࡸ࡯࡯࡯ࠤᜋ") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack1l1l11_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ᜌ")):
        logger.warning(bstack1l1l11_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥᜍ"))
        return False
    if bstack11ll11ll11l_opy_ < bstack11ll11l1lll_opy_.bstack1ll11l1llll_opy_:
        logger.warning(bstack1lll11llll1_opy_ (u"ࠨࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡸࡥࡲࡷ࡬ࡶࡪࡹࠠࡄࡪࡵࡳࡲ࡫ࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡽࡆࡓࡓ࡙ࡔࡂࡐࡗࡗ࠳ࡓࡉࡏࡋࡐ࡙ࡒࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡗࡓࡔࡔࡘࡔࡆࡆࡢࡇࡍࡘࡏࡎࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࢁࠥࡵࡲࠡࡪ࡬࡫࡭࡫ࡲ࠯ࠩᜎ"))
        return False
    if chrome_options and any(bstack1l1l11_opy_ (u"ࠩ࠰࠱࡭࡫ࡡࡥ࡮ࡨࡷࡸ࠭ᜏ") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack1l1l11_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧᜐ"))
        return False
    return True
  except Exception as e:
    logger.error(bstack1l1l11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡣࡩࡧࡦ࡯࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡷࡺࡶࡰࡰࡴࡷࠤ࡫ࡵࡲࠡ࡮ࡲࡧࡦࡲࠠࡄࡪࡵࡳࡲ࡫࠺ࠡࠤᜑ") + str(e))
    return False
def bstack1l1lll11l1_opy_(bstack1ll111ll_opy_, config):
    try:
      bstack1ll11llll11_opy_ = bstack1l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᜒ") in config and config[bstack1l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᜓ")] == True
      bstack11ll1lll111_opy_ = bstack1l1l11_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨ᜔ࠫ") in config and str(config[bstack1l1l11_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩ᜕ࠬ")]).lower() != bstack1l1l11_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ᜖")
      if not (bstack1ll11llll11_opy_ and (not bstack1l11111ll1_opy_(config) or bstack11ll1lll111_opy_)):
        return bstack1ll111ll_opy_
      bstack11ll1ll11l1_opy_ = bstack11l1111ll1_opy_.bstack11ll1l1lll1_opy_
      if bstack11ll1ll11l1_opy_ is None:
        logger.debug(bstack1l1l11_opy_ (u"ࠥࡋࡴࡵࡧ࡭ࡧࠣࡧ࡭ࡸ࡯࡮ࡧࠣࡳࡵࡺࡩࡰࡰࡶࠤࡦࡸࡥࠡࡐࡲࡲࡪࠨ᜗"))
        return bstack1ll111ll_opy_
      bstack11ll1l1l1ll_opy_ = int(str(bstack11ll1lll1l1_opy_()).split(bstack1l1l11_opy_ (u"ࠫ࠳࠭᜘"))[0])
      logger.debug(bstack1l1l11_opy_ (u"࡙ࠧࡥ࡭ࡧࡱ࡭ࡺࡳࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡦࡨࡸࡪࡩࡴࡦࡦ࠽ࠤࠧ᜙") + str(bstack11ll1l1l1ll_opy_) + bstack1l1l11_opy_ (u"ࠨࠢ᜚"))
      if bstack11ll1l1l1ll_opy_ == 3 and isinstance(bstack1ll111ll_opy_, dict) and bstack1l1l11_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ᜛") in bstack1ll111ll_opy_ and bstack11ll1ll11l1_opy_ is not None:
        if bstack1l1l11_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭᜜") not in bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ᜝")]:
          bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ᜞")][bstack1l1l11_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᜟ")] = {}
        if bstack1l1l11_opy_ (u"ࠬࡧࡲࡨࡵࠪᜠ") in bstack11ll1ll11l1_opy_:
          if bstack1l1l11_opy_ (u"࠭ࡡࡳࡩࡶࠫᜡ") not in bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧᜢ")][bstack1l1l11_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᜣ")]:
            bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᜤ")][bstack1l1l11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᜥ")][bstack1l1l11_opy_ (u"ࠫࡦࡸࡧࡴࠩᜦ")] = []
          for arg in bstack11ll1ll11l1_opy_[bstack1l1l11_opy_ (u"ࠬࡧࡲࡨࡵࠪᜧ")]:
            if arg not in bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ᜨ")][bstack1l1l11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᜩ")][bstack1l1l11_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ᜪ")]:
              bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᜫ")][bstack1l1l11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᜬ")][bstack1l1l11_opy_ (u"ࠫࡦࡸࡧࡴࠩᜭ")].append(arg)
        if bstack1l1l11_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩᜮ") in bstack11ll1ll11l1_opy_:
          if bstack1l1l11_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪᜯ") not in bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧᜰ")][bstack1l1l11_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᜱ")]:
            bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᜲ")][bstack1l1l11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᜳ")][bstack1l1l11_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ᜴")] = []
          for ext in bstack11ll1ll11l1_opy_[bstack1l1l11_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ᜵")]:
            if ext not in bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭᜶")][bstack1l1l11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ᜷")][bstack1l1l11_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ᜸")]:
              bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ᜹")][bstack1l1l11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ᜺")][bstack1l1l11_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ᜻")].append(ext)
        if bstack1l1l11_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ᜼") in bstack11ll1ll11l1_opy_:
          if bstack1l1l11_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ᜽") not in bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ᜾")][bstack1l1l11_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭᜿")]:
            bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᝀ")][bstack1l1l11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᝁ")][bstack1l1l11_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪᝂ")] = {}
          bstack11ll1ll111l_opy_(bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᝃ")][bstack1l1l11_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᝄ")][bstack1l1l11_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ᝅ")],
                    bstack11ll1ll11l1_opy_[bstack1l1l11_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧᝆ")])
        os.environ[bstack1l1l11_opy_ (u"ࠩࡌࡗࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡆࡕࡖࡍࡔࡔࠧᝇ")] = bstack1l1l11_opy_ (u"ࠪࡸࡷࡻࡥࠨᝈ")
        return bstack1ll111ll_opy_
      else:
        chrome_options = None
        if isinstance(bstack1ll111ll_opy_, ChromeOptions):
          chrome_options = bstack1ll111ll_opy_
        elif isinstance(bstack1ll111ll_opy_, dict):
          for value in bstack1ll111ll_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1ll111ll_opy_, dict):
            bstack1ll111ll_opy_[bstack1l1l11_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬᝉ")] = chrome_options
          else:
            bstack1ll111ll_opy_ = chrome_options
        if bstack11ll1ll11l1_opy_ is not None:
          if bstack1l1l11_opy_ (u"ࠬࡧࡲࡨࡵࠪᝊ") in bstack11ll1ll11l1_opy_:
                bstack11ll1l111l1_opy_ = chrome_options.arguments or []
                new_args = bstack11ll1ll11l1_opy_[bstack1l1l11_opy_ (u"࠭ࡡࡳࡩࡶࠫᝋ")]
                for arg in new_args:
                    if arg not in bstack11ll1l111l1_opy_:
                        chrome_options.add_argument(arg)
          if bstack1l1l11_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫᝌ") in bstack11ll1ll11l1_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack1l1l11_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬᝍ"), [])
                bstack11ll11lll1l_opy_ = bstack11ll1ll11l1_opy_[bstack1l1l11_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ᝎ")]
                for extension in bstack11ll11lll1l_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack1l1l11_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩᝏ") in bstack11ll1ll11l1_opy_:
                bstack11ll1l1l1l1_opy_ = chrome_options.experimental_options.get(bstack1l1l11_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪᝐ"), {})
                bstack11ll1llllll_opy_ = bstack11ll1ll11l1_opy_[bstack1l1l11_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫᝑ")]
                bstack11ll1ll111l_opy_(bstack11ll1l1l1l1_opy_, bstack11ll1llllll_opy_)
                chrome_options.add_experimental_option(bstack1l1l11_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬᝒ"), bstack11ll1l1l1l1_opy_)
        os.environ[bstack1l1l11_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬᝓ")] = bstack1l1l11_opy_ (u"ࠨࡶࡵࡹࡪ࠭᝔")
        return bstack1ll111ll_opy_
    except Exception as e:
      logger.error(bstack1l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡢࡦࡧ࡭ࡳ࡭ࠠ࡯ࡱࡱ࠱ࡇ࡙ࠠࡪࡰࡩࡶࡦࠦࡡ࠲࠳ࡼࠤࡨ࡮ࡲࡰ࡯ࡨࠤࡴࡶࡴࡪࡱࡱࡷ࠿ࠦࠢ᝕") + str(e))
      return bstack1ll111ll_opy_