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
class RobotHandler():
    def __init__(self, args, logger, bstack1111l1l1l1_opy_, bstack1111l1l1ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l1l1l1_opy_ = bstack1111l1l1l1_opy_
        self.bstack1111l1l1ll_opy_ = bstack1111l1l1ll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1111ll11ll_opy_(bstack111111l111_opy_):
        bstack1111111lll_opy_ = []
        if bstack111111l111_opy_:
            tokens = str(os.path.basename(bstack111111l111_opy_)).split(bstack1l1l11_opy_ (u"ࠨ࡟ࠣ႑"))
            camelcase_name = bstack1l1l11_opy_ (u"ࠢࠡࠤ႒").join(t.title() for t in tokens)
            suite_name, bstack111111l1l1_opy_ = os.path.splitext(camelcase_name)
            bstack1111111lll_opy_.append(suite_name)
        return bstack1111111lll_opy_
    @staticmethod
    def bstack111111l11l_opy_(typename):
        if bstack1l1l11_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦ႓") in typename:
            return bstack1l1l11_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥ႔")
        return bstack1l1l11_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦ႕")