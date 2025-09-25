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
class bstack1ll1l1lll_opy_:
    def __init__(self, handler):
        self._1lllll1lll11_opy_ = None
        self.handler = handler
        self._1lllll1lll1l_opy_ = self.bstack1lllll1ll1l1_opy_()
        self.patch()
    def patch(self):
        self._1lllll1lll11_opy_ = self._1lllll1lll1l_opy_.execute
        self._1lllll1lll1l_opy_.execute = self.bstack1lllll1ll1ll_opy_()
    def bstack1lllll1ll1ll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1l11l11_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤΎ"), driver_command, None, this, args)
            response = self._1lllll1lll11_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1l11l11_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤῬ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1lllll1lll1l_opy_.execute = self._1lllll1lll11_opy_
    @staticmethod
    def bstack1lllll1ll1l1_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver