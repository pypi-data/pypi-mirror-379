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
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llllllll1l_opy_,
    bstack1llll1lllll_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1ll1l1l11l1_opy_ import bstack1lll1ll1111_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack11l1l1111l_opy_
from bstack_utils.helper import bstack1l1ll1l11ll_opy_
import threading
import os
import urllib.parse
class bstack1lll1ll1l11_opy_(bstack1llll11lll1_opy_):
    def __init__(self, bstack1ll1l1lll11_opy_):
        super().__init__()
        bstack1lll1ll1111_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1llll1lll1l_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1l1l11ll111_opy_)
        bstack1lll1ll1111_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1llll1lll1l_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1l1l11ll11l_opy_)
        bstack1lll1ll1111_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1llllllllll_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1l1l11l111l_opy_)
        bstack1lll1ll1111_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1lllll1ll1l_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1l1l111ll1l_opy_)
        bstack1lll1ll1111_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.bstack1llll1lll1l_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1l1l111l1ll_opy_)
        bstack1lll1ll1111_opy_.bstack1ll111l11l1_opy_((bstack1lllll1lll1_opy_.QUIT, bstack1llllllll1l_opy_.PRE), self.on_close)
        self.bstack1ll1l1lll11_opy_ = bstack1ll1l1lll11_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1l1l11ll111_opy_(
        self,
        f: bstack1lll1ll1111_opy_,
        bstack1l1l11l1l1l_opy_: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l11_opy_ (u"ࠤ࡯ࡥࡺࡴࡣࡩࠤዼ"):
            return
        if not bstack1l1ll1l11ll_opy_():
            self.logger.debug(bstack1l1l11_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢ࡯ࡥࡺࡴࡣࡩࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢዽ"))
            return
        def wrapped(bstack1l1l11l1l1l_opy_, launch, *args, **kwargs):
            response = self.bstack1l1l11l1l11_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l1l11_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪዾ"): True}).encode(bstack1l1l11_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦዿ")))
            if response is not None and response.capabilities:
                if not bstack1l1ll1l11ll_opy_():
                    browser = launch(bstack1l1l11l1l1l_opy_)
                    return browser
                bstack1l1l11l1111_opy_ = json.loads(response.capabilities.decode(bstack1l1l11_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧጀ")))
                if not bstack1l1l11l1111_opy_: # empty caps bstack1l1l111l11l_opy_ bstack1l1l11l1ll1_opy_ bstack1l1l11l11l1_opy_ bstack1lll11ll1ll_opy_ or error in processing
                    return
                bstack1l1l111lll1_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1l1l11l1111_opy_))
                f.bstack1llll1l1ll1_opy_(instance, bstack1lll1ll1111_opy_.bstack1l1l111l1l1_opy_, bstack1l1l111lll1_opy_)
                f.bstack1llll1l1ll1_opy_(instance, bstack1lll1ll1111_opy_.bstack1l1l1111lll_opy_, bstack1l1l11l1111_opy_)
                browser = bstack1l1l11l1l1l_opy_.connect(bstack1l1l111lll1_opy_)
                return browser
        return wrapped
    def bstack1l1l11l111l_opy_(
        self,
        f: bstack1lll1ll1111_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l11_opy_ (u"ࠢࡥ࡫ࡶࡴࡦࡺࡣࡩࠤጁ"):
            self.logger.debug(bstack1l1l11_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠࡥ࡫ࡶࡴࡦࡺࡣࡩࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢጂ"))
            return
        if not bstack1l1ll1l11ll_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1l1l11_opy_ (u"ࠩࡳࡥࡷࡧ࡭ࡴࠩጃ"), {}).get(bstack1l1l11_opy_ (u"ࠪࡦࡸࡖࡡࡳࡣࡰࡷࠬጄ")):
                    bstack1l1l111l111_opy_ = args[0][bstack1l1l11_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦጅ")][bstack1l1l11_opy_ (u"ࠧࡨࡳࡑࡣࡵࡥࡲࡹࠢጆ")]
                    session_id = bstack1l1l111l111_opy_.get(bstack1l1l11_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴࡉࡥࠤጇ"))
                    f.bstack1llll1l1ll1_opy_(instance, bstack1lll1ll1111_opy_.bstack1l1l111llll_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡤࡪࡵࡳࡥࡹࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࠥገ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1l1l111l1ll_opy_(
        self,
        f: bstack1lll1ll1111_opy_,
        bstack1l1l11l1l1l_opy_: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l11_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࠤጉ"):
            return
        if not bstack1l1ll1l11ll_opy_():
            self.logger.debug(bstack1l1l11_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡥࡲࡲࡳ࡫ࡣࡵࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢጊ"))
            return
        def wrapped(bstack1l1l11l1l1l_opy_, connect, *args, **kwargs):
            response = self.bstack1l1l11l1l11_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l1l11_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩጋ"): True}).encode(bstack1l1l11_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥጌ")))
            if response is not None and response.capabilities:
                bstack1l1l11l1111_opy_ = json.loads(response.capabilities.decode(bstack1l1l11_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦግ")))
                if not bstack1l1l11l1111_opy_:
                    return
                bstack1l1l111lll1_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1l1l11l1111_opy_))
                if bstack1l1l11l1111_opy_.get(bstack1l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬጎ")):
                    browser = bstack1l1l11l1l1l_opy_.bstack1l1l11l11ll_opy_(bstack1l1l111lll1_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1l1l111lll1_opy_
                    return connect(bstack1l1l11l1l1l_opy_, *args, **kwargs)
        return wrapped
    def bstack1l1l11ll11l_opy_(
        self,
        f: bstack1lll1ll1111_opy_,
        bstack1l1llll111l_opy_: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l11_opy_ (u"ࠢ࡯ࡧࡺࡣࡵࡧࡧࡦࠤጏ"):
            return
        if not bstack1l1ll1l11ll_opy_():
            self.logger.debug(bstack1l1l11_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠ࡯ࡧࡺࡣࡵࡧࡧࡦࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢጐ"))
            return
        def wrapped(bstack1l1llll111l_opy_, bstack1l1l111ll11_opy_, *args, **kwargs):
            contexts = bstack1l1llll111l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1l1l11_opy_ (u"ࠤࡤࡦࡴࡻࡴ࠻ࡤ࡯ࡥࡳࡱࠢ጑") in page.url:
                                    return page
                    else:
                        return bstack1l1l111ll11_opy_(bstack1l1llll111l_opy_)
        return wrapped
    def bstack1l1l11l1l11_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1l1l11_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱ࡭ࡹࡀࠠࠣጒ") + str(req) + bstack1l1l11_opy_ (u"ࠦࠧጓ"))
        try:
            r = self.bstack1lll11111l1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l1l11_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣጔ") + str(r.success) + bstack1l1l11_opy_ (u"ࠨࠢጕ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l11_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧ጖") + str(e) + bstack1l1l11_opy_ (u"ࠣࠤ጗"))
            traceback.print_exc()
            raise e
    def bstack1l1l111ll1l_opy_(
        self,
        f: bstack1lll1ll1111_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l11_opy_ (u"ࠤࡢࡷࡪࡴࡤࡠ࡯ࡨࡷࡸࡧࡧࡦࡡࡷࡳࡤࡹࡥࡳࡸࡨࡶࠧጘ"):
            return
        if not bstack1l1ll1l11ll_opy_():
            return
        def wrapped(Connection, bstack1l1l11l1lll_opy_, *args, **kwargs):
            return bstack1l1l11l1lll_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1ll1111_opy_,
        bstack1l1l11l1l1l_opy_: object,
        exec: Tuple[bstack1llll1lllll_opy_, str],
        bstack1lllll11ll1_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l11_opy_ (u"ࠥࡧࡱࡵࡳࡦࠤጙ"):
            return
        if not bstack1l1ll1l11ll_opy_():
            self.logger.debug(bstack1l1l11_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡧࡱࡵࡳࡦࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢጚ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped