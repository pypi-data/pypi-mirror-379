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
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11l11l11ll1_opy_, bstack11ll11111_opy_, bstack1l11111lll_opy_, bstack11ll1ll1l_opy_, \
    bstack11l11l1ll1l_opy_
from bstack_utils.measure import measure
def bstack111lllllll_opy_(bstack1lllll1l1ll1_opy_):
    for driver in bstack1lllll1l1ll1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l11l111ll_opy_, stage=STAGE.bstack1ll11lll_opy_)
def bstack1l1l1ll111_opy_(driver, status, reason=bstack1l1l11_opy_ (u"ࠫࠬ῭")):
    bstack1lll11l111_opy_ = Config.bstack1l11111l1l_opy_()
    if bstack1lll11l111_opy_.bstack11111ll111_opy_():
        return
    bstack1ll1ll1ll_opy_ = bstack1ll11lllll_opy_(bstack1l1l11_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ΅"), bstack1l1l11_opy_ (u"࠭ࠧ`"), status, reason, bstack1l1l11_opy_ (u"ࠧࠨ῰"), bstack1l1l11_opy_ (u"ࠨࠩ῱"))
    driver.execute_script(bstack1ll1ll1ll_opy_)
@measure(event_name=EVENTS.bstack1l11l111ll_opy_, stage=STAGE.bstack1ll11lll_opy_)
def bstack1l1l111l11_opy_(page, status, reason=bstack1l1l11_opy_ (u"ࠩࠪῲ")):
    try:
        if page is None:
            return
        bstack1lll11l111_opy_ = Config.bstack1l11111l1l_opy_()
        if bstack1lll11l111_opy_.bstack11111ll111_opy_():
            return
        bstack1ll1ll1ll_opy_ = bstack1ll11lllll_opy_(bstack1l1l11_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ῳ"), bstack1l1l11_opy_ (u"ࠫࠬῴ"), status, reason, bstack1l1l11_opy_ (u"ࠬ࠭῵"), bstack1l1l11_opy_ (u"࠭ࠧῶ"))
        page.evaluate(bstack1l1l11_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣῷ"), bstack1ll1ll1ll_opy_)
    except Exception as e:
        print(bstack1l1l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨῸ"), e)
def bstack1ll11lllll_opy_(type, name, status, reason, bstack11lllll1l_opy_, bstack11l1111l11_opy_):
    bstack11l111l1l1_opy_ = {
        bstack1l1l11_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩΌ"): type,
        bstack1l1l11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭Ὼ"): {}
    }
    if type == bstack1l1l11_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭Ώ"):
        bstack11l111l1l1_opy_[bstack1l1l11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨῼ")][bstack1l1l11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ´")] = bstack11lllll1l_opy_
        bstack11l111l1l1_opy_[bstack1l1l11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ῾")][bstack1l1l11_opy_ (u"ࠨࡦࡤࡸࡦ࠭῿")] = json.dumps(str(bstack11l1111l11_opy_))
    if type == bstack1l1l11_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ "):
        bstack11l111l1l1_opy_[bstack1l1l11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ ")][bstack1l1l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ ")] = name
    if type == bstack1l1l11_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ "):
        bstack11l111l1l1_opy_[bstack1l1l11_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ ")][bstack1l1l11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ ")] = status
        if status == bstack1l1l11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ ") and str(reason) != bstack1l1l11_opy_ (u"ࠤࠥ "):
            bstack11l111l1l1_opy_[bstack1l1l11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ ")][bstack1l1l11_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ ")] = json.dumps(str(reason))
    bstack1llllll1ll_opy_ = bstack1l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪ ").format(json.dumps(bstack11l111l1l1_opy_))
    return bstack1llllll1ll_opy_
def bstack11lllllll_opy_(url, config, logger, bstack1ll1lllll_opy_=False):
    hostname = bstack11ll11111_opy_(url)
    is_private = bstack11ll1ll1l_opy_(hostname)
    try:
        if is_private or bstack1ll1lllll_opy_:
            file_path = bstack11l11l11ll1_opy_(bstack1l1l11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭​"), bstack1l1l11_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭‌"), logger)
            if os.environ.get(bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭‍")) and eval(
                    os.environ.get(bstack1l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧ‎"))):
                return
            if (bstack1l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ‏") in config and not config[bstack1l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ‐")]):
                os.environ[bstack1l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪ‑")] = str(True)
                bstack1lllll1l1lll_opy_ = {bstack1l1l11_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ‒"): hostname}
                bstack11l11l1ll1l_opy_(bstack1l1l11_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭–"), bstack1l1l11_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭—"), bstack1lllll1l1lll_opy_, logger)
    except Exception as e:
        pass
def bstack1111ll1l_opy_(caps, bstack1lllll1ll11l_opy_):
    if bstack1l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ―") in caps:
        caps[bstack1l1l11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ‖")][bstack1l1l11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪ‗")] = True
        if bstack1lllll1ll11l_opy_:
            caps[bstack1l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭‘")][bstack1l1l11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ’")] = bstack1lllll1ll11l_opy_
    else:
        caps[bstack1l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬ‚")] = True
        if bstack1lllll1ll11l_opy_:
            caps[bstack1l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ‛")] = bstack1lllll1ll11l_opy_
def bstack1lllllll11ll_opy_(bstack111l1l1ll1_opy_):
    bstack1lllll1ll111_opy_ = bstack1l11111lll_opy_(threading.current_thread(), bstack1l1l11_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭“"), bstack1l1l11_opy_ (u"ࠪࠫ”"))
    if bstack1lllll1ll111_opy_ == bstack1l1l11_opy_ (u"ࠫࠬ„") or bstack1lllll1ll111_opy_ == bstack1l1l11_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭‟"):
        threading.current_thread().testStatus = bstack111l1l1ll1_opy_
    else:
        if bstack111l1l1ll1_opy_ == bstack1l1l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭†"):
            threading.current_thread().testStatus = bstack111l1l1ll1_opy_