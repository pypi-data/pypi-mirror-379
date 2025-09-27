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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1lll1ll1l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1111111l_opy_ import bstack11lllll1ll_opy_
class bstack1111l11l_opy_:
  working_dir = os.getcwd()
  bstack1lllll11l_opy_ = False
  config = {}
  bstack111lll11ll1_opy_ = bstack1l1l11_opy_ (u"ࠬ࠭ấ")
  binary_path = bstack1l1l11_opy_ (u"࠭ࠧẦ")
  bstack1111l1l1l1l_opy_ = bstack1l1l11_opy_ (u"ࠧࠨầ")
  bstack11llll111_opy_ = False
  bstack11111ll1l1l_opy_ = None
  bstack11111l1l111_opy_ = {}
  bstack11111l11ll1_opy_ = 300
  bstack11111ll1ll1_opy_ = False
  logger = None
  bstack11111l11l1l_opy_ = False
  bstack1ll111l11_opy_ = False
  percy_build_id = None
  bstack1111l11ll1l_opy_ = bstack1l1l11_opy_ (u"ࠨࠩẨ")
  bstack11111lll1l1_opy_ = {
    bstack1l1l11_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩẩ") : 1,
    bstack1l1l11_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫẪ") : 2,
    bstack1l1l11_opy_ (u"ࠫࡪࡪࡧࡦࠩẫ") : 3,
    bstack1l1l11_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬẬ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1111l1l11l1_opy_(self):
    bstack1111l1111ll_opy_ = bstack1l1l11_opy_ (u"࠭ࠧậ")
    bstack1111l1ll11l_opy_ = sys.platform
    bstack1111l11l111_opy_ = bstack1l1l11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭Ắ")
    if re.match(bstack1l1l11_opy_ (u"ࠣࡦࡤࡶࡼ࡯࡮ࡽ࡯ࡤࡧࠥࡵࡳࠣắ"), bstack1111l1ll11l_opy_) != None:
      bstack1111l1111ll_opy_ = bstack11l1l1lll11_opy_ + bstack1l1l11_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯ࡲࡷࡽ࠴ࡺࡪࡲࠥẰ")
      self.bstack1111l11ll1l_opy_ = bstack1l1l11_opy_ (u"ࠪࡱࡦࡩࠧằ")
    elif re.match(bstack1l1l11_opy_ (u"ࠦࡲࡹࡷࡪࡰࡿࡱࡸࡿࡳࡽ࡯࡬ࡲ࡬ࡽࡼࡤࡻࡪࡻ࡮ࡴࡼࡣࡥࡦࡻ࡮ࡴࡼࡸ࡫ࡱࡧࡪࢂࡥ࡮ࡥࡿࡻ࡮ࡴ࠳࠳ࠤẲ"), bstack1111l1ll11l_opy_) != None:
      bstack1111l1111ll_opy_ = bstack11l1l1lll11_opy_ + bstack1l1l11_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡽࡩ࡯࠰ࡽ࡭ࡵࠨẳ")
      bstack1111l11l111_opy_ = bstack1l1l11_opy_ (u"ࠨࡰࡦࡴࡦࡽ࠳࡫ࡸࡦࠤẴ")
      self.bstack1111l11ll1l_opy_ = bstack1l1l11_opy_ (u"ࠧࡸ࡫ࡱࠫẵ")
    else:
      bstack1111l1111ll_opy_ = bstack11l1l1lll11_opy_ + bstack1l1l11_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮࡮࡬ࡲࡺࡾ࠮ࡻ࡫ࡳࠦẶ")
      self.bstack1111l11ll1l_opy_ = bstack1l1l11_opy_ (u"ࠩ࡯࡭ࡳࡻࡸࠨặ")
    return bstack1111l1111ll_opy_, bstack1111l11l111_opy_
  def bstack11111l1ll11_opy_(self):
    try:
      bstack1111ll11111_opy_ = [os.path.join(expanduser(bstack1l1l11_opy_ (u"ࠥࢂࠧẸ")), bstack1l1l11_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫẹ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1111ll11111_opy_:
        if(self.bstack1111l1111l1_opy_(path)):
          return path
      raise bstack1l1l11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠤẺ")
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡴࡦࡺࡨࠡࡨࡲࡶࠥࡶࡥࡳࡥࡼࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࠱ࠥࢁࡽࠣẻ").format(e))
  def bstack1111l1111l1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack11111llll11_opy_(self, bstack1111l1llll1_opy_):
    return os.path.join(bstack1111l1llll1_opy_, self.bstack111lll11ll1_opy_ + bstack1l1l11_opy_ (u"ࠢ࠯ࡧࡷࡥ࡬ࠨẼ"))
  def bstack11111lll1ll_opy_(self, bstack1111l1llll1_opy_, bstack11111l111l1_opy_):
    if not bstack11111l111l1_opy_: return
    try:
      bstack1111l1lll11_opy_ = self.bstack11111llll11_opy_(bstack1111l1llll1_opy_)
      with open(bstack1111l1lll11_opy_, bstack1l1l11_opy_ (u"ࠣࡹࠥẽ")) as f:
        f.write(bstack11111l111l1_opy_)
        self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡖࡥࡻ࡫ࡤࠡࡰࡨࡻࠥࡋࡔࡢࡩࠣࡪࡴࡸࠠࡱࡧࡵࡧࡾࠨẾ"))
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡢࡸࡨࠤࡹ࡮ࡥࠡࡧࡷࡥ࡬࠲ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥế").format(e))
  def bstack1111l1l1111_opy_(self, bstack1111l1llll1_opy_):
    try:
      bstack1111l1lll11_opy_ = self.bstack11111llll11_opy_(bstack1111l1llll1_opy_)
      if os.path.exists(bstack1111l1lll11_opy_):
        with open(bstack1111l1lll11_opy_, bstack1l1l11_opy_ (u"ࠦࡷࠨỀ")) as f:
          bstack11111l111l1_opy_ = f.read().strip()
          return bstack11111l111l1_opy_ if bstack11111l111l1_opy_ else None
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡅࡕࡣࡪ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣề").format(e))
  def bstack11111l11l11_opy_(self, bstack1111l1llll1_opy_, bstack1111l1111ll_opy_):
    bstack11111ll11ll_opy_ = self.bstack1111l1l1111_opy_(bstack1111l1llll1_opy_)
    if bstack11111ll11ll_opy_:
      try:
        bstack11111ll111l_opy_ = self.bstack11111llllll_opy_(bstack11111ll11ll_opy_, bstack1111l1111ll_opy_)
        if not bstack11111ll111l_opy_:
          self.logger.debug(bstack1l1l11_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥ࡯ࡳࠡࡷࡳࠤࡹࡵࠠࡥࡣࡷࡩࠥ࠮ࡅࡕࡣࡪࠤࡺࡴࡣࡩࡣࡱ࡫ࡪࡪࠩࠣỂ"))
          return True
        self.logger.debug(bstack1l1l11_opy_ (u"ࠢࡏࡧࡺࠤࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡺࡪࡸࡳࡪࡱࡱࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡵࡱࡦࡤࡸࡪࠨể"))
        return False
      except Exception as e:
        self.logger.warn(bstack1l1l11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡨ࡮ࡥࡤ࡭ࠣࡪࡴࡸࠠࡣ࡫ࡱࡥࡷࡿࠠࡶࡲࡧࡥࡹ࡫ࡳ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡦ࡮ࡴࡡࡳࡻ࠽ࠤࢀࢃࠢỄ").format(e))
    return False
  def bstack11111llllll_opy_(self, bstack11111ll11ll_opy_, bstack1111l1111ll_opy_):
    try:
      headers = {
        bstack1l1l11_opy_ (u"ࠤࡌࡪ࠲ࡔ࡯࡯ࡧ࠰ࡑࡦࡺࡣࡩࠤễ"): bstack11111ll11ll_opy_
      }
      response = bstack1lll1ll1l_opy_(bstack1l1l11_opy_ (u"ࠪࡋࡊ࡚ࠧỆ"), bstack1111l1111ll_opy_, {}, {bstack1l1l11_opy_ (u"ࠦ࡭࡫ࡡࡥࡧࡵࡷࠧệ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡨ࡮ࡥࡤ࡭࡬ࡲ࡬ࠦࡦࡰࡴࠣࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡸࡴࡩࡧࡴࡦࡵ࠽ࠤࢀࢃࠢỈ").format(e))
  @measure(event_name=EVENTS.bstack11l1lll1111_opy_, stage=STAGE.bstack1ll11lll_opy_)
  def bstack11111l1lll1_opy_(self, bstack1111l1111ll_opy_, bstack1111l11l111_opy_):
    try:
      bstack1111l11ll11_opy_ = self.bstack11111l1ll11_opy_()
      bstack11111l1l1ll_opy_ = os.path.join(bstack1111l11ll11_opy_, bstack1l1l11_opy_ (u"࠭ࡰࡦࡴࡦࡽ࠳ࢀࡩࡱࠩỉ"))
      bstack111111lllll_opy_ = os.path.join(bstack1111l11ll11_opy_, bstack1111l11l111_opy_)
      if self.bstack11111l11l11_opy_(bstack1111l11ll11_opy_, bstack1111l1111ll_opy_): # if bstack11111ll1lll_opy_, bstack1l1l111l11l_opy_ bstack11111l111l1_opy_ is bstack1111l11111l_opy_ to bstack11l111ll111_opy_ version available (response 304)
        if os.path.exists(bstack111111lllll_opy_):
          self.logger.info(bstack1l1l11_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡽࢀ࠰ࠥࡹ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡥࡱࡺࡲࡱࡵࡡࡥࠤỊ").format(bstack111111lllll_opy_))
          return bstack111111lllll_opy_
        if os.path.exists(bstack11111l1l1ll_opy_):
          self.logger.info(bstack1l1l11_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡻ࡫ࡳࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡻࡾ࠮ࠣࡹࡳࢀࡩࡱࡲ࡬ࡲ࡬ࠨị").format(bstack11111l1l1ll_opy_))
          return self.bstack1111l1ll1ll_opy_(bstack11111l1l1ll_opy_, bstack1111l11l111_opy_)
      self.logger.info(bstack1l1l11_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡦࡳࡱࡰࠤࢀࢃࠢỌ").format(bstack1111l1111ll_opy_))
      response = bstack1lll1ll1l_opy_(bstack1l1l11_opy_ (u"ࠪࡋࡊ࡚ࠧọ"), bstack1111l1111ll_opy_, {}, {})
      if response.status_code == 200:
        bstack11111l1ll1l_opy_ = response.headers.get(bstack1l1l11_opy_ (u"ࠦࡊ࡚ࡡࡨࠤỎ"), bstack1l1l11_opy_ (u"ࠧࠨỏ"))
        if bstack11111l1ll1l_opy_:
          self.bstack11111lll1ll_opy_(bstack1111l11ll11_opy_, bstack11111l1ll1l_opy_)
        with open(bstack11111l1l1ll_opy_, bstack1l1l11_opy_ (u"࠭ࡷࡣࠩỐ")) as file:
          file.write(response.content)
        self.logger.info(bstack1l1l11_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥࡧࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡥࡳࡪࠠࡴࡣࡹࡩࡩࠦࡡࡵࠢࡾࢁࠧố").format(bstack11111l1l1ll_opy_))
        return self.bstack1111l1ll1ll_opy_(bstack11111l1l1ll_opy_, bstack1111l11l111_opy_)
      else:
        raise(bstack1l1l11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡴࡩࡧࠣࡪ࡮ࡲࡥ࠯ࠢࡖࡸࡦࡺࡵࡴࠢࡦࡳࡩ࡫࠺ࠡࡽࢀࠦỒ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࡀࠠࡼࡿࠥồ").format(e))
  def bstack1111l1l111l_opy_(self, bstack1111l1111ll_opy_, bstack1111l11l111_opy_):
    try:
      retry = 2
      bstack111111lllll_opy_ = None
      bstack1111l111111_opy_ = False
      while retry > 0:
        bstack111111lllll_opy_ = self.bstack11111l1lll1_opy_(bstack1111l1111ll_opy_, bstack1111l11l111_opy_)
        bstack1111l111111_opy_ = self.bstack1111l11lll1_opy_(bstack1111l1111ll_opy_, bstack1111l11l111_opy_, bstack111111lllll_opy_)
        if bstack1111l111111_opy_:
          break
        retry -= 1
      return bstack111111lllll_opy_, bstack1111l111111_opy_
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡧࡦࡶࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡳࡥࡹ࡮ࠢỔ").format(e))
    return bstack111111lllll_opy_, False
  def bstack1111l11lll1_opy_(self, bstack1111l1111ll_opy_, bstack1111l11l111_opy_, bstack111111lllll_opy_, bstack11111l1llll_opy_ = 0):
    if bstack11111l1llll_opy_ > 1:
      return False
    if bstack111111lllll_opy_ == None or os.path.exists(bstack111111lllll_opy_) == False:
      self.logger.warn(bstack1l1l11_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡴࡦࡺࡨࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡸࡥࡵࡴࡼ࡭ࡳ࡭ࠠࡥࡱࡺࡲࡱࡵࡡࡥࠤổ"))
      return False
    bstack1111l111l11_opy_ = bstack1l1l11_opy_ (u"ࡷࠨ࡞࠯ࠬࡃࡴࡪࡸࡣࡺ࠱ࡦࡰ࡮ࠦ࡜ࡥ࠭࡟࠲ࡡࡪࠫ࡝࠰࡟ࡨ࠰ࠨỖ")
    command = bstack1l1l11_opy_ (u"࠭ࡻࡾࠢ࠰࠱ࡻ࡫ࡲࡴ࡫ࡲࡲࠬỗ").format(bstack111111lllll_opy_)
    bstack1111l11l11l_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1111l111l11_opy_, bstack1111l11l11l_opy_) != None:
      return True
    else:
      self.logger.error(bstack1l1l11_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡤࡪࡨࡧࡰࠦࡦࡢ࡫࡯ࡩࡩࠨỘ"))
      return False
  def bstack1111l1ll1ll_opy_(self, bstack11111l1l1ll_opy_, bstack1111l11l111_opy_):
    try:
      working_dir = os.path.dirname(bstack11111l1l1ll_opy_)
      shutil.unpack_archive(bstack11111l1l1ll_opy_, working_dir)
      bstack111111lllll_opy_ = os.path.join(working_dir, bstack1111l11l111_opy_)
      os.chmod(bstack111111lllll_opy_, 0o755)
      return bstack111111lllll_opy_
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡺࡴࡺࡪࡲࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠤộ"))
  def bstack1111l1l1l11_opy_(self):
    try:
      bstack1111l111lll_opy_ = self.config.get(bstack1l1l11_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨỚ"))
      bstack1111l1l1l11_opy_ = bstack1111l111lll_opy_ or (bstack1111l111lll_opy_ is None and self.bstack1lllll11l_opy_)
      if not bstack1111l1l1l11_opy_ or self.config.get(bstack1l1l11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ớ"), None) not in bstack11l1llll111_opy_:
        return False
      self.bstack11llll111_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡨࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨỜ").format(e))
  def bstack1111l11l1ll_opy_(self):
    try:
      bstack1111l11l1ll_opy_ = self.percy_capture_mode
      return bstack1111l11l1ll_opy_
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡩࡴࠡࡲࡨࡶࡨࡿࠠࡤࡣࡳࡸࡺࡸࡥࠡ࡯ࡲࡨࡪ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨờ").format(e))
  def init(self, bstack1lllll11l_opy_, config, logger):
    self.bstack1lllll11l_opy_ = bstack1lllll11l_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1111l1l1l11_opy_():
      return
    self.bstack11111l1l111_opy_ = config.get(bstack1l1l11_opy_ (u"࠭ࡰࡦࡴࡦࡽࡔࡶࡴࡪࡱࡱࡷࠬỞ"), {})
    self.percy_capture_mode = config.get(bstack1l1l11_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪở"))
    try:
      bstack1111l1111ll_opy_, bstack1111l11l111_opy_ = self.bstack1111l1l11l1_opy_()
      self.bstack111lll11ll1_opy_ = bstack1111l11l111_opy_
      bstack111111lllll_opy_, bstack1111l111111_opy_ = self.bstack1111l1l111l_opy_(bstack1111l1111ll_opy_, bstack1111l11l111_opy_)
      if bstack1111l111111_opy_:
        self.binary_path = bstack111111lllll_opy_
        thread = Thread(target=self.bstack1111l1l1lll_opy_)
        thread.start()
      else:
        self.bstack11111l11l1l_opy_ = True
        self.logger.error(bstack1l1l11_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡳࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦࡦࡰࡷࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤ࡚ࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡐࡦࡴࡦࡽࠧỠ").format(bstack111111lllll_opy_))
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥỡ").format(e))
  def bstack1111l1lll1l_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1l1l11_opy_ (u"ࠪࡰࡴ࡭ࠧỢ"), bstack1l1l11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡰࡴ࡭ࠧợ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡖࡵࡴࡪ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࡵࠣࡥࡹࠦࡻࡾࠤỤ").format(logfile))
      self.bstack1111l1l1l1l_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࠢࡳࡥࡹ࡮ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢụ").format(e))
  @measure(event_name=EVENTS.bstack11l1lll1l1l_opy_, stage=STAGE.bstack1ll11lll_opy_)
  def bstack1111l1l1lll_opy_(self):
    bstack11111ll1l11_opy_ = self.bstack11111l1l1l1_opy_()
    if bstack11111ll1l11_opy_ == None:
      self.bstack11111l11l1l_opy_ = True
      self.logger.error(bstack1l1l11_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻࠥỦ"))
      return False
    bstack11111l11111_opy_ = [bstack1l1l11_opy_ (u"ࠣࡣࡳࡴ࠿࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠤủ") if self.bstack1lllll11l_opy_ else bstack1l1l11_opy_ (u"ࠩࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹ࠭Ứ")]
    bstack111l1l1lll1_opy_ = self.bstack11111l111ll_opy_()
    if bstack111l1l1lll1_opy_ != None:
      bstack11111l11111_opy_.append(bstack1l1l11_opy_ (u"ࠥ࠱ࡨࠦࡻࡾࠤứ").format(bstack111l1l1lll1_opy_))
    env = os.environ.copy()
    env[bstack1l1l11_opy_ (u"ࠦࡕࡋࡒࡄ࡛ࡢࡘࡔࡑࡅࡏࠤỪ")] = bstack11111ll1l11_opy_
    env[bstack1l1l11_opy_ (u"࡚ࠧࡈࡠࡄࡘࡍࡑࡊ࡟ࡖࡗࡌࡈࠧừ")] = os.environ.get(bstack1l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫỬ"), bstack1l1l11_opy_ (u"ࠧࠨử"))
    bstack11111lll11l_opy_ = [self.binary_path]
    self.bstack1111l1lll1l_opy_()
    self.bstack11111ll1l1l_opy_ = self.bstack1111l1ll111_opy_(bstack11111lll11l_opy_ + bstack11111l11111_opy_, env)
    self.logger.debug(bstack1l1l11_opy_ (u"ࠣࡕࡷࡥࡷࡺࡩ࡯ࡩࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠤỮ"))
    bstack11111l1llll_opy_ = 0
    while self.bstack11111ll1l1l_opy_.poll() == None:
      bstack11111ll11l1_opy_ = self.bstack1111l11llll_opy_()
      if bstack11111ll11l1_opy_:
        self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠧữ"))
        self.bstack11111ll1ll1_opy_ = True
        return True
      bstack11111l1llll_opy_ += 1
      self.logger.debug(bstack1l1l11_opy_ (u"ࠥࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡕࡩࡹࡸࡹࠡ࠯ࠣࡿࢂࠨỰ").format(bstack11111l1llll_opy_))
      time.sleep(2)
    self.logger.error(bstack1l1l11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡌࡡࡪ࡮ࡨࡨࠥࡧࡦࡵࡧࡵࠤࢀࢃࠠࡢࡶࡷࡩࡲࡶࡴࡴࠤự").format(bstack11111l1llll_opy_))
    self.bstack11111l11l1l_opy_ = True
    return False
  def bstack1111l11llll_opy_(self, bstack11111l1llll_opy_ = 0):
    if bstack11111l1llll_opy_ > 10:
      return False
    try:
      bstack11111l1111l_opy_ = os.environ.get(bstack1l1l11_opy_ (u"ࠬࡖࡅࡓࡅ࡜ࡣࡘࡋࡒࡗࡇࡕࡣࡆࡊࡄࡓࡇࡖࡗࠬỲ"), bstack1l1l11_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵࡬ࡰࡥࡤࡰ࡭ࡵࡳࡵ࠼࠸࠷࠸࠾ࠧỳ"))
      bstack1111l111ll1_opy_ = bstack11111l1111l_opy_ + bstack11l1ll11l11_opy_
      response = requests.get(bstack1111l111ll1_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩ࠭Ỵ"), {}).get(bstack1l1l11_opy_ (u"ࠨ࡫ࡧࠫỵ"), None)
      return True
    except:
      self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡲࡦࡦࠣࡻ࡭࡯࡬ࡦࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡨࡦࡣ࡯ࡸ࡭ࠦࡣࡩࡧࡦ࡯ࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢỶ"))
      return False
  def bstack11111l1l1l1_opy_(self):
    bstack1111l1l1ll1_opy_ = bstack1l1l11_opy_ (u"ࠪࡥࡵࡶࠧỷ") if self.bstack1lllll11l_opy_ else bstack1l1l11_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭Ỹ")
    bstack1111l1ll1l1_opy_ = bstack1l1l11_opy_ (u"ࠧࡻ࡮ࡥࡧࡩ࡭ࡳ࡫ࡤࠣỹ") if self.config.get(bstack1l1l11_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬỺ")) is None else True
    bstack11ll11l111l_opy_ = bstack1l1l11_opy_ (u"ࠢࡢࡲ࡬࠳ࡦࡶࡰࡠࡲࡨࡶࡨࡿ࠯ࡨࡧࡷࡣࡵࡸ࡯࡫ࡧࡦࡸࡤࡺ࡯࡬ࡧࡱࡃࡳࡧ࡭ࡦ࠿ࡾࢁࠫࡺࡹࡱࡧࡀࡿࢂࠬࡰࡦࡴࡦࡽࡂࢁࡽࠣỻ").format(self.config[bstack1l1l11_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭Ỽ")], bstack1111l1l1ll1_opy_, bstack1111l1ll1l1_opy_)
    if self.percy_capture_mode:
      bstack11ll11l111l_opy_ += bstack1l1l11_opy_ (u"ࠤࠩࡴࡪࡸࡣࡺࡡࡦࡥࡵࡺࡵࡳࡧࡢࡱࡴࡪࡥ࠾ࡽࢀࠦỽ").format(self.percy_capture_mode)
    uri = bstack11lllll1ll_opy_(bstack11ll11l111l_opy_)
    try:
      response = bstack1lll1ll1l_opy_(bstack1l1l11_opy_ (u"ࠪࡋࡊ࡚ࠧỾ"), uri, {}, {bstack1l1l11_opy_ (u"ࠫࡦࡻࡴࡩࠩỿ"): (self.config[bstack1l1l11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧἀ")], self.config[bstack1l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩἁ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack11llll111_opy_ = data.get(bstack1l1l11_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨἂ"))
        self.percy_capture_mode = data.get(bstack1l1l11_opy_ (u"ࠨࡲࡨࡶࡨࡿ࡟ࡤࡣࡳࡸࡺࡸࡥࡠ࡯ࡲࡨࡪ࠭ἃ"))
        os.environ[bstack1l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧἄ")] = str(self.bstack11llll111_opy_)
        os.environ[bstack1l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧἅ")] = str(self.percy_capture_mode)
        if bstack1111l1ll1l1_opy_ == bstack1l1l11_opy_ (u"ࠦࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠢἆ") and str(self.bstack11llll111_opy_).lower() == bstack1l1l11_opy_ (u"ࠧࡺࡲࡶࡧࠥἇ"):
          self.bstack1ll111l11_opy_ = True
        if bstack1l1l11_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧἈ") in data:
          return data[bstack1l1l11_opy_ (u"ࠢࡵࡱ࡮ࡩࡳࠨἉ")]
        else:
          raise bstack1l1l11_opy_ (u"ࠨࡖࡲ࡯ࡪࡴࠠࡏࡱࡷࠤࡋࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽࠨἊ").format(data)
      else:
        raise bstack1l1l11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡵ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡹࡴࡢࡶࡸࡷࠥ࠳ࠠࡼࡿ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡂࡰࡦࡼࠤ࠲ࠦࡻࡾࠤἋ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡴࡷࡵࡪࡦࡥࡷࠦἌ").format(e))
  def bstack11111l111ll_opy_(self):
    bstack11111llll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l11_opy_ (u"ࠦࡵ࡫ࡲࡤࡻࡆࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠢἍ"))
    try:
      if bstack1l1l11_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭Ἆ") not in self.bstack11111l1l111_opy_:
        self.bstack11111l1l111_opy_[bstack1l1l11_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧἏ")] = 2
      with open(bstack11111llll1l_opy_, bstack1l1l11_opy_ (u"ࠧࡸࠩἐ")) as fp:
        json.dump(self.bstack11111l1l111_opy_, fp)
      return bstack11111llll1l_opy_
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡨࡸࡥࡢࡶࡨࠤࡵ࡫ࡲࡤࡻࠣࡧࡴࡴࡦ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣἑ").format(e))
  def bstack1111l1ll111_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1111l11ll1l_opy_ == bstack1l1l11_opy_ (u"ࠩࡺ࡭ࡳ࠭ἒ"):
        bstack11111l1l11l_opy_ = [bstack1l1l11_opy_ (u"ࠪࡧࡲࡪ࠮ࡦࡺࡨࠫἓ"), bstack1l1l11_opy_ (u"ࠫ࠴ࡩࠧἔ")]
        cmd = bstack11111l1l11l_opy_ + cmd
      cmd = bstack1l1l11_opy_ (u"ࠬࠦࠧἕ").join(cmd)
      self.logger.debug(bstack1l1l11_opy_ (u"ࠨࡒࡶࡰࡱ࡭ࡳ࡭ࠠࡼࡿࠥ἖").format(cmd))
      with open(self.bstack1111l1l1l1l_opy_, bstack1l1l11_opy_ (u"ࠢࡢࠤ἗")) as bstack11111ll1111_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack11111ll1111_opy_, text=True, stderr=bstack11111ll1111_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack11111l11l1l_opy_ = True
      self.logger.error(bstack1l1l11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺࠢࡺ࡭ࡹ࡮ࠠࡤ࡯ࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠥἘ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack11111ll1ll1_opy_:
        self.logger.info(bstack1l1l11_opy_ (u"ࠤࡖࡸࡴࡶࡰࡪࡰࡪࠤࡕ࡫ࡲࡤࡻࠥἙ"))
        cmd = [self.binary_path, bstack1l1l11_opy_ (u"ࠥࡩࡽ࡫ࡣ࠻ࡵࡷࡳࡵࠨἚ")]
        self.bstack1111l1ll111_opy_(cmd)
        self.bstack11111ll1ll1_opy_ = False
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡲࡴࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡨࡵ࡭࡮ࡣࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦἛ").format(cmd, e))
  def bstack1ll111llll_opy_(self):
    if not self.bstack11llll111_opy_:
      return
    try:
      bstack1111l1lllll_opy_ = 0
      while not self.bstack11111ll1ll1_opy_ and bstack1111l1lllll_opy_ < self.bstack11111l11ll1_opy_:
        if self.bstack11111l11l1l_opy_:
          self.logger.info(bstack1l1l11_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡪࡦ࡯࡬ࡦࡦࠥἜ"))
          return
        time.sleep(1)
        bstack1111l1lllll_opy_ += 1
      os.environ[bstack1l1l11_opy_ (u"࠭ࡐࡆࡔࡆ࡝ࡤࡈࡅࡔࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࠬἝ")] = str(self.bstack11111l11lll_opy_())
      self.logger.info(bstack1l1l11_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡳࡦࡶࡸࡴࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠣ἞"))
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤ἟").format(e))
  def bstack11111l11lll_opy_(self):
    if self.bstack1lllll11l_opy_:
      return
    try:
      bstack1111l111l1l_opy_ = [platform[bstack1l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧἠ")].lower() for platform in self.config.get(bstack1l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ἡ"), [])]
      bstack1111l11l1l1_opy_ = sys.maxsize
      bstack111111llll1_opy_ = bstack1l1l11_opy_ (u"ࠫࠬἢ")
      for browser in bstack1111l111l1l_opy_:
        if browser in self.bstack11111lll1l1_opy_:
          bstack11111lllll1_opy_ = self.bstack11111lll1l1_opy_[browser]
        if bstack11111lllll1_opy_ < bstack1111l11l1l1_opy_:
          bstack1111l11l1l1_opy_ = bstack11111lllll1_opy_
          bstack111111llll1_opy_ = browser
      return bstack111111llll1_opy_
    except Exception as e:
      self.logger.error(bstack1l1l11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡢࡦࡵࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨἣ").format(e))
  @classmethod
  def bstack1llll11lll_opy_(self):
    return os.getenv(bstack1l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫἤ"), bstack1l1l11_opy_ (u"ࠧࡇࡣ࡯ࡷࡪ࠭ἥ")).lower()
  @classmethod
  def bstack1l11lll1l1_opy_(self):
    return os.getenv(bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬἦ"), bstack1l1l11_opy_ (u"ࠩࠪἧ"))
  @classmethod
  def bstack1l1l1l111l1_opy_(cls, value):
    cls.bstack1ll111l11_opy_ = value
  @classmethod
  def bstack1111l1l11ll_opy_(cls):
    return cls.bstack1ll111l11_opy_
  @classmethod
  def bstack1l1l1l11111_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack11111lll111_opy_(cls):
    return cls.percy_build_id