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
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11lll1llll_opy_ import get_logger
from bstack_utils.bstack111l11ll_opy_ import bstack1lll111lll1_opy_
bstack111l11ll_opy_ = bstack1lll111lll1_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1l11l111l1_opy_: Optional[str] = None):
    bstack1l1l11_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡇࡩࡨࡵࡲࡢࡶࡲࡶࠥࡺ࡯ࠡ࡮ࡲ࡫ࠥࡺࡨࡦࠢࡶࡸࡦࡸࡴࠡࡶ࡬ࡱࡪࠦ࡯ࡧࠢࡤࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࡡ࡭ࡱࡱ࡫ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࠢࡱࡥࡲ࡫ࠠࡢࡰࡧࠤࡸࡺࡡࡨࡧ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᷬ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll11ll11l1_opy_: str = bstack111l11ll_opy_.bstack11ll1l11ll1_opy_(label)
            start_mark: str = label + bstack1l1l11_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᷭ")
            end_mark: str = label + bstack1l1l11_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᷮ")
            result = None
            try:
                if stage.value == STAGE.bstack1l1l1lll_opy_.value:
                    bstack111l11ll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack111l11ll_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1l11l111l1_opy_)
                elif stage.value == STAGE.bstack1ll11lll_opy_.value:
                    start_mark: str = bstack1ll11ll11l1_opy_ + bstack1l1l11_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᷯ")
                    end_mark: str = bstack1ll11ll11l1_opy_ + bstack1l1l11_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᷰ")
                    bstack111l11ll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack111l11ll_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1l11l111l1_opy_)
            except Exception as e:
                bstack111l11ll_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1l11l111l1_opy_)
            return result
        return wrapper
    return decorator