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
from uuid import uuid4
from bstack_utils.helper import bstack111l11l11_opy_, bstack11l11ll1l11_opy_
from bstack_utils.bstack11llll1lll_opy_ import bstack1lllllll1l1l_opy_
class bstack1111ll1lll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack1lllll11l111_opy_=None, bstack1lllll1l111l_opy_=True, bstack1l11111111l_opy_=None, bstack11lllll1_opy_=None, result=None, duration=None, bstack111l1l1111_opy_=None, meta={}):
        self.bstack111l1l1111_opy_ = bstack111l1l1111_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1lllll1l111l_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1lllll11l111_opy_ = bstack1lllll11l111_opy_
        self.bstack1l11111111l_opy_ = bstack1l11111111l_opy_
        self.bstack11lllll1_opy_ = bstack11lllll1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1111lllll1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack111ll111ll_opy_(self, meta):
        self.meta = meta
    def bstack111ll1111l_opy_(self, hooks):
        self.hooks = hooks
    def bstack1lllll1l1l11_opy_(self):
        bstack1lllll111ll1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1l11l11_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ‡"): bstack1lllll111ll1_opy_,
            bstack1l11l11_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪ•"): bstack1lllll111ll1_opy_,
            bstack1l11l11_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧ‣"): bstack1lllll111ll1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1l11l11_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦ․") + key)
            setattr(self, key, val)
    def bstack1lllll11lll1_opy_(self):
        return {
            bstack1l11l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ‥"): self.name,
            bstack1l11l11_opy_ (u"ࠬࡨ࡯ࡥࡻࠪ…"): {
                bstack1l11l11_opy_ (u"࠭࡬ࡢࡰࡪࠫ‧"): bstack1l11l11_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ "),
                bstack1l11l11_opy_ (u"ࠨࡥࡲࡨࡪ࠭ "): self.code
            },
            bstack1l11l11_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩ‪"): self.scope,
            bstack1l11l11_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ‫"): self.tags,
            bstack1l11l11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ‬"): self.framework,
            bstack1l11l11_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ‭"): self.started_at
        }
    def bstack1lllll1l1111_opy_(self):
        return {
         bstack1l11l11_opy_ (u"࠭࡭ࡦࡶࡤࠫ‮"): self.meta
        }
    def bstack1lllll11ll1l_opy_(self):
        return {
            bstack1l11l11_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪ "): {
                bstack1l11l11_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬ‰"): self.bstack1lllll11l111_opy_
            }
        }
    def bstack1lllll11l11l_opy_(self, bstack1lllll11llll_opy_, details):
        step = next(filter(lambda st: st[bstack1l11l11_opy_ (u"ࠩ࡬ࡨࠬ‱")] == bstack1lllll11llll_opy_, self.meta[bstack1l11l11_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩ′")]), None)
        step.update(details)
    def bstack1ll1llll11_opy_(self, bstack1lllll11llll_opy_):
        step = next(filter(lambda st: st[bstack1l11l11_opy_ (u"ࠫ࡮ࡪࠧ″")] == bstack1lllll11llll_opy_, self.meta[bstack1l11l11_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫ‴")]), None)
        step.update({
            bstack1l11l11_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ‵"): bstack111l11l11_opy_()
        })
    def bstack111ll11lll_opy_(self, bstack1lllll11llll_opy_, result, duration=None):
        bstack1l11111111l_opy_ = bstack111l11l11_opy_()
        if bstack1lllll11llll_opy_ is not None and self.meta.get(bstack1l11l11_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭‶")):
            step = next(filter(lambda st: st[bstack1l11l11_opy_ (u"ࠨ࡫ࡧࠫ‷")] == bstack1lllll11llll_opy_, self.meta[bstack1l11l11_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨ‸")]), None)
            step.update({
                bstack1l11l11_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ‹"): bstack1l11111111l_opy_,
                bstack1l11l11_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭›"): duration if duration else bstack11l11ll1l11_opy_(step[bstack1l11l11_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ※")], bstack1l11111111l_opy_),
                bstack1l11l11_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭‼"): result.result,
                bstack1l11l11_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ‽"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1lllll11ll11_opy_):
        if self.meta.get(bstack1l11l11_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧ‾")):
            self.meta[bstack1l11l11_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨ‿")].append(bstack1lllll11ll11_opy_)
        else:
            self.meta[bstack1l11l11_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩ⁀")] = [ bstack1lllll11ll11_opy_ ]
    def bstack1lllll11l1l1_opy_(self):
        return {
            bstack1l11l11_opy_ (u"ࠫࡺࡻࡩࡥࠩ⁁"): self.bstack1111lllll1_opy_(),
            **self.bstack1lllll11lll1_opy_(),
            **self.bstack1lllll1l1l11_opy_(),
            **self.bstack1lllll1l1111_opy_()
        }
    def bstack1lllll111lll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1l11l11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⁂"): self.bstack1l11111111l_opy_,
            bstack1l11l11_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ⁃"): self.duration,
            bstack1l11l11_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⁄"): self.result.result
        }
        if data[bstack1l11l11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⁅")] == bstack1l11l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ⁆"):
            data[bstack1l11l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩ⁇")] = self.result.bstack111111l11l_opy_()
            data[bstack1l11l11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬ⁈")] = [{bstack1l11l11_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨ⁉"): self.result.bstack111ll1llll1_opy_()}]
        return data
    def bstack1lllll1l11l1_opy_(self):
        return {
            bstack1l11l11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⁊"): self.bstack1111lllll1_opy_(),
            **self.bstack1lllll11lll1_opy_(),
            **self.bstack1lllll1l1l11_opy_(),
            **self.bstack1lllll111lll_opy_(),
            **self.bstack1lllll1l1111_opy_()
        }
    def bstack111l1l1l11_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1l11l11_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡫ࡤࠨ⁋") in event:
            return self.bstack1lllll11l1l1_opy_()
        elif bstack1l11l11_opy_ (u"ࠨࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⁌") in event:
            return self.bstack1lllll1l11l1_opy_()
    def bstack1111lll1l1_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1l11111111l_opy_ = time if time else bstack111l11l11_opy_()
        self.duration = duration if duration else bstack11l11ll1l11_opy_(self.started_at, self.bstack1l11111111l_opy_)
        if result:
            self.result = result
class bstack111ll1l111_opy_(bstack1111ll1lll_opy_):
    def __init__(self, hooks=[], bstack111ll1llll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack111ll1llll_opy_ = bstack111ll1llll_opy_
        super().__init__(*args, **kwargs, bstack11lllll1_opy_=bstack1l11l11_opy_ (u"ࠩࡷࡩࡸࡺࠧ⁍"))
    @classmethod
    def bstack1lllll1l1l1l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l11l11_opy_ (u"ࠪ࡭ࡩ࠭⁎"): id(step),
                bstack1l11l11_opy_ (u"ࠫࡹ࡫ࡸࡵࠩ⁏"): step.name,
                bstack1l11l11_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭⁐"): step.keyword,
            })
        return bstack111ll1l111_opy_(
            **kwargs,
            meta={
                bstack1l11l11_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧ⁑"): {
                    bstack1l11l11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ⁒"): feature.name,
                    bstack1l11l11_opy_ (u"ࠨࡲࡤࡸ࡭࠭⁓"): feature.filename,
                    bstack1l11l11_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ⁔"): feature.description
                },
                bstack1l11l11_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬ⁕"): {
                    bstack1l11l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ⁖"): scenario.name
                },
                bstack1l11l11_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫ⁗"): steps,
                bstack1l11l11_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨ⁘"): bstack1lllllll1l1l_opy_(test)
            }
        )
    def bstack1lllll111l1l_opy_(self):
        return {
            bstack1l11l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⁙"): self.hooks
        }
    def bstack1lllll11l1ll_opy_(self):
        if self.bstack111ll1llll_opy_:
            return {
                bstack1l11l11_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧ⁚"): self.bstack111ll1llll_opy_
            }
        return {}
    def bstack1lllll1l11l1_opy_(self):
        return {
            **super().bstack1lllll1l11l1_opy_(),
            **self.bstack1lllll111l1l_opy_()
        }
    def bstack1lllll11l1l1_opy_(self):
        return {
            **super().bstack1lllll11l1l1_opy_(),
            **self.bstack1lllll11l1ll_opy_()
        }
    def bstack1111lll1l1_opy_(self):
        return bstack1l11l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ⁛")
class bstack111ll1l1l1_opy_(bstack1111ll1lll_opy_):
    def __init__(self, hook_type, *args,bstack111ll1llll_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1ll1111l11l_opy_ = None
        self.bstack111ll1llll_opy_ = bstack111ll1llll_opy_
        super().__init__(*args, **kwargs, bstack11lllll1_opy_=bstack1l11l11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ⁜"))
    def bstack111l111lll_opy_(self):
        return self.hook_type
    def bstack1lllll1l11ll_opy_(self):
        return {
            bstack1l11l11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧ⁝"): self.hook_type
        }
    def bstack1lllll1l11l1_opy_(self):
        return {
            **super().bstack1lllll1l11l1_opy_(),
            **self.bstack1lllll1l11ll_opy_()
        }
    def bstack1lllll11l1l1_opy_(self):
        return {
            **super().bstack1lllll11l1l1_opy_(),
            bstack1l11l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪ⁞"): self.bstack1ll1111l11l_opy_,
            **self.bstack1lllll1l11ll_opy_()
        }
    def bstack1111lll1l1_opy_(self):
        return bstack1l11l11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨ ")
    def bstack111ll1ll11_opy_(self, bstack1ll1111l11l_opy_):
        self.bstack1ll1111l11l_opy_ = bstack1ll1111l11l_opy_