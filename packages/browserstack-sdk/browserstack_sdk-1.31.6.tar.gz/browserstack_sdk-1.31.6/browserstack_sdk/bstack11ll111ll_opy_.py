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
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack111ll1llll_opy_ import bstack111ll1111l_opy_, bstack111l1llll1_opy_
from bstack_utils.bstack111lll11l1_opy_ import bstack1111111l1_opy_
from bstack_utils.helper import bstack1l11111lll_opy_, bstack11llll11_opy_, Result
from bstack_utils.bstack111l1lll11_opy_ import bstack1l1l1lll1l_opy_
from bstack_utils.capture import bstack111ll11l11_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11ll111ll_opy_:
    def __init__(self):
        self.bstack111ll1ll1l_opy_ = bstack111ll11l11_opy_(self.bstack111ll1l111_opy_)
        self.tests = {}
    @staticmethod
    def bstack111ll1l111_opy_(log):
        if not (log[bstack1l1l11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ༸")] and log[bstack1l1l11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ༹࠭")].strip()):
            return
        active = bstack1111111l1_opy_.bstack111ll1l1l1_opy_()
        log = {
            bstack1l1l11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ༺"): log[bstack1l1l11_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭༻")],
            bstack1l1l11_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ༼"): bstack11llll11_opy_(),
            bstack1l1l11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ༽"): log[bstack1l1l11_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ༾")],
        }
        if active:
            if active[bstack1l1l11_opy_ (u"ࠫࡹࡿࡰࡦࠩ༿")] == bstack1l1l11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪཀ"):
                log[bstack1l1l11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ཁ")] = active[bstack1l1l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧག")]
            elif active[bstack1l1l11_opy_ (u"ࠨࡶࡼࡴࡪ࠭གྷ")] == bstack1l1l11_opy_ (u"ࠩࡷࡩࡸࡺࠧང"):
                log[bstack1l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪཅ")] = active[bstack1l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫཆ")]
        bstack1l1l1lll1l_opy_.bstack1l111l111l_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack111ll1ll1l_opy_.start()
        driver = bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫཇ"), None)
        bstack111ll1llll_opy_ = bstack111l1llll1_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack11llll11_opy_(),
            file_path=attrs.feature.filename,
            result=bstack1l1l11_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢ཈"),
            framework=bstack1l1l11_opy_ (u"ࠧࡃࡧ࡫ࡥࡻ࡫ࠧཉ"),
            scope=[attrs.feature.name],
            bstack111lll111l_opy_=bstack1l1l1lll1l_opy_.bstack111lll1111_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack1l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫཊ")] = bstack111ll1llll_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1l1l1lll1l_opy_.bstack111l1lll1l_opy_(bstack1l1l11_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪཋ"), bstack111ll1llll_opy_)
    def end_test(self, attrs):
        bstack111l1lllll_opy_ = {
            bstack1l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣཌ"): attrs.feature.name,
            bstack1l1l11_opy_ (u"ࠦࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠤཌྷ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack111ll1llll_opy_ = self.tests[current_test_uuid][bstack1l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨཎ")]
        meta = {
            bstack1l1l11_opy_ (u"ࠨࡦࡦࡣࡷࡹࡷ࡫ࠢཏ"): bstack111l1lllll_opy_,
            bstack1l1l11_opy_ (u"ࠢࡴࡶࡨࡴࡸࠨཐ"): bstack111ll1llll_opy_.meta.get(bstack1l1l11_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧད"), []),
            bstack1l1l11_opy_ (u"ࠤࡶࡧࡪࡴࡡࡳ࡫ࡲࠦདྷ"): {
                bstack1l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣན"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack111ll1llll_opy_.bstack111ll111ll_opy_(meta)
        bstack111ll1llll_opy_.bstack111l1ll1ll_opy_(bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩཔ"), []))
        bstack111ll11ll1_opy_, exception = self._111ll111l1_opy_(attrs)
        bstack111ll11111_opy_ = Result(result=attrs.status.name, exception=exception, bstack111ll1lll1_opy_=[bstack111ll11ll1_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack1l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨཕ")].stop(time=bstack11llll11_opy_(), duration=int(attrs.duration)*1000, result=bstack111ll11111_opy_)
        bstack1l1l1lll1l_opy_.bstack111l1lll1l_opy_(bstack1l1l11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨབ"), self.tests[threading.current_thread().current_test_uuid][bstack1l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪབྷ")])
    def bstack11lll11l11_opy_(self, attrs):
        bstack111ll1l11l_opy_ = {
            bstack1l1l11_opy_ (u"ࠨ࡫ࡧࠫམ"): uuid4().__str__(),
            bstack1l1l11_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪཙ"): attrs.keyword,
            bstack1l1l11_opy_ (u"ࠪࡷࡹ࡫ࡰࡠࡣࡵ࡫ࡺࡳࡥ࡯ࡶࠪཚ"): [],
            bstack1l1l11_opy_ (u"ࠫࡹ࡫ࡸࡵࠩཛ"): attrs.name,
            bstack1l1l11_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩཛྷ"): bstack11llll11_opy_(),
            bstack1l1l11_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ཝ"): bstack1l1l11_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨཞ"),
            bstack1l1l11_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ཟ"): bstack1l1l11_opy_ (u"ࠩࠪའ")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack1l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ཡ")].add_step(bstack111ll1l11l_opy_)
        threading.current_thread().current_step_uuid = bstack111ll1l11l_opy_[bstack1l1l11_opy_ (u"ࠫ࡮ࡪࠧར")]
    def bstack1l1l11ll_opy_(self, attrs):
        current_test_id = bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩལ"), None)
        current_step_uuid = bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡶࡨࡴࡤࡻࡵࡪࡦࠪཤ"), None)
        bstack111ll11ll1_opy_, exception = self._111ll111l1_opy_(attrs)
        bstack111ll11111_opy_ = Result(result=attrs.status.name, exception=exception, bstack111ll1lll1_opy_=[bstack111ll11ll1_opy_])
        self.tests[current_test_id][bstack1l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪཥ")].bstack111ll11lll_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack111ll11111_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack11lll1lll1_opy_(self, name, attrs):
        try:
            bstack111ll11l1l_opy_ = uuid4().__str__()
            self.tests[bstack111ll11l1l_opy_] = {}
            self.bstack111ll1ll1l_opy_.start()
            scopes = []
            driver = bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧས"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack1l1l11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹࠧཧ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack111ll11l1l_opy_)
            if name in [bstack1l1l11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢཨ"), bstack1l1l11_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠢཀྵ")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack1l1l11_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨཪ"), bstack1l1l11_opy_ (u"ࠨࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪࠨཫ")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack1l1l11_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨཬ")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack111ll1111l_opy_(
                name=name,
                uuid=bstack111ll11l1l_opy_,
                started_at=bstack11llll11_opy_(),
                file_path=file_path,
                framework=bstack1l1l11_opy_ (u"ࠣࡄࡨ࡬ࡦࡼࡥࠣ཭"),
                bstack111lll111l_opy_=bstack1l1l1lll1l_opy_.bstack111lll1111_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack1l1l11_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥ཮"),
                hook_type=name
            )
            self.tests[bstack111ll11l1l_opy_][bstack1l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡦࡤࡸࡦࠨ཯")] = hook_data
            current_test_id = bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠦࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠣ཰"), None)
            if current_test_id:
                hook_data.bstack111lll11ll_opy_(current_test_id)
            if name == bstack1l1l11_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤཱ"):
                threading.current_thread().before_all_hook_uuid = bstack111ll11l1l_opy_
            threading.current_thread().current_hook_uuid = bstack111ll11l1l_opy_
            bstack1l1l1lll1l_opy_.bstack111l1lll1l_opy_(bstack1l1l11_opy_ (u"ࠨࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪིࠢ"), hook_data)
        except Exception as e:
            logger.debug(bstack1l1l11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡ࡫ࡱࠤࡸࡺࡡࡳࡶࠣ࡬ࡴࡵ࡫ࠡࡧࡹࡩࡳࡺࡳ࠭ࠢ࡫ࡳࡴࡱࠠ࡯ࡣࡰࡩ࠿ࠦࠥࡴ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠩࡸࠨཱི"), name, e)
    def bstack1ll1l1l111_opy_(self, attrs):
        bstack111ll1l1ll_opy_ = bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨུࠬ"), None)
        hook_data = self.tests[bstack111ll1l1ll_opy_][bstack1l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥཱུࠬ")]
        status = bstack1l1l11_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥྲྀ")
        exception = None
        bstack111ll11ll1_opy_ = None
        if hook_data.name == bstack1l1l11_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠢཷ"):
            self.bstack111ll1ll1l_opy_.reset()
            bstack111ll1ll11_opy_ = self.tests[bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬླྀ"), None)][bstack1l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩཹ")].result.result
            if bstack111ll1ll11_opy_ == bstack1l1l11_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪེࠢ"):
                if attrs.hook_failures == 1:
                    status = bstack1l1l11_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤཻࠣ")
                elif attrs.hook_failures == 2:
                    status = bstack1l1l11_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤོ")
            elif attrs.aborted:
                status = bstack1l1l11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦཽࠥ")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack1l1l11_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠨཾ") and attrs.hook_failures == 1:
                status = bstack1l1l11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧཿ")
            elif hasattr(attrs, bstack1l1l11_opy_ (u"࠭ࡥࡳࡴࡲࡶࡤࡳࡥࡴࡵࡤ࡫ࡪྀ࠭")) and attrs.error_message:
                status = bstack1l1l11_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪཱྀࠢ")
            bstack111ll11ll1_opy_, exception = self._111ll111l1_opy_(attrs)
        bstack111ll11111_opy_ = Result(result=status, exception=exception, bstack111ll1lll1_opy_=[bstack111ll11ll1_opy_])
        hook_data.stop(time=bstack11llll11_opy_(), duration=0, result=bstack111ll11111_opy_)
        bstack1l1l1lll1l_opy_.bstack111l1lll1l_opy_(bstack1l1l11_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪྂ"), self.tests[bstack111ll1l1ll_opy_][bstack1l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬྃ")])
        threading.current_thread().current_hook_uuid = None
    def _111ll111l1_opy_(self, attrs):
        try:
            import traceback
            bstack1lll111ll1_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack111ll11ll1_opy_ = bstack1lll111ll1_opy_[-1] if bstack1lll111ll1_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack1l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡲࡧࡨࡻࡲࡳࡧࡧࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡨࡻࡳࡵࡱࡰࠤࡹࡸࡡࡤࡧࡥࡥࡨࡱ྄ࠢ"))
            bstack111ll11ll1_opy_ = None
            exception = None
        return bstack111ll11ll1_opy_, exception