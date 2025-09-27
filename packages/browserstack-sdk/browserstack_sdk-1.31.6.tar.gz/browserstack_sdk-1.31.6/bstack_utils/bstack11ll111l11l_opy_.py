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
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11l1l1l1lll_opy_
logger = logging.getLogger(__name__)
class bstack11ll111l1ll_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack1lllll1llll1_opy_ = urljoin(builder, bstack1l1l11_opy_ (u"ࠫ࡮ࡹࡳࡶࡧࡶࠫᾠ"))
        if params:
            bstack1lllll1llll1_opy_ += bstack1l1l11_opy_ (u"ࠧࡅࡻࡾࠤᾡ").format(urlencode({bstack1l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᾢ"): params.get(bstack1l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᾣ"))}))
        return bstack11ll111l1ll_opy_.bstack1llllll111ll_opy_(bstack1lllll1llll1_opy_)
    @staticmethod
    def bstack11ll111ll11_opy_(builder,params=None):
        bstack1lllll1llll1_opy_ = urljoin(builder, bstack1l1l11_opy_ (u"ࠨ࡫ࡶࡷࡺ࡫ࡳ࠮ࡵࡸࡱࡲࡧࡲࡺࠩᾤ"))
        if params:
            bstack1lllll1llll1_opy_ += bstack1l1l11_opy_ (u"ࠤࡂࡿࢂࠨᾥ").format(urlencode({bstack1l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᾦ"): params.get(bstack1l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᾧ"))}))
        return bstack11ll111l1ll_opy_.bstack1llllll111ll_opy_(bstack1lllll1llll1_opy_)
    @staticmethod
    def bstack1llllll111ll_opy_(bstack1llllll111l1_opy_):
        bstack1llllll11ll1_opy_ = os.environ.get(bstack1l1l11_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᾨ"), os.environ.get(bstack1l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᾩ"), bstack1l1l11_opy_ (u"ࠧࠨᾪ")))
        headers = {bstack1l1l11_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᾫ"): bstack1l1l11_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᾬ").format(bstack1llllll11ll1_opy_)}
        response = requests.get(bstack1llllll111l1_opy_, headers=headers)
        bstack1llllll11l1l_opy_ = {}
        try:
            bstack1llllll11l1l_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1l1l11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᾭ").format(e))
            pass
        if bstack1llllll11l1l_opy_ is not None:
            bstack1llllll11l1l_opy_[bstack1l1l11_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᾮ")] = response.headers.get(bstack1l1l11_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᾯ"), str(int(datetime.now().timestamp() * 1000)))
            bstack1llllll11l1l_opy_[bstack1l1l11_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᾰ")] = response.status_code
        return bstack1llllll11l1l_opy_
    @staticmethod
    def bstack1llllll1111l_opy_(bstack1llllll11l11_opy_, data):
        logger.debug(bstack1l1l11_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡗ࡫ࡱࡶࡧࡶࡸࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࡙ࡰ࡭࡫ࡷࡘࡪࡹࡴࡴࠤᾱ"))
        return bstack11ll111l1ll_opy_.bstack1lllll1lllll_opy_(bstack1l1l11_opy_ (u"ࠨࡒࡒࡗ࡙࠭ᾲ"), bstack1llllll11l11_opy_, data=data)
    @staticmethod
    def bstack1llllll11111_opy_(bstack1llllll11l11_opy_, data):
        logger.debug(bstack1l1l11_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡒࡦࡳࡸࡩࡸࡺࠠࡧࡱࡵࠤ࡬࡫ࡴࡕࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡷࡪࡥࡳࡧࡧࡘࡪࡹࡴࡴࠤᾳ"))
        res = bstack11ll111l1ll_opy_.bstack1lllll1lllll_opy_(bstack1l1l11_opy_ (u"ࠪࡋࡊ࡚ࠧᾴ"), bstack1llllll11l11_opy_, data=data)
        return res
    @staticmethod
    def bstack1lllll1lllll_opy_(method, bstack1llllll11l11_opy_, data=None, params=None, extra_headers=None):
        bstack1llllll11ll1_opy_ = os.environ.get(bstack1l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ᾵"), bstack1l1l11_opy_ (u"ࠬ࠭ᾶ"))
        headers = {
            bstack1l1l11_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᾷ"): bstack1l1l11_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᾸ").format(bstack1llllll11ll1_opy_),
            bstack1l1l11_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᾹ"): bstack1l1l11_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᾺ"),
            bstack1l1l11_opy_ (u"ࠪࡅࡨࡩࡥࡱࡶࠪΆ"): bstack1l1l11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᾼ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11l1l1l1lll_opy_ + bstack1l1l11_opy_ (u"ࠧ࠵ࠢ᾽") + bstack1llllll11l11_opy_.lstrip(bstack1l1l11_opy_ (u"࠭࠯ࠨι"))
        try:
            if method == bstack1l1l11_opy_ (u"ࠧࡈࡇࡗࠫ᾿"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack1l1l11_opy_ (u"ࠨࡒࡒࡗ࡙࠭῀"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack1l1l11_opy_ (u"ࠩࡓ࡙࡙࠭῁"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack1l1l11_opy_ (u"࡙ࠥࡳࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡊࡗࡘࡕࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠠࡼࡿࠥῂ").format(method))
            logger.debug(bstack1l1l11_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡳࡡࡥࡧࠣࡸࡴࠦࡕࡓࡎ࠽ࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡳࡥࡵࡪࡲࡨ࠿ࠦࡻࡾࠤῃ").format(url, method))
            bstack1llllll11l1l_opy_ = {}
            try:
                bstack1llllll11l1l_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack1l1l11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤῄ").format(e, response.text))
            if bstack1llllll11l1l_opy_ is not None:
                bstack1llllll11l1l_opy_[bstack1l1l11_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧ῅")] = response.headers.get(
                    bstack1l1l11_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨῆ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack1llllll11l1l_opy_[bstack1l1l11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨῇ")] = response.status_code
            return bstack1llllll11l1l_opy_
        except Exception as e:
            logger.error(bstack1l1l11_opy_ (u"ࠤࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡵࡩࡶࡻࡥࡴࡶࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࢀࢃࠠ࠮ࠢࡾࢁࠧῈ").format(e, url))
            return None
    @staticmethod
    def bstack11l1l11llll_opy_(bstack1llllll111l1_opy_, data):
        bstack1l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡔࡧࡱࡨࡸࠦࡡࠡࡒࡘࡘࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡶ࡫ࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣΈ")
        bstack1llllll11ll1_opy_ = os.environ.get(bstack1l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨῊ"), bstack1l1l11_opy_ (u"ࠬ࠭Ή"))
        headers = {
            bstack1l1l11_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ῌ"): bstack1l1l11_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪ῍").format(bstack1llllll11ll1_opy_),
            bstack1l1l11_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ῎"): bstack1l1l11_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ῏")
        }
        response = requests.put(bstack1llllll111l1_opy_, headers=headers, json=data)
        bstack1llllll11l1l_opy_ = {}
        try:
            bstack1llllll11l1l_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1l1l11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤῐ").format(e))
            pass
        logger.debug(bstack1l1l11_opy_ (u"ࠦࡗ࡫ࡱࡶࡧࡶࡸ࡚ࡺࡩ࡭ࡵ࠽ࠤࡵࡻࡴࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨῑ").format(bstack1llllll11l1l_opy_))
        if bstack1llllll11l1l_opy_ is not None:
            bstack1llllll11l1l_opy_[bstack1l1l11_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ῒ")] = response.headers.get(
                bstack1l1l11_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧΐ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack1llllll11l1l_opy_[bstack1l1l11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ῔")] = response.status_code
        return bstack1llllll11l1l_opy_
    @staticmethod
    def bstack11l1l1111l1_opy_(bstack1llllll111l1_opy_):
        bstack1l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤ࡙ࠥࡥ࡯ࡦࡶࠤࡦࠦࡇࡆࡖࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡨࡧࡷࠤࡹ࡮ࡥࠡࡥࡲࡹࡳࡺࠠࡰࡨࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ῕")
        bstack1llllll11ll1_opy_ = os.environ.get(bstack1l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ῖ"), bstack1l1l11_opy_ (u"ࠪࠫῗ"))
        headers = {
            bstack1l1l11_opy_ (u"ࠫࡦࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫῘ"): bstack1l1l11_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨῙ").format(bstack1llllll11ll1_opy_),
            bstack1l1l11_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬῚ"): bstack1l1l11_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪΊ")
        }
        response = requests.get(bstack1llllll111l1_opy_, headers=headers)
        bstack1llllll11l1l_opy_ = {}
        try:
            bstack1llllll11l1l_opy_ = response.json()
            logger.debug(bstack1l1l11_opy_ (u"ࠣࡔࡨࡵࡺ࡫ࡳࡵࡗࡷ࡭ࡱࡹ࠺ࠡࡩࡨࡸࡤ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥ῜").format(bstack1llllll11l1l_opy_))
        except Exception as e:
            logger.debug(bstack1l1l11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡏ࡙ࡏࡏࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠡ࠯ࠣࡿࢂࠨ῝").format(e, response.text))
            pass
        if bstack1llllll11l1l_opy_ is not None:
            bstack1llllll11l1l_opy_[bstack1l1l11_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫ῞")] = response.headers.get(
                bstack1l1l11_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬ῟"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack1llllll11l1l_opy_[bstack1l1l11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬῠ")] = response.status_code
        return bstack1llllll11l1l_opy_
    @staticmethod
    def bstack111l111l1ll_opy_(bstack11ll11l111l_opy_, payload):
        bstack1l1l11_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡑࡦࡱࡥࡴࠢࡤࠤࡕࡕࡓࡕࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡴࡩࡧࠣࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡧࡻࡩ࡭ࡦ࠰ࡨࡦࡺࡡࠡࡧࡱࡨࡵࡵࡩ࡯ࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡨࡲࡩࡶ࡯ࡪࡰࡷࠤ࠭ࡹࡴࡳࠫ࠽ࠤ࡙࡮ࡥࠡࡃࡓࡍࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺࠠࡱࡣࡷ࡬࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡵࡧࡹ࡭ࡱࡤࡨࠥ࠮ࡤࡪࡥࡷ࠭࠿ࠦࡔࡩࡧࠣࡶࡪࡷࡵࡦࡵࡷࠤࡵࡧࡹ࡭ࡱࡤࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡅࡕࡏࠬࠡࡱࡵࠤࡓࡵ࡮ࡦࠢ࡬ࡪࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥῡ")
        try:
            url = bstack1l1l11_opy_ (u"ࠢࡼࡿ࠲ࡿࢂࠨῢ").format(bstack11l1l1l1lll_opy_, bstack11ll11l111l_opy_)
            bstack1llllll11ll1_opy_ = os.environ.get(bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬΰ"), bstack1l1l11_opy_ (u"ࠩࠪῤ"))
            headers = {
                bstack1l1l11_opy_ (u"ࠪࡥࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪῥ"): bstack1l1l11_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧῦ").format(bstack1llllll11ll1_opy_),
                bstack1l1l11_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫῧ"): bstack1l1l11_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩῨ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            if response.status_code == 200 or response.status_code == 202:
                return response.json()
            else:
                logger.error(bstack1l1l11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡲ࡬ࡦࡥࡷࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡ࠯ࠢࡖࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨῩ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack1l1l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡶࡸࡤࡩ࡯࡭࡮ࡨࡧࡹࡥࡢࡶ࡫࡯ࡨࡤࡪࡡࡵࡣ࠽ࠤࢀࢃࠢῪ").format(e))
            return None