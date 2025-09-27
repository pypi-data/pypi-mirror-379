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
from browserstack_sdk.bstack1l11lllll_opy_ import bstack11ll111lll_opy_
from browserstack_sdk.bstack111l11ll11_opy_ import RobotHandler
def bstack11l111ll_opy_(framework):
    if framework.lower() == bstack1l1l11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭᫼"):
        return bstack11ll111lll_opy_.version()
    elif framework.lower() == bstack1l1l11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭᫽"):
        return RobotHandler.version()
    elif framework.lower() == bstack1l1l11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ᫾"):
        import behave
        return behave.__version__
    else:
        return bstack1l1l11_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࠪ᫿")
def bstack11lllll111_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1l1l11_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬᬀ"))
        framework_version.append(importlib.metadata.version(bstack1l1l11_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨᬁ")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1l1l11_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᬂ"))
        framework_version.append(importlib.metadata.version(bstack1l1l11_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥᬃ")))
    except:
        pass
    return {
        bstack1l1l11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᬄ"): bstack1l1l11_opy_ (u"ࠨࡡࠪᬅ").join(framework_name),
        bstack1l1l11_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪᬆ"): bstack1l1l11_opy_ (u"ࠪࡣࠬᬇ").join(framework_version)
    }