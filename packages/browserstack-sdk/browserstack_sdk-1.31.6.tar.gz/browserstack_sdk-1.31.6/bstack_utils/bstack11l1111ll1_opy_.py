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
from bstack_utils.bstack11lll1llll_opy_ import get_logger
logger = get_logger(__name__)
class bstack11ll11l1ll1_opy_(object):
  bstack11ll1l1l11_opy_ = os.path.join(os.path.expanduser(bstack1l1l11_opy_ (u"ࠪࢂࠬ᝖")), bstack1l1l11_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ᝗"))
  bstack11ll11l11ll_opy_ = os.path.join(bstack11ll1l1l11_opy_, bstack1l1l11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹ࠮࡫ࡵࡲࡲࠬ᝘"))
  commands_to_wrap = None
  perform_scan = None
  bstack1ll1l11ll_opy_ = None
  bstack1ll1l111ll_opy_ = None
  bstack11ll1l1111l_opy_ = None
  bstack11ll1l1lll1_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1l1l11_opy_ (u"࠭ࡩ࡯ࡵࡷࡥࡳࡩࡥࠨ᝙")):
      cls.instance = super(bstack11ll11l1ll1_opy_, cls).__new__(cls)
      cls.instance.bstack11ll11l11l1_opy_()
    return cls.instance
  def bstack11ll11l11l1_opy_(self):
    try:
      with open(self.bstack11ll11l11ll_opy_, bstack1l1l11_opy_ (u"ࠧࡳࠩ᝚")) as bstack11ll111l_opy_:
        bstack11ll11l1l1l_opy_ = bstack11ll111l_opy_.read()
        data = json.loads(bstack11ll11l1l1l_opy_)
        if bstack1l1l11_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪ᝛") in data:
          self.bstack11ll1ll1l1l_opy_(data[bstack1l1l11_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫ᝜")])
        if bstack1l1l11_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫ᝝") in data:
          self.bstack1ll11l11ll_opy_(data[bstack1l1l11_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬ᝞")])
        if bstack1l1l11_opy_ (u"ࠬࡴ࡯࡯ࡄࡖࡸࡦࡩ࡫ࡊࡰࡩࡶࡦࡇ࠱࠲ࡻࡆ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᝟") in data:
          self.bstack11ll11l1l11_opy_(data[bstack1l1l11_opy_ (u"࠭࡮ࡰࡰࡅࡗࡹࡧࡣ࡬ࡋࡱࡪࡷࡧࡁ࠲࠳ࡼࡇ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᝠ")])
    except:
      pass
  def bstack11ll11l1l11_opy_(self, bstack11ll1l1lll1_opy_):
    if bstack11ll1l1lll1_opy_ != None:
      self.bstack11ll1l1lll1_opy_ = bstack11ll1l1lll1_opy_
  def bstack1ll11l11ll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack1l1l11_opy_ (u"ࠧࡴࡥࡤࡲࠬᝡ"),bstack1l1l11_opy_ (u"ࠨࠩᝢ"))
      self.bstack1ll1l11ll_opy_ = scripts.get(bstack1l1l11_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࠭ᝣ"),bstack1l1l11_opy_ (u"ࠪࠫᝤ"))
      self.bstack1ll1l111ll_opy_ = scripts.get(bstack1l1l11_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨᝥ"),bstack1l1l11_opy_ (u"ࠬ࠭ᝦ"))
      self.bstack11ll1l1111l_opy_ = scripts.get(bstack1l1l11_opy_ (u"࠭ࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠫᝧ"),bstack1l1l11_opy_ (u"ࠧࠨᝨ"))
  def bstack11ll1ll1l1l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack11ll11l11ll_opy_, bstack1l1l11_opy_ (u"ࠨࡹࠪᝩ")) as file:
        json.dump({
          bstack1l1l11_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࠦᝪ"): self.commands_to_wrap,
          bstack1l1l11_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࡶࠦᝫ"): {
            bstack1l1l11_opy_ (u"ࠦࡸࡩࡡ࡯ࠤᝬ"): self.perform_scan,
            bstack1l1l11_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠤ᝭"): self.bstack1ll1l11ll_opy_,
            bstack1l1l11_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠥᝮ"): self.bstack1ll1l111ll_opy_,
            bstack1l1l11_opy_ (u"ࠢࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠧᝯ"): self.bstack11ll1l1111l_opy_
          },
          bstack1l1l11_opy_ (u"ࠣࡰࡲࡲࡇ࡙ࡴࡢࡥ࡮ࡍࡳ࡬ࡲࡢࡃ࠴࠵ࡾࡉࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠧᝰ"): self.bstack11ll1l1lll1_opy_
        }, file)
    except Exception as e:
      logger.error(bstack1l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡴࡶࡲࡶ࡮ࡴࡧࠡࡥࡲࡱࡲࡧ࡮ࡥࡵ࠽ࠤࢀࢃࠢ᝱").format(e))
      pass
  def bstack111l111ll_opy_(self, command_name):
    try:
      return any(command.get(bstack1l1l11_opy_ (u"ࠪࡲࡦࡳࡥࠨᝲ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack11l1111ll1_opy_ = bstack11ll11l1ll1_opy_()