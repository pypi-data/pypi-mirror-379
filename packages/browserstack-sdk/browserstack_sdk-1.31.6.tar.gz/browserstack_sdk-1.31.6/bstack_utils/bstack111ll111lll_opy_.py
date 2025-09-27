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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l11l1l111_opy_
from browserstack_sdk.bstack1l11lllll_opy_ import bstack11ll111lll_opy_
def _111ll111l11_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack111ll111ll1_opy_:
    def __init__(self, handler):
        self._111l1llll1l_opy_ = {}
        self._111l1llllll_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack11ll111lll_opy_.version()
        if bstack11l11l1l111_opy_(pytest_version, bstack1l1l11_opy_ (u"ࠦ࠽࠴࠱࠯࠳ࠥᵾ")) >= 0:
            self._111l1llll1l_opy_[bstack1l1l11_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᵿ")] = Module._register_setup_function_fixture
            self._111l1llll1l_opy_[bstack1l1l11_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᶀ")] = Module._register_setup_module_fixture
            self._111l1llll1l_opy_[bstack1l1l11_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᶁ")] = Class._register_setup_class_fixture
            self._111l1llll1l_opy_[bstack1l1l11_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᶂ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack111ll11l1l1_opy_(bstack1l1l11_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᶃ"))
            Module._register_setup_module_fixture = self.bstack111ll11l1l1_opy_(bstack1l1l11_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᶄ"))
            Class._register_setup_class_fixture = self.bstack111ll11l1l1_opy_(bstack1l1l11_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᶅ"))
            Class._register_setup_method_fixture = self.bstack111ll11l1l1_opy_(bstack1l1l11_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᶆ"))
        else:
            self._111l1llll1l_opy_[bstack1l1l11_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᶇ")] = Module._inject_setup_function_fixture
            self._111l1llll1l_opy_[bstack1l1l11_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᶈ")] = Module._inject_setup_module_fixture
            self._111l1llll1l_opy_[bstack1l1l11_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᶉ")] = Class._inject_setup_class_fixture
            self._111l1llll1l_opy_[bstack1l1l11_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᶊ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack111ll11l1l1_opy_(bstack1l1l11_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᶋ"))
            Module._inject_setup_module_fixture = self.bstack111ll11l1l1_opy_(bstack1l1l11_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᶌ"))
            Class._inject_setup_class_fixture = self.bstack111ll11l1l1_opy_(bstack1l1l11_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᶍ"))
            Class._inject_setup_method_fixture = self.bstack111ll11l1l1_opy_(bstack1l1l11_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᶎ"))
    def bstack111ll111111_opy_(self, bstack111ll11l11l_opy_, hook_type):
        bstack111ll111l1l_opy_ = id(bstack111ll11l11l_opy_.__class__)
        if (bstack111ll111l1l_opy_, hook_type) in self._111l1llllll_opy_:
            return
        meth = getattr(bstack111ll11l11l_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._111l1llllll_opy_[(bstack111ll111l1l_opy_, hook_type)] = meth
            setattr(bstack111ll11l11l_opy_, hook_type, self.bstack111l1lll1ll_opy_(hook_type, bstack111ll111l1l_opy_))
    def bstack111l1lllll1_opy_(self, instance, bstack111ll11111l_opy_):
        if bstack111ll11111l_opy_ == bstack1l1l11_opy_ (u"ࠢࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠥᶏ"):
            self.bstack111ll111111_opy_(instance.obj, bstack1l1l11_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤᶐ"))
            self.bstack111ll111111_opy_(instance.obj, bstack1l1l11_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨᶑ"))
        if bstack111ll11111l_opy_ == bstack1l1l11_opy_ (u"ࠥࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠦᶒ"):
            self.bstack111ll111111_opy_(instance.obj, bstack1l1l11_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠥᶓ"))
            self.bstack111ll111111_opy_(instance.obj, bstack1l1l11_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠢᶔ"))
        if bstack111ll11111l_opy_ == bstack1l1l11_opy_ (u"ࠨࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪࠨᶕ"):
            self.bstack111ll111111_opy_(instance.obj, bstack1l1l11_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠧᶖ"))
            self.bstack111ll111111_opy_(instance.obj, bstack1l1l11_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠤᶗ"))
        if bstack111ll11111l_opy_ == bstack1l1l11_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠥᶘ"):
            self.bstack111ll111111_opy_(instance.obj, bstack1l1l11_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠤᶙ"))
            self.bstack111ll111111_opy_(instance.obj, bstack1l1l11_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩࠨᶚ"))
    @staticmethod
    def bstack111ll1111ll_opy_(hook_type, func, args):
        if hook_type in [bstack1l1l11_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫᶛ"), bstack1l1l11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨᶜ")]:
            _111ll111l11_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack111l1lll1ll_opy_(self, hook_type, bstack111ll111l1l_opy_):
        def bstack111ll11l111_opy_(arg=None):
            self.handler(hook_type, bstack1l1l11_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧᶝ"))
            result = None
            try:
                bstack1lllllll1ll_opy_ = self._111l1llllll_opy_[(bstack111ll111l1l_opy_, hook_type)]
                self.bstack111ll1111ll_opy_(hook_type, bstack1lllllll1ll_opy_, (arg,))
                result = Result(result=bstack1l1l11_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᶞ"))
            except Exception as e:
                result = Result(result=bstack1l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᶟ"), exception=e)
                self.handler(hook_type, bstack1l1l11_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩᶠ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1l11_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪᶡ"), result)
        def bstack111l1llll11_opy_(this, arg=None):
            self.handler(hook_type, bstack1l1l11_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬᶢ"))
            result = None
            exception = None
            try:
                self.bstack111ll1111ll_opy_(hook_type, self._111l1llllll_opy_[hook_type], (this, arg))
                result = Result(result=bstack1l1l11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᶣ"))
            except Exception as e:
                result = Result(result=bstack1l1l11_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᶤ"), exception=e)
                self.handler(hook_type, bstack1l1l11_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧᶥ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1l11_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨᶦ"), result)
        if hook_type in [bstack1l1l11_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩᶧ"), bstack1l1l11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᶨ")]:
            return bstack111l1llll11_opy_
        return bstack111ll11l111_opy_
    def bstack111ll11l1l1_opy_(self, bstack111ll11111l_opy_):
        def bstack111ll1111l1_opy_(this, *args, **kwargs):
            self.bstack111l1lllll1_opy_(this, bstack111ll11111l_opy_)
            self._111l1llll1l_opy_[bstack111ll11111l_opy_](this, *args, **kwargs)
        return bstack111ll1111l1_opy_