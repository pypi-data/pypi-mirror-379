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
import re
from bstack_utils.bstack11llllll1_opy_ import bstack1lllllllll11_opy_
def bstack1llllllll111_opy_(fixture_name):
    if fixture_name.startswith(bstack1l11l11_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭Ὠ")):
        return bstack1l11l11_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭Ὡ")
    elif fixture_name.startswith(bstack1l11l11_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭Ὢ")):
        return bstack1l11l11_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳࡭ࡰࡦࡸࡰࡪ࠭Ὣ")
    elif fixture_name.startswith(bstack1l11l11_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭Ὤ")):
        return bstack1l11l11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭Ὥ")
    elif fixture_name.startswith(bstack1l11l11_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨὮ")):
        return bstack1l11l11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳࡭ࡰࡦࡸࡰࡪ࠭Ὧ")
def bstack1llllllll11l_opy_(fixture_name):
    return bool(re.match(bstack1l11l11_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࠫࡪࡺࡴࡣࡵ࡫ࡲࡲࢁࡳ࡯ࡥࡷ࡯ࡩ࠮ࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪὰ"), fixture_name))
def bstack1lllllllllll_opy_(fixture_name):
    return bool(re.match(bstack1l11l11_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࡣ࠳࠰ࠧά"), fixture_name))
def bstack1lllllllll1l_opy_(fixture_name):
    return bool(re.match(bstack1l11l11_opy_ (u"ࠧ࡟ࡡࡻࡹࡳ࡯ࡴࡠࠪࡶࡩࡹࡻࡰࡽࡶࡨࡥࡷࡪ࡯ࡸࡰࠬࡣࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࡣ࠳࠰ࠧὲ"), fixture_name))
def bstack1lllllll1ll1_opy_(fixture_name):
    if fixture_name.startswith(bstack1l11l11_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪέ")):
        return bstack1l11l11_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪὴ"), bstack1l11l11_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨή")
    elif fixture_name.startswith(bstack1l11l11_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫὶ")):
        return bstack1l11l11_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱ࡲࡵࡤࡶ࡮ࡨࠫί"), bstack1l11l11_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎࠪὸ")
    elif fixture_name.startswith(bstack1l11l11_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬό")):
        return bstack1l11l11_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬὺ"), bstack1l11l11_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ύ")
    elif fixture_name.startswith(bstack1l11l11_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ὼ")):
        return bstack1l11l11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳࡭ࡰࡦࡸࡰࡪ࠭ώ"), bstack1l11l11_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨ὾")
    return None, None
def bstack1lllllll1lll_opy_(hook_name):
    if hook_name in [bstack1l11l11_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ὿"), bstack1l11l11_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᾀ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1llllllll1ll_opy_(hook_name):
    if hook_name in [bstack1l11l11_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᾁ"), bstack1l11l11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨᾂ")]:
        return bstack1l11l11_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᾃ")
    elif hook_name in [bstack1l11l11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᾄ"), bstack1l11l11_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪᾅ")]:
        return bstack1l11l11_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎࠪᾆ")
    elif hook_name in [bstack1l11l11_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫᾇ"), bstack1l11l11_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪᾈ")]:
        return bstack1l11l11_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᾉ")
    elif hook_name in [bstack1l11l11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬᾊ"), bstack1l11l11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬᾋ")]:
        return bstack1l11l11_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨᾌ")
    return hook_name
def bstack1llllllll1l1_opy_(node, scenario):
    if hasattr(node, bstack1l11l11_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨᾍ")):
        parts = node.nodeid.rsplit(bstack1l11l11_opy_ (u"ࠢ࡜ࠤᾎ"))
        params = parts[-1]
        return bstack1l11l11_opy_ (u"ࠣࡽࢀࠤࡠࢁࡽࠣᾏ").format(scenario.name, params)
    return scenario.name
def bstack1lllllll1l1l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1l11l11_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫᾐ")):
            examples = list(node.callspec.params[bstack1l11l11_opy_ (u"ࠪࡣࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡧࡻࡥࡲࡶ࡬ࡦࠩᾑ")].values())
        return examples
    except:
        return []
def bstack1lllllll11ll_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1lllllll1l11_opy_(report):
    try:
        status = bstack1l11l11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᾒ")
        if report.passed or (report.failed and hasattr(report, bstack1l11l11_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢᾓ"))):
            status = bstack1l11l11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᾔ")
        elif report.skipped:
            status = bstack1l11l11_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᾕ")
        bstack1lllllllll11_opy_(status)
    except:
        pass
def bstack111llll11_opy_(status):
    try:
        bstack1llllllllll1_opy_ = bstack1l11l11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᾖ")
        if status == bstack1l11l11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᾗ"):
            bstack1llllllllll1_opy_ = bstack1l11l11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᾘ")
        elif status == bstack1l11l11_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᾙ"):
            bstack1llllllllll1_opy_ = bstack1l11l11_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᾚ")
        bstack1lllllllll11_opy_(bstack1llllllllll1_opy_)
    except:
        pass
def bstack1lllllll11l1_opy_(item=None, report=None, summary=None, extra=None):
    return