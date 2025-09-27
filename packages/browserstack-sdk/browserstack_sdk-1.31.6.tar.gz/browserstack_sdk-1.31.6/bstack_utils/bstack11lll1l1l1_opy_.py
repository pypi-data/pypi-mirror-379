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
class bstack1ll1ll11ll_opy_:
    def __init__(self, handler):
        self._1lllll1ll1l1_opy_ = None
        self.handler = handler
        self._1lllll1lll1l_opy_ = self.bstack1lllll1ll1ll_opy_()
        self.patch()
    def patch(self):
        self._1lllll1ll1l1_opy_ = self._1lllll1lll1l_opy_.execute
        self._1lllll1lll1l_opy_.execute = self.bstack1lllll1lll11_opy_()
    def bstack1lllll1lll11_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1l1l11_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤΎ"), driver_command, None, this, args)
            response = self._1lllll1ll1l1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1l1l11_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤῬ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1lllll1lll1l_opy_.execute = self._1lllll1ll1l1_opy_
    @staticmethod
    def bstack1lllll1ll1ll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver