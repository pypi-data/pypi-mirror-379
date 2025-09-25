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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111lll1l11l_opy_, bstack111lllll1_opy_, bstack1lll1lll11_opy_, bstack1l1111l1l1_opy_, \
    bstack11l111lll11_opy_
from bstack_utils.measure import measure
def bstack11l111ll1l_opy_(bstack1lllll1l1lll_opy_):
    for driver in bstack1lllll1l1lll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11ll111l1_opy_, stage=STAGE.bstack1lll1111l_opy_)
def bstack1l11111l_opy_(driver, status, reason=bstack1l11l11_opy_ (u"ࠫࠬ῭")):
    bstack11ll1111ll_opy_ = Config.bstack1lllll1ll1_opy_()
    if bstack11ll1111ll_opy_.bstack11111ll1ll_opy_():
        return
    bstack11l111111_opy_ = bstack1ll111111_opy_(bstack1l11l11_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ΅"), bstack1l11l11_opy_ (u"࠭ࠧ`"), status, reason, bstack1l11l11_opy_ (u"ࠧࠨ῰"), bstack1l11l11_opy_ (u"ࠨࠩ῱"))
    driver.execute_script(bstack11l111111_opy_)
@measure(event_name=EVENTS.bstack11ll111l1_opy_, stage=STAGE.bstack1lll1111l_opy_)
def bstack1l1l1ll111_opy_(page, status, reason=bstack1l11l11_opy_ (u"ࠩࠪῲ")):
    try:
        if page is None:
            return
        bstack11ll1111ll_opy_ = Config.bstack1lllll1ll1_opy_()
        if bstack11ll1111ll_opy_.bstack11111ll1ll_opy_():
            return
        bstack11l111111_opy_ = bstack1ll111111_opy_(bstack1l11l11_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ῳ"), bstack1l11l11_opy_ (u"ࠫࠬῴ"), status, reason, bstack1l11l11_opy_ (u"ࠬ࠭῵"), bstack1l11l11_opy_ (u"࠭ࠧῶ"))
        page.evaluate(bstack1l11l11_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣῷ"), bstack11l111111_opy_)
    except Exception as e:
        print(bstack1l11l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨῸ"), e)
def bstack1ll111111_opy_(type, name, status, reason, bstack111llll1l1_opy_, bstack1ll11l1ll_opy_):
    bstack11l111llll_opy_ = {
        bstack1l11l11_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩΌ"): type,
        bstack1l11l11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭Ὼ"): {}
    }
    if type == bstack1l11l11_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭Ώ"):
        bstack11l111llll_opy_[bstack1l11l11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨῼ")][bstack1l11l11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ´")] = bstack111llll1l1_opy_
        bstack11l111llll_opy_[bstack1l11l11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ῾")][bstack1l11l11_opy_ (u"ࠨࡦࡤࡸࡦ࠭῿")] = json.dumps(str(bstack1ll11l1ll_opy_))
    if type == bstack1l11l11_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ "):
        bstack11l111llll_opy_[bstack1l11l11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ ")][bstack1l11l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ ")] = name
    if type == bstack1l11l11_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ "):
        bstack11l111llll_opy_[bstack1l11l11_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ ")][bstack1l11l11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ ")] = status
        if status == bstack1l11l11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ ") and str(reason) != bstack1l11l11_opy_ (u"ࠤࠥ "):
            bstack11l111llll_opy_[bstack1l11l11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ ")][bstack1l11l11_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ ")] = json.dumps(str(reason))
    bstack1llll1lll1_opy_ = bstack1l11l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪ ").format(json.dumps(bstack11l111llll_opy_))
    return bstack1llll1lll1_opy_
def bstack111ll1l1l_opy_(url, config, logger, bstack11111llll_opy_=False):
    hostname = bstack111lllll1_opy_(url)
    is_private = bstack1l1111l1l1_opy_(hostname)
    try:
        if is_private or bstack11111llll_opy_:
            file_path = bstack111lll1l11l_opy_(bstack1l11l11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭​"), bstack1l11l11_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭‌"), logger)
            if os.environ.get(bstack1l11l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭‍")) and eval(
                    os.environ.get(bstack1l11l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧ‎"))):
                return
            if (bstack1l11l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ‏") in config and not config[bstack1l11l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ‐")]):
                os.environ[bstack1l11l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪ‑")] = str(True)
                bstack1lllll1ll11l_opy_ = {bstack1l11l11_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ‒"): hostname}
                bstack11l111lll11_opy_(bstack1l11l11_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭–"), bstack1l11l11_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭—"), bstack1lllll1ll11l_opy_, logger)
    except Exception as e:
        pass
def bstack1l11l11l_opy_(caps, bstack1lllll1ll111_opy_):
    if bstack1l11l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ―") in caps:
        caps[bstack1l11l11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ‖")][bstack1l11l11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪ‗")] = True
        if bstack1lllll1ll111_opy_:
            caps[bstack1l11l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭‘")][bstack1l11l11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ’")] = bstack1lllll1ll111_opy_
    else:
        caps[bstack1l11l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬ‚")] = True
        if bstack1lllll1ll111_opy_:
            caps[bstack1l11l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ‛")] = bstack1lllll1ll111_opy_
def bstack1lllllllll11_opy_(bstack111l1ll111_opy_):
    bstack1lllll1l1ll1_opy_ = bstack1lll1lll11_opy_(threading.current_thread(), bstack1l11l11_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭“"), bstack1l11l11_opy_ (u"ࠪࠫ”"))
    if bstack1lllll1l1ll1_opy_ == bstack1l11l11_opy_ (u"ࠫࠬ„") or bstack1lllll1l1ll1_opy_ == bstack1l11l11_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭‟"):
        threading.current_thread().testStatus = bstack111l1ll111_opy_
    else:
        if bstack111l1ll111_opy_ == bstack1l11l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭†"):
            threading.current_thread().testStatus = bstack111l1ll111_opy_