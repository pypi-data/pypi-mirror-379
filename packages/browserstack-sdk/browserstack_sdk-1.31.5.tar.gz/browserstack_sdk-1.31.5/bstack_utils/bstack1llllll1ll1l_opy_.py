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
import threading
import logging
logger = logging.getLogger(__name__)
bstack1llllll1ll11_opy_ = 1000
bstack1llllll1llll_opy_ = 2
class bstack1llllll1l11l_opy_:
    def __init__(self, handler, bstack1llllll11lll_opy_=bstack1llllll1ll11_opy_, bstack1llllll1l111_opy_=bstack1llllll1llll_opy_):
        self.queue = []
        self.handler = handler
        self.bstack1llllll11lll_opy_ = bstack1llllll11lll_opy_
        self.bstack1llllll1l111_opy_ = bstack1llllll1l111_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack1111111ll1_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack1llllll1l1l1_opy_()
    def bstack1llllll1l1l1_opy_(self):
        self.bstack1111111ll1_opy_ = threading.Event()
        def bstack1llllll1l1ll_opy_():
            self.bstack1111111ll1_opy_.wait(self.bstack1llllll1l111_opy_)
            if not self.bstack1111111ll1_opy_.is_set():
                self.bstack1lllllll1111_opy_()
        self.timer = threading.Thread(target=bstack1llllll1l1ll_opy_, daemon=True)
        self.timer.start()
    def bstack1lllllll111l_opy_(self):
        try:
            if self.bstack1111111ll1_opy_ and not self.bstack1111111ll1_opy_.is_set():
                self.bstack1111111ll1_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack1l11l11_opy_ (u"࡛࠭ࡴࡶࡲࡴࡤࡺࡩ࡮ࡧࡵࡡࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࠪᾛ") + (str(e) or bstack1l11l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡧࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡦࡳࡳࡼࡥࡳࡶࡨࡨࠥࡺ࡯ࠡࡵࡷࡶ࡮ࡴࡧࠣᾜ")))
        finally:
            self.timer = None
    def bstack1llllll1lll1_opy_(self):
        if self.timer:
            self.bstack1lllllll111l_opy_()
        self.bstack1llllll1l1l1_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack1llllll11lll_opy_:
                threading.Thread(target=self.bstack1lllllll1111_opy_).start()
    def bstack1lllllll1111_opy_(self, source = bstack1l11l11_opy_ (u"ࠨࠩᾝ")):
        with self.lock:
            if not self.queue:
                self.bstack1llllll1lll1_opy_()
                return
            data = self.queue[:self.bstack1llllll11lll_opy_]
            del self.queue[:self.bstack1llllll11lll_opy_]
        self.handler(data)
        if source != bstack1l11l11_opy_ (u"ࠩࡶ࡬ࡺࡺࡤࡰࡹࡱࠫᾞ"):
            self.bstack1llllll1lll1_opy_()
    def shutdown(self):
        self.bstack1lllllll111l_opy_()
        while self.queue:
            self.bstack1lllllll1111_opy_(source=bstack1l11l11_opy_ (u"ࠪࡷ࡭ࡻࡴࡥࡱࡺࡲࠬᾟ"))