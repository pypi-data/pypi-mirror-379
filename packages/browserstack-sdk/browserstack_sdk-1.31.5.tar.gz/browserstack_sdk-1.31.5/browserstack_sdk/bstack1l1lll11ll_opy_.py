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
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1ll11lll1l_opy_():
  def __init__(self, args, logger, bstack1111l11l11_opy_, bstack1111l111ll_opy_, bstack111111ll11_opy_):
    self.args = args
    self.logger = logger
    self.bstack1111l11l11_opy_ = bstack1111l11l11_opy_
    self.bstack1111l111ll_opy_ = bstack1111l111ll_opy_
    self.bstack111111ll11_opy_ = bstack111111ll11_opy_
  def bstack1ll111ll11_opy_(self, bstack11111lll1l_opy_, bstack11l1111111_opy_, bstack111111l1ll_opy_=False):
    bstack1llll1ll1l_opy_ = []
    manager = multiprocessing.Manager()
    bstack1111l1l1l1_opy_ = manager.list()
    bstack11ll1111ll_opy_ = Config.bstack1lllll1ll1_opy_()
    if bstack111111l1ll_opy_:
      for index, platform in enumerate(self.bstack1111l11l11_opy_[bstack1l11l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩႊ")]):
        if index == 0:
          bstack11l1111111_opy_[bstack1l11l11_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪႋ")] = self.args
        bstack1llll1ll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111lll1l_opy_,
                                                    args=(bstack11l1111111_opy_, bstack1111l1l1l1_opy_)))
    else:
      for index, platform in enumerate(self.bstack1111l11l11_opy_[bstack1l11l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫႌ")]):
        bstack1llll1ll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111lll1l_opy_,
                                                    args=(bstack11l1111111_opy_, bstack1111l1l1l1_opy_)))
    i = 0
    for t in bstack1llll1ll1l_opy_:
      try:
        if bstack11ll1111ll_opy_.get_property(bstack1l11l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰႍࠪ")):
          os.environ[bstack1l11l11_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫႎ")] = json.dumps(self.bstack1111l11l11_opy_[bstack1l11l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧႏ")][i % self.bstack111111ll11_opy_])
      except Exception as e:
        self.logger.debug(bstack1l11l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡧࡷࡥ࡮ࡲࡳ࠻ࠢࡾࢁࠧ႐").format(str(e)))
      i += 1
      t.start()
    for t in bstack1llll1ll1l_opy_:
      t.join()
    return list(bstack1111l1l1l1_opy_)