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
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack1l1111ll1l_opy_ import get_logger
logger = get_logger(__name__)
bstack11111111lll_opy_: Dict[str, float] = {}
bstack1111111l1ll_opy_: List = []
bstack1111111l11l_opy_ = 5
bstack1l1l1l11ll_opy_ = os.path.join(os.getcwd(), bstack1l11l11_opy_ (u"ࠫࡱࡵࡧࠨἩ"), bstack1l11l11_opy_ (u"ࠬࡱࡥࡺ࠯ࡰࡩࡹࡸࡩࡤࡵ࠱࡮ࡸࡵ࡮ࠨἪ"))
logging.getLogger(bstack1l11l11_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠨἫ")).setLevel(logging.WARNING)
lock = FileLock(bstack1l1l1l11ll_opy_+bstack1l11l11_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨἬ"))
class bstack1111111l1l1_opy_:
    duration: float
    name: str
    startTime: float
    worker: int
    status: bool
    failure: str
    details: Optional[str]
    entryType: str
    platform: Optional[int]
    command: Optional[str]
    hookType: Optional[str]
    cli: Optional[bool]
    def __init__(self, duration: float, name: str, start_time: float, bstack1111111l111_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack1111111l111_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack1l11l11_opy_ (u"ࠣ࡯ࡨࡥࡸࡻࡲࡦࠤἭ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1lll11lll11_opy_:
    global bstack11111111lll_opy_
    @staticmethod
    def bstack1ll111lll11_opy_(key: str):
        bstack1ll11lll1l1_opy_ = bstack1lll11lll11_opy_.bstack11ll1l1111l_opy_(key)
        bstack1lll11lll11_opy_.mark(bstack1ll11lll1l1_opy_+bstack1l11l11_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤἮ"))
        return bstack1ll11lll1l1_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11111111lll_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack1l11l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨἯ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1lll11lll11_opy_.mark(end)
            bstack1lll11lll11_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack1l11l11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶ࠾ࠥࢁࡽࠣἰ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11111111lll_opy_ or end not in bstack11111111lll_opy_:
                logger.debug(bstack1l11l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡶࡤࡶࡹࠦ࡫ࡦࡻࠣࡻ࡮ࡺࡨࠡࡸࡤࡰࡺ࡫ࠠࡼࡿࠣࡳࡷࠦࡥ࡯ࡦࠣ࡯ࡪࡿࠠࡸ࡫ࡷ࡬ࠥࡼࡡ࡭ࡷࡨࠤࢀࢃࠢἱ").format(start,end))
                return
            duration: float = bstack11111111lll_opy_[end] - bstack11111111lll_opy_[start]
            bstack1111111lll1_opy_ = os.environ.get(bstack1l11l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡏࡓࡠࡔࡘࡒࡓࡏࡎࡈࠤἲ"), bstack1l11l11_opy_ (u"ࠢࡧࡣ࡯ࡷࡪࠨἳ")).lower() == bstack1l11l11_opy_ (u"ࠣࡶࡵࡹࡪࠨἴ")
            bstack1111111llll_opy_: bstack1111111l1l1_opy_ = bstack1111111l1l1_opy_(duration, label, bstack11111111lll_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack1l11l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤἵ"), 0), command, test_name, hook_type, bstack1111111lll1_opy_)
            del bstack11111111lll_opy_[start]
            del bstack11111111lll_opy_[end]
            bstack1lll11lll11_opy_.bstack1111111ll11_opy_(bstack1111111llll_opy_)
        except Exception as e:
            logger.debug(bstack1l11l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡨࡥࡸࡻࡲࡪࡰࡪࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴ࠼ࠣࡿࢂࠨἶ").format(e))
    @staticmethod
    def bstack1111111ll11_opy_(bstack1111111llll_opy_):
        os.makedirs(os.path.dirname(bstack1l1l1l11ll_opy_)) if not os.path.exists(os.path.dirname(bstack1l1l1l11ll_opy_)) else None
        bstack1lll11lll11_opy_.bstack1111111ll1l_opy_()
        try:
            with lock:
                with open(bstack1l1l1l11ll_opy_, bstack1l11l11_opy_ (u"ࠦࡷ࠱ࠢἷ"), encoding=bstack1l11l11_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦἸ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack1111111llll_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack111111l1111_opy_:
            logger.debug(bstack1l11l11_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠠࡼࡿࠥἹ").format(bstack111111l1111_opy_))
            with lock:
                with open(bstack1l1l1l11ll_opy_, bstack1l11l11_opy_ (u"ࠢࡸࠤἺ"), encoding=bstack1l11l11_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢἻ")) as file:
                    data = [bstack1111111llll_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack1l11l11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴࠢࡤࡴࡵ࡫࡮ࡥࠢࡾࢁࠧἼ").format(str(e)))
        finally:
            if os.path.exists(bstack1l1l1l11ll_opy_+bstack1l11l11_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤἽ")):
                os.remove(bstack1l1l1l11ll_opy_+bstack1l11l11_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥἾ"))
    @staticmethod
    def bstack1111111ll1l_opy_():
        attempt = 0
        while (attempt < bstack1111111l11l_opy_):
            attempt += 1
            if os.path.exists(bstack1l1l1l11ll_opy_+bstack1l11l11_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦἿ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1l1111l_opy_(label: str) -> str:
        try:
            return bstack1l11l11_opy_ (u"ࠨࡻࡾ࠼ࡾࢁࠧὀ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack1l11l11_opy_ (u"ࠢࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥὁ").format(e))