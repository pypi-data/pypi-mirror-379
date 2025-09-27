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
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack111l11lllll_opy_
bstack1lll11l111_opy_ = Config.bstack1l11111l1l_opy_()
def bstack111111111l1_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1111111111l_opy_(bstack11111111ll1_opy_, bstack11111111l1l_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11111111ll1_opy_):
        with open(bstack11111111ll1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack111111111l1_opy_(bstack11111111ll1_opy_):
        pac = get_pac(url=bstack11111111ll1_opy_)
    else:
        raise Exception(bstack1l1l11_opy_ (u"ࠨࡒࡤࡧࠥ࡬ࡩ࡭ࡧࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠾ࠥࢁࡽࠨὂ").format(bstack11111111ll1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1l1l11_opy_ (u"ࠤ࠻࠲࠽࠴࠸࠯࠺ࠥὃ"), 80))
        bstack111111111ll_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack111111111ll_opy_ = bstack1l1l11_opy_ (u"ࠪ࠴࠳࠶࠮࠱࠰࠳ࠫὄ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11111111l1l_opy_, bstack111111111ll_opy_)
    return proxy_url
def bstack1llll1lll1_opy_(config):
    return bstack1l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧὅ") in config or bstack1l1l11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ὆") in config
def bstack1l11l11ll1_opy_(config):
    if not bstack1llll1lll1_opy_(config):
        return
    if config.get(bstack1l1l11_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ὇")):
        return config.get(bstack1l1l11_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪὈ"))
    if config.get(bstack1l1l11_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬὉ")):
        return config.get(bstack1l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭Ὂ"))
def bstack1l1l11111_opy_(config, bstack11111111l1l_opy_):
    proxy = bstack1l11l11ll1_opy_(config)
    proxies = {}
    if config.get(bstack1l1l11_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭Ὃ")) or config.get(bstack1l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨὌ")):
        if proxy.endswith(bstack1l1l11_opy_ (u"ࠬ࠴ࡰࡢࡥࠪὍ")):
            proxies = bstack1l1111ll1_opy_(proxy, bstack11111111l1l_opy_)
        else:
            proxies = {
                bstack1l1l11_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ὎"): proxy
            }
    bstack1lll11l111_opy_.bstack11lll11ll_opy_(bstack1l1l11_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠧ὏"), proxies)
    return proxies
def bstack1l1111ll1_opy_(bstack11111111ll1_opy_, bstack11111111l1l_opy_):
    proxies = {}
    global bstack11111111111_opy_
    if bstack1l1l11_opy_ (u"ࠨࡒࡄࡇࡤࡖࡒࡐ࡚࡜ࠫὐ") in globals():
        return bstack11111111111_opy_
    try:
        proxy = bstack1111111111l_opy_(bstack11111111ll1_opy_, bstack11111111l1l_opy_)
        if bstack1l1l11_opy_ (u"ࠤࡇࡍࡗࡋࡃࡕࠤὑ") in proxy:
            proxies = {}
        elif bstack1l1l11_opy_ (u"ࠥࡌ࡙࡚ࡐࠣὒ") in proxy or bstack1l1l11_opy_ (u"ࠦࡍ࡚ࡔࡑࡕࠥὓ") in proxy or bstack1l1l11_opy_ (u"࡙ࠧࡏࡄࡍࡖࠦὔ") in proxy:
            bstack11111111l11_opy_ = proxy.split(bstack1l1l11_opy_ (u"ࠨࠠࠣὕ"))
            if bstack1l1l11_opy_ (u"ࠢ࠻࠱࠲ࠦὖ") in bstack1l1l11_opy_ (u"ࠣࠤὗ").join(bstack11111111l11_opy_[1:]):
                proxies = {
                    bstack1l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨ὘"): bstack1l1l11_opy_ (u"ࠥࠦὙ").join(bstack11111111l11_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪ὚"): str(bstack11111111l11_opy_[0]).lower() + bstack1l1l11_opy_ (u"ࠧࡀ࠯࠰ࠤὛ") + bstack1l1l11_opy_ (u"ࠨࠢ὜").join(bstack11111111l11_opy_[1:])
                }
        elif bstack1l1l11_opy_ (u"ࠢࡑࡔࡒ࡜࡞ࠨὝ") in proxy:
            bstack11111111l11_opy_ = proxy.split(bstack1l1l11_opy_ (u"ࠣࠢࠥ὞"))
            if bstack1l1l11_opy_ (u"ࠤ࠽࠳࠴ࠨὟ") in bstack1l1l11_opy_ (u"ࠥࠦὠ").join(bstack11111111l11_opy_[1:]):
                proxies = {
                    bstack1l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪὡ"): bstack1l1l11_opy_ (u"ࠧࠨὢ").join(bstack11111111l11_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l1l11_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬὣ"): bstack1l1l11_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣὤ") + bstack1l1l11_opy_ (u"ࠣࠤὥ").join(bstack11111111l11_opy_[1:])
                }
        else:
            proxies = {
                bstack1l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨὦ"): proxy
            }
    except Exception as e:
        print(bstack1l1l11_opy_ (u"ࠥࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢὧ"), bstack111l11lllll_opy_.format(bstack11111111ll1_opy_, str(e)))
    bstack11111111111_opy_ = proxies
    return proxies