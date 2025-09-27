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
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1111111ll1_opy_ import bstack11111111ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1ll11lll_opy_ import bstack1llll111lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1ll1l_opy_ import bstack1lll111l11l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1l1ll1_opy_ import bstack1lll1111lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1llll11l11l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1ll1ll1l_opy_ import bstack1ll1ll1111l_opy_
from browserstack_sdk.sdk_cli.bstack1llll11ll11_opy_ import bstack1lll1ll1l11_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1l1lll_opy_ import bstack1lll1llll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll111111l_opy_ import bstack1ll1l1l1111_opy_
from browserstack_sdk.sdk_cli.bstack1l111ll111_opy_ import bstack1l111ll111_opy_, bstack111ll1ll1_opy_, bstack1l1l11llll_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1ll1ll1llll_opy_ import bstack1lll11lll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll11111ll_opy_ import bstack1ll1ll111ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lllll11lll_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1l11l1_opy_ import bstack1lll1ll1111_opy_
from bstack_utils.helper import Notset, bstack1llll11ll1l_opy_, get_cli_dir, bstack1lll1ll111l_opy_, bstack1l11lll1ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1lll1111l11_opy_ import bstack1lll1ll11ll_opy_
from browserstack_sdk.sdk_cli.utils.bstack11111ll11_opy_ import bstack11l1l1ll_opy_
from bstack_utils.helper import Notset, bstack1llll11ll1l_opy_, get_cli_dir, bstack1lll1ll111l_opy_, bstack1l11lll1ll_opy_, bstack1lll1ll1l_opy_, bstack1l1l11l11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1ll1_opy_, bstack1lll1l11l11_opy_, bstack1lll1l1l1l1_opy_, bstack1lll111llll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1llll1lllll_opy_, bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_
from bstack_utils.constants import *
from bstack_utils.bstack1111111l_opy_ import bstack11lllll1ll_opy_
from bstack_utils import bstack11lll1llll_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11l1ll11l1_opy_, bstack1l11l1l11l_opy_
logger = bstack11lll1llll_opy_.get_logger(__name__, bstack11lll1llll_opy_.bstack1ll1lllll11_opy_())
def bstack1ll1ll11l11_opy_(bs_config):
    bstack1lll1l11lll_opy_ = None
    bstack1lll1l11111_opy_ = None
    try:
        bstack1lll1l11111_opy_ = get_cli_dir()
        bstack1lll1l11lll_opy_ = bstack1lll1ll111l_opy_(bstack1lll1l11111_opy_)
        bstack1ll1ll1l1l1_opy_ = bstack1llll11ll1l_opy_(bstack1lll1l11lll_opy_, bstack1lll1l11111_opy_, bs_config)
        bstack1lll1l11lll_opy_ = bstack1ll1ll1l1l1_opy_ if bstack1ll1ll1l1l1_opy_ else bstack1lll1l11lll_opy_
        if not bstack1lll1l11lll_opy_:
            raise ValueError(bstack1l1l11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡘࡊࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡓࡅ࡙ࡎࠢႪ"))
    except Exception as ex:
        logger.debug(bstack1l1l11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡱࡧࡴࡦࡵࡷࠤࡧ࡯࡮ࡢࡴࡼࠤࢀࢃࠢႫ").format(ex))
        bstack1lll1l11lll_opy_ = os.environ.get(bstack1l1l11_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡔࡆ࡚ࡈࠣႬ"))
        if bstack1lll1l11lll_opy_:
            logger.debug(bstack1l1l11_opy_ (u"ࠨࡆࡢ࡮࡯࡭ࡳ࡭ࠠࡣࡣࡦ࡯ࠥࡺ࡯ࠡࡕࡇࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡐࡂࡖࡋࠤ࡫ࡸ࡯࡮ࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺ࠺ࠡࠤႭ") + str(bstack1lll1l11lll_opy_) + bstack1l1l11_opy_ (u"ࠢࠣႮ"))
        else:
            logger.debug(bstack1l1l11_opy_ (u"ࠣࡐࡲࠤࡻࡧ࡬ࡪࡦࠣࡗࡉࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡒࡄࡘࡍࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡧࡱࡺ࡮ࡸ࡯࡯࡯ࡨࡲࡹࡁࠠࡴࡧࡷࡹࡵࠦ࡭ࡢࡻࠣࡦࡪࠦࡩ࡯ࡥࡲࡱࡵࡲࡥࡵࡧ࠱ࠦႯ"))
    return bstack1lll1l11lll_opy_, bstack1lll1l11111_opy_
bstack1lll111ll11_opy_ = bstack1l1l11_opy_ (u"ࠤ࠼࠽࠾࠿ࠢႰ")
bstack1lll1ll11l1_opy_ = bstack1l1l11_opy_ (u"ࠥࡶࡪࡧࡤࡺࠤႱ")
bstack1lll11ll11l_opy_ = bstack1l1l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡘࡋࡓࡔࡋࡒࡒࡤࡏࡄࠣႲ")
bstack1ll1l1llll1_opy_ = bstack1l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡒࡉࡔࡖࡈࡒࡤࡇࡄࡅࡔࠥႳ")
bstack1llll1l1_opy_ = bstack1l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠤႴ")
bstack1lll1ll1l1l_opy_ = re.compile(bstack1l1l11_opy_ (u"ࡲࠣࠪࡂ࡭࠮࠴ࠪࠩࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑࡼࡃࡕࠬ࠲࠯ࠨႵ"))
bstack1ll1llll11l_opy_ = bstack1l1l11_opy_ (u"ࠣࡦࡨࡺࡪࡲ࡯ࡱ࡯ࡨࡲࡹࠨႶ")
bstack1lll11l1lll_opy_ = bstack1l1l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡒࡖࡈࡋ࡟ࡇࡃࡏࡐࡇࡇࡃࡌࠤႷ")
bstack1ll1ll1ll11_opy_ = [
    bstack111ll1ll1_opy_.bstack1llll1l11_opy_,
    bstack111ll1ll1_opy_.CONNECT,
    bstack111ll1ll1_opy_.bstack1l1l11l11l_opy_,
]
class SDKCLI:
    _1lll1l111ll_opy_ = None
    process: Union[None, Any]
    bstack1ll1l1lll1l_opy_: bool
    bstack1llll1111ll_opy_: bool
    bstack1ll1llllll1_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1lll11l111l_opy_: Union[None, grpc.Channel]
    bstack1lll1l1l11l_opy_: str
    test_framework: TestFramework
    bstack1llll1ll111_opy_: bstack1lllll11lll_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1lll11ll1l1_opy_: bstack1ll1l1l1111_opy_
    accessibility: bstack1llll111lll_opy_
    bstack11111ll11_opy_: bstack11l1l1ll_opy_
    ai: bstack1lll111l11l_opy_
    bstack1ll1ll11l1l_opy_: bstack1lll1111lll_opy_
    bstack1lll11ll111_opy_: List[bstack1llll11lll1_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1lll1l1lll1_opy_: Any
    bstack1lll111ll1l_opy_: Dict[str, timedelta]
    bstack1ll1l1ll111_opy_: str
    bstack1111111ll1_opy_: bstack11111111ll_opy_
    def __new__(cls):
        if not cls._1lll1l111ll_opy_:
            cls._1lll1l111ll_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1lll1l111ll_opy_
    def __init__(self):
        self.process = None
        self.bstack1ll1l1lll1l_opy_ = False
        self.bstack1lll11l111l_opy_ = None
        self.bstack1lll11111l1_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1ll1l1llll1_opy_, None)
        self.bstack1ll1lll1l1l_opy_ = os.environ.get(bstack1lll11ll11l_opy_, bstack1l1l11_opy_ (u"ࠥࠦႸ")) == bstack1l1l11_opy_ (u"ࠦࠧႹ")
        self.bstack1llll1111ll_opy_ = False
        self.bstack1ll1llllll1_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1lll1l1lll1_opy_ = None
        self.test_framework = None
        self.bstack1llll1ll111_opy_ = None
        self.bstack1lll1l1l11l_opy_=bstack1l1l11_opy_ (u"ࠧࠨႺ")
        self.session_framework = None
        self.logger = bstack11lll1llll_opy_.get_logger(self.__class__.__name__, bstack11lll1llll_opy_.bstack1ll1lllll11_opy_())
        self.bstack1lll111ll1l_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1111111ll1_opy_ = bstack11111111ll_opy_()
        self.bstack1lll11lllll_opy_ = None
        self.bstack1ll1l1lll11_opy_ = None
        self.bstack1lll11ll1l1_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1lll11ll111_opy_ = []
    def bstack1l11111ll1_opy_(self):
        return os.environ.get(bstack1llll1l1_opy_).lower().__eq__(bstack1l1l11_opy_ (u"ࠨࡴࡳࡷࡨࠦႻ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1lll11l1lll_opy_, bstack1l1l11_opy_ (u"ࠧࠨႼ")).lower() in [bstack1l1l11_opy_ (u"ࠨࡶࡵࡹࡪ࠭Ⴝ"), bstack1l1l11_opy_ (u"ࠩ࠴ࠫႾ"), bstack1l1l11_opy_ (u"ࠪࡽࡪࡹࠧႿ")]:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡋࡵࡲࡤ࡫ࡱ࡫ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱࠠ࡮ࡱࡧࡩࠥࡪࡵࡦࠢࡷࡳࠥࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡕࡒࡄࡇࡢࡊࡆࡒࡌࡃࡃࡆࡏࠥ࡫࡮ࡷ࡫ࡵࡳࡳࡳࡥ࡯ࡶࠣࡺࡦࡸࡩࡢࡤ࡯ࡩࠧჀ"))
            os.environ[bstack1l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡎ࡙࡟ࡓࡗࡑࡒࡎࡔࡇࠣჁ")] = bstack1l1l11_opy_ (u"ࠨࡆࡢ࡮ࡶࡩࠧჂ")
            return False
        if bstack1l1l11_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫჃ") in config and str(config[bstack1l1l11_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬჄ")]).lower() != bstack1l1l11_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨჅ"):
            return False
        bstack1ll1lllllll_opy_ = [bstack1l1l11_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥ჆"), bstack1l1l11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣჇ")]
        bstack1lll1lllll1_opy_ = config.get(bstack1l1l11_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠣ჈")) in bstack1ll1lllllll_opy_ or os.environ.get(bstack1l1l11_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧ჉")) in bstack1ll1lllllll_opy_
        os.environ[bstack1l1l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡉࡔࡡࡕ࡙ࡓࡔࡉࡏࡉࠥ჊")] = str(bstack1lll1lllll1_opy_) # bstack1llll111ll1_opy_ bstack1ll1lll1111_opy_ VAR to bstack1llll111111_opy_ is binary running
        return bstack1lll1lllll1_opy_
    def bstack11ll11l1l_opy_(self):
        for event in bstack1ll1ll1ll11_opy_:
            bstack1l111ll111_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1l111ll111_opy_.logger.debug(bstack1l1l11_opy_ (u"ࠣࡽࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࢃࠠ࠾ࡀࠣࡿࡦࡸࡧࡴࡿࠣࠦ჋") + str(kwargs) + bstack1l1l11_opy_ (u"ࠤࠥ჌"))
            )
        bstack1l111ll111_opy_.register(bstack111ll1ll1_opy_.bstack1llll1l11_opy_, self.__1lll1l111l1_opy_)
        bstack1l111ll111_opy_.register(bstack111ll1ll1_opy_.CONNECT, self.__1lll11l11ll_opy_)
        bstack1l111ll111_opy_.register(bstack111ll1ll1_opy_.bstack1l1l11l11l_opy_, self.__1lll1lll11l_opy_)
        bstack1l111ll111_opy_.register(bstack111ll1ll1_opy_.bstack1ll1111l_opy_, self.__1llll11l111_opy_)
    def bstack1l1ll1l1_opy_(self):
        return not self.bstack1ll1lll1l1l_opy_ and os.environ.get(bstack1lll11ll11l_opy_, bstack1l1l11_opy_ (u"ࠥࠦჍ")) != bstack1l1l11_opy_ (u"ࠦࠧ჎")
    def is_running(self):
        if self.bstack1ll1lll1l1l_opy_:
            return self.bstack1ll1l1lll1l_opy_
        else:
            return bool(self.bstack1lll11l111l_opy_)
    def bstack1ll1lll111l_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1lll11ll111_opy_) and cli.is_running()
    def __1ll1lll1l11_opy_(self, bstack1lll11l1111_opy_=10):
        if self.bstack1lll11111l1_opy_:
            return
        bstack11l1ll1111_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1ll1l1llll1_opy_, self.cli_listen_addr)
        self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡡࠢ჏") + str(id(self)) + bstack1l1l11_opy_ (u"ࠨ࡝ࠡࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡱ࡫ࠧა"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack1l1l11_opy_ (u"ࠢࡨࡴࡳࡧ࠳࡫࡮ࡢࡤ࡯ࡩࡤ࡮ࡴࡵࡲࡢࡴࡷࡵࡸࡺࠤბ"), 0), (bstack1l1l11_opy_ (u"ࠣࡩࡵࡴࡨ࠴ࡥ࡯ࡣࡥࡰࡪࡥࡨࡵࡶࡳࡷࡤࡶࡲࡰࡺࡼࠦგ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1lll11l1111_opy_)
        self.bstack1lll11l111l_opy_ = channel
        self.bstack1lll11111l1_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1lll11l111l_opy_)
        self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡤࡱࡱࡲࡪࡩࡴࠣდ"), datetime.now() - bstack11l1ll1111_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1ll1l1llll1_opy_] = self.cli_listen_addr
        self.logger.debug(bstack1l1l11_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨ࠿ࠦࡩࡴࡡࡦ࡬࡮ࡲࡤࡠࡲࡵࡳࡨ࡫ࡳࡴ࠿ࠥე") + str(self.bstack1l1ll1l1_opy_()) + bstack1l1l11_opy_ (u"ࠦࠧვ"))
    def __1lll1lll11l_opy_(self, event_name):
        if self.bstack1l1ll1l1_opy_():
            self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡳࡵࡱࡳࡴ࡮ࡴࡧࠡࡅࡏࡍࠧზ"))
        self.__1ll1l1lllll_opy_()
    def __1llll11l111_opy_(self, event_name, bstack1llll1l1111_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack1l1l11_opy_ (u"ࠨࡓࡰ࡯ࡨࡸ࡭࡯࡮ࡨࠢࡺࡩࡳࡺࠠࡸࡴࡲࡲ࡬ࠨთ"))
        bstack1lll1lll1l1_opy_ = Path(bstack1lll11llll1_opy_ (u"ࠢࡼࡵࡨࡰ࡫࠴ࡣ࡭࡫ࡢࡨ࡮ࡸࡽ࠰ࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࡵ࠱࡮ࡸࡵ࡮ࠣი"))
        if self.bstack1lll1l11111_opy_ and bstack1lll1lll1l1_opy_.exists():
            with open(bstack1lll1lll1l1_opy_, bstack1l1l11_opy_ (u"ࠨࡴࠪკ"), encoding=bstack1l1l11_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨლ")) as fp:
                data = json.load(fp)
                try:
                    bstack1lll1ll1l_opy_(bstack1l1l11_opy_ (u"ࠪࡔࡔ࡙ࡔࠨმ"), bstack11lllll1ll_opy_(bstack1ll1l1l1l1_opy_), data, {
                        bstack1l1l11_opy_ (u"ࠫࡦࡻࡴࡩࠩნ"): (self.config[bstack1l1l11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧო")], self.config[bstack1l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩპ")])
                    })
                except Exception as e:
                    logger.debug(bstack1l11l1l11l_opy_.format(str(e)))
            bstack1lll1lll1l1_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1lll1l11l1l_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def __1lll1l111l1_opy_(self, event_name: str, data):
        from bstack_utils.bstack111l11ll_opy_ import bstack1lll111lll1_opy_
        self.bstack1lll1l1l11l_opy_, self.bstack1lll1l11111_opy_ = bstack1ll1ll11l11_opy_(data.bs_config)
        os.environ[bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡗࡓࡋࡗࡅࡇࡒࡅࡠࡆࡌࡖࠬჟ")] = self.bstack1lll1l11111_opy_
        if not self.bstack1lll1l1l11l_opy_ or not self.bstack1lll1l11111_opy_:
            raise ValueError(bstack1l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡷ࡬ࡪࠦࡓࡅࡍࠣࡇࡑࡏࠠࡣ࡫ࡱࡥࡷࡿࠢრ"))
        if self.bstack1l1ll1l1_opy_():
            self.__1lll11l11ll_opy_(event_name, bstack1l1l11llll_opy_())
            return
        try:
            bstack1lll111lll1_opy_.end(EVENTS.bstack1l1ll11l1l_opy_.value, EVENTS.bstack1l1ll11l1l_opy_.value + bstack1l1l11_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤს"), EVENTS.bstack1l1ll11l1l_opy_.value + bstack1l1l11_opy_ (u"ࠥ࠾ࡪࡴࡤࠣტ"), status=True, failure=None, test_name=None)
            logger.debug(bstack1l1l11_opy_ (u"ࠦࡈࡵ࡭ࡱ࡮ࡨࡸࡪࠦࡓࡅࡍࠣࡗࡪࡺࡵࡱ࠰ࠥუ"))
        except Exception as e:
            logger.debug(bstack1l1l11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡻࡾࠤფ").format(e))
        start = datetime.now()
        is_started = self.__1ll1lll11l1_opy_()
        self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠨࡳࡱࡣࡺࡲࡤࡺࡩ࡮ࡧࠥქ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1ll1lll1l11_opy_()
            self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࡠࡶ࡬ࡱࡪࠨღ"), datetime.now() - start)
            start = datetime.now()
            self.__1lll1l1ll11_opy_(data)
            self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠣࡵࡷࡥࡷࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡶ࡬ࡱࡪࠨყ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1lll11l1ll1_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def __1lll11l11ll_opy_(self, event_name: str, data: bstack1l1l11llll_opy_):
        if not self.bstack1l1ll1l1_opy_():
            self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩ࡯࡯ࡰࡨࡧࡹࡀࠠ࡯ࡱࡷࠤࡦࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࠨშ"))
            return
        bin_session_id = os.environ.get(bstack1lll11ll11l_opy_)
        start = datetime.now()
        self.__1ll1lll1l11_opy_()
        self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࡣࡹ࡯࡭ࡦࠤჩ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡪࡪࠠࡵࡱࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡉࡌࡊࠢࠥც") + str(bin_session_id) + bstack1l1l11_opy_ (u"ࠧࠨძ"))
        start = datetime.now()
        self.__1ll1ll11ll1_opy_()
        self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦწ"), datetime.now() - start)
    def __1ll1ll1lll1_opy_(self):
        if not self.bstack1lll11111l1_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠢࡤࡣࡱࡲࡴࡺࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡧࠣࡱࡴࡪࡵ࡭ࡧࡶࠦჭ"))
            return
        bstack1ll1l1l1l11_opy_ = {
            bstack1l1l11_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧხ"): (bstack1lll1ll1l11_opy_, bstack1lll1llll11_opy_, bstack1lll1ll1111_opy_),
            bstack1l1l11_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦჯ"): (bstack1llll11l11l_opy_, bstack1ll1ll1111l_opy_, bstack1ll1ll111ll_opy_),
        }
        if not self.bstack1lll11lllll_opy_ and self.session_framework in bstack1ll1l1l1l11_opy_:
            bstack1llll111l11_opy_, bstack1lll1llllll_opy_, bstack1lll111l1ll_opy_ = bstack1ll1l1l1l11_opy_[self.session_framework]
            bstack1lll1l1111l_opy_ = bstack1lll1llllll_opy_()
            self.bstack1ll1l1lll11_opy_ = bstack1lll1l1111l_opy_
            self.bstack1lll11lllll_opy_ = bstack1lll111l1ll_opy_
            self.bstack1lll11ll111_opy_.append(bstack1lll1l1111l_opy_)
            self.bstack1lll11ll111_opy_.append(bstack1llll111l11_opy_(self.bstack1ll1l1lll11_opy_))
        if not self.bstack1lll11ll1l1_opy_ and self.config_observability and self.config_observability.success: # bstack1lll11ll1ll_opy_
            self.bstack1lll11ll1l1_opy_ = bstack1ll1l1l1111_opy_(self.bstack1lll11lllll_opy_, self.bstack1ll1l1lll11_opy_) # bstack1ll1lll1ll1_opy_
            self.bstack1lll11ll111_opy_.append(self.bstack1lll11ll1l1_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1llll111lll_opy_(self.bstack1lll11lllll_opy_, self.bstack1ll1l1lll11_opy_)
            self.bstack1lll11ll111_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack1l1l11_opy_ (u"ࠥࡷࡪࡲࡦࡉࡧࡤࡰࠧჰ"), False) == True:
            self.ai = bstack1lll111l11l_opy_()
            self.bstack1lll11ll111_opy_.append(self.ai)
        if not self.percy and self.bstack1lll1l1lll1_opy_ and self.bstack1lll1l1lll1_opy_.success:
            self.percy = bstack1lll1111lll_opy_(self.bstack1lll1l1lll1_opy_)
            self.bstack1lll11ll111_opy_.append(self.percy)
        for mod in self.bstack1lll11ll111_opy_:
            if not mod.bstack1llll1l111l_opy_():
                mod.configure(self.bstack1lll11111l1_opy_, self.config, self.cli_bin_session_id, self.bstack1111111ll1_opy_)
    def __1lll11l1l11_opy_(self):
        for mod in self.bstack1lll11ll111_opy_:
            if mod.bstack1llll1l111l_opy_():
                mod.configure(self.bstack1lll11111l1_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1lll1lll111_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def __1lll1l1ll11_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1llll1111ll_opy_:
            return
        self.__1lll1l1l1ll_opy_(data)
        bstack11l1ll1111_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack1l1l11_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࠦჱ")
        req.sdk_language = bstack1l1l11_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧჲ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1lll1ll1l1l_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠨ࡛ࠣჳ") + str(id(self)) + bstack1l1l11_opy_ (u"ࠢ࡞ࠢࡰࡥ࡮ࡴ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡶࡸࡦࡸࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨჴ"))
            r = self.bstack1lll11111l1_opy_.StartBinSession(req)
            self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡵࡣࡵࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥჵ"), datetime.now() - bstack11l1ll1111_opy_)
            os.environ[bstack1lll11ll11l_opy_] = r.bin_session_id
            self.__1ll1llll1l1_opy_(r)
            self.__1ll1ll1lll1_opy_()
            self.bstack1111111ll1_opy_.start()
            self.bstack1llll1111ll_opy_ = True
            self.logger.debug(bstack1l1l11_opy_ (u"ࠤ࡞ࠦჶ") + str(id(self)) + bstack1l1l11_opy_ (u"ࠥࡡࠥࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤࠣჷ"))
        except grpc.bstack1lll1lll1ll_opy_ as bstack1lll1l11ll1_opy_:
            self.logger.error(bstack1l1l11_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡸ࡮ࡳࡥࡰࡧࡸࡸ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨჸ") + str(bstack1lll1l11ll1_opy_) + bstack1l1l11_opy_ (u"ࠧࠨჹ"))
            traceback.print_exc()
            raise bstack1lll1l11ll1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥჺ") + str(e) + bstack1l1l11_opy_ (u"ࠢࠣ჻"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lll1ll1lll_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def __1ll1ll11ll1_opy_(self):
        if not self.bstack1l1ll1l1_opy_() or not self.cli_bin_session_id or self.bstack1ll1llllll1_opy_:
            return
        bstack11l1ll1111_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨჼ"), bstack1l1l11_opy_ (u"ࠩ࠳ࠫჽ")))
        try:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠥ࡟ࠧჾ") + str(id(self)) + bstack1l1l11_opy_ (u"ࠦࡢࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡤࡱࡱࡲࡪࡩࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨჿ"))
            r = self.bstack1lll11111l1_opy_.ConnectBinSession(req)
            self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡧࡴࡴ࡮ࡦࡥࡷࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᄀ"), datetime.now() - bstack11l1ll1111_opy_)
            self.__1ll1llll1l1_opy_(r)
            self.__1ll1ll1lll1_opy_()
            self.bstack1111111ll1_opy_.start()
            self.bstack1ll1llllll1_opy_ = True
            self.logger.debug(bstack1l1l11_opy_ (u"ࠨ࡛ࠣᄁ") + str(id(self)) + bstack1l1l11_opy_ (u"ࠢ࡞ࠢࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࠨᄂ"))
        except grpc.bstack1lll1lll1ll_opy_ as bstack1lll1l11ll1_opy_:
            self.logger.error(bstack1l1l11_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡵ࡫ࡰࡩࡴ࡫ࡵࡵ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᄃ") + str(bstack1lll1l11ll1_opy_) + bstack1l1l11_opy_ (u"ࠤࠥᄄ"))
            traceback.print_exc()
            raise bstack1lll1l11ll1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᄅ") + str(e) + bstack1l1l11_opy_ (u"ࠦࠧᄆ"))
            traceback.print_exc()
            raise e
    def __1ll1llll1l1_opy_(self, r):
        self.bstack1lll111l1l1_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack1l1l11_opy_ (u"ࠧࡻ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡶࡩࡷࡼࡥࡳࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦᄇ") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack1l1l11_opy_ (u"ࠨࡥ࡮ࡲࡷࡽࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡬࡯ࡶࡰࡧࠦᄈ"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack1l1l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕ࡫ࡲࡤࡻࠣ࡭ࡸࠦࡳࡦࡰࡷࠤࡴࡴ࡬ࡺࠢࡤࡷࠥࡶࡡࡳࡶࠣࡳ࡫ࠦࡴࡩࡧࠣࠦࡈࡵ࡮࡯ࡧࡦࡸࡇ࡯࡮ࡔࡧࡶࡷ࡮ࡵ࡮࠭ࠤࠣࡥࡳࡪࠠࡵࡪ࡬ࡷࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡪࡵࠣࡥࡱࡹ࡯ࠡࡷࡶࡩࡩࠦࡢࡺࠢࡖࡸࡦࡸࡴࡃ࡫ࡱࡗࡪࡹࡳࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡔࡩࡧࡵࡩ࡫ࡵࡲࡦ࠮ࠣࡒࡴࡴࡥࠡࡪࡤࡲࡩࡲࡩ࡯ࡩࠣ࡭ࡸࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᄉ")
        self.bstack1lll1l1lll1_opy_ = getattr(r, bstack1l1l11_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᄊ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack1l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᄋ")] = self.config_testhub.jwt
        os.environ[bstack1l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᄌ")] = self.config_testhub.build_hashed_id
    def bstack1lll11l1l1l_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1ll1l1lll1l_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1ll1ll1l111_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1ll1ll1l111_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1lll11l1l1l_opy_(event_name=EVENTS.bstack1lll1111l1l_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def __1ll1lll11l1_opy_(self, bstack1lll11l1111_opy_=10):
        if self.bstack1ll1l1lll1l_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡸࡺࡡࡳࡶ࠽ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡸࡵ࡯ࡰ࡬ࡲ࡬ࠨᄍ"))
            return True
        self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡹࡴࡢࡴࡷࠦᄎ"))
        if os.getenv(bstack1l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡈࡒ࡛ࠨᄏ")) == bstack1ll1llll11l_opy_:
            self.cli_bin_session_id = bstack1ll1llll11l_opy_
            self.cli_listen_addr = bstack1l1l11_opy_ (u"ࠢࡶࡰ࡬ࡼ࠿࠵ࡴ࡮ࡲ࠲ࡷࡩࡱ࠭ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠯ࠨࡷ࠳ࡹ࡯ࡤ࡭ࠥᄐ") % (self.cli_bin_session_id)
            self.bstack1ll1l1lll1l_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1lll1l1l11l_opy_, bstack1l1l11_opy_ (u"ࠣࡵࡧ࡯ࠧᄑ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1lll1l1l111_opy_ compat for text=True in bstack1ll1ll1l11l_opy_ python
            encoding=bstack1l1l11_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᄒ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1lll11lll1l_opy_ = threading.Thread(target=self.__1ll1llll1ll_opy_, args=(bstack1lll11l1111_opy_,))
        bstack1lll11lll1l_opy_.start()
        bstack1lll11lll1l_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡶࡴࡦࡽ࡮࠻ࠢࡵࡩࡹࡻࡲ࡯ࡥࡲࡨࡪࡃࡻࡴࡧ࡯ࡪ࠳ࡶࡲࡰࡥࡨࡷࡸ࠴ࡲࡦࡶࡸࡶࡳࡩ࡯ࡥࡧࢀࠤࡴࡻࡴ࠾ࡽࡶࡩࡱ࡬࠮ࡱࡴࡲࡧࡪࡹࡳ࠯ࡵࡷࡨࡴࡻࡴ࠯ࡴࡨࡥࡩ࠮ࠩࡾࠢࡨࡶࡷࡃࠢᄓ") + str(self.process.stderr.read()) + bstack1l1l11_opy_ (u"ࠦࠧᄔ"))
        if not self.bstack1ll1l1lll1l_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡡࠢᄕ") + str(id(self)) + bstack1l1l11_opy_ (u"ࠨ࡝ࠡࡥ࡯ࡩࡦࡴࡵࡱࠤᄖ"))
            self.__1ll1l1lllll_opy_()
        self.logger.debug(bstack1l1l11_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡰࡳࡱࡦࡩࡸࡹ࡟ࡳࡧࡤࡨࡾࡀࠠࠣᄗ") + str(self.bstack1ll1l1lll1l_opy_) + bstack1l1l11_opy_ (u"ࠣࠤᄘ"))
        return self.bstack1ll1l1lll1l_opy_
    def __1ll1llll1ll_opy_(self, bstack1llll11llll_opy_=10):
        bstack1ll1l1ll1l1_opy_ = time.time()
        while self.process and time.time() - bstack1ll1l1ll1l1_opy_ < bstack1llll11llll_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack1l1l11_opy_ (u"ࠤ࡬ࡨࡂࠨᄙ") in line:
                    self.cli_bin_session_id = line.split(bstack1l1l11_opy_ (u"ࠥ࡭ࡩࡃࠢᄚ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡨࡲࡩࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥ࠼ࠥᄛ") + str(self.cli_bin_session_id) + bstack1l1l11_opy_ (u"ࠧࠨᄜ"))
                    continue
                if bstack1l1l11_opy_ (u"ࠨ࡬ࡪࡵࡷࡩࡳࡃࠢᄝ") in line:
                    self.cli_listen_addr = line.split(bstack1l1l11_opy_ (u"ࠢ࡭࡫ࡶࡸࡪࡴ࠽ࠣᄞ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1l11_opy_ (u"ࠣࡥ࡯࡭ࡤࡲࡩࡴࡶࡨࡲࡤࡧࡤࡥࡴ࠽ࠦᄟ") + str(self.cli_listen_addr) + bstack1l1l11_opy_ (u"ࠤࠥᄠ"))
                    continue
                if bstack1l1l11_opy_ (u"ࠥࡴࡴࡸࡴ࠾ࠤᄡ") in line:
                    port = line.split(bstack1l1l11_opy_ (u"ࠦࡵࡵࡲࡵ࠿ࠥᄢ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡶ࡯ࡳࡶ࠽ࠦᄣ") + str(port) + bstack1l1l11_opy_ (u"ࠨࠢᄤ"))
                    continue
                if line.strip() == bstack1lll1ll11l1_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack1l1l11_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡉࡐࡡࡖࡘࡗࡋࡁࡎࠤᄥ"), bstack1l1l11_opy_ (u"ࠣ࠳ࠥᄦ")) == bstack1l1l11_opy_ (u"ࠤ࠴ࠦᄧ"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1ll1l1lll1l_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠥࡩࡷࡸ࡯ࡳ࠼ࠣࠦᄨ") + str(e) + bstack1l1l11_opy_ (u"ࠦࠧᄩ"))
        return False
    @measure(event_name=EVENTS.bstack1ll1ll1l1ll_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def __1ll1l1lllll_opy_(self):
        if self.bstack1lll11l111l_opy_:
            self.bstack1111111ll1_opy_.stop()
            start = datetime.now()
            if self.bstack1ll1lll11ll_opy_():
                self.cli_bin_session_id = None
                if self.bstack1ll1llllll1_opy_:
                    self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠧࡹࡴࡰࡲࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤᄪ"), datetime.now() - start)
                else:
                    self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠨࡳࡵࡱࡳࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡺࡩ࡮ࡧࠥᄫ"), datetime.now() - start)
            self.__1lll11l1l11_opy_()
            start = datetime.now()
            self.bstack1lll11l111l_opy_.close()
            self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠢࡥ࡫ࡶࡧࡴࡴ࡮ࡦࡥࡷࡣࡹ࡯࡭ࡦࠤᄬ"), datetime.now() - start)
            self.bstack1lll11l111l_opy_ = None
        if self.process:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠣࡵࡷࡳࡵࠨᄭ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠤ࡮࡭ࡱࡲ࡟ࡵ࡫ࡰࡩࠧᄮ"), datetime.now() - start)
            self.process = None
            if self.bstack1ll1lll1l1l_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1l1ll1l1l1_opy_()
                self.logger.info(
                    bstack1l1l11_opy_ (u"࡚ࠥ࡮ࡹࡩࡵࠢ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠦࡴࡰࠢࡹ࡭ࡪࡽࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡲࡲࡶࡹ࠲ࠠࡪࡰࡶ࡭࡬࡮ࡴࡴ࠮ࠣࡥࡳࡪࠠ࡮ࡣࡱࡽࠥࡳ࡯ࡳࡧࠣࡨࡪࡨࡵࡨࡩ࡬ࡲ࡬ࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤࡦࡲ࡬ࠡࡣࡷࠤࡴࡴࡥࠡࡲ࡯ࡥࡨ࡫ࠡ࡝ࡰࠥᄯ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack1l1l11_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪᄰ")] = self.config_testhub.build_hashed_id
        self.bstack1ll1l1lll1l_opy_ = False
    def __1lll1l1l1ll_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack1l1l11_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢᄱ")] = selenium.__version__
            data.frameworks.append(bstack1l1l11_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣᄲ"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack1l1l11_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦᄳ")] = __version__
            data.frameworks.append(bstack1l1l11_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧᄴ"))
        except:
            pass
    def bstack1llll111l1l_opy_(self, hub_url: str, platform_index: int, bstack111ll1l1_opy_: Any):
        if self.bstack1llll1ll111_opy_:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡶ࡯࡮ࡶࡰࡦࡦࠣࡷࡪࡺࡵࡱࠢࡶࡩࡱ࡫࡮ࡪࡷࡰ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡳࡦࡶࠣࡹࡵࠨᄵ"))
            return
        try:
            bstack11l1ll1111_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack1l1l11_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧᄶ")
            self.bstack1llll1ll111_opy_ = bstack1ll1ll111ll_opy_(
                cli.config.get(bstack1l1l11_opy_ (u"ࠦ࡭ࡻࡢࡖࡴ࡯ࠦᄷ"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1llll11l1ll_opy_={bstack1l1l11_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡤࡵࡰࡵ࡫ࡲࡲࡸࡥࡦࡳࡱࡰࡣࡨࡧࡰࡴࠤᄸ"): bstack111ll1l1_opy_}
            )
            def bstack1ll1l1l11ll_opy_(self):
                return
            if self.config.get(bstack1l1l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠣᄹ"), True):
                Service.start = bstack1ll1l1l11ll_opy_
                Service.stop = bstack1ll1l1l11ll_opy_
            def get_accessibility_results(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results(driver, framework_name=framework)
            def get_accessibility_results_summary(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results_summary(driver, framework_name=framework)
            def perform_scan(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.perform_scan(driver, method=None, framework_name=framework)
            WebDriver.getAccessibilityResults = get_accessibility_results
            WebDriver.get_accessibility_results = get_accessibility_results
            WebDriver.getAccessibilityResultsSummary = get_accessibility_results_summary
            WebDriver.get_accessibility_results_summary = get_accessibility_results_summary
            WebDriver.upload_attachment = staticmethod(bstack11l1l1ll_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1lll1ll11ll_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣᄺ"), datetime.now() - bstack11l1ll1111_opy_)
        except Exception as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡷࡪࡲࡥ࡯࡫ࡸࡱ࠿ࠦࠢᄻ") + str(e) + bstack1l1l11_opy_ (u"ࠤࠥᄼ"))
    def bstack1lll1111111_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack1lll11ll11_opy_
            self.bstack1llll1ll111_opy_ = bstack1lll1ll1111_opy_(
                platform_index,
                framework_name=bstack1l1l11_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢᄽ"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠽ࠤࠧᄾ") + str(e) + bstack1l1l11_opy_ (u"ࠧࠨᄿ"))
            pass
    def bstack1ll1lllll1l_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠠࡴࡧࡷࡹࡵࠦࡰࡺࡶࡨࡷࡹࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡵࡨࡸࠥࡻࡰࠣᅀ"))
            return
        if bstack1l11lll1ll_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack1l1l11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢᅁ"): pytest.__version__ }, [bstack1l1l11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᅂ")], self.bstack1111111ll1_opy_, self.bstack1lll11111l1_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1lll11lll11_opy_({ bstack1l1l11_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤᅃ"): pytest.__version__ }, [bstack1l1l11_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥᅄ")], self.bstack1111111ll1_opy_, self.bstack1lll11111l1_opy_)
        except Exception as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰࡺࡶࡨࡷࡹࡀࠠࠣᅅ") + str(e) + bstack1l1l11_opy_ (u"ࠧࠨᅆ"))
        self.bstack1llll11111l_opy_()
    def bstack1llll11111l_opy_(self):
        if not self.bstack1l11111ll1_opy_():
            return
        bstack11ll1l1ll_opy_ = None
        def bstack1l1l1l1l1l_opy_(config, startdir):
            return bstack1l1l11_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࠲ࢀࠦᅇ").format(bstack1l1l11_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨᅈ"))
        def bstack1ll1l1l11_opy_():
            return
        def bstack1ll1111l1l_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack1l1l11_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨᅉ"):
                return bstack1l1l11_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣᅊ")
            else:
                return bstack11ll1l1ll_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack11ll1l1ll_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1l1l1l1l1l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1ll1l1l11_opy_
            Config.getoption = bstack1ll1111l1l_opy_
        except Exception as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡶࡦ࡬ࠥࡶࡹࡵࡧࡶࡸࠥࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠠࡧࡱࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠽ࠤࠧᅋ") + str(e) + bstack1l1l11_opy_ (u"ࠦࠧᅌ"))
    def bstack1ll1l1ll11l_opy_(self):
        bstack1ll1ll1ll1_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1ll1ll1ll1_opy_, dict):
            if cli.config_observability:
                bstack1ll1ll1ll1_opy_.update(
                    {bstack1l1l11_opy_ (u"ࠧࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠧᅍ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack1l1l11_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࡠࡶࡲࡣࡼࡸࡡࡱࠤᅎ") in accessibility.get(bstack1l1l11_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣᅏ"), {}):
                    bstack1lll1llll1l_opy_ = accessibility.get(bstack1l1l11_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᅐ"))
                    bstack1lll1llll1l_opy_.update({ bstack1l1l11_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࡘࡴ࡝ࡲࡢࡲࠥᅑ"): bstack1lll1llll1l_opy_.pop(bstack1l1l11_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷࡤࡺ࡯ࡠࡹࡵࡥࡵࠨᅒ")) })
                bstack1ll1ll1ll1_opy_.update({bstack1l1l11_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠦᅓ"): accessibility })
        return bstack1ll1ll1ll1_opy_
    @measure(event_name=EVENTS.bstack1ll1l1l111l_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def bstack1ll1lll11ll_opy_(self, bstack1ll1l1ll1ll_opy_: str = None, bstack1lll1111ll1_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1lll11111l1_opy_:
            return
        bstack11l1ll1111_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1ll1l1ll1ll_opy_:
            req.bstack1ll1l1ll1ll_opy_ = bstack1ll1l1ll1ll_opy_
        if bstack1lll1111ll1_opy_:
            req.bstack1lll1111ll1_opy_ = bstack1lll1111ll1_opy_
        try:
            r = self.bstack1lll11111l1_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡹࡵࡰࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᅔ"), datetime.now() - bstack11l1ll1111_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack11ll1l1ll1_opy_(self, key: str, value: timedelta):
        tag = bstack1l1l11_opy_ (u"ࠨࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࠨᅕ") if self.bstack1l1ll1l1_opy_() else bstack1l1l11_opy_ (u"ࠢ࡮ࡣ࡬ࡲ࠲ࡶࡲࡰࡥࡨࡷࡸࠨᅖ")
        self.bstack1lll111ll1l_opy_[bstack1l1l11_opy_ (u"ࠣ࠼ࠥᅗ").join([tag + bstack1l1l11_opy_ (u"ࠤ࠰ࠦᅘ") + str(id(self)), key])] += value
    def bstack1l1ll1l1l1_opy_(self):
        if not os.getenv(bstack1l1l11_opy_ (u"ࠥࡈࡊࡈࡕࡈࡡࡓࡉࡗࡌࠢᅙ"), bstack1l1l11_opy_ (u"ࠦ࠵ࠨᅚ")) == bstack1l1l11_opy_ (u"ࠧ࠷ࠢᅛ"):
            return
        bstack1ll1llll111_opy_ = dict()
        bstack1lllllllll1_opy_ = []
        if self.test_framework:
            bstack1lllllllll1_opy_.extend(list(self.test_framework.bstack1lllllllll1_opy_.values()))
        if self.bstack1llll1ll111_opy_:
            bstack1lllllllll1_opy_.extend(list(self.bstack1llll1ll111_opy_.bstack1lllllllll1_opy_.values()))
        for instance in bstack1lllllllll1_opy_:
            if not instance.platform_index in bstack1ll1llll111_opy_:
                bstack1ll1llll111_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1ll1llll111_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1ll111l1_opy_().items():
                report[k] += v
                report[k.split(bstack1l1l11_opy_ (u"ࠨ࠺ࠣᅜ"))[0]] += v
        bstack1lll1l1llll_opy_ = sorted([(k, v) for k, v in self.bstack1lll111ll1l_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1ll1l1l1l1l_opy_ = 0
        for r in bstack1lll1l1llll_opy_:
            bstack1ll1ll11111_opy_ = r[1].total_seconds()
            bstack1ll1l1l1l1l_opy_ += bstack1ll1ll11111_opy_
            self.logger.debug(bstack1l1l11_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡤ࡮࡬࠾ࢀࡸ࡛࠱࡟ࢀࡁࠧᅝ") + str(bstack1ll1ll11111_opy_) + bstack1l1l11_opy_ (u"ࠣࠤᅞ"))
        self.logger.debug(bstack1l1l11_opy_ (u"ࠤ࠰࠱ࠧᅟ"))
        bstack1ll1lll1lll_opy_ = []
        for platform_index, report in bstack1ll1llll111_opy_.items():
            bstack1ll1lll1lll_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1ll1lll1lll_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1l1l111ll_opy_ = set()
        bstack1llll11l1l1_opy_ = 0
        for r in bstack1ll1lll1lll_opy_:
            bstack1ll1ll11111_opy_ = r[2].total_seconds()
            bstack1llll11l1l1_opy_ += bstack1ll1ll11111_opy_
            bstack1l1l111ll_opy_.add(r[0])
            self.logger.debug(bstack1l1l11_opy_ (u"ࠥ࡟ࡵ࡫ࡲࡧ࡟ࠣࡸࡪࡹࡴ࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠰ࡿࡷࡡ࠰࡞ࡿ࠽ࡿࡷࡡ࠱࡞ࡿࡀࠦᅠ") + str(bstack1ll1ll11111_opy_) + bstack1l1l11_opy_ (u"ࠦࠧᅡ"))
        if self.bstack1l1ll1l1_opy_():
            self.logger.debug(bstack1l1l11_opy_ (u"ࠧ࠳࠭ࠣᅢ"))
            self.logger.debug(bstack1l1l11_opy_ (u"ࠨ࡛ࡱࡧࡵࡪࡢࠦࡣ࡭࡫࠽ࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵࡀࡿࡹࡵࡴࡢ࡮ࡢࡧࡱ࡯ࡽࠡࡶࡨࡷࡹࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴ࠯ࡾࡷࡹࡸࠨࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠬࢁࡂࠨᅣ") + str(bstack1llll11l1l1_opy_) + bstack1l1l11_opy_ (u"ࠢࠣᅤ"))
        else:
            self.logger.debug(bstack1l1l11_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡥ࡯࡭࠿ࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶࡁࠧᅥ") + str(bstack1ll1l1l1l1l_opy_) + bstack1l1l11_opy_ (u"ࠤࠥᅦ"))
        self.logger.debug(bstack1l1l11_opy_ (u"ࠥ࠱࠲ࠨᅧ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files
        )
        if not self.bstack1lll11111l1_opy_:
            self.logger.error(bstack1l1l11_opy_ (u"ࠦࡨࡲࡩࡠࡵࡨࡶࡻ࡯ࡣࡦࠢ࡬ࡷࠥࡴ࡯ࡵࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡪ࠮ࠡࡅࡤࡲࡳࡵࡴࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠮ࠣᅨ"))
            return None
        response = self.bstack1lll11111l1_opy_.TestOrchestration(request)
        self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡺࡥࡴࡶ࠰ࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠰ࡷࡪࡹࡳࡪࡱࡱࡁࢀࢃࠢᅩ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1lll111l1l1_opy_(self, r):
        if r is not None and getattr(r, bstack1l1l11_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࠧᅪ"), None) and getattr(r.testhub, bstack1l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧᅫ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack1l1l11_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᅬ")))
            for bstack1llll1111l1_opy_, err in errors.items():
                if err[bstack1l1l11_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᅭ")] == bstack1l1l11_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨᅮ"):
                    self.logger.info(err[bstack1l1l11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᅯ")])
                else:
                    self.logger.error(err[bstack1l1l11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᅰ")])
    def bstack1l1llll1l1_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()