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
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack11l1l11ll_opy_():
  def __init__(self, args, logger, bstack1111l1l1l1_opy_, bstack1111l1l1ll_opy_, bstack111111l1ll_opy_):
    self.args = args
    self.logger = logger
    self.bstack1111l1l1l1_opy_ = bstack1111l1l1l1_opy_
    self.bstack1111l1l1ll_opy_ = bstack1111l1l1ll_opy_
    self.bstack111111l1ll_opy_ = bstack111111l1ll_opy_
  def bstack11l11l11_opy_(self, bstack11111ll1l1_opy_, bstack1lll11lll1_opy_, bstack111111ll11_opy_=False):
    bstack1111ll11_opy_ = []
    manager = multiprocessing.Manager()
    bstack1111l1l11l_opy_ = manager.list()
    bstack1lll11l111_opy_ = Config.bstack1l11111l1l_opy_()
    if bstack111111ll11_opy_:
      for index, platform in enumerate(self.bstack1111l1l1l1_opy_[bstack1l1l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩႊ")]):
        if index == 0:
          bstack1lll11lll1_opy_[bstack1l1l11_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪႋ")] = self.args
        bstack1111ll11_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111ll1l1_opy_,
                                                    args=(bstack1lll11lll1_opy_, bstack1111l1l11l_opy_)))
    else:
      for index, platform in enumerate(self.bstack1111l1l1l1_opy_[bstack1l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫႌ")]):
        bstack1111ll11_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111ll1l1_opy_,
                                                    args=(bstack1lll11lll1_opy_, bstack1111l1l11l_opy_)))
    i = 0
    for t in bstack1111ll11_opy_:
      try:
        if bstack1lll11l111_opy_.get_property(bstack1l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰႍࠪ")):
          os.environ[bstack1l1l11_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫႎ")] = json.dumps(self.bstack1111l1l1l1_opy_[bstack1l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧႏ")][i % self.bstack111111l1ll_opy_])
      except Exception as e:
        self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡧࡷࡥ࡮ࡲࡳ࠻ࠢࡾࢁࠧ႐").format(str(e)))
      i += 1
      t.start()
    for t in bstack1111ll11_opy_:
      t.join()
    return list(bstack1111l1l11l_opy_)