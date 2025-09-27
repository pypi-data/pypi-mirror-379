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
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llllllll1l_opy_,
    bstack1llll1lllll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll11111ll_opy_ import bstack1ll1ll111ll_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack11l1l1111l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack111l11ll_opy_ import bstack1lll111lll1_opy_
class bstack1llll11l11l_opy_(bstack1llll11lll1_opy_):
    bstack1l11ll11111_opy_ = bstack1l1l11_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠ࡫ࡱ࡭ࡹࠨ፰")
    bstack1l11ll11ll1_opy_ = bstack1l1l11_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴࠣ፱")
    bstack1l11lll111l_opy_ = bstack1l1l11_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰࠣ፲")
    def __init__(self, bstack1ll1ll11lll_opy_):
        super().__init__()
        bstack1ll1ll111ll_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1llll1lll1l_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1l11l1llll1_opy_)
        bstack1ll1ll111ll_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1lllll1ll1l_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1ll11111ll1_opy_)
        bstack1ll1ll111ll_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1lllll1ll1l_opy_, bstack1llllllll1l_opy_.POST), self.bstack1l11l1ll1l1_opy_)
        bstack1ll1ll111ll_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1lllll1ll1l_opy_, bstack1llllllll1l_opy_.POST), self.bstack1l11lll11ll_opy_)
        bstack1ll1ll111ll_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.QUIT, bstack1llllllll1l_opy_.POST), self.bstack1l11ll1l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1llll1_opy_(
        self,
        f: bstack1ll1ll111ll_opy_,
        driver: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l11_opy_ (u"ࠤࡢࡣ࡮ࡴࡩࡵࡡࡢࠦ፳"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack1l1l11_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨ፴")), str):
                    url = kwargs.get(bstack1l1l11_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢ፵"))
                elif hasattr(kwargs.get(bstack1l1l11_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣ፶")), bstack1l1l11_opy_ (u"࠭࡟ࡤ࡮࡬ࡩࡳࡺ࡟ࡤࡱࡱࡪ࡮࡭ࠧ፷")):
                    url = kwargs.get(bstack1l1l11_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥ፸"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack1l1l11_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦ፹"))._url
            except Exception as e:
                url = bstack1l1l11_opy_ (u"ࠩࠪ፺")
                self.logger.error(bstack1l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡸࡶࡱࠦࡦࡳࡱࡰࠤࡩࡸࡩࡷࡧࡵ࠾ࠥࢁࡽࠣ፻").format(e))
            self.logger.info(bstack1l1l11_opy_ (u"ࠦࡗ࡫࡭ࡰࡶࡨࠤࡘ࡫ࡲࡷࡧࡵࠤࡆࡪࡤࡳࡧࡶࡷࠥࡨࡥࡪࡰࡪࠤࡵࡧࡳࡴࡧࡧࠤࡦࡹࠠ࠻ࠢࡾࢁࠧ፼").format(str(url)))
            self.bstack1l11lll1111_opy_(instance, url, f, kwargs)
            self.logger.info(bstack1l1l11_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠳ࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࡻࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࡾ࠼ࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥ፽").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1ll11111ll1_opy_(
        self,
        f: bstack1ll1ll111ll_opy_,
        driver: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.bstack1lllll1l1l1_opy_(instance, bstack1llll11l11l_opy_.bstack1l11ll11111_opy_, False):
            return
        if not f.bstack1llllll111l_opy_(instance, bstack1ll1ll111ll_opy_.bstack1ll1l1111l1_opy_):
            return
        platform_index = f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll111ll_opy_.bstack1ll1l1111l1_opy_)
        if f.bstack1ll11l111ll_opy_(method_name, *args) and len(args) > 1:
            bstack11l1ll1111_opy_ = datetime.now()
            hub_url = bstack1ll1ll111ll_opy_.hub_url(driver)
            self.logger.warning(bstack1l1l11_opy_ (u"ࠨࡨࡶࡤࡢࡹࡷࡲ࠽ࠣ፾") + str(hub_url) + bstack1l1l11_opy_ (u"ࠢࠣ፿"))
            bstack1l11ll1lll1_opy_ = args[1][bstack1l1l11_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᎀ")] if isinstance(args[1], dict) and bstack1l1l11_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᎁ") in args[1] else None
            bstack1l11ll1111l_opy_ = bstack1l1l11_opy_ (u"ࠥࡥࡱࡽࡡࡺࡵࡐࡥࡹࡩࡨࠣᎂ")
            if isinstance(bstack1l11ll1lll1_opy_, dict):
                bstack11l1ll1111_opy_ = datetime.now()
                r = self.bstack1l11ll1llll_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵࠤᎃ"), datetime.now() - bstack11l1ll1111_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1l1l11_opy_ (u"ࠧࡹ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫࠿ࠦࠢᎄ") + str(r) + bstack1l1l11_opy_ (u"ࠨࠢᎅ"))
                        return
                    if r.hub_url:
                        f.bstack1l11ll111l1_opy_(instance, driver, r.hub_url)
                        f.bstack1llll1l1ll1_opy_(instance, bstack1llll11l11l_opy_.bstack1l11ll11111_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1l1l11_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨᎆ"), e)
    def bstack1l11l1ll1l1_opy_(
        self,
        f: bstack1ll1ll111ll_opy_,
        driver: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1ll1ll111ll_opy_.session_id(driver)
            if session_id:
                bstack1l11l1lll1l_opy_ = bstack1l1l11_opy_ (u"ࠣࡽࢀ࠾ࡸࡺࡡࡳࡶࠥᎇ").format(session_id)
                bstack1lll111lll1_opy_.mark(bstack1l11l1lll1l_opy_)
    def bstack1l11lll11ll_opy_(
        self,
        f: bstack1ll1ll111ll_opy_,
        driver: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.bstack1lllll1l1l1_opy_(instance, bstack1llll11l11l_opy_.bstack1l11ll11ll1_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1ll1ll111ll_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1l1l11_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤ࡭ࡻࡢࡠࡷࡵࡰࡂࠨᎈ") + str(hub_url) + bstack1l1l11_opy_ (u"ࠥࠦᎉ"))
            return
        framework_session_id = bstack1ll1ll111ll_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1l1l11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࡃࠢᎊ") + str(framework_session_id) + bstack1l1l11_opy_ (u"ࠧࠨᎋ"))
            return
        if bstack1ll1ll111ll_opy_.bstack1l11ll11l11_opy_(*args) == bstack1ll1ll111ll_opy_.bstack1l11l1ll1ll_opy_:
            bstack1l11ll1l1l1_opy_ = bstack1l1l11_opy_ (u"ࠨࡻࡾ࠼ࡨࡲࡩࠨᎌ").format(framework_session_id)
            bstack1l11l1lll1l_opy_ = bstack1l1l11_opy_ (u"ࠢࡼࡿ࠽ࡷࡹࡧࡲࡵࠤᎍ").format(framework_session_id)
            bstack1lll111lll1_opy_.end(
                label=bstack1l1l11_opy_ (u"ࠣࡵࡧ࡯࠿ࡪࡲࡪࡸࡨࡶ࠿ࡶ࡯ࡴࡶ࠰࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠦᎎ"),
                start=bstack1l11l1lll1l_opy_,
                end=bstack1l11ll1l1l1_opy_,
                status=True,
                failure=None
            )
            bstack11l1ll1111_opy_ = datetime.now()
            r = self.bstack1l11ll1ll11_opy_(
                ref,
                f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll111ll_opy_.bstack1ll1l1111l1_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴࠣᎏ"), datetime.now() - bstack11l1ll1111_opy_)
            f.bstack1llll1l1ll1_opy_(instance, bstack1llll11l11l_opy_.bstack1l11ll11ll1_opy_, r.success)
    def bstack1l11ll1l1ll_opy_(
        self,
        f: bstack1ll1ll111ll_opy_,
        driver: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.bstack1lllll1l1l1_opy_(instance, bstack1llll11l11l_opy_.bstack1l11lll111l_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1ll1ll111ll_opy_.session_id(driver)
        hub_url = bstack1ll1ll111ll_opy_.hub_url(driver)
        bstack11l1ll1111_opy_ = datetime.now()
        r = self.bstack1l11ll11lll_opy_(
            ref,
            f.bstack1lllll1l1l1_opy_(instance, bstack1ll1ll111ll_opy_.bstack1ll1l1111l1_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack11ll1l1ll1_opy_(bstack1l1l11_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰࠣ᎐"), datetime.now() - bstack11l1ll1111_opy_)
        f.bstack1llll1l1ll1_opy_(instance, bstack1llll11l11l_opy_.bstack1l11lll111l_opy_, r.success)
    @measure(event_name=EVENTS.bstack111l1l111_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def bstack1l1l11l1l11_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲ࡮ࡺ࠺ࠡࠤ᎑") + str(req) + bstack1l1l11_opy_ (u"ࠧࠨ᎒"))
        try:
            r = self.bstack1lll11111l1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࡴࡷࡦࡧࡪࡹࡳ࠾ࠤ᎓") + str(r.success) + bstack1l1l11_opy_ (u"ࠢࠣ᎔"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨ᎕") + str(e) + bstack1l1l11_opy_ (u"ࠤࠥ᎖"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l11l1lll11_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def bstack1l11ll1llll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1ll1111ll11_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack1l1l11_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤ࡯࡮ࡪࡶ࠽ࠤࠧ᎗") + str(req) + bstack1l1l11_opy_ (u"ࠦࠧ᎘"))
        try:
            r = self.bstack1lll11111l1_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣ᎙") + str(r.success) + bstack1l1l11_opy_ (u"ࠨࠢ᎚"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧ᎛") + str(e) + bstack1l1l11_opy_ (u"ࠣࠤ᎜"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l11lll1l11_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def bstack1l11ll1ll11_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1ll1111ll11_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶ࠽ࠤࠧ᎝") + str(req) + bstack1l1l11_opy_ (u"ࠥࠦ᎞"))
        try:
            r = self.bstack1lll11111l1_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨ᎟") + str(r) + bstack1l1l11_opy_ (u"ࠧࠨᎠ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᎡ") + str(e) + bstack1l1l11_opy_ (u"ࠢࠣᎢ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l11ll11l1l_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def bstack1l11ll11lll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1ll1111ll11_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1l11_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰ࠻ࠢࠥᎣ") + str(req) + bstack1l1l11_opy_ (u"ࠤࠥᎤ"))
        try:
            r = self.bstack1lll11111l1_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧᎥ") + str(r) + bstack1l1l11_opy_ (u"ࠦࠧᎦ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᎧ") + str(e) + bstack1l1l11_opy_ (u"ࠨࠢᎨ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1lll1lll_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def bstack1l11lll1111_opy_(self, instance: bstack1llll1lllll_opy_, url: str, f: bstack1ll1ll111ll_opy_, kwargs):
        bstack1l11ll1l11l_opy_ = version.parse(f.framework_version)
        bstack1l11ll111ll_opy_ = kwargs.get(bstack1l1l11_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣᎩ"))
        bstack1l11l1ll11l_opy_ = kwargs.get(bstack1l1l11_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᎪ"))
        bstack1l1l11l1111_opy_ = {}
        bstack1l11l1lllll_opy_ = {}
        bstack1l11lll11l1_opy_ = None
        bstack1l11ll1l111_opy_ = {}
        if bstack1l11l1ll11l_opy_ is not None or bstack1l11ll111ll_opy_ is not None: # check top level caps
            if bstack1l11l1ll11l_opy_ is not None:
                bstack1l11ll1l111_opy_[bstack1l1l11_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᎫ")] = bstack1l11l1ll11l_opy_
            if bstack1l11ll111ll_opy_ is not None and callable(getattr(bstack1l11ll111ll_opy_, bstack1l1l11_opy_ (u"ࠥࡸࡴࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᎬ"))):
                bstack1l11ll1l111_opy_[bstack1l1l11_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࡤࡧࡳࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧᎭ")] = bstack1l11ll111ll_opy_.to_capabilities()
        response = self.bstack1l1l11l1l11_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1l11ll1l111_opy_).encode(bstack1l1l11_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᎮ")))
        if response is not None and response.capabilities:
            bstack1l1l11l1111_opy_ = json.loads(response.capabilities.decode(bstack1l1l11_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᎯ")))
            if not bstack1l1l11l1111_opy_: # empty caps bstack1l1l111l11l_opy_ bstack1l1l11l1ll1_opy_ bstack1l1l11l11l1_opy_ bstack1lll11ll1ll_opy_ or error in processing
                return
            bstack1l11lll11l1_opy_ = f.bstack1llll11l1ll_opy_[bstack1l1l11_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫࡟ࡰࡲࡷ࡭ࡴࡴࡳࡠࡨࡵࡳࡲࡥࡣࡢࡲࡶࠦᎰ")](bstack1l1l11l1111_opy_)
        if bstack1l11ll111ll_opy_ is not None and bstack1l11ll1l11l_opy_ >= version.parse(bstack1l1l11_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧᎱ")):
            bstack1l11l1lllll_opy_ = None
        if (
                not bstack1l11ll111ll_opy_ and not bstack1l11l1ll11l_opy_
        ) or (
                bstack1l11ll1l11l_opy_ < version.parse(bstack1l1l11_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨᎲ"))
        ):
            bstack1l11l1lllll_opy_ = {}
            bstack1l11l1lllll_opy_.update(bstack1l1l11l1111_opy_)
        self.logger.info(bstack11l1l1111l_opy_)
        if os.environ.get(bstack1l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓࠨᎳ")).lower().__eq__(bstack1l1l11_opy_ (u"ࠦࡹࡸࡵࡦࠤᎴ")):
            kwargs.update(
                {
                    bstack1l1l11_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣᎵ"): f.bstack1l11ll1ll1l_opy_,
                }
            )
        if bstack1l11ll1l11l_opy_ >= version.parse(bstack1l1l11_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭Ꮆ")):
            if bstack1l11l1ll11l_opy_ is not None:
                del kwargs[bstack1l1l11_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᎷ")]
            kwargs.update(
                {
                    bstack1l1l11_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᎸ"): bstack1l11lll11l1_opy_,
                    bstack1l1l11_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨᎹ"): True,
                    bstack1l1l11_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥᎺ"): None,
                }
            )
        elif bstack1l11ll1l11l_opy_ >= version.parse(bstack1l1l11_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪᎻ")):
            kwargs.update(
                {
                    bstack1l1l11_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᎼ"): bstack1l11l1lllll_opy_,
                    bstack1l1l11_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢᎽ"): bstack1l11lll11l1_opy_,
                    bstack1l1l11_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦᎾ"): True,
                    bstack1l1l11_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣᎿ"): None,
                }
            )
        elif bstack1l11ll1l11l_opy_ >= version.parse(bstack1l1l11_opy_ (u"ࠩ࠵࠲࠺࠹࠮࠱ࠩᏀ")):
            kwargs.update(
                {
                    bstack1l1l11_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᏁ"): bstack1l11l1lllll_opy_,
                    bstack1l1l11_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣᏂ"): True,
                    bstack1l1l11_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧᏃ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1l1l11_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᏄ"): bstack1l11l1lllll_opy_,
                    bstack1l1l11_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦᏅ"): True,
                    bstack1l1l11_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣᏆ"): None,
                }
            )