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
class RobotHandler():
    def __init__(self, args, logger, bstack1111l11l11_opy_, bstack1111l111ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l11l11_opy_ = bstack1111l11l11_opy_
        self.bstack1111l111ll_opy_ = bstack1111l111ll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack111l11111l_opy_(bstack111111l1l1_opy_):
        bstack111111l111_opy_ = []
        if bstack111111l1l1_opy_:
            tokens = str(os.path.basename(bstack111111l1l1_opy_)).split(bstack1l11l11_opy_ (u"ࠨ࡟ࠣ႑"))
            camelcase_name = bstack1l11l11_opy_ (u"ࠢࠡࠤ႒").join(t.title() for t in tokens)
            suite_name, bstack1111111lll_opy_ = os.path.splitext(camelcase_name)
            bstack111111l111_opy_.append(suite_name)
        return bstack111111l111_opy_
    @staticmethod
    def bstack111111l11l_opy_(typename):
        if bstack1l11l11_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦ႓") in typename:
            return bstack1l11l11_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥ႔")
        return bstack1l11l11_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦ႕")