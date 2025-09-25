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
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack111l1l111l1_opy_
bstack11ll1111ll_opy_ = Config.bstack1lllll1ll1_opy_()
def bstack11111111ll1_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11111111111_opy_(bstack111111111l1_opy_, bstack11111111l1l_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack111111111l1_opy_):
        with open(bstack111111111l1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11111111ll1_opy_(bstack111111111l1_opy_):
        pac = get_pac(url=bstack111111111l1_opy_)
    else:
        raise Exception(bstack1l11l11_opy_ (u"ࠨࡒࡤࡧࠥ࡬ࡩ࡭ࡧࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠾ࠥࢁࡽࠨὂ").format(bstack111111111l1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1l11l11_opy_ (u"ࠤ࠻࠲࠽࠴࠸࠯࠺ࠥὃ"), 80))
        bstack11111111l11_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11111111l11_opy_ = bstack1l11l11_opy_ (u"ࠪ࠴࠳࠶࠮࠱࠰࠳ࠫὄ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11111111l1l_opy_, bstack11111111l11_opy_)
    return proxy_url
def bstack1ll1l11lll_opy_(config):
    return bstack1l11l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧὅ") in config or bstack1l11l11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ὆") in config
def bstack1llll111ll_opy_(config):
    if not bstack1ll1l11lll_opy_(config):
        return
    if config.get(bstack1l11l11_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ὇")):
        return config.get(bstack1l11l11_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪὈ"))
    if config.get(bstack1l11l11_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬὉ")):
        return config.get(bstack1l11l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭Ὂ"))
def bstack1lll111l1l_opy_(config, bstack11111111l1l_opy_):
    proxy = bstack1llll111ll_opy_(config)
    proxies = {}
    if config.get(bstack1l11l11_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭Ὃ")) or config.get(bstack1l11l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨὌ")):
        if proxy.endswith(bstack1l11l11_opy_ (u"ࠬ࠴ࡰࡢࡥࠪὍ")):
            proxies = bstack1111111l_opy_(proxy, bstack11111111l1l_opy_)
        else:
            proxies = {
                bstack1l11l11_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ὎"): proxy
            }
    bstack11ll1111ll_opy_.bstack1l1l11lll1_opy_(bstack1l11l11_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠧ὏"), proxies)
    return proxies
def bstack1111111l_opy_(bstack111111111l1_opy_, bstack11111111l1l_opy_):
    proxies = {}
    global bstack1111111111l_opy_
    if bstack1l11l11_opy_ (u"ࠨࡒࡄࡇࡤࡖࡒࡐ࡚࡜ࠫὐ") in globals():
        return bstack1111111111l_opy_
    try:
        proxy = bstack11111111111_opy_(bstack111111111l1_opy_, bstack11111111l1l_opy_)
        if bstack1l11l11_opy_ (u"ࠤࡇࡍࡗࡋࡃࡕࠤὑ") in proxy:
            proxies = {}
        elif bstack1l11l11_opy_ (u"ࠥࡌ࡙࡚ࡐࠣὒ") in proxy or bstack1l11l11_opy_ (u"ࠦࡍ࡚ࡔࡑࡕࠥὓ") in proxy or bstack1l11l11_opy_ (u"࡙ࠧࡏࡄࡍࡖࠦὔ") in proxy:
            bstack111111111ll_opy_ = proxy.split(bstack1l11l11_opy_ (u"ࠨࠠࠣὕ"))
            if bstack1l11l11_opy_ (u"ࠢ࠻࠱࠲ࠦὖ") in bstack1l11l11_opy_ (u"ࠣࠤὗ").join(bstack111111111ll_opy_[1:]):
                proxies = {
                    bstack1l11l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨ὘"): bstack1l11l11_opy_ (u"ࠥࠦὙ").join(bstack111111111ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l11l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪ὚"): str(bstack111111111ll_opy_[0]).lower() + bstack1l11l11_opy_ (u"ࠧࡀ࠯࠰ࠤὛ") + bstack1l11l11_opy_ (u"ࠨࠢ὜").join(bstack111111111ll_opy_[1:])
                }
        elif bstack1l11l11_opy_ (u"ࠢࡑࡔࡒ࡜࡞ࠨὝ") in proxy:
            bstack111111111ll_opy_ = proxy.split(bstack1l11l11_opy_ (u"ࠣࠢࠥ὞"))
            if bstack1l11l11_opy_ (u"ࠤ࠽࠳࠴ࠨὟ") in bstack1l11l11_opy_ (u"ࠥࠦὠ").join(bstack111111111ll_opy_[1:]):
                proxies = {
                    bstack1l11l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪὡ"): bstack1l11l11_opy_ (u"ࠧࠨὢ").join(bstack111111111ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l11l11_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬὣ"): bstack1l11l11_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣὤ") + bstack1l11l11_opy_ (u"ࠣࠤὥ").join(bstack111111111ll_opy_[1:])
                }
        else:
            proxies = {
                bstack1l11l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨὦ"): proxy
            }
    except Exception as e:
        print(bstack1l11l11_opy_ (u"ࠥࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢὧ"), bstack111l1l111l1_opy_.format(bstack111111111l1_opy_, str(e)))
    bstack1111111111l_opy_ = proxies
    return proxies