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
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1l11l1l_opy_, bstack11ll11ll111_opy_, bstack1lll1ll1l_opy_, error_handler, bstack111ll1ll11l_opy_, bstack111llllllll_opy_, bstack11l11l1lll1_opy_, bstack11llll11_opy_, bstack1l11111lll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1llllll1l111_opy_ import bstack1llllll1ll11_opy_
import bstack_utils.bstack1l1l1111_opy_ as bstack1l1ll1ll11_opy_
from bstack_utils.bstack111lll11l1_opy_ import bstack1111111l1_opy_
import bstack_utils.accessibility as bstack1ll11l111l_opy_
from bstack_utils.bstack11l1111ll1_opy_ import bstack11l1111ll1_opy_
from bstack_utils.bstack111ll1llll_opy_ import bstack1111ll111l_opy_
from bstack_utils.constants import bstack111l11111_opy_
bstack1llll1l1ll11_opy_ = bstack1l1l11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡣࡰ࡮࡯ࡩࡨࡺ࡯ࡳ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ₤")
logger = logging.getLogger(__name__)
class bstack1l1l1lll1l_opy_:
    bstack1llllll1l111_opy_ = None
    bs_config = None
    bstack1ll11ll11_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1ll1l11l_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def launch(cls, bs_config, bstack1ll11ll11_opy_):
        cls.bs_config = bs_config
        cls.bstack1ll11ll11_opy_ = bstack1ll11ll11_opy_
        try:
            cls.bstack1llll1ll11l1_opy_()
            bstack11ll1ll1ll1_opy_ = bstack11ll1l11l1l_opy_(bs_config)
            bstack11ll1llll11_opy_ = bstack11ll11ll111_opy_(bs_config)
            data = bstack1l1ll1ll11_opy_.bstack1llll11lll1l_opy_(bs_config, bstack1ll11ll11_opy_)
            config = {
                bstack1l1l11_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ₥"): (bstack11ll1ll1ll1_opy_, bstack11ll1llll11_opy_),
                bstack1l1l11_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ₦"): cls.default_headers()
            }
            response = bstack1lll1ll1l_opy_(bstack1l1l11_opy_ (u"ࠨࡒࡒࡗ࡙࠭₧"), cls.request_url(bstack1l1l11_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠳࠱ࡥࡹ࡮ࡲࡤࡴࠩ₨")), data, config)
            if response.status_code != 200:
                bstack1ll1ll1ll1_opy_ = response.json()
                if bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ₩")] == False:
                    cls.bstack1llll1l11l11_opy_(bstack1ll1ll1ll1_opy_)
                    return
                cls.bstack1llll1l1ll1l_opy_(bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ₪")])
                cls.bstack1llll1l111l1_opy_(bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ₫")])
                return None
            bstack1llll1l1111l_opy_ = cls.bstack1llll1ll1l11_opy_(response)
            return bstack1llll1l1111l_opy_, response.json()
        except Exception as error:
            logger.error(bstack1l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࡽࢀࠦ€").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll1l11111_opy_=None):
        if not bstack1111111l1_opy_.on() and not bstack1ll11l111l_opy_.on():
            return
        if os.environ.get(bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ₭")) == bstack1l1l11_opy_ (u"ࠣࡰࡸࡰࡱࠨ₮") or os.environ.get(bstack1l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ₯")) == bstack1l1l11_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ₰"):
            logger.error(bstack1l1l11_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡵࡰࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࠦࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡢࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡶࡲ࡯ࡪࡴࠧ₱"))
            return {
                bstack1l1l11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ₲"): bstack1l1l11_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ₳"),
                bstack1l1l11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ₴"): bstack1l1l11_opy_ (u"ࠨࡖࡲ࡯ࡪࡴ࠯ࡣࡷ࡬ࡰࡩࡏࡄࠡ࡫ࡶࠤࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠬࠡࡤࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡰ࡭࡬࡮ࡴࠡࡪࡤࡺࡪࠦࡦࡢ࡫࡯ࡩࡩ࠭₵")
            }
        try:
            cls.bstack1llllll1l111_opy_.shutdown()
            data = {
                bstack1l1l11_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ₶"): bstack11llll11_opy_()
            }
            if not bstack1llll1l11111_opy_ is None:
                data[bstack1l1l11_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡳࡥࡵࡣࡧࡥࡹࡧࠧ₷")] = [{
                    bstack1l1l11_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ₸"): bstack1l1l11_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪ₹"),
                    bstack1l1l11_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭₺"): bstack1llll1l11111_opy_
                }]
            config = {
                bstack1l1l11_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ₻"): cls.default_headers()
            }
            bstack11ll11l111l_opy_ = bstack1l1l11_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸࡺ࡯ࡱࠩ₼").format(os.environ[bstack1l1l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢ₽")])
            bstack1llll1l1llll_opy_ = cls.request_url(bstack11ll11l111l_opy_)
            response = bstack1lll1ll1l_opy_(bstack1l1l11_opy_ (u"ࠪࡔ࡚࡚ࠧ₾"), bstack1llll1l1llll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1l1l11_opy_ (u"ࠦࡘࡺ࡯ࡱࠢࡵࡩࡶࡻࡥࡴࡶࠣࡲࡴࡺࠠࡰ࡭ࠥ₿"))
        except Exception as error:
            logger.error(bstack1l1l11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺ࡯ࡱࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳ࡚ࠥࡥࡴࡶࡋࡹࡧࡀ࠺ࠡࠤ⃀") + str(error))
            return {
                bstack1l1l11_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭⃁"): bstack1l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭⃂"),
                bstack1l1l11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⃃"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1ll1l11_opy_(cls, response):
        bstack1ll1ll1ll1_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll1l1111l_opy_ = {}
        if bstack1ll1ll1ll1_opy_.get(bstack1l1l11_opy_ (u"ࠩ࡭ࡻࡹ࠭⃄")) is None:
            os.environ[bstack1l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ⃅")] = bstack1l1l11_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ⃆")
        else:
            os.environ[bstack1l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ⃇")] = bstack1ll1ll1ll1_opy_.get(bstack1l1l11_opy_ (u"࠭ࡪࡸࡶࠪ⃈"), bstack1l1l11_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ⃉"))
        os.environ[bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭⃊")] = bstack1ll1ll1ll1_opy_.get(bstack1l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ⃋"), bstack1l1l11_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ⃌"))
        logger.info(bstack1l1l11_opy_ (u"࡙ࠫ࡫ࡳࡵࡪࡸࡦࠥࡹࡴࡢࡴࡷࡩࡩࠦࡷࡪࡶ࡫ࠤ࡮ࡪ࠺ࠡࠩ⃍") + os.getenv(bstack1l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ⃎")));
        if bstack1111111l1_opy_.bstack1llll1l11ll1_opy_(cls.bs_config, cls.bstack1ll11ll11_opy_.get(bstack1l1l11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡸࡷࡪࡪࠧ⃏"), bstack1l1l11_opy_ (u"ࠧࠨ⃐"))) is True:
            bstack1llllll11ll1_opy_, build_hashed_id, bstack1llll1l1l11l_opy_ = cls.bstack1llll1l111ll_opy_(bstack1ll1ll1ll1_opy_)
            if bstack1llllll11ll1_opy_ != None and build_hashed_id != None:
                bstack1llll1l1111l_opy_[bstack1l1l11_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⃑")] = {
                    bstack1l1l11_opy_ (u"ࠩ࡭ࡻࡹࡥࡴࡰ࡭ࡨࡲ⃒ࠬ"): bstack1llllll11ll1_opy_,
                    bstack1l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨ⃓ࠬ"): build_hashed_id,
                    bstack1l1l11_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ⃔"): bstack1llll1l1l11l_opy_
                }
            else:
                bstack1llll1l1111l_opy_[bstack1l1l11_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ⃕")] = {}
        else:
            bstack1llll1l1111l_opy_[bstack1l1l11_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭⃖")] = {}
        bstack1llll11llll1_opy_, build_hashed_id = cls.bstack1llll1l1l1l1_opy_(bstack1ll1ll1ll1_opy_)
        if bstack1llll11llll1_opy_ != None and build_hashed_id != None:
            bstack1llll1l1111l_opy_[bstack1l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃗")] = {
                bstack1l1l11_opy_ (u"ࠨࡣࡸࡸ࡭ࡥࡴࡰ࡭ࡨࡲ⃘ࠬ"): bstack1llll11llll1_opy_,
                bstack1l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧ⃙ࠫ"): build_hashed_id,
            }
        else:
            bstack1llll1l1111l_opy_[bstack1l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻ⃚ࠪ")] = {}
        if bstack1llll1l1111l_opy_[bstack1l1l11_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⃛")].get(bstack1l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ⃜")) != None or bstack1llll1l1111l_opy_[bstack1l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⃝")].get(bstack1l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ⃞")) != None:
            cls.bstack1llll11lll11_opy_(bstack1ll1ll1ll1_opy_.get(bstack1l1l11_opy_ (u"ࠨ࡬ࡺࡸࠬ⃟")), bstack1ll1ll1ll1_opy_.get(bstack1l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ⃠")))
        return bstack1llll1l1111l_opy_
    @classmethod
    def bstack1llll1l111ll_opy_(cls, bstack1ll1ll1ll1_opy_):
        if bstack1ll1ll1ll1_opy_.get(bstack1l1l11_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⃡")) == None:
            cls.bstack1llll1l1ll1l_opy_()
            return [None, None, None]
        if bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⃢")][bstack1l1l11_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭⃣")] != True:
            cls.bstack1llll1l1ll1l_opy_(bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭⃤")])
            return [None, None, None]
        logger.debug(bstack1l1l11_opy_ (u"ࠧࡼࡿࠣࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬⃥ࠢࠩ").format(bstack111l11111_opy_))
        os.environ[bstack1l1l11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊ⃦ࠧ")] = bstack1l1l11_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⃧")
        if bstack1ll1ll1ll1_opy_.get(bstack1l1l11_opy_ (u"ࠪ࡮ࡼࡺ⃨ࠧ")):
            os.environ[bstack1l1l11_opy_ (u"ࠫࡈࡘࡅࡅࡇࡑࡘࡎࡇࡌࡔࡡࡉࡓࡗࡥࡃࡓࡃࡖࡌࡤࡘࡅࡑࡑࡕࡘࡎࡔࡇࠨ⃩")] = json.dumps({
                bstack1l1l11_opy_ (u"ࠬࡻࡳࡦࡴࡱࡥࡲ࡫⃪ࠧ"): bstack11ll1l11l1l_opy_(cls.bs_config),
                bstack1l1l11_opy_ (u"࠭ࡰࡢࡵࡶࡻࡴࡸࡤࠨ⃫"): bstack11ll11ll111_opy_(cls.bs_config)
            })
        if bstack1ll1ll1ll1_opy_.get(bstack1l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥ⃬ࠩ")):
            os.environ[bstack1l1l11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊ⃭ࠧ")] = bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧ⃮ࠫ")]
        if bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ⃯ࠪ")].get(bstack1l1l11_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ⃰"), {}).get(bstack1l1l11_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ⃱")):
            os.environ[bstack1l1l11_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧ⃲")] = str(bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ⃳")][bstack1l1l11_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⃴")][bstack1l1l11_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭⃵")])
        else:
            os.environ[bstack1l1l11_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ⃶")] = bstack1l1l11_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ⃷")
        return [bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠬࡰࡷࡵࠩ⃸")], bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ⃹")], os.environ[bstack1l1l11_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨ⃺")]]
    @classmethod
    def bstack1llll1l1l1l1_opy_(cls, bstack1ll1ll1ll1_opy_):
        if bstack1ll1ll1ll1_opy_.get(bstack1l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⃻")) == None:
            cls.bstack1llll1l111l1_opy_()
            return [None, None]
        if bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⃼")][bstack1l1l11_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ⃽")] != True:
            cls.bstack1llll1l111l1_opy_(bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⃾")])
            return [None, None]
        if bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⃿")].get(bstack1l1l11_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ℀")):
            logger.debug(bstack1l1l11_opy_ (u"ࠧࡕࡧࡶࡸࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫ℁"))
            parsed = json.loads(os.getenv(bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩℂ"), bstack1l1l11_opy_ (u"ࠩࡾࢁࠬ℃")))
            capabilities = bstack1l1ll1ll11_opy_.bstack1llll1ll1l1l_opy_(bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ℄")][bstack1l1l11_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ℅")][bstack1l1l11_opy_ (u"ࠬࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ℆")], bstack1l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫℇ"), bstack1l1l11_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭℈"))
            bstack1llll11llll1_opy_ = capabilities[bstack1l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳ࠭℉")]
            os.environ[bstack1l1l11_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧℊ")] = bstack1llll11llll1_opy_
            if bstack1l1l11_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧℋ") in bstack1ll1ll1ll1_opy_ and bstack1ll1ll1ll1_opy_.get(bstack1l1l11_opy_ (u"ࠦࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠥℌ")) is None:
                parsed[bstack1l1l11_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ℍ")] = capabilities[bstack1l1l11_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧℎ")]
            os.environ[bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨℏ")] = json.dumps(parsed)
            scripts = bstack1l1ll1ll11_opy_.bstack1llll1ll1l1l_opy_(bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨℐ")][bstack1l1l11_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪℑ")][bstack1l1l11_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫℒ")], bstack1l1l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩℓ"), bstack1l1l11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩ࠭℔"))
            bstack11l1111ll1_opy_.bstack1ll11l11ll_opy_(scripts)
            commands = bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ℕ")][bstack1l1l11_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ№")][bstack1l1l11_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࡗࡳ࡜ࡸࡡࡱࠩ℗")].get(bstack1l1l11_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫ℘"))
            bstack11l1111ll1_opy_.bstack11ll1ll1l1l_opy_(commands)
            bstack11ll1l1lll1_opy_ = capabilities.get(bstack1l1l11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨℙ"))
            bstack11l1111ll1_opy_.bstack11ll11l1l11_opy_(bstack11ll1l1lll1_opy_)
            bstack11l1111ll1_opy_.store()
        return [bstack1llll11llll1_opy_, bstack1ll1ll1ll1_opy_[bstack1l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ℚ")]]
    @classmethod
    def bstack1llll1l1ll1l_opy_(cls, response=None):
        os.environ[bstack1l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪℛ")] = bstack1l1l11_opy_ (u"࠭࡮ࡶ࡮࡯ࠫℜ")
        os.environ[bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫℝ")] = bstack1l1l11_opy_ (u"ࠨࡰࡸࡰࡱ࠭℞")
        os.environ[bstack1l1l11_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡉࡏࡎࡒࡏࡉ࡙ࡋࡄࠨ℟")] = bstack1l1l11_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ℠")
        os.environ[bstack1l1l11_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪ℡")] = bstack1l1l11_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ™")
        os.environ[bstack1l1l11_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧ℣")] = bstack1l1l11_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧℤ")
        cls.bstack1llll1l11l11_opy_(response, bstack1l1l11_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣ℥"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l111l1_opy_(cls, response=None):
        os.environ[bstack1l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧΩ")] = bstack1l1l11_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ℧")
        os.environ[bstack1l1l11_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩℨ")] = bstack1l1l11_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ℩")
        os.environ[bstack1l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪK")] = bstack1l1l11_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬÅ")
        cls.bstack1llll1l11l11_opy_(response, bstack1l1l11_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣℬ"))
        return [None, None, None]
    @classmethod
    def bstack1llll11lll11_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ℭ")] = jwt
        os.environ[bstack1l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ℮")] = build_hashed_id
    @classmethod
    def bstack1llll1l11l11_opy_(cls, response=None, product=bstack1l1l11_opy_ (u"ࠦࠧℯ")):
        if response == None or response.get(bstack1l1l11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬℰ")) == None:
            logger.error(product + bstack1l1l11_opy_ (u"ࠨࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠣℱ"))
            return
        for error in response[bstack1l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧℲ")]:
            bstack11l11ll1111_opy_ = error[bstack1l1l11_opy_ (u"ࠨ࡭ࡨࡽࠬℳ")]
            error_message = error[bstack1l1l11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪℴ")]
            if error_message:
                if bstack11l11ll1111_opy_ == bstack1l1l11_opy_ (u"ࠥࡉࡗࡘࡏࡓࡡࡄࡇࡈࡋࡓࡔࡡࡇࡉࡓࡏࡅࡅࠤℵ"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1l1l11_opy_ (u"ࠦࡉࡧࡴࡢࠢࡸࡴࡱࡵࡡࡥࠢࡷࡳࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࠧℶ") + product + bstack1l1l11_opy_ (u"ࠧࠦࡦࡢ࡫࡯ࡩࡩࠦࡤࡶࡧࠣࡸࡴࠦࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥℷ"))
    @classmethod
    def bstack1llll1ll11l1_opy_(cls):
        if cls.bstack1llllll1l111_opy_ is not None:
            return
        cls.bstack1llllll1l111_opy_ = bstack1llllll1ll11_opy_(cls.bstack1llll1l11l1l_opy_)
        cls.bstack1llllll1l111_opy_.start()
    @classmethod
    def bstack111l1l1l11_opy_(cls):
        if cls.bstack1llllll1l111_opy_ is None:
            return
        cls.bstack1llllll1l111_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l11l1l_opy_(cls, bstack111l11111l_opy_, event_url=bstack1l1l11_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡢࡶࡦ࡬ࠬℸ")):
        config = {
            bstack1l1l11_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨℹ"): cls.default_headers()
        }
        logger.debug(bstack1l1l11_opy_ (u"ࠣࡲࡲࡷࡹࡥࡤࡢࡶࡤ࠾࡙ࠥࡥ࡯ࡦ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤࡹࡵࠠࡵࡧࡶࡸ࡭ࡻࡢࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࡷࠥࢁࡽࠣ℺").format(bstack1l1l11_opy_ (u"ࠩ࠯ࠤࠬ℻").join([event[bstack1l1l11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧℼ")] for event in bstack111l11111l_opy_])))
        response = bstack1lll1ll1l_opy_(bstack1l1l11_opy_ (u"ࠫࡕࡕࡓࡕࠩℽ"), cls.request_url(event_url), bstack111l11111l_opy_, config)
        bstack11lll111111_opy_ = response.json()
    @classmethod
    def bstack111l11l1l_opy_(cls, bstack111l11111l_opy_, event_url=bstack1l1l11_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫℾ")):
        logger.debug(bstack1l1l11_opy_ (u"ࠨࡳࡦࡰࡧࡣࡩࡧࡴࡢ࠼ࠣࡅࡹࡺࡥ࡮ࡲࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡥࡩࡪࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡤࡸࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨℿ").format(bstack111l11111l_opy_[bstack1l1l11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⅀")]))
        if not bstack1l1ll1ll11_opy_.bstack1llll11lllll_opy_(bstack111l11111l_opy_[bstack1l1l11_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⅁")]):
            logger.debug(bstack1l1l11_opy_ (u"ࠤࡶࡩࡳࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡎࡰࡶࠣࡥࡩࡪࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧ࠽ࠤࢀࢃࠢ⅂").format(bstack111l11111l_opy_[bstack1l1l11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⅃")]))
            return
        bstack1ll11l1l1l_opy_ = bstack1l1ll1ll11_opy_.bstack1llll1l1l1ll_opy_(bstack111l11111l_opy_[bstack1l1l11_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⅄")], bstack111l11111l_opy_.get(bstack1l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧⅅ")))
        if bstack1ll11l1l1l_opy_ != None:
            if bstack111l11111l_opy_.get(bstack1l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨⅆ")) != None:
                bstack111l11111l_opy_[bstack1l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩⅇ")][bstack1l1l11_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭ⅈ")] = bstack1ll11l1l1l_opy_
            else:
                bstack111l11111l_opy_[bstack1l1l11_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧⅉ")] = bstack1ll11l1l1l_opy_
        if event_url == bstack1l1l11_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ⅊"):
            cls.bstack1llll1ll11l1_opy_()
            logger.debug(bstack1l1l11_opy_ (u"ࠦࡸ࡫࡮ࡥࡡࡧࡥࡹࡧ࠺ࠡࡃࡧࡨ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡴࡰࠢࡥࡥࡹࡩࡨࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧ࠽ࠤࢀࢃࠢ⅋").format(bstack111l11111l_opy_[bstack1l1l11_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⅌")]))
            cls.bstack1llllll1l111_opy_.add(bstack111l11111l_opy_)
        elif event_url == bstack1l1l11_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫ⅍"):
            cls.bstack1llll1l11l1l_opy_([bstack111l11111l_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l111l111l_opy_(cls, logs):
        for log in logs:
            bstack1llll1ll11ll_opy_ = {
                bstack1l1l11_opy_ (u"ࠧ࡬࡫ࡱࡨࠬⅎ"): bstack1l1l11_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡌࡐࡉࠪ⅏"),
                bstack1l1l11_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ⅐"): log[bstack1l1l11_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ⅑")],
                bstack1l1l11_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⅒"): log[bstack1l1l11_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ⅓")],
                bstack1l1l11_opy_ (u"࠭ࡨࡵࡶࡳࡣࡷ࡫ࡳࡱࡱࡱࡷࡪ࠭⅔"): {},
                bstack1l1l11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⅕"): log[bstack1l1l11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⅖")],
            }
            if bstack1l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⅗") in log:
                bstack1llll1ll11ll_opy_[bstack1l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⅘")] = log[bstack1l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⅙")]
            elif bstack1l1l11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⅚") in log:
                bstack1llll1ll11ll_opy_[bstack1l1l11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⅛")] = log[bstack1l1l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⅜")]
            cls.bstack111l11l1l_opy_({
                bstack1l1l11_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⅝"): bstack1l1l11_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭⅞"),
                bstack1l1l11_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ⅟"): [bstack1llll1ll11ll_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l1lll1_opy_(cls, steps):
        bstack1llll1l11lll_opy_ = []
        for step in steps:
            bstack1llll1l1l111_opy_ = {
                bstack1l1l11_opy_ (u"ࠫࡰ࡯࡮ࡥࠩⅠ"): bstack1l1l11_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗ࡙ࡋࡐࠨⅡ"),
                bstack1l1l11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬⅢ"): step[bstack1l1l11_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭Ⅳ")],
                bstack1l1l11_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫⅤ"): step[bstack1l1l11_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬⅥ")],
                bstack1l1l11_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫⅦ"): step[bstack1l1l11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬⅧ")],
                bstack1l1l11_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧⅨ"): step[bstack1l1l11_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨⅩ")]
            }
            if bstack1l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧⅪ") in step:
                bstack1llll1l1l111_opy_[bstack1l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨⅫ")] = step[bstack1l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩⅬ")]
            elif bstack1l1l11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪⅭ") in step:
                bstack1llll1l1l111_opy_[bstack1l1l11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫⅮ")] = step[bstack1l1l11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬⅯ")]
            bstack1llll1l11lll_opy_.append(bstack1llll1l1l111_opy_)
        cls.bstack111l11l1l_opy_({
            bstack1l1l11_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪⅰ"): bstack1l1l11_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫⅱ"),
            bstack1l1l11_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭ⅲ"): bstack1llll1l11lll_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack1l1lll1ll1_opy_, stage=STAGE.bstack1ll11lll_opy_)
    def bstack111lllll_opy_(cls, screenshot):
        cls.bstack111l11l1l_opy_({
            bstack1l1l11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ⅳ"): bstack1l1l11_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧⅴ"),
            bstack1l1l11_opy_ (u"ࠫࡱࡵࡧࡴࠩⅵ"): [{
                bstack1l1l11_opy_ (u"ࠬࡱࡩ࡯ࡦࠪⅶ"): bstack1l1l11_opy_ (u"࠭ࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠨⅷ"),
                bstack1l1l11_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪⅸ"): datetime.datetime.utcnow().isoformat() + bstack1l1l11_opy_ (u"ࠨ࡜ࠪⅹ"),
                bstack1l1l11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪⅺ"): screenshot[bstack1l1l11_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩⅻ")],
                bstack1l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫⅼ"): screenshot[bstack1l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬⅽ")]
            }]
        }, event_url=bstack1l1l11_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫⅾ"))
    @classmethod
    @error_handler(class_method=True)
    def bstack1ll1ll1l11_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack111l11l1l_opy_({
            bstack1l1l11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫⅿ"): bstack1l1l11_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬↀ"),
            bstack1l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫↁ"): {
                bstack1l1l11_opy_ (u"ࠥࡹࡺ࡯ࡤࠣↂ"): cls.current_test_uuid(),
                bstack1l1l11_opy_ (u"ࠦ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠥↃ"): cls.bstack111lll1111_opy_(driver)
            }
        })
    @classmethod
    def bstack111l1lll1l_opy_(cls, event: str, bstack111l11111l_opy_: bstack1111ll111l_opy_):
        bstack111l111l11_opy_ = {
            bstack1l1l11_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩↄ"): event,
            bstack111l11111l_opy_.bstack111l11l11l_opy_(): bstack111l11111l_opy_.bstack111l111l1l_opy_(event)
        }
        cls.bstack111l11l1l_opy_(bstack111l111l11_opy_)
        result = getattr(bstack111l11111l_opy_, bstack1l1l11_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ↅ"), None)
        if event == bstack1l1l11_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨↆ"):
            threading.current_thread().bstackTestMeta = {bstack1l1l11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨↇ"): bstack1l1l11_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪↈ")}
        elif event == bstack1l1l11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ↉"):
            threading.current_thread().bstackTestMeta = {bstack1l1l11_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ↊"): getattr(result, bstack1l1l11_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ↋"), bstack1l1l11_opy_ (u"࠭ࠧ↌"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ↍"), None) is None or os.environ[bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ↎")] == bstack1l1l11_opy_ (u"ࠤࡱࡹࡱࡲࠢ↏")) and (os.environ.get(bstack1l1l11_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ←"), None) is None or os.environ[bstack1l1l11_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ↑")] == bstack1l1l11_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ→")):
            return False
        return True
    @staticmethod
    def bstack1llll1ll1111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1l1lll1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1l1l11_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ↓"): bstack1l1l11_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ↔"),
            bstack1l1l11_opy_ (u"ࠨ࡚࠰ࡆࡘ࡚ࡁࡄࡍ࠰ࡘࡊ࡙ࡔࡐࡒࡖࠫ↕"): bstack1l1l11_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ↖")
        }
        if os.environ.get(bstack1l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ↗"), None):
            headers[bstack1l1l11_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫ↘")] = bstack1l1l11_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨ↙").format(os.environ[bstack1l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠥ↚")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1l1l11_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭↛").format(bstack1llll1l1ll11_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1l1l11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ↜"), None)
    @staticmethod
    def bstack111lll1111_opy_(driver):
        return {
            bstack111ll1ll11l_opy_(): bstack111llllllll_opy_(driver)
        }
    @staticmethod
    def bstack1llll1ll111l_opy_(exception_info, report):
        return [{bstack1l1l11_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬ↝"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack111111l11l_opy_(typename):
        if bstack1l1l11_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨ↞") in typename:
            return bstack1l1l11_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧ↟")
        return bstack1l1l11_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨ↠")