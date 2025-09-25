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
from browserstack_sdk.bstack111ll1l1_opy_ import bstack1lll1ll1ll_opy_
from browserstack_sdk.bstack1111l1lll1_opy_ import RobotHandler
def bstack11lll1ll11_opy_(framework):
    if framework.lower() == bstack1l11l11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭᫼"):
        return bstack1lll1ll1ll_opy_.version()
    elif framework.lower() == bstack1l11l11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭᫽"):
        return RobotHandler.version()
    elif framework.lower() == bstack1l11l11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ᫾"):
        import behave
        return behave.__version__
    else:
        return bstack1l11l11_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࠪ᫿")
def bstack11l1l1l111_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1l11l11_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬᬀ"))
        framework_version.append(importlib.metadata.version(bstack1l11l11_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨᬁ")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1l11l11_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᬂ"))
        framework_version.append(importlib.metadata.version(bstack1l11l11_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥᬃ")))
    except:
        pass
    return {
        bstack1l11l11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᬄ"): bstack1l11l11_opy_ (u"ࠨࡡࠪᬅ").join(framework_name),
        bstack1l11l11_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪᬆ"): bstack1l11l11_opy_ (u"ࠪࡣࠬᬇ").join(framework_version)
    }