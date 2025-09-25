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
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack111111111l_opy_ import bstack11111111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll11l_opy_ import bstack1llll1l1ll1_opy_, bstack1lllll11l11_opy_
class bstack1ll1ll11111_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1l11l11_opy_ (u"࡚ࠧࡥࡴࡶࡋࡳࡴࡱࡓࡵࡣࡷࡩ࠳ࢁࡽࠣᖻ").format(self.name)
class bstack1llll11ll11_opy_(Enum):
    NONE = 0
    BEFORE_ALL = 1
    LOG = 2
    SETUP_FIXTURE = 3
    INIT_TEST = 4
    BEFORE_EACH = 5
    AFTER_EACH = 6
    TEST = 7
    STEP = 8
    LOG_REPORT = 9
    AFTER_ALL = 10
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack1l11l11_opy_ (u"ࠨࡔࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡙ࡴࡢࡶࡨ࠲ࢀࢃࠢᖼ").format(self.name)
class bstack1ll1lllll11_opy_(bstack1llll1l1ll1_opy_):
    bstack1ll1111ll11_opy_: List[str]
    bstack11lllll1ll1_opy_: Dict[str, str]
    state: bstack1llll11ll11_opy_
    bstack1lllll111ll_opy_: datetime
    bstack1lllll1ll1l_opy_: datetime
    def __init__(
        self,
        context: bstack1lllll11l11_opy_,
        bstack1ll1111ll11_opy_: List[str],
        bstack11lllll1ll1_opy_: Dict[str, str],
        state=bstack1llll11ll11_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll1111ll11_opy_ = bstack1ll1111ll11_opy_
        self.bstack11lllll1ll1_opy_ = bstack11lllll1ll1_opy_
        self.state = state
        self.bstack1lllll111ll_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1lllll1ll1l_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllll1l1l1_opy_(self, bstack1llll1l11l1_opy_: bstack1llll11ll11_opy_):
        bstack1llll1l1l1l_opy_ = bstack1llll11ll11_opy_(bstack1llll1l11l1_opy_).name
        if not bstack1llll1l1l1l_opy_:
            return False
        if bstack1llll1l11l1_opy_ == self.state:
            return False
        self.state = bstack1llll1l11l1_opy_
        self.bstack1lllll1ll1l_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1l111l1ll1l_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1lll1llll1l_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1l1ll111l1l_opy_: int = None
    bstack1l1l1l11lll_opy_: str = None
    bstack1l1l1l1_opy_: str = None
    bstack1lll111ll1_opy_: str = None
    bstack1l1ll11ll11_opy_: str = None
    bstack11lllll1l11_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1ll111ll1ll_opy_ = bstack1l11l11_opy_ (u"ࠢࡵࡧࡶࡸࡤࡻࡵࡪࡦࠥᖽ")
    bstack1l11l111111_opy_ = bstack1l11l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡩࡥࠤᖾ")
    bstack1ll1111ll1l_opy_ = bstack1l11l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡯ࡣࡰࡩࠧᖿ")
    bstack1l1111lll11_opy_ = bstack1l11l11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡥࡰࡢࡶ࡫ࠦᗀ")
    bstack11lllll1lll_opy_ = bstack1l11l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡷࡥ࡬ࡹࠢᗁ")
    bstack1l11llll11l_opy_ = bstack1l11l11_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡪࡹࡵ࡭ࡶࠥᗂ")
    bstack1l1lll1ll11_opy_ = bstack1l11l11_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷ࡫ࡳࡶ࡮ࡷࡣࡦࡺࠢᗃ")
    bstack1l1l1l1l1ll_opy_ = bstack1l11l11_opy_ (u"ࠢࡵࡧࡶࡸࡤࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤᗄ")
    bstack1l1l1ll1111_opy_ = bstack1l11l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡥ࡯ࡦࡨࡨࡤࡧࡴࠣᗅ")
    bstack11lllllll11_opy_ = bstack1l11l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡭ࡱࡦࡥࡹ࡯࡯࡯ࠤᗆ")
    bstack1ll11l1l1ll_opy_ = bstack1l11l11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠤᗇ")
    bstack1l1l1ll1lll_opy_ = bstack1l11l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳࠨᗈ")
    bstack11lllll1l1l_opy_ = bstack1l11l11_opy_ (u"ࠧࡺࡥࡴࡶࡢࡧࡴࡪࡥࠣᗉ")
    bstack1l1l11lllll_opy_ = bstack1l11l11_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠣᗊ")
    bstack1ll11ll111l_opy_ = bstack1l11l11_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࠣᗋ")
    bstack1l11llll1ll_opy_ = bstack1l11l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡢ࡫࡯ࡹࡷ࡫ࠢᗌ")
    bstack1l11111l11l_opy_ = bstack1l11l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪࠨᗍ")
    bstack11lllll1111_opy_ = bstack1l11l11_opy_ (u"ࠥࡸࡪࡹࡴࡠ࡮ࡲ࡫ࡸࠨᗎ")
    bstack11lllll111l_opy_ = bstack1l11l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡰࡩࡹࡧࠢᗏ")
    bstack11llll1ll11_opy_ = bstack1l11l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡷࡨࡵࡰࡦࡵࠪᗐ")
    bstack1l11l1l11ll_opy_ = bstack1l11l11_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡱࡥࡲ࡫ࠢᗑ")
    bstack1l111ll1l11_opy_ = bstack1l11l11_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᗒ")
    bstack1l1111ll1l1_opy_ = bstack1l11l11_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟ࡦࡰࡧࡩࡩࡥࡡࡵࠤᗓ")
    bstack1l11l11111l_opy_ = bstack1l11l11_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟ࡪࡦࠥᗔ")
    bstack1l111ll11l1_opy_ = bstack1l11l11_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠࡴࡨࡷࡺࡲࡴࠣᗕ")
    bstack11lllll11ll_opy_ = bstack1l11l11_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡ࡯ࡳ࡬ࡹࠢᗖ")
    bstack1l111lll111_opy_ = bstack1l11l11_opy_ (u"ࠧ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠣᗗ")
    bstack1l1111ll1ll_opy_ = bstack1l11l11_opy_ (u"ࠨ࡬ࡰࡩࡶࠦᗘ")
    bstack1l111ll11ll_opy_ = bstack1l11l11_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳ࡟࡮ࡧࡷࡥࡩࡧࡴࡢࠤᗙ")
    bstack1l1111l1l1l_opy_ = bstack1l11l11_opy_ (u"ࠣࡲࡨࡲࡩ࡯࡮ࡨࠤᗚ")
    bstack1l1111ll111_opy_ = bstack1l11l11_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥᗛ")
    bstack1l1ll1lllll_opy_ = bstack1l11l11_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࠧᗜ")
    bstack1l1l1l1lll1_opy_ = bstack1l11l11_opy_ (u"࡙ࠦࡋࡓࡕࡡࡏࡓࡌࠨᗝ")
    bstack1l1l1l1ll1l_opy_ = bstack1l11l11_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᗞ")
    bstack1lllll1111l_opy_: Dict[str, bstack1ll1lllll11_opy_] = dict()
    bstack11llll111l1_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll1111ll11_opy_: List[str]
    bstack11lllll1ll1_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll1111ll11_opy_: List[str],
        bstack11lllll1ll1_opy_: Dict[str, str],
        bstack111111111l_opy_: bstack11111111l1_opy_
    ):
        self.bstack1ll1111ll11_opy_ = bstack1ll1111ll11_opy_
        self.bstack11lllll1ll1_opy_ = bstack11lllll1ll1_opy_
        self.bstack111111111l_opy_ = bstack111111111l_opy_
    def track_event(
        self,
        context: bstack1l111l1ll1l_opy_,
        test_framework_state: bstack1llll11ll11_opy_,
        test_hook_state: bstack1ll1ll11111_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack1l11l11_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡽࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠦࡡࡳࡩࡶࡁࢀࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼࡿࠥᗟ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1l1111l111l_opy_(
        self,
        instance: bstack1ll1lllll11_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_],
        *args,
        **kwargs,
    ):
        bstack1l11l111l11_opy_ = TestFramework.bstack1l11l11l11l_opy_(bstack1lllllll1l1_opy_)
        if not bstack1l11l111l11_opy_ in TestFramework.bstack11llll111l1_opy_:
            return
        self.logger.debug(bstack1l11l11_opy_ (u"ࠢࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡾࢁࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࡳࠣᗠ").format(len(TestFramework.bstack11llll111l1_opy_[bstack1l11l111l11_opy_])))
        for callback in TestFramework.bstack11llll111l1_opy_[bstack1l11l111l11_opy_]:
            try:
                callback(self, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack1l11l11_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠣᗡ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1l1l1l1l111_opy_(self):
        return
    @abc.abstractmethod
    def bstack1l1lll1l1ll_opy_(self, instance, bstack1lllllll1l1_opy_):
        return
    @abc.abstractmethod
    def bstack1l1lll11111_opy_(self, instance, bstack1lllllll1l1_opy_):
        return
    @staticmethod
    def bstack1lllllll111_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1llll1l1ll1_opy_.create_context(target)
        instance = TestFramework.bstack1lllll1111l_opy_.get(ctx.id, None)
        if instance and instance.bstack1llllll1ll1_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l1ll11lll1_opy_(reverse=True) -> List[bstack1ll1lllll11_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lllll1111l_opy_.values(),
            ),
            key=lambda t: t.bstack1lllll111ll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llll1l1lll_opy_(ctx: bstack1lllll11l11_opy_, reverse=True) -> List[bstack1ll1lllll11_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lllll1111l_opy_.values(),
            ),
            key=lambda t: t.bstack1lllll111ll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllll1l11l_opy_(instance: bstack1ll1lllll11_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def bstack1llllll1l1l_opy_(instance: bstack1ll1lllll11_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllll1l1l1_opy_(instance: bstack1ll1lllll11_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1l11l11_opy_ (u"ࠤࡶࡩࡹࡥࡳࡵࡣࡷࡩ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽࢀࠤࡰ࡫ࡹ࠾ࡽࢀࠤࡻࡧ࡬ࡶࡧࡀࡿࢂࠨᗢ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1l111lll1l1_opy_(instance: bstack1ll1lllll11_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack1l11l11_opy_ (u"ࠥࡷࡪࡺ࡟ࡴࡶࡤࡸࡪࡥࡥ࡯ࡶࡵ࡭ࡪࡹ࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿࢂࠦࡥ࡯ࡶࡵ࡭ࡪࡹ࠽ࡼࡿࠥᗣ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack11lll1lllll_opy_(instance: bstack1llll11ll11_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1l11l11_opy_ (u"ࠦࡺࡶࡤࡢࡶࡨࡣࡸࡺࡡࡵࡧ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡾࠢ࡮ࡩࡾࡃࡻࡾࠢࡹࡥࡱࡻࡥ࠾ࡽࢀࠦᗤ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1lllllll111_opy_(target, strict)
        return TestFramework.bstack1llllll1l1l_opy_(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1lllllll111_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack11llllll11l_opy_(instance: bstack1ll1lllll11_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1l11111llll_opy_(instance: bstack1ll1lllll11_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l11l11l11l_opy_(bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_]):
        return bstack1l11l11_opy_ (u"ࠧࡀࠢᗥ").join((bstack1llll11ll11_opy_(bstack1lllllll1l1_opy_[0]).name, bstack1ll1ll11111_opy_(bstack1lllllll1l1_opy_[1]).name))
    @staticmethod
    def bstack1ll111l11ll_opy_(bstack1lllllll1l1_opy_: Tuple[bstack1llll11ll11_opy_, bstack1ll1ll11111_opy_], callback: Callable):
        bstack1l11l111l11_opy_ = TestFramework.bstack1l11l11l11l_opy_(bstack1lllllll1l1_opy_)
        TestFramework.logger.debug(bstack1l11l11_opy_ (u"ࠨࡳࡦࡶࡢ࡬ࡴࡵ࡫ࡠࡥࡤࡰࡱࡨࡡࡤ࡭࠽ࠤ࡭ࡵ࡯࡬ࡡࡵࡩ࡬࡯ࡳࡵࡴࡼࡣࡰ࡫ࡹ࠾ࡽࢀࠦᗦ").format(bstack1l11l111l11_opy_))
        if not bstack1l11l111l11_opy_ in TestFramework.bstack11llll111l1_opy_:
            TestFramework.bstack11llll111l1_opy_[bstack1l11l111l11_opy_] = []
        TestFramework.bstack11llll111l1_opy_[bstack1l11l111l11_opy_].append(callback)
    @staticmethod
    def bstack1l1lll11l1l_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack1l11l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡹ࡯࡮ࡴࠤᗧ"):
            return klass.__qualname__
        return module + bstack1l11l11_opy_ (u"ࠣ࠰ࠥᗨ") + klass.__qualname__
    @staticmethod
    def bstack1l1ll1l1111_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}