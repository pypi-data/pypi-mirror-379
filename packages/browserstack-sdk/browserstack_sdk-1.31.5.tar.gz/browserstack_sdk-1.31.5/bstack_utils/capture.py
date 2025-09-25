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
import builtins
import logging
class bstack111ll1l1ll_opy_:
    def __init__(self, handler):
        self._11ll1111ll1_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._11ll1111l11_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1l11l11_opy_ (u"࠭ࡩ࡯ࡨࡲࠫដ"), bstack1l11l11_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ឋ"), bstack1l11l11_opy_ (u"ࠨࡹࡤࡶࡳ࡯࡮ࡨࠩឌ"), bstack1l11l11_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨឍ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._11ll11111ll_opy_
        self._11ll1111l1l_opy_()
    def _11ll11111ll_opy_(self, *args, **kwargs):
        self._11ll1111ll1_opy_(*args, **kwargs)
        message = bstack1l11l11_opy_ (u"ࠪࠤࠬណ").join(map(str, args)) + bstack1l11l11_opy_ (u"ࠫࡡࡴࠧត")
        self._log_message(bstack1l11l11_opy_ (u"ࠬࡏࡎࡇࡑࠪថ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1l11l11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬទ"): level, bstack1l11l11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨធ"): msg})
    def _11ll1111l1l_opy_(self):
        for level, bstack11ll11111l1_opy_ in self._11ll1111l11_opy_.items():
            setattr(logging, level, self._11ll111111l_opy_(level, bstack11ll11111l1_opy_))
    def _11ll111111l_opy_(self, level, bstack11ll11111l1_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack11ll11111l1_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._11ll1111ll1_opy_
        for level, bstack11ll11111l1_opy_ in self._11ll1111l11_opy_.items():
            setattr(logging, level, bstack11ll11111l1_opy_)