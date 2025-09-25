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
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1lll1l1ll1_opy_
import subprocess
from browserstack_sdk.bstack1l11l11l11_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1ll1llllll_opy_
from bstack_utils.bstack1l1l1l111_opy_ import bstack1l111lll_opy_
from bstack_utils.constants import bstack1111l1l11l_opy_
from bstack_utils.bstack111l11ll1_opy_ import bstack11lll11l11_opy_
class bstack1lll1ll1ll_opy_:
    def __init__(self, args, logger, bstack1111l11l11_opy_, bstack1111l111ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l11l11_opy_ = bstack1111l11l11_opy_
        self.bstack1111l111ll_opy_ = bstack1111l111ll_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1llllll1ll_opy_ = []
        self.bstack1111l1l1ll_opy_ = None
        self.bstack1ll111ll_opy_ = []
        self.bstack11111ll11l_opy_ = self.bstack1lll111lll_opy_()
        self.bstack1ll111ll1l_opy_ = -1
    def bstack11l1111111_opy_(self, bstack111111ll1l_opy_):
        self.parse_args()
        self.bstack11111llll1_opy_()
        self.bstack1111l1l111_opy_(bstack111111ll1l_opy_)
        self.bstack1111l11ll1_opy_()
    def bstack111l11lll_opy_(self):
        bstack111l11ll1_opy_ = bstack11lll11l11_opy_.bstack1lllll1ll1_opy_(self.bstack1111l11l11_opy_, self.logger)
        if bstack111l11ll1_opy_ is None:
            self.logger.warn(bstack1l11l11_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡲࡩࡲࡥࡳࠢ࡬ࡷࠥࡴ࡯ࡵࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡪ࠮ࠡࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦၔ"))
            return
        bstack11111l1l1l_opy_ = False
        bstack111l11ll1_opy_.bstack1111l1111l_opy_(bstack1l11l11_opy_ (u"ࠤࡨࡲࡦࡨ࡬ࡦࡦࠥၕ"), bstack111l11ll1_opy_.bstack111111ll_opy_())
        start_time = time.time()
        if bstack111l11ll1_opy_.bstack111111ll_opy_():
            test_files = self.bstack11111ll111_opy_()
            bstack11111l1l1l_opy_ = True
            bstack1111l111l1_opy_ = bstack111l11ll1_opy_.bstack11111lllll_opy_(test_files)
            if bstack1111l111l1_opy_:
                self.bstack1llllll1ll_opy_ = [os.path.normpath(item).replace(bstack1l11l11_opy_ (u"ࠪࡠࡡ࠭ၖ"), bstack1l11l11_opy_ (u"ࠫ࠴࠭ၗ")) for item in bstack1111l111l1_opy_]
                self.__1111l11111_opy_()
                bstack111l11ll1_opy_.bstack111111llll_opy_(bstack11111l1l1l_opy_)
                self.logger.info(bstack1l11l11_opy_ (u"࡚ࠧࡥࡴࡶࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡶࡵ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥၘ").format(self.bstack1llllll1ll_opy_))
            else:
                self.logger.info(bstack1l11l11_opy_ (u"ࠨࡎࡰࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡦࡴࡨࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡣࡻࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦၙ"))
        bstack111l11ll1_opy_.bstack1111l1111l_opy_(bstack1l11l11_opy_ (u"ࠢࡵ࡫ࡰࡩ࡙ࡧ࡫ࡦࡰࡗࡳࡆࡶࡰ࡭ࡻࠥၚ"), int((time.time() - start_time) * 1000)) # bstack11111l1l11_opy_ to bstack11111l1ll1_opy_
    def __1111l11111_opy_(self):
        bstack1l11l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡱ࡮ࡤࡧࡪࠦࡡ࡭࡮ࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࠦࡡࡳࡩࡸࡱࡪࡴࡴࡴࠢ࡬ࡲࠥࡹࡥ࡭ࡨ࠱ࡥࡷ࡭ࡳࠡࡹ࡬ࡸ࡭ࠦࡳࡦ࡮ࡩ࠲ࡸࡶࡥࡤࡡࡩ࡭ࡱ࡫ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡓࡳࡲࡹࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡷࡪ࡮࡯ࠤࡧ࡫ࠠࡳࡷࡱ࠿ࠥࡧ࡬࡭ࠢࡲࡸ࡭࡫ࡲࠡࡅࡏࡍࠥ࡬࡬ࡢࡩࡶࠤࡦࡸࡥࠡࡲࡵࡩࡸ࡫ࡲࡷࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤၛ")
        bstack11111l111l_opy_ = [arg for arg in self.args if not (arg.endswith(bstack1l11l11_opy_ (u"ࠩ࠱ࡴࡾ࠭ၜ")) and os.path.exists(arg))]
        self.args = self.bstack1llllll1ll_opy_ + bstack11111l111l_opy_
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack11111l11l1_opy_():
        import importlib
        if getattr(importlib, bstack1l11l11_opy_ (u"ࠪࡪ࡮ࡴࡤࡠ࡮ࡲࡥࡩ࡫ࡲࠨၝ"), False):
            bstack11111l1lll_opy_ = importlib.find_loader(bstack1l11l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ၞ"))
        else:
            bstack11111l1lll_opy_ = importlib.util.find_spec(bstack1l11l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧၟ"))
    def bstack1111l11lll_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1ll111ll1l_opy_ = -1
        if self.bstack1111l111ll_opy_ and bstack1l11l11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၠ") in self.bstack1111l11l11_opy_:
            self.bstack1ll111ll1l_opy_ = int(self.bstack1111l11l11_opy_[bstack1l11l11_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧၡ")])
        try:
            bstack11111l1111_opy_ = [bstack1l11l11_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪၢ"), bstack1l11l11_opy_ (u"ࠩ࠰࠱ࡵࡲࡵࡨ࡫ࡱࡷࠬၣ"), bstack1l11l11_opy_ (u"ࠪ࠱ࡵ࠭ၤ")]
            if self.bstack1ll111ll1l_opy_ >= 0:
                bstack11111l1111_opy_.extend([bstack1l11l11_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬၥ"), bstack1l11l11_opy_ (u"ࠬ࠳࡮ࠨၦ")])
            for arg in bstack11111l1111_opy_:
                self.bstack1111l11lll_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11111llll1_opy_(self):
        bstack1111l1l1ll_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1111l1l1ll_opy_ = bstack1111l1l1ll_opy_
        return bstack1111l1l1ll_opy_
    def bstack11l11l111_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack11111l11l1_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1ll1llllll_opy_)
    def bstack1111l1l111_opy_(self, bstack111111ll1l_opy_):
        bstack11ll1111ll_opy_ = Config.bstack1lllll1ll1_opy_()
        if bstack111111ll1l_opy_:
            self.bstack1111l1l1ll_opy_.append(bstack1l11l11_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪၧ"))
            self.bstack1111l1l1ll_opy_.append(bstack1l11l11_opy_ (u"ࠧࡕࡴࡸࡩࠬၨ"))
        if bstack11ll1111ll_opy_.bstack11111ll1ll_opy_():
            self.bstack1111l1l1ll_opy_.append(bstack1l11l11_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧၩ"))
            self.bstack1111l1l1ll_opy_.append(bstack1l11l11_opy_ (u"ࠩࡗࡶࡺ࡫ࠧၪ"))
        self.bstack1111l1l1ll_opy_.append(bstack1l11l11_opy_ (u"ࠪ࠱ࡵ࠭ၫ"))
        self.bstack1111l1l1ll_opy_.append(bstack1l11l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠩၬ"))
        self.bstack1111l1l1ll_opy_.append(bstack1l11l11_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠧၭ"))
        self.bstack1111l1l1ll_opy_.append(bstack1l11l11_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ၮ"))
        if self.bstack1ll111ll1l_opy_ > 1:
            self.bstack1111l1l1ll_opy_.append(bstack1l11l11_opy_ (u"ࠧ࠮ࡰࠪၯ"))
            self.bstack1111l1l1ll_opy_.append(str(self.bstack1ll111ll1l_opy_))
    def bstack1111l11ll1_opy_(self):
        if bstack1l111lll_opy_.bstack1lllllll11_opy_(self.bstack1111l11l11_opy_):
             self.bstack1111l1l1ll_opy_ += [
                bstack1111l1l11l_opy_.get(bstack1l11l11_opy_ (u"ࠨࡴࡨࡶࡺࡴࠧၰ")), str(bstack1l111lll_opy_.bstack1ll11lllll_opy_(self.bstack1111l11l11_opy_)),
                bstack1111l1l11l_opy_.get(bstack1l11l11_opy_ (u"ࠩࡧࡩࡱࡧࡹࠨၱ")), str(bstack1111l1l11l_opy_.get(bstack1l11l11_opy_ (u"ࠪࡶࡪࡸࡵ࡯࠯ࡧࡩࡱࡧࡹࠨၲ")))
            ]
    def bstack11111l11ll_opy_(self):
        bstack1ll111ll_opy_ = []
        for spec in self.bstack1llllll1ll_opy_:
            bstack1l1111llll_opy_ = [spec]
            bstack1l1111llll_opy_ += self.bstack1111l1l1ll_opy_
            bstack1ll111ll_opy_.append(bstack1l1111llll_opy_)
        self.bstack1ll111ll_opy_ = bstack1ll111ll_opy_
        return bstack1ll111ll_opy_
    def bstack1lll111lll_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack11111ll11l_opy_ = True
            return True
        except Exception as e:
            self.bstack11111ll11l_opy_ = False
        return self.bstack11111ll11l_opy_
    def bstack11ll1lllll_opy_(self):
        bstack1l11l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡍࡥࡵࠢࡷ࡬ࡪࠦࡣࡰࡷࡱࡸࠥࡵࡦࠡࡶࡨࡷࡹࡹࠠࡸ࡫ࡷ࡬ࡴࡻࡴࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡷ࡬ࡪࡳࠠࡶࡵ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹ࠭ࡳࠡ࠯࠰ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡴࡴ࡬ࡺࠢࡩࡰࡦ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡭ࡳࡺ࠺ࠡࡖ࡫ࡩࠥࡺ࡯ࡵࡣ࡯ࠤࡳࡻ࡭ࡣࡧࡵࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࡣࡰ࡮࡯ࡩࡨࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢၳ")
        try:
            self.logger.info(bstack1l11l11_opy_ (u"ࠧࡉ࡯࡭࡮ࡨࡧࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠠ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠣၴ"))
            bstack111111lll1_opy_ = [bstack1l11l11_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨၵ"), *self.bstack1111l1l1ll_opy_, bstack1l11l11_opy_ (u"ࠢ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠣၶ")]
            result = subprocess.run(bstack111111lll1_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                self.logger.error(bstack1l11l11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡣࡰ࡮࡯ࡩࡨࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨၷ").format(result.stderr))
                return 0
            test_count = result.stdout.count(bstack1l11l11_opy_ (u"ࠤ࠿ࡊࡺࡴࡣࡵ࡫ࡲࡲࠥࠨၸ"))
            self.logger.info(bstack1l11l11_opy_ (u"ࠥࡘࡴࡺࡡ࡭ࠢࡷࡩࡸࡺࡳࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧ࠾ࠥࢁࡽࠣၹ").format(test_count))
            return test_count
        except Exception as e:
            self.logger.error(bstack1l11l11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡯ࡶࡰࡷ࠾ࠥࢁࡽࠣၺ").format(e))
            return 0
    def bstack1ll111ll11_opy_(self, bstack11111lll1l_opy_, bstack11l1111111_opy_):
        bstack11l1111111_opy_[bstack1l11l11_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬၻ")] = self.bstack1111l11l11_opy_
        multiprocessing.set_start_method(bstack1l11l11_opy_ (u"࠭ࡳࡱࡣࡺࡲࠬၼ"))
        bstack1llll1ll1l_opy_ = []
        manager = multiprocessing.Manager()
        bstack1111l1l1l1_opy_ = manager.list()
        if bstack1l11l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪၽ") in self.bstack1111l11l11_opy_:
            for index, platform in enumerate(self.bstack1111l11l11_opy_[bstack1l11l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫၾ")]):
                bstack1llll1ll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack11111lll1l_opy_,
                                                            args=(self.bstack1111l1l1ll_opy_, bstack11l1111111_opy_, bstack1111l1l1l1_opy_)))
            bstack11111ll1l1_opy_ = len(self.bstack1111l11l11_opy_[bstack1l11l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬၿ")])
        else:
            bstack1llll1ll1l_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack11111lll1l_opy_,
                                                        args=(self.bstack1111l1l1ll_opy_, bstack11l1111111_opy_, bstack1111l1l1l1_opy_)))
            bstack11111ll1l1_opy_ = 1
        i = 0
        for t in bstack1llll1ll1l_opy_:
            os.environ[bstack1l11l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪႀ")] = str(i)
            if bstack1l11l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧႁ") in self.bstack1111l11l11_opy_:
                os.environ[bstack1l11l11_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭ႂ")] = json.dumps(self.bstack1111l11l11_opy_[bstack1l11l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩႃ")][i % bstack11111ll1l1_opy_])
            i += 1
            t.start()
        for t in bstack1llll1ll1l_opy_:
            t.join()
        return list(bstack1111l1l1l1_opy_)
    @staticmethod
    def bstack11ll11ll1_opy_(driver, bstack11111lll11_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1l11l11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫႄ"), None)
        if item and getattr(item, bstack1l11l11_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࠪႅ"), None) and not getattr(item, bstack1l11l11_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡳࡵࡥࡤࡰࡰࡨࠫႆ"), False):
            logger.info(
                bstack1l11l11_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠤႇ"))
            bstack1111l11l1l_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1lll1l1ll1_opy_.bstack11llll11l1_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack11111ll111_opy_(self):
        bstack1l11l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡹࡵࠠࡣࡧࠣࡩࡽ࡫ࡣࡶࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥႈ")
        test_files = []
        for arg in self.args:
            if arg.endswith(bstack1l11l11_opy_ (u"ࠬ࠴ࡰࡺࠩႉ")) and os.path.exists(arg):
                test_files.append(arg)
        return test_files