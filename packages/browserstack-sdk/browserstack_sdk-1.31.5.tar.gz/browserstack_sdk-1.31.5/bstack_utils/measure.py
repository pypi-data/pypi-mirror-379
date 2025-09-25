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
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1l1111ll1l_opy_ import get_logger
from bstack_utils.bstack1l1lllll1l_opy_ import bstack1lll11lll11_opy_
bstack1l1lllll1l_opy_ = bstack1lll11lll11_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1l1ll11l_opy_: Optional[str] = None):
    bstack1l11l11_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡇࡩࡨࡵࡲࡢࡶࡲࡶࠥࡺ࡯ࠡ࡮ࡲ࡫ࠥࡺࡨࡦࠢࡶࡸࡦࡸࡴࠡࡶ࡬ࡱࡪࠦ࡯ࡧࠢࡤࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࡡ࡭ࡱࡱ࡫ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࠢࡱࡥࡲ࡫ࠠࡢࡰࡧࠤࡸࡺࡡࡨࡧ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᷬ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll11lll1l1_opy_: str = bstack1l1lllll1l_opy_.bstack11ll1l1111l_opy_(label)
            start_mark: str = label + bstack1l11l11_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᷭ")
            end_mark: str = label + bstack1l11l11_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᷮ")
            result = None
            try:
                if stage.value == STAGE.bstack1lll11l1ll_opy_.value:
                    bstack1l1lllll1l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1l1lllll1l_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1l1ll11l_opy_)
                elif stage.value == STAGE.bstack1lll1111l_opy_.value:
                    start_mark: str = bstack1ll11lll1l1_opy_ + bstack1l11l11_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᷯ")
                    end_mark: str = bstack1ll11lll1l1_opy_ + bstack1l11l11_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᷰ")
                    bstack1l1lllll1l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1l1lllll1l_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1l1ll11l_opy_)
            except Exception as e:
                bstack1l1lllll1l_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1l1ll11l_opy_)
            return result
        return wrapper
    return decorator