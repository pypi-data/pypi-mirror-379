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
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1llll11l_opy_, bstack11l1l1ll11l_opy_, bstack11l1ll1l1l1_opy_
import tempfile
import json
bstack111l1l11l1l_opy_ = os.getenv(bstack1l11l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡇࡠࡈࡌࡐࡊࠨᶩ"), None) or os.path.join(tempfile.gettempdir(), bstack1l11l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡥࡣࡷࡪ࠲ࡱࡵࡧࠣᶪ"))
bstack111l1l1ll1l_opy_ = os.path.join(bstack1l11l11_opy_ (u"ࠢ࡭ࡱࡪࠦᶫ"), bstack1l11l11_opy_ (u"ࠨࡵࡧ࡯࠲ࡩ࡬ࡪ࠯ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠬᶬ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1l11l11_opy_ (u"ࠩࠨࠬࡦࡹࡣࡵ࡫ࡰࡩ࠮ࡹࠠ࡜ࠧࠫࡲࡦࡳࡥࠪࡵࡠ࡟ࠪ࠮࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠫࡶࡡࠥ࠳ࠠࠦࠪࡰࡩࡸࡹࡡࡨࡧࠬࡷࠬᶭ"),
      datefmt=bstack1l11l11_opy_ (u"ࠪࠩ࡞࠳ࠥ࡮࠯ࠨࡨ࡙ࠫࡈ࠻ࠧࡐ࠾࡙࡚ࠪࠨᶮ"),
      stream=sys.stdout
    )
  return logger
def bstack1ll1ll1ll11_opy_():
  bstack111l1lll111_opy_ = os.environ.get(bstack1l11l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢࡈࡊࡈࡕࡈࠤᶯ"), bstack1l11l11_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦᶰ"))
  return logging.DEBUG if bstack111l1lll111_opy_.lower() == bstack1l11l11_opy_ (u"ࠨࡴࡳࡷࡨࠦᶱ") else logging.INFO
def bstack1l1lll11111_opy_():
  global bstack111l1l11l1l_opy_
  if os.path.exists(bstack111l1l11l1l_opy_):
    os.remove(bstack111l1l11l1l_opy_)
  if os.path.exists(bstack111l1l1ll1l_opy_):
    os.remove(bstack111l1l1ll1l_opy_)
def bstack11l11111l_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack111l1ll1ll1_opy_ = log_level
  if bstack1l11l11_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᶲ") in config and config[bstack1l11l11_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪᶳ")] in bstack11l1l1ll11l_opy_:
    bstack111l1ll1ll1_opy_ = bstack11l1l1ll11l_opy_[config[bstack1l11l11_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫᶴ")]]
  if config.get(bstack1l11l11_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬᶵ"), False):
    logging.getLogger().setLevel(bstack111l1ll1ll1_opy_)
    return bstack111l1ll1ll1_opy_
  global bstack111l1l11l1l_opy_
  bstack11l11111l_opy_()
  bstack111l1ll1111_opy_ = logging.Formatter(
    fmt=bstack1l11l11_opy_ (u"ࠫࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧᶶ"),
    datefmt=bstack1l11l11_opy_ (u"࡙ࠬࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࡜ࠪᶷ"),
  )
  bstack111l1l111ll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack111l1l11l1l_opy_)
  file_handler.setFormatter(bstack111l1ll1111_opy_)
  bstack111l1l111ll_opy_.setFormatter(bstack111l1ll1111_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack111l1l111ll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1l11l11_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࡷ࡫࡭ࡰࡶࡨ࠲ࡷ࡫࡭ࡰࡶࡨࡣࡨࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࠨᶸ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack111l1l111ll_opy_.setLevel(bstack111l1ll1ll1_opy_)
  logging.getLogger().addHandler(bstack111l1l111ll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack111l1ll1ll1_opy_
def bstack111l1ll111l_opy_(config):
  try:
    bstack111l1lll11l_opy_ = set(bstack11l1ll1l1l1_opy_)
    bstack111l1l11ll1_opy_ = bstack1l11l11_opy_ (u"ࠧࠨᶹ")
    with open(bstack1l11l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫᶺ")) as bstack111l1l1lll1_opy_:
      bstack111l1lll1l1_opy_ = bstack111l1l1lll1_opy_.read()
      bstack111l1l11ll1_opy_ = re.sub(bstack1l11l11_opy_ (u"ࡴࠪࡢ࠭ࡢࡳࠬࠫࡂࠧ࠳࠰ࠤ࡝ࡰࠪᶻ"), bstack1l11l11_opy_ (u"ࠪࠫᶼ"), bstack111l1lll1l1_opy_, flags=re.M)
      bstack111l1l11ll1_opy_ = re.sub(
        bstack1l11l11_opy_ (u"ࡶࠬࡤࠨ࡝ࡵ࠮࠭ࡄ࠮ࠧᶽ") + bstack1l11l11_opy_ (u"ࠬࢂࠧᶾ").join(bstack111l1lll11l_opy_) + bstack1l11l11_opy_ (u"࠭ࠩ࠯ࠬࠧࠫᶿ"),
        bstack1l11l11_opy_ (u"ࡲࠨ࡞࠵࠾ࠥࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩ᷀"),
        bstack111l1l11ll1_opy_, flags=re.M | re.I
      )
    def bstack111l1ll1l1l_opy_(dic):
      bstack111l1l1l1ll_opy_ = {}
      for key, value in dic.items():
        if key in bstack111l1lll11l_opy_:
          bstack111l1l1l1ll_opy_[key] = bstack1l11l11_opy_ (u"ࠨ࡝ࡕࡉࡉࡇࡃࡕࡇࡇࡡࠬ᷁")
        else:
          if isinstance(value, dict):
            bstack111l1l1l1ll_opy_[key] = bstack111l1ll1l1l_opy_(value)
          else:
            bstack111l1l1l1ll_opy_[key] = value
      return bstack111l1l1l1ll_opy_
    bstack111l1l1l1ll_opy_ = bstack111l1ll1l1l_opy_(config)
    return {
      bstack1l11l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰ᷂ࠬ"): bstack111l1l11ll1_opy_,
      bstack1l11l11_opy_ (u"ࠪࡪ࡮ࡴࡡ࡭ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭᷃"): json.dumps(bstack111l1l1l1ll_opy_)
    }
  except Exception as e:
    return {}
def bstack111l1l11l11_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack1l11l11_opy_ (u"ࠫࡱࡵࡧࠨ᷄"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack111l1l1l11l_opy_ = os.path.join(log_dir, bstack1l11l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠭᷅"))
  if not os.path.exists(bstack111l1l1l11l_opy_):
    bstack111l1l11lll_opy_ = {
      bstack1l11l11_opy_ (u"ࠨࡩ࡯࡫ࡳࡥࡹ࡮ࠢ᷆"): str(inipath),
      bstack1l11l11_opy_ (u"ࠢࡳࡱࡲࡸࡵࡧࡴࡩࠤ᷇"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack1l11l11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧ᷈")), bstack1l11l11_opy_ (u"ࠩࡺࠫ᷉")) as bstack111l1l1llll_opy_:
      bstack111l1l1llll_opy_.write(json.dumps(bstack111l1l11lll_opy_))
def bstack111l1l1ll11_opy_():
  try:
    bstack111l1l1l11l_opy_ = os.path.join(os.getcwd(), bstack1l11l11_opy_ (u"ࠪࡰࡴ࡭᷊ࠧ"), bstack1l11l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷ࠳ࡰࡳࡰࡰࠪ᷋"))
    if os.path.exists(bstack111l1l1l11l_opy_):
      with open(bstack111l1l1l11l_opy_, bstack1l11l11_opy_ (u"ࠬࡸࠧ᷌")) as bstack111l1l1llll_opy_:
        bstack111l1l1l1l1_opy_ = json.load(bstack111l1l1llll_opy_)
      return bstack111l1l1l1l1_opy_.get(bstack1l11l11_opy_ (u"࠭ࡩ࡯࡫ࡳࡥࡹ࡮ࠧ᷍"), bstack1l11l11_opy_ (u"ࠧࠨ᷎")), bstack111l1l1l1l1_opy_.get(bstack1l11l11_opy_ (u"ࠨࡴࡲࡳࡹࡶࡡࡵࡪ᷏ࠪ"), bstack1l11l11_opy_ (u"᷐ࠩࠪ"))
  except:
    pass
  return None, None
def bstack111l1l1l111_opy_():
  try:
    bstack111l1l1l11l_opy_ = os.path.join(os.getcwd(), bstack1l11l11_opy_ (u"ࠪࡰࡴ࡭ࠧ᷑"), bstack1l11l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷ࠳ࡰࡳࡰࡰࠪ᷒"))
    if os.path.exists(bstack111l1l1l11l_opy_):
      os.remove(bstack111l1l1l11l_opy_)
  except:
    pass
def bstack11lll1l1l1_opy_(config):
  try:
    from bstack_utils.helper import bstack11ll1111ll_opy_, bstack1l1l1llll_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack111l1l11l1l_opy_
    if config.get(bstack1l11l11_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧᷓ"), False):
      return
    uuid = os.getenv(bstack1l11l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᷔ")) if os.getenv(bstack1l11l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᷕ")) else bstack11ll1111ll_opy_.get_property(bstack1l11l11_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥᷖ"))
    if not uuid or uuid == bstack1l11l11_opy_ (u"ࠩࡱࡹࡱࡲࠧᷗ"):
      return
    bstack111l1ll1l11_opy_ = [bstack1l11l11_opy_ (u"ࠪࡶࡪࡷࡵࡪࡴࡨࡱࡪࡴࡴࡴ࠰ࡷࡼࡹ࠭ᷘ"), bstack1l11l11_opy_ (u"ࠫࡕ࡯ࡰࡧ࡫࡯ࡩࠬᷙ"), bstack1l11l11_opy_ (u"ࠬࡶࡹࡱࡴࡲ࡮ࡪࡩࡴ࠯ࡶࡲࡱࡱ࠭ᷚ"), bstack111l1l11l1l_opy_, bstack111l1l1ll1l_opy_]
    bstack111l1ll11ll_opy_, root_path = bstack111l1l1ll11_opy_()
    if bstack111l1ll11ll_opy_ != None:
      bstack111l1ll1l11_opy_.append(bstack111l1ll11ll_opy_)
    if root_path != None:
      bstack111l1ll1l11_opy_.append(os.path.join(root_path, bstack1l11l11_opy_ (u"࠭ࡣࡰࡰࡩࡸࡪࡹࡴ࠯ࡲࡼࠫᷛ")))
    bstack11l11111l_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1l11l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭࡭ࡱࡪࡷ࠲࠭ᷜ") + uuid + bstack1l11l11_opy_ (u"ࠨ࠰ࡷࡥࡷ࠴ࡧࡻࠩᷝ"))
    with tarfile.open(output_file, bstack1l11l11_opy_ (u"ࠤࡺ࠾࡬ࢀࠢᷞ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack111l1ll1l11_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack111l1ll111l_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack111l1ll11l1_opy_ = data.encode()
        tarinfo.size = len(bstack111l1ll11l1_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack111l1ll11l1_opy_))
    bstack1111ll1l1_opy_ = MultipartEncoder(
      fields= {
        bstack1l11l11_opy_ (u"ࠪࡨࡦࡺࡡࠨᷟ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1l11l11_opy_ (u"ࠫࡷࡨࠧᷠ")), bstack1l11l11_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲ࡼ࠲࡭ࡺࡪࡲࠪᷡ")),
        bstack1l11l11_opy_ (u"࠭ࡣ࡭࡫ࡨࡲࡹࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨᷢ"): uuid
      }
    )
    bstack111l1ll1lll_opy_ = bstack1l1l1llll_opy_(cli.config, [bstack1l11l11_opy_ (u"ࠢࡢࡲ࡬ࡷࠧᷣ"), bstack1l11l11_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣᷤ"), bstack1l11l11_opy_ (u"ࠤࡸࡴࡱࡵࡡࡥࠤᷥ")], bstack11l1llll11l_opy_)
    response = requests.post(
      bstack1l11l11_opy_ (u"ࠥࡿࢂ࠵ࡣ࡭࡫ࡨࡲࡹ࠳࡬ࡰࡩࡶ࠳ࡺࡶ࡬ࡰࡣࡧࠦᷦ").format(bstack111l1ll1lll_opy_),
      data=bstack1111ll1l1_opy_,
      headers={bstack1l11l11_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᷧ"): bstack1111ll1l1_opy_.content_type},
      auth=(config[bstack1l11l11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᷨ")], config[bstack1l11l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᷩ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1l11l11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡵࡱ࡮ࡲࡥࡩࠦ࡬ࡰࡩࡶ࠾ࠥ࠭ᷪ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1l11l11_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡱࡨ࡮ࡴࡧࠡ࡮ࡲ࡫ࡸࡀࠧᷫ") + str(e))
  finally:
    try:
      bstack1l1lll11111_opy_()
      bstack111l1l1l111_opy_()
    except:
      pass