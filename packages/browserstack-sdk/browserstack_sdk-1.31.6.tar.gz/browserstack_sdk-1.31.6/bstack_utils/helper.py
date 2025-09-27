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
import collections
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
from unittest import result
import urllib
from urllib.parse import urlparse
import copy
import zipfile
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack11l11l111l_opy_, bstack111ll1l1l_opy_, bstack11l1llll_opy_,
                                    bstack11l1l1llll1_opy_, bstack11l1ll11111_opy_, bstack11l1lllll1l_opy_, bstack11l1ll1111l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l111lll1l_opy_, bstack111l1ll11_opy_
from bstack_utils.proxy import bstack1l1l11111_opy_, bstack1l11l11ll1_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11lll1llll_opy_
from bstack_utils.bstack1111111l_opy_ import bstack11lllll1ll_opy_
from browserstack_sdk._version import __version__
bstack1lll11l111_opy_ = Config.bstack1l11111l1l_opy_()
logger = bstack11lll1llll_opy_.get_logger(__name__, bstack11lll1llll_opy_.bstack1ll1lllll11_opy_())
def bstack11ll1l11l1l_opy_(config):
    return config[bstack1l1l11_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᬈ")]
def bstack11ll11ll111_opy_(config):
    return config[bstack1l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᬉ")]
def bstack1l1l11l11_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack11l111ll11l_opy_(obj):
    values = []
    bstack111ll1l11ll_opy_ = re.compile(bstack1l1l11_opy_ (u"ࡸࠢ࡟ࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤࡢࡤࠬࠦࠥᬊ"), re.I)
    for key in obj.keys():
        if bstack111ll1l11ll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack11l11ll1ll1_opy_(config):
    tags = []
    tags.extend(bstack11l111ll11l_opy_(os.environ))
    tags.extend(bstack11l111ll11l_opy_(config))
    return tags
def bstack111lll111ll_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack11l111lll11_opy_(bstack11l11lll11l_opy_):
    if not bstack11l11lll11l_opy_:
        return bstack1l1l11_opy_ (u"ࠧࠨᬋ")
    return bstack1l1l11_opy_ (u"ࠣࡽࢀࠤ࠭ࢁࡽࠪࠤᬌ").format(bstack11l11lll11l_opy_.name, bstack11l11lll11l_opy_.email)
def bstack11ll1l11111_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111ll1l111l_opy_ = repo.common_dir
        info = {
            bstack1l1l11_opy_ (u"ࠤࡶ࡬ࡦࠨᬍ"): repo.head.commit.hexsha,
            bstack1l1l11_opy_ (u"ࠥࡷ࡭ࡵࡲࡵࡡࡶ࡬ࡦࠨᬎ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1l1l11_opy_ (u"ࠦࡧࡸࡡ࡯ࡥ࡫ࠦᬏ"): repo.active_branch.name,
            bstack1l1l11_opy_ (u"ࠧࡺࡡࡨࠤᬐ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1l1l11_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࠤᬑ"): bstack11l111lll11_opy_(repo.head.commit.committer),
            bstack1l1l11_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࡢࡨࡦࡺࡥࠣᬒ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1l1l11_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࠣᬓ"): bstack11l111lll11_opy_(repo.head.commit.author),
            bstack1l1l11_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡡࡧࡥࡹ࡫ࠢᬔ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1l1l11_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦᬕ"): repo.head.commit.message,
            bstack1l1l11_opy_ (u"ࠦࡷࡵ࡯ࡵࠤᬖ"): repo.git.rev_parse(bstack1l1l11_opy_ (u"ࠧ࠳࠭ࡴࡪࡲࡻ࠲ࡺ࡯ࡱ࡮ࡨࡺࡪࡲࠢᬗ")),
            bstack1l1l11_opy_ (u"ࠨࡣࡰ࡯ࡰࡳࡳࡥࡧࡪࡶࡢࡨ࡮ࡸࠢᬘ"): bstack111ll1l111l_opy_,
            bstack1l1l11_opy_ (u"ࠢࡸࡱࡵ࡯ࡹࡸࡥࡦࡡࡪ࡭ࡹࡥࡤࡪࡴࠥᬙ"): subprocess.check_output([bstack1l1l11_opy_ (u"ࠣࡩ࡬ࡸࠧᬚ"), bstack1l1l11_opy_ (u"ࠤࡵࡩࡻ࠳ࡰࡢࡴࡶࡩࠧᬛ"), bstack1l1l11_opy_ (u"ࠥ࠱࠲࡭ࡩࡵ࠯ࡦࡳࡲࡳ࡯࡯࠯ࡧ࡭ࡷࠨᬜ")]).strip().decode(
                bstack1l1l11_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᬝ")),
            bstack1l1l11_opy_ (u"ࠧࡲࡡࡴࡶࡢࡸࡦ࡭ࠢᬞ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1l1l11_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡹ࡟ࡴ࡫ࡱࡧࡪࡥ࡬ࡢࡵࡷࡣࡹࡧࡧࠣᬟ"): repo.git.rev_list(
                bstack1l1l11_opy_ (u"ࠢࡼࡿ࠱࠲ࢀࢃࠢᬠ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack11l111l111l_opy_ = []
        for remote in remotes:
            bstack111lll1l111_opy_ = {
                bstack1l1l11_opy_ (u"ࠣࡰࡤࡱࡪࠨᬡ"): remote.name,
                bstack1l1l11_opy_ (u"ࠤࡸࡶࡱࠨᬢ"): remote.url,
            }
            bstack11l111l111l_opy_.append(bstack111lll1l111_opy_)
        bstack11l111111ll_opy_ = {
            bstack1l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣᬣ"): bstack1l1l11_opy_ (u"ࠦ࡬࡯ࡴࠣᬤ"),
            **info,
            bstack1l1l11_opy_ (u"ࠧࡸࡥ࡮ࡱࡷࡩࡸࠨᬥ"): bstack11l111l111l_opy_
        }
        bstack11l111111ll_opy_ = bstack11l111111l1_opy_(bstack11l111111ll_opy_)
        return bstack11l111111ll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡱࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡊ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤᬦ").format(err))
        return {}
def bstack11l1111llll_opy_(bstack111ll1lll1l_opy_=None):
    bstack1l1l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡈࡧࡷࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡷࡵ࡫ࡣࡪࡨ࡬ࡧࡦࡲ࡬ࡺࠢࡩࡳࡷࡳࡡࡵࡶࡨࡨࠥ࡬࡯ࡳࠢࡄࡍࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡷࡶࡩࠥࡩࡡࡴࡧࡶࠤ࡫ࡵࡲࠡࡧࡤࡧ࡭ࠦࡦࡰ࡮ࡧࡩࡷࠦࡩ࡯ࠢࡷ࡬ࡪࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡩࡳࡱࡪࡥࡳࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡨࡲࡰࡩ࡫ࡲࠡࡲࡤࡸ࡭ࡹࠠࡵࡱࠣࡩࡽࡺࡲࡢࡥࡷࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡪࡷࡵ࡭࠯ࠢࡇࡩ࡫ࡧࡵ࡭ࡶࡶࠤࡹࡵࠠ࡜ࡱࡶ࠲࡬࡫ࡴࡤࡹࡧࠬ࠮ࡣ࠮ࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡮࡬ࡷࡹࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡦ࡬ࡧࡹࡹࠬࠡࡧࡤࡧ࡭ࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡩࡳࡷࠦࡡࠡࡨࡲࡰࡩ࡫ࡲ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᬧ")
    if not bstack111ll1lll1l_opy_: # bstack111ll1l11l1_opy_ for bstack11l11ll1lll_opy_-repo
        bstack111ll1lll1l_opy_ = [os.getcwd()]
    results = []
    for folder in bstack111ll1lll1l_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack1l1l11_opy_ (u"ࠣࡲࡵࡍࡩࠨᬨ"): bstack1l1l11_opy_ (u"ࠤࠥᬩ"),
                bstack1l1l11_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᬪ"): [],
                bstack1l1l11_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧᬫ"): [],
                bstack1l1l11_opy_ (u"ࠧࡶࡲࡅࡣࡷࡩࠧᬬ"): bstack1l1l11_opy_ (u"ࠨࠢᬭ"),
                bstack1l1l11_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡍࡦࡵࡶࡥ࡬࡫ࡳࠣᬮ"): [],
                bstack1l1l11_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᬯ"): bstack1l1l11_opy_ (u"ࠤࠥᬰ"),
                bstack1l1l11_opy_ (u"ࠥࡴࡷࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠥᬱ"): bstack1l1l11_opy_ (u"ࠦࠧᬲ"),
                bstack1l1l11_opy_ (u"ࠧࡶࡲࡓࡣࡺࡈ࡮࡬ࡦࠣᬳ"): bstack1l1l11_opy_ (u"ࠨ᬴ࠢ")
            }
            bstack111llllll11_opy_ = repo.active_branch.name
            bstack11l11l11111_opy_ = repo.head.commit
            result[bstack1l1l11_opy_ (u"ࠢࡱࡴࡌࡨࠧᬵ")] = bstack11l11l11111_opy_.hexsha
            bstack111ll1ll1ll_opy_ = _11l111l1l11_opy_(repo)
            logger.debug(bstack1l1l11_opy_ (u"ࠣࡄࡤࡷࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡦࡰࡴࠣࡧࡴࡳࡰࡢࡴ࡬ࡷࡴࡴ࠺ࠡࠤᬶ") + str(bstack111ll1ll1ll_opy_) + bstack1l1l11_opy_ (u"ࠤࠥᬷ"))
            if bstack111ll1ll1ll_opy_:
                try:
                    bstack111llll1111_opy_ = repo.git.diff(bstack1l1l11_opy_ (u"ࠥ࠱࠲ࡴࡡ࡮ࡧ࠰ࡳࡳࡲࡹࠣᬸ"), bstack1lll11llll1_opy_ (u"ࠦࢀࡨࡡࡴࡧࡢࡦࡷࡧ࡮ࡤࡪࢀ࠲࠳࠴ࡻࡤࡷࡵࡶࡪࡴࡴࡠࡤࡵࡥࡳࡩࡨࡾࠤᬹ")).split(bstack1l1l11_opy_ (u"ࠬࡢ࡮ࠨᬺ"))
                    logger.debug(bstack1l1l11_opy_ (u"ࠨࡃࡩࡣࡱ࡫ࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡢࡦࡶࡺࡩࡪࡴࠠࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃࠠࡢࡰࡧࠤࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃ࠺ࠡࠤᬻ") + str(bstack111llll1111_opy_) + bstack1l1l11_opy_ (u"ࠢࠣᬼ"))
                    result[bstack1l1l11_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᬽ")] = [f.strip() for f in bstack111llll1111_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll11llll1_opy_ (u"ࠤࡾࡦࡦࡹࡥࡠࡤࡵࡥࡳࡩࡨࡾ࠰࠱ࡿࡨࡻࡲࡳࡧࡱࡸࡤࡨࡲࡢࡰࡦ࡬ࢂࠨᬾ")))
                except Exception:
                    logger.debug(bstack1l1l11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡶࠣࡧ࡭ࡧ࡮ࡨࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡪࡷࡵ࡭ࠡࡤࡵࡥࡳࡩࡨࠡࡥࡲࡱࡵࡧࡲࡪࡵࡲࡲ࠳ࠦࡆࡢ࡮࡯࡭ࡳ࡭ࠠࡣࡣࡦ࡯ࠥࡺ࡯ࠡࡴࡨࡧࡪࡴࡴࠡࡥࡲࡱࡲ࡯ࡴࡴ࠰ࠥᬿ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack1l1l11_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᭀ")] = _11l11ll111l_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack1l1l11_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᭁ")] = _11l11ll111l_opy_(commits[:5])
            bstack11l11ll11ll_opy_ = set()
            bstack111ll1l1l11_opy_ = []
            for commit in commits:
                logger.debug(bstack1l1l11_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡪࡶ࠽ࠤࠧᭂ") + str(commit.message) + bstack1l1l11_opy_ (u"ࠢࠣᭃ"))
                bstack111lll11111_opy_ = commit.author.name if commit.author else bstack1l1l11_opy_ (u"ࠣࡗࡱ࡯ࡳࡵࡷ࡯ࠤ᭄")
                bstack11l11ll11ll_opy_.add(bstack111lll11111_opy_)
                bstack111ll1l1l11_opy_.append({
                    bstack1l1l11_opy_ (u"ࠤࡰࡩࡸࡹࡡࡨࡧࠥᭅ"): commit.message.strip(),
                    bstack1l1l11_opy_ (u"ࠥࡹࡸ࡫ࡲࠣᭆ"): bstack111lll11111_opy_
                })
            result[bstack1l1l11_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧᭇ")] = list(bstack11l11ll11ll_opy_)
            result[bstack1l1l11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡒ࡫ࡳࡴࡣࡪࡩࡸࠨᭈ")] = bstack111ll1l1l11_opy_
            result[bstack1l1l11_opy_ (u"ࠨࡰࡳࡆࡤࡸࡪࠨᭉ")] = bstack11l11l11111_opy_.committed_datetime.strftime(bstack1l1l11_opy_ (u"࡛ࠢࠦ࠰ࠩࡲ࠳ࠥࡥࠤᭊ"))
            if (not result[bstack1l1l11_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᭋ")] or result[bstack1l1l11_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᭌ")].strip() == bstack1l1l11_opy_ (u"ࠥࠦ᭍")) and bstack11l11l11111_opy_.message:
                bstack11l11l11lll_opy_ = bstack11l11l11111_opy_.message.strip().splitlines()
                result[bstack1l1l11_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧ᭎")] = bstack11l11l11lll_opy_[0] if bstack11l11l11lll_opy_ else bstack1l1l11_opy_ (u"ࠧࠨ᭏")
                if len(bstack11l11l11lll_opy_) > 2:
                    result[bstack1l1l11_opy_ (u"ࠨࡰࡳࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠨ᭐")] = bstack1l1l11_opy_ (u"ࠧ࡝ࡰࠪ᭑").join(bstack11l11l11lll_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack1l1l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡳࡹࡱࡧࡴࡪࡰࡪࠤࡌ࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡪࡴࡸࠠࡂࡋࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࠨࡧࡱ࡯ࡨࡪࡸ࠺ࠡࡽࡩࡳࡱࡪࡥࡳࡿࠬ࠾ࠥࠨ᭒") + str(err) + bstack1l1l11_opy_ (u"ࠤࠥ᭓"))
    filtered_results = [
        r
        for r in results
        if _111llll1l11_opy_(r)
    ]
    return filtered_results
def _111llll1l11_opy_(result):
    bstack1l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡌࡪࡲࡰࡦࡴࠣࡸࡴࠦࡣࡩࡧࡦ࡯ࠥ࡯ࡦࠡࡣࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡵࡩࡸࡻ࡬ࡵࠢ࡬ࡷࠥࡼࡡ࡭࡫ࡧࠤ࠭ࡴ࡯࡯࠯ࡨࡱࡵࡺࡹࠡࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠠࡢࡰࡧࠤࡦࡻࡴࡩࡱࡵࡷ࠮࠴ࠊࠡࠢࠣࠤࠧࠨࠢ᭔")
    return (
        isinstance(result.get(bstack1l1l11_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥ᭕"), None), list)
        and len(result[bstack1l1l11_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦ᭖")]) > 0
        and isinstance(result.get(bstack1l1l11_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡹࠢ᭗"), None), list)
        and len(result[bstack1l1l11_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣ᭘")]) > 0
    )
def _11l111l1l11_opy_(repo):
    bstack1l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡖࡵࡽࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡹ࡮ࡥࠡࡤࡤࡷࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡲࡦࡲࡲࠤࡼ࡯ࡴࡩࡱࡸࡸࠥ࡮ࡡࡳࡦࡦࡳࡩ࡫ࡤࠡࡰࡤࡱࡪࡹࠠࡢࡰࡧࠤࡼࡵࡲ࡬ࠢࡺ࡭ࡹ࡮ࠠࡢ࡮࡯ࠤ࡛ࡉࡓࠡࡲࡵࡳࡻ࡯ࡤࡦࡴࡶ࠲ࠏࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠࡥࡧࡩࡥࡺࡲࡴࠡࡤࡵࡥࡳࡩࡨࠡ࡫ࡩࠤࡵࡵࡳࡴ࡫ࡥࡰࡪ࠲ࠠࡦ࡮ࡶࡩࠥࡔ࡯࡯ࡧ࠱ࠎࠥࠦࠠࠡࠤࠥࠦ᭙")
    try:
        try:
            origin = repo.remotes.origin
            bstack11l11llll1l_opy_ = origin.refs[bstack1l1l11_opy_ (u"ࠩࡋࡉࡆࡊࠧ᭚")]
            target = bstack11l11llll1l_opy_.reference.name
            if target.startswith(bstack1l1l11_opy_ (u"ࠪࡳࡷ࡯ࡧࡪࡰ࠲ࠫ᭛")):
                return target
        except Exception:
            pass
        if repo.heads:
            return repo.heads[0].name
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack1l1l11_opy_ (u"ࠫࡴࡸࡩࡨ࡫ࡱ࠳ࠬ᭜")):
                    return ref.name
    except Exception:
        pass
    return None
def _11l11ll111l_opy_(commits):
    bstack1l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡍࡥࡵࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡧ࡭ࡧ࡮ࡨࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡪࡷࡵ࡭ࠡࡣࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡨࡵ࡭࡮࡫ࡷࡷ࠳ࠐࠠࠡࠢࠣࠦࠧࠨ᭝")
    bstack111llll1111_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111ll11lll1_opy_ in diff:
                        if bstack111ll11lll1_opy_.a_path:
                            bstack111llll1111_opy_.add(bstack111ll11lll1_opy_.a_path)
                        if bstack111ll11lll1_opy_.b_path:
                            bstack111llll1111_opy_.add(bstack111ll11lll1_opy_.b_path)
    except Exception:
        pass
    return list(bstack111llll1111_opy_)
def bstack11l111111l1_opy_(bstack11l111111ll_opy_):
    bstack111llll11ll_opy_ = bstack11l111l1lll_opy_(bstack11l111111ll_opy_)
    if bstack111llll11ll_opy_ and bstack111llll11ll_opy_ > bstack11l1l1llll1_opy_:
        bstack11l11l1l1l1_opy_ = bstack111llll11ll_opy_ - bstack11l1l1llll1_opy_
        bstack11l11l11l1l_opy_ = bstack111lll111l1_opy_(bstack11l111111ll_opy_[bstack1l1l11_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢ᭞")], bstack11l11l1l1l1_opy_)
        bstack11l111111ll_opy_[bstack1l1l11_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣ᭟")] = bstack11l11l11l1l_opy_
        logger.info(bstack1l1l11_opy_ (u"ࠣࡖ࡫ࡩࠥࡩ࡯࡮࡯࡬ࡸࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦ࠱ࠤࡘ࡯ࡺࡦࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࠥࡧࡦࡵࡧࡵࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࢀࢃࠠࡌࡄࠥ᭠")
                    .format(bstack11l111l1lll_opy_(bstack11l111111ll_opy_) / 1024))
    return bstack11l111111ll_opy_
def bstack11l111l1lll_opy_(bstack1l1l11111l_opy_):
    try:
        if bstack1l1l11111l_opy_:
            bstack111ll1lllll_opy_ = json.dumps(bstack1l1l11111l_opy_)
            bstack111lll11l11_opy_ = sys.getsizeof(bstack111ll1lllll_opy_)
            return bstack111lll11l11_opy_
    except Exception as e:
        logger.debug(bstack1l1l11_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡥࡤࡰࡨࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡋࡕࡒࡒࠥࡵࡢ࡫ࡧࡦࡸ࠿ࠦࡻࡾࠤ᭡").format(e))
    return -1
def bstack111lll111l1_opy_(field, bstack11l111ll1ll_opy_):
    try:
        bstack11l1111l111_opy_ = len(bytes(bstack11l1ll11111_opy_, bstack1l1l11_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩ᭢")))
        bstack11l11l1l11l_opy_ = bytes(field, bstack1l1l11_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ᭣"))
        bstack11l1111ll1l_opy_ = len(bstack11l11l1l11l_opy_)
        bstack111lll1ll1l_opy_ = ceil(bstack11l1111ll1l_opy_ - bstack11l111ll1ll_opy_ - bstack11l1111l111_opy_)
        if bstack111lll1ll1l_opy_ > 0:
            bstack11l111l1ll1_opy_ = bstack11l11l1l11l_opy_[:bstack111lll1ll1l_opy_].decode(bstack1l1l11_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ᭤"), errors=bstack1l1l11_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࠭᭥")) + bstack11l1ll11111_opy_
            return bstack11l111l1ll1_opy_
    except Exception as e:
        logger.debug(bstack1l1l11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡪࡲࡤ࠭ࠢࡱࡳࡹ࡮ࡩ࡯ࡩࠣࡻࡦࡹࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦࠣ࡬ࡪࡸࡥ࠻ࠢࡾࢁࠧ᭦").format(e))
    return field
def bstack1l1111l11l_opy_():
    env = os.environ
    if (bstack1l1l11_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨ᭧") in env and len(env[bstack1l1l11_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢ᭨")]) > 0) or (
            bstack1l1l11_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤ᭩") in env and len(env[bstack1l1l11_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥ᭪")]) > 0):
        return {
            bstack1l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᭫"): bstack1l1l11_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹ᭬ࠢ"),
            bstack1l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᭭"): env.get(bstack1l1l11_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ᭮")),
            bstack1l1l11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᭯"): env.get(bstack1l1l11_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ᭰")),
            bstack1l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᭱"): env.get(bstack1l1l11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᭲"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠨࡃࡊࠤ᭳")) == bstack1l1l11_opy_ (u"ࠢࡵࡴࡸࡩࠧ᭴") and bstack1lllll1l1_opy_(env.get(bstack1l1l11_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥ᭵"))):
        return {
            bstack1l1l11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᭶"): bstack1l1l11_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧ᭷"),
            bstack1l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᭸"): env.get(bstack1l1l11_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣ᭹")),
            bstack1l1l11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᭺"): env.get(bstack1l1l11_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦ᭻")),
            bstack1l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᭼"): env.get(bstack1l1l11_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧ᭽"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠥࡇࡎࠨ᭾")) == bstack1l1l11_opy_ (u"ࠦࡹࡸࡵࡦࠤ᭿") and bstack1lllll1l1_opy_(env.get(bstack1l1l11_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧᮀ"))):
        return {
            bstack1l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᮁ"): bstack1l1l11_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥᮂ"),
            bstack1l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᮃ"): env.get(bstack1l1l11_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤᮄ")),
            bstack1l1l11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᮅ"): env.get(bstack1l1l11_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᮆ")),
            bstack1l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᮇ"): env.get(bstack1l1l11_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᮈ"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠢࡄࡋࠥᮉ")) == bstack1l1l11_opy_ (u"ࠣࡶࡵࡹࡪࠨᮊ") and env.get(bstack1l1l11_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥᮋ")) == bstack1l1l11_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧᮌ"):
        return {
            bstack1l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᮍ"): bstack1l1l11_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢᮎ"),
            bstack1l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᮏ"): None,
            bstack1l1l11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᮐ"): None,
            bstack1l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᮑ"): None
        }
    if env.get(bstack1l1l11_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧᮒ")) and env.get(bstack1l1l11_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᮓ")):
        return {
            bstack1l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᮔ"): bstack1l1l11_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣᮕ"),
            bstack1l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᮖ"): env.get(bstack1l1l11_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧᮗ")),
            bstack1l1l11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᮘ"): None,
            bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᮙ"): env.get(bstack1l1l11_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᮚ"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠦࡈࡏࠢᮛ")) == bstack1l1l11_opy_ (u"ࠧࡺࡲࡶࡧࠥᮜ") and bstack1lllll1l1_opy_(env.get(bstack1l1l11_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧᮝ"))):
        return {
            bstack1l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᮞ"): bstack1l1l11_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢᮟ"),
            bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᮠ"): env.get(bstack1l1l11_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨᮡ")),
            bstack1l1l11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᮢ"): None,
            bstack1l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᮣ"): env.get(bstack1l1l11_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᮤ"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠢࡄࡋࠥᮥ")) == bstack1l1l11_opy_ (u"ࠣࡶࡵࡹࡪࠨᮦ") and bstack1lllll1l1_opy_(env.get(bstack1l1l11_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧᮧ"))):
        return {
            bstack1l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣᮨ"): bstack1l1l11_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢᮩ"),
            bstack1l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬᮪ࠣ"): env.get(bstack1l1l11_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐ᮫ࠧ")),
            bstack1l1l11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᮬ"): env.get(bstack1l1l11_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᮭ")),
            bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᮮ"): env.get(bstack1l1l11_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨᮯ"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠦࡈࡏࠢ᮰")) == bstack1l1l11_opy_ (u"ࠧࡺࡲࡶࡧࠥ᮱") and bstack1lllll1l1_opy_(env.get(bstack1l1l11_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤ᮲"))):
        return {
            bstack1l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᮳"): bstack1l1l11_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣ᮴"),
            bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᮵"): env.get(bstack1l1l11_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢ᮶")),
            bstack1l1l11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᮷"): env.get(bstack1l1l11_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥ᮸")),
            bstack1l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᮹"): env.get(bstack1l1l11_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥᮺ"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠣࡅࡌࠦᮻ")) == bstack1l1l11_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᮼ") and bstack1lllll1l1_opy_(env.get(bstack1l1l11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨᮽ"))):
        return {
            bstack1l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᮾ"): bstack1l1l11_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣᮿ"),
            bstack1l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᯀ"): env.get(bstack1l1l11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᯁ")),
            bstack1l1l11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᯂ"): env.get(bstack1l1l11_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦᯃ")) or env.get(bstack1l1l11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᯄ")),
            bstack1l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᯅ"): env.get(bstack1l1l11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᯆ"))
        }
    if bstack1lllll1l1_opy_(env.get(bstack1l1l11_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣᯇ"))):
        return {
            bstack1l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᯈ"): bstack1l1l11_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳࠣᯉ"),
            bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᯊ"): bstack1l1l11_opy_ (u"ࠥࡿࢂࢁࡽࠣᯋ").format(env.get(bstack1l1l11_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧᯌ")), env.get(bstack1l1l11_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬᯍ"))),
            bstack1l1l11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᯎ"): env.get(bstack1l1l11_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨᯏ")),
            bstack1l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᯐ"): env.get(bstack1l1l11_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤᯑ"))
        }
    if bstack1lllll1l1_opy_(env.get(bstack1l1l11_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧᯒ"))):
        return {
            bstack1l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᯓ"): bstack1l1l11_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢᯔ"),
            bstack1l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᯕ"): bstack1l1l11_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨᯖ").format(env.get(bstack1l1l11_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧᯗ")), env.get(bstack1l1l11_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪᯘ")), env.get(bstack1l1l11_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫᯙ")), env.get(bstack1l1l11_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨᯚ"))),
            bstack1l1l11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᯛ"): env.get(bstack1l1l11_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᯜ")),
            bstack1l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᯝ"): env.get(bstack1l1l11_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᯞ"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥᯟ")) and env.get(bstack1l1l11_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧᯠ")):
        return {
            bstack1l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᯡ"): bstack1l1l11_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢᯢ"),
            bstack1l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᯣ"): bstack1l1l11_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥᯤ").format(env.get(bstack1l1l11_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫᯥ")), env.get(bstack1l1l11_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ᯦࡚ࠧ")), env.get(bstack1l1l11_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪᯧ"))),
            bstack1l1l11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᯨ"): env.get(bstack1l1l11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧᯩ")),
            bstack1l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᯪ"): env.get(bstack1l1l11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢᯫ"))
        }
    if any([env.get(bstack1l1l11_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᯬ")), env.get(bstack1l1l11_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣᯭ")), env.get(bstack1l1l11_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢᯮ"))]):
        return {
            bstack1l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᯯ"): bstack1l1l11_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨࠧᯰ"),
            bstack1l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᯱ"): env.get(bstack1l1l11_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᯲")),
            bstack1l1l11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧ᯳ࠥ"): env.get(bstack1l1l11_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢ᯴")),
            bstack1l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᯵"): env.get(bstack1l1l11_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤ᯶"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥ᯷")):
        return {
            bstack1l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᯸"): bstack1l1l11_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵࠢ᯹"),
            bstack1l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᯺"): env.get(bstack1l1l11_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯ࠦ᯻")),
            bstack1l1l11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᯼"): env.get(bstack1l1l11_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧࠥ᯽")),
            bstack1l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᯾"): env.get(bstack1l1l11_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦ᯿"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࠣᰀ")) or env.get(bstack1l1l11_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥᰁ")):
        return {
            bstack1l1l11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᰂ"): bstack1l1l11_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵࠦᰃ"),
            bstack1l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᰄ"): env.get(bstack1l1l11_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᰅ")),
            bstack1l1l11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᰆ"): bstack1l1l11_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠢᰇ") if env.get(bstack1l1l11_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥᰈ")) else None,
            bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᰉ"): env.get(bstack1l1l11_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔࠣᰊ"))
        }
    if any([env.get(bstack1l1l11_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤᰋ")), env.get(bstack1l1l11_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᰌ")), env.get(bstack1l1l11_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᰍ"))]):
        return {
            bstack1l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᰎ"): bstack1l1l11_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪࠢᰏ"),
            bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᰐ"): None,
            bstack1l1l11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᰑ"): env.get(bstack1l1l11_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣᰒ")),
            bstack1l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᰓ"): env.get(bstack1l1l11_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣᰔ"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥᰕ")):
        return {
            bstack1l1l11_opy_ (u"ࠣࡰࡤࡱࡪࠨᰖ"): bstack1l1l11_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩࠧᰗ"),
            bstack1l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᰘ"): env.get(bstack1l1l11_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᰙ")),
            bstack1l1l11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᰚ"): bstack1l1l11_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃࠢᰛ").format(env.get(bstack1l1l11_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠪᰜ"))) if env.get(bstack1l1l11_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦᰝ")) else None,
            bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᰞ"): env.get(bstack1l1l11_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᰟ"))
        }
    if bstack1lllll1l1_opy_(env.get(bstack1l1l11_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝ࠧᰠ"))):
        return {
            bstack1l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᰡ"): bstack1l1l11_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿࠢᰢ"),
            bstack1l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᰣ"): env.get(bstack1l1l11_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧᰤ")),
            bstack1l1l11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᰥ"): env.get(bstack1l1l11_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨᰦ")),
            bstack1l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᰧ"): env.get(bstack1l1l11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᰨ"))
        }
    if bstack1lllll1l1_opy_(env.get(bstack1l1l11_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ࡙ࠢᰩ"))):
        return {
            bstack1l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᰪ"): bstack1l1l11_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤᰫ"),
            bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᰬ"): bstack1l1l11_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦᰭ").format(env.get(bstack1l1l11_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨᰮ")), env.get(bstack1l1l11_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩᰯ")), env.get(bstack1l1l11_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ࠭ᰰ"))),
            bstack1l1l11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᰱ"): env.get(bstack1l1l11_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥᰲ")),
            bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᰳ"): env.get(bstack1l1l11_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥᰴ"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠦࡈࡏࠢᰵ")) == bstack1l1l11_opy_ (u"ࠧࡺࡲࡶࡧࠥᰶ") and env.get(bstack1l1l11_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨ᰷")) == bstack1l1l11_opy_ (u"ࠢ࠲ࠤ᰸"):
        return {
            bstack1l1l11_opy_ (u"ࠣࡰࡤࡱࡪࠨ᰹"): bstack1l1l11_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤ᰺"),
            bstack1l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᰻"): bstack1l1l11_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢ᰼").format(env.get(bstack1l1l11_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩ᰽"))),
            bstack1l1l11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᰾"): None,
            bstack1l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᰿"): None,
        }
    if env.get(bstack1l1l11_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦ᱀")):
        return {
            bstack1l1l11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᱁"): bstack1l1l11_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧ᱂"),
            bstack1l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᱃"): None,
            bstack1l1l11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᱄"): env.get(bstack1l1l11_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢ᱅")),
            bstack1l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᱆"): env.get(bstack1l1l11_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢ᱇"))
        }
    if any([env.get(bstack1l1l11_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧ᱈")), env.get(bstack1l1l11_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥ᱉")), env.get(bstack1l1l11_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤ᱊")), env.get(bstack1l1l11_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨ᱋"))]):
        return {
            bstack1l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᱌"): bstack1l1l11_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥᱍ"),
            bstack1l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᱎ"): None,
            bstack1l1l11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱏ"): env.get(bstack1l1l11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦ᱐")) or None,
            bstack1l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᱑"): env.get(bstack1l1l11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢ᱒"), 0)
        }
    if env.get(bstack1l1l11_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦ᱓")):
        return {
            bstack1l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᱔"): bstack1l1l11_opy_ (u"ࠣࡉࡲࡇࡉࠨ᱕"),
            bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᱖"): None,
            bstack1l1l11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᱗"): env.get(bstack1l1l11_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤ᱘")),
            bstack1l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᱙"): env.get(bstack1l1l11_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧᱚ"))
        }
    if env.get(bstack1l1l11_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᱛ")):
        return {
            bstack1l1l11_opy_ (u"ࠣࡰࡤࡱࡪࠨᱜ"): bstack1l1l11_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧᱝ"),
            bstack1l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᱞ"): env.get(bstack1l1l11_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᱟ")),
            bstack1l1l11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᱠ"): env.get(bstack1l1l11_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤᱡ")),
            bstack1l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᱢ"): env.get(bstack1l1l11_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᱣ"))
        }
    return {bstack1l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᱤ"): None}
def get_host_info():
    return {
        bstack1l1l11_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧᱥ"): platform.node(),
        bstack1l1l11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨᱦ"): platform.system(),
        bstack1l1l11_opy_ (u"ࠧࡺࡹࡱࡧࠥᱧ"): platform.machine(),
        bstack1l1l11_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢᱨ"): platform.version(),
        bstack1l1l11_opy_ (u"ࠢࡢࡴࡦ࡬ࠧᱩ"): platform.architecture()[0]
    }
def bstack1llll1111_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111ll1ll11l_opy_():
    if bstack1lll11l111_opy_.get_property(bstack1l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩᱪ")):
        return bstack1l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᱫ")
    return bstack1l1l11_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩᱬ")
def bstack111llllllll_opy_(driver):
    info = {
        bstack1l1l11_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᱭ"): driver.capabilities,
        bstack1l1l11_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩᱮ"): driver.session_id,
        bstack1l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᱯ"): driver.capabilities.get(bstack1l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᱰ"), None),
        bstack1l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪᱱ"): driver.capabilities.get(bstack1l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᱲ"), None),
        bstack1l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬᱳ"): driver.capabilities.get(bstack1l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪᱴ"), None),
        bstack1l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᱵ"):driver.capabilities.get(bstack1l1l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᱶ"), None),
    }
    if bstack111ll1ll11l_opy_() == bstack1l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᱷ"):
        if bstack1lllll11l_opy_():
            info[bstack1l1l11_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᱸ")] = bstack1l1l11_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨᱹ")
        elif driver.capabilities.get(bstack1l1l11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᱺ"), {}).get(bstack1l1l11_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᱻ"), False):
            info[bstack1l1l11_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᱼ")] = bstack1l1l11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᱽ")
        else:
            info[bstack1l1l11_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨ᱾")] = bstack1l1l11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪ᱿")
    return info
def bstack1lllll11l_opy_():
    if bstack1lll11l111_opy_.get_property(bstack1l1l11_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨᲀ")):
        return True
    if bstack1lllll1l1_opy_(os.environ.get(bstack1l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫᲁ"), None)):
        return True
    return False
def bstack1lll1ll1l_opy_(bstack111ll1l1lll_opy_, url, data, config):
    headers = config.get(bstack1l1l11_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᲂ"), None)
    proxies = bstack1l1l11111_opy_(config, url)
    auth = config.get(bstack1l1l11_opy_ (u"ࠬࡧࡵࡵࡪࠪᲃ"), None)
    response = requests.request(
            bstack111ll1l1lll_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1ll1ll11l1_opy_(bstack1ll11llll_opy_, size):
    bstack11lllll11_opy_ = []
    while len(bstack1ll11llll_opy_) > size:
        bstack1lll11111l_opy_ = bstack1ll11llll_opy_[:size]
        bstack11lllll11_opy_.append(bstack1lll11111l_opy_)
        bstack1ll11llll_opy_ = bstack1ll11llll_opy_[size:]
    bstack11lllll11_opy_.append(bstack1ll11llll_opy_)
    return bstack11lllll11_opy_
def bstack11l11l1lll1_opy_(message, bstack11l11l1llll_opy_=False):
    os.write(1, bytes(message, bstack1l1l11_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᲄ")))
    os.write(1, bytes(bstack1l1l11_opy_ (u"ࠧ࡝ࡰࠪᲅ"), bstack1l1l11_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᲆ")))
    if bstack11l11l1llll_opy_:
        with open(bstack1l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯ࡲ࠵࠶ࡿ࠭ࠨᲇ") + os.environ[bstack1l1l11_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᲈ")] + bstack1l1l11_opy_ (u"ࠫ࠳ࡲ࡯ࡨࠩᲉ"), bstack1l1l11_opy_ (u"ࠬࡧࠧᲊ")) as f:
            f.write(message + bstack1l1l11_opy_ (u"࠭࡜࡯ࠩ᲋"))
def bstack1l1ll1l11ll_opy_():
    return os.environ[bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪ᲌")].lower() == bstack1l1l11_opy_ (u"ࠨࡶࡵࡹࡪ࠭᲍")
def bstack11llll11_opy_():
    return bstack1111ll1lll_opy_().replace(tzinfo=None).isoformat() + bstack1l1l11_opy_ (u"ࠩ࡝ࠫ᲎")
def bstack111lll11l1l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1l1l11_opy_ (u"ࠪ࡞ࠬ᲏"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1l1l11_opy_ (u"ࠫ࡟࠭Ა")))).total_seconds() * 1000
def bstack111ll1ll1l1_opy_(timestamp):
    return bstack11l1111l11l_opy_(timestamp).isoformat() + bstack1l1l11_opy_ (u"ࠬࡠࠧᲑ")
def bstack111ll1llll1_opy_(bstack111lllll111_opy_):
    date_format = bstack1l1l11_opy_ (u"࡚࠭ࠥࠧࡰࠩࡩࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࠯ࠧࡩࠫᲒ")
    bstack11l111l11ll_opy_ = datetime.datetime.strptime(bstack111lllll111_opy_, date_format)
    return bstack11l111l11ll_opy_.isoformat() + bstack1l1l11_opy_ (u"࡛ࠧࠩᲓ")
def bstack11l11lllll1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1l1l11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᲔ")
    else:
        return bstack1l1l11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᲕ")
def bstack1lllll1l1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1l1l11_opy_ (u"ࠪࡸࡷࡻࡥࠨᲖ")
def bstack11l1111ll11_opy_(val):
    return val.__str__().lower() == bstack1l1l11_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪᲗ")
def error_handler(bstack11l11ll1111_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack11l11ll1111_opy_ as e:
                print(bstack1l1l11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᲘ").format(func.__name__, bstack11l11ll1111_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack11l11111l11_opy_(bstack11l111l1111_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack11l111l1111_opy_(cls, *args, **kwargs)
            except bstack11l11ll1111_opy_ as e:
                print(bstack1l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨᲙ").format(bstack11l111l1111_opy_.__name__, bstack11l11ll1111_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack11l11111l11_opy_
    else:
        return decorator
def bstack1l11111ll1_opy_(bstack1111l1l1l1_opy_):
    if os.getenv(bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᲚ")) is not None:
        return bstack1lllll1l1_opy_(os.getenv(bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᲛ")))
    if bstack1l1l11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭Ნ") in bstack1111l1l1l1_opy_ and bstack11l1111ll11_opy_(bstack1111l1l1l1_opy_[bstack1l1l11_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᲝ")]):
        return False
    if bstack1l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭Პ") in bstack1111l1l1l1_opy_ and bstack11l1111ll11_opy_(bstack1111l1l1l1_opy_[bstack1l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᲟ")]):
        return False
    return True
def bstack1l11lll1ll_opy_():
    try:
        from pytest_bdd import reporting
        bstack111ll1ll111_opy_ = os.environ.get(bstack1l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࠨᲠ"), None)
        return bstack111ll1ll111_opy_ is None or bstack111ll1ll111_opy_ == bstack1l1l11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᲡ")
    except Exception as e:
        return False
def bstack1ll1l1lll_opy_(hub_url, CONFIG):
    if bstack1l1ll1lll_opy_() <= version.parse(bstack1l1l11_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨᲢ")):
        if hub_url:
            return bstack1l1l11_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥᲣ") + hub_url + bstack1l1l11_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢᲤ")
        return bstack111ll1l1l_opy_
    if hub_url:
        return bstack1l1l11_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᲥ") + hub_url + bstack1l1l11_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨᲦ")
    return bstack11l1llll_opy_
def bstack11l11ll1l1l_opy_():
    return isinstance(os.getenv(bstack1l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡌࡖࡉࡌࡒࠬᲧ")), str)
def bstack11ll11111_opy_(url):
    return urlparse(url).hostname
def bstack11ll1ll1l_opy_(hostname):
    for bstack11llll1111_opy_ in bstack11l11l111l_opy_:
        regex = re.compile(bstack11llll1111_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11l11l11ll1_opy_(bstack111lll1l11l_opy_, file_name, logger):
    bstack11ll1l1l11_opy_ = os.path.join(os.path.expanduser(bstack1l1l11_opy_ (u"ࠧࡿࠩᲨ")), bstack111lll1l11l_opy_)
    try:
        if not os.path.exists(bstack11ll1l1l11_opy_):
            os.makedirs(bstack11ll1l1l11_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1l1l11_opy_ (u"ࠨࢀࠪᲩ")), bstack111lll1l11l_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1l1l11_opy_ (u"ࠩࡺࠫᲪ")):
                pass
            with open(file_path, bstack1l1l11_opy_ (u"ࠥࡻ࠰ࠨᲫ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l111lll1l_opy_.format(str(e)))
def bstack11l11l1ll1l_opy_(file_name, key, value, logger):
    file_path = bstack11l11l11ll1_opy_(bstack1l1l11_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᲬ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1lll1ll1l1_opy_ = json.load(open(file_path, bstack1l1l11_opy_ (u"ࠬࡸࡢࠨᲭ")))
        else:
            bstack1lll1ll1l1_opy_ = {}
        bstack1lll1ll1l1_opy_[key] = value
        with open(file_path, bstack1l1l11_opy_ (u"ࠨࡷࠬࠤᲮ")) as outfile:
            json.dump(bstack1lll1ll1l1_opy_, outfile)
def bstack1ll1l111l_opy_(file_name, logger):
    file_path = bstack11l11l11ll1_opy_(bstack1l1l11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᲯ"), file_name, logger)
    bstack1lll1ll1l1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1l1l11_opy_ (u"ࠨࡴࠪᲰ")) as bstack11ll111l_opy_:
            bstack1lll1ll1l1_opy_ = json.load(bstack11ll111l_opy_)
    return bstack1lll1ll1l1_opy_
def bstack11l1111l1_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1l1l11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨ࠾ࠥ࠭Ჱ") + file_path + bstack1l1l11_opy_ (u"ࠪࠤࠬᲲ") + str(e))
def bstack1l1ll1lll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1l1l11_opy_ (u"ࠦࡁࡔࡏࡕࡕࡈࡘࡃࠨᲳ")
def bstack11l1l111_opy_(config):
    if bstack1l1l11_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᲴ") in config:
        del (config[bstack1l1l11_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᲵ")])
        return False
    if bstack1l1ll1lll_opy_() < version.parse(bstack1l1l11_opy_ (u"ࠧ࠴࠰࠷࠲࠵࠭Ჶ")):
        return False
    if bstack1l1ll1lll_opy_() >= version.parse(bstack1l1l11_opy_ (u"ࠨ࠶࠱࠵࠳࠻ࠧᲷ")):
        return True
    if bstack1l1l11_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᲸ") in config and config[bstack1l1l11_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᲹ")] is False:
        return False
    else:
        return True
def bstack111l11lll_opy_(args_list, bstack11l1111l1l1_opy_):
    index = -1
    for value in bstack11l1111l1l1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack11ll1ll111l_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack11ll1ll111l_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack111ll1lll1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack111ll1lll1_opy_ = bstack111ll1lll1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1l1l11_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᲺ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ᲻"), exception=exception)
    def bstack111111l11l_opy_(self):
        if self.result != bstack1l1l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭᲼"):
            return None
        if isinstance(self.exception_type, str) and bstack1l1l11_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥᲽ") in self.exception_type:
            return bstack1l1l11_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤᲾ")
        return bstack1l1l11_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥᲿ")
    def bstack111llll111l_opy_(self):
        if self.result != bstack1l1l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ᳀"):
            return None
        if self.bstack111ll1lll1_opy_:
            return self.bstack111ll1lll1_opy_
        return bstack11l11llllll_opy_(self.exception)
def bstack11l11llllll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack11l11llll11_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l11111lll_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l1ll11l1_opy_(config, logger):
    try:
        import playwright
        bstack11l11111l1l_opy_ = playwright.__file__
        bstack11l11l111l1_opy_ = os.path.split(bstack11l11111l1l_opy_)
        bstack11l11lll111_opy_ = bstack11l11l111l1_opy_[0] + bstack1l1l11_opy_ (u"ࠫ࠴ࡪࡲࡪࡸࡨࡶ࠴ࡶࡡࡤ࡭ࡤ࡫ࡪ࠵࡬ࡪࡤ࠲ࡧࡱ࡯࠯ࡤ࡮࡬࠲࡯ࡹࠧ᳁")
        os.environ[bstack1l1l11_opy_ (u"ࠬࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠨ᳂")] = bstack1l11l11ll1_opy_(config)
        with open(bstack11l11lll111_opy_, bstack1l1l11_opy_ (u"࠭ࡲࠨ᳃")) as f:
            bstack1llll1ll1_opy_ = f.read()
            bstack11l11111lll_opy_ = bstack1l1l11_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹ࠭᳄")
            bstack111lll11lll_opy_ = bstack1llll1ll1_opy_.find(bstack11l11111lll_opy_)
            if bstack111lll11lll_opy_ == -1:
              process = subprocess.Popen(bstack1l1l11_opy_ (u"ࠣࡰࡳࡱࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠧ᳅"), shell=True, cwd=bstack11l11l111l1_opy_[0])
              process.wait()
              bstack111ll11l1ll_opy_ = bstack1l1l11_opy_ (u"ࠩࠥࡹࡸ࡫ࠠࡴࡶࡵ࡭ࡨࡺࠢ࠼ࠩ᳆")
              bstack111ll1l1l1l_opy_ = bstack1l1l11_opy_ (u"ࠥࠦࠧࠦ࡜ࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࡡࠨ࠻ࠡࡥࡲࡲࡸࡺࠠࡼࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴࠥࢃࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪ࠭ࡀࠦࡩࡧࠢࠫࡴࡷࡵࡣࡦࡵࡶ࠲ࡪࡴࡶ࠯ࡉࡏࡓࡇࡇࡌࡠࡃࡊࡉࡓ࡚࡟ࡉࡖࡗࡔࡤࡖࡒࡐ࡚࡜࠭ࠥࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠩࠫ࠾ࠤࠧࠨࠢ᳇")
              bstack111lll1111l_opy_ = bstack1llll1ll1_opy_.replace(bstack111ll11l1ll_opy_, bstack111ll1l1l1l_opy_)
              with open(bstack11l11lll111_opy_, bstack1l1l11_opy_ (u"ࠫࡼ࠭᳈")) as f:
                f.write(bstack111lll1111l_opy_)
    except Exception as e:
        logger.error(bstack111l1ll11_opy_.format(str(e)))
def bstack1l111ll1ll_opy_():
  try:
    bstack111lllllll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l11_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬ᳉"))
    bstack11l1111l1ll_opy_ = []
    if os.path.exists(bstack111lllllll1_opy_):
      with open(bstack111lllllll1_opy_) as f:
        bstack11l1111l1ll_opy_ = json.load(f)
      os.remove(bstack111lllllll1_opy_)
    return bstack11l1111l1ll_opy_
  except:
    pass
  return []
def bstack1l1l1ll11_opy_(bstack11lll1ll11_opy_):
  try:
    bstack11l1111l1ll_opy_ = []
    bstack111lllllll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l11_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬࠯࡬ࡶࡳࡳ࠭᳊"))
    if os.path.exists(bstack111lllllll1_opy_):
      with open(bstack111lllllll1_opy_) as f:
        bstack11l1111l1ll_opy_ = json.load(f)
    bstack11l1111l1ll_opy_.append(bstack11lll1ll11_opy_)
    with open(bstack111lllllll1_opy_, bstack1l1l11_opy_ (u"ࠧࡸࠩ᳋")) as f:
        json.dump(bstack11l1111l1ll_opy_, f)
  except:
    pass
def bstack11lll1lll_opy_(logger, bstack111llll1lll_opy_ = False):
  try:
    test_name = os.environ.get(bstack1l1l11_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫ᳌"), bstack1l1l11_opy_ (u"ࠩࠪ᳍"))
    if test_name == bstack1l1l11_opy_ (u"ࠪࠫ᳎"):
        test_name = threading.current_thread().__dict__.get(bstack1l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡆࡩࡪ࡟ࡵࡧࡶࡸࡤࡴࡡ࡮ࡧࠪ᳏"), bstack1l1l11_opy_ (u"ࠬ࠭᳐"))
    bstack11l1111111l_opy_ = bstack1l1l11_opy_ (u"࠭ࠬࠡࠩ᳑").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111llll1lll_opy_:
        bstack1lll11lll_opy_ = os.environ.get(bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ᳒"), bstack1l1l11_opy_ (u"ࠨ࠲ࠪ᳓"))
        bstack1lll1llll1_opy_ = {bstack1l1l11_opy_ (u"ࠩࡱࡥࡲ࡫᳔ࠧ"): test_name, bstack1l1l11_opy_ (u"ࠪࡩࡷࡸ࡯ࡳ᳕ࠩ"): bstack11l1111111l_opy_, bstack1l1l11_opy_ (u"ࠫ࡮ࡴࡤࡦࡺ᳖ࠪ"): bstack1lll11lll_opy_}
        bstack11l11lll1l1_opy_ = []
        bstack11l111l1l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡶࡰࡱࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱ᳗ࠫ"))
        if os.path.exists(bstack11l111l1l1l_opy_):
            with open(bstack11l111l1l1l_opy_) as f:
                bstack11l11lll1l1_opy_ = json.load(f)
        bstack11l11lll1l1_opy_.append(bstack1lll1llll1_opy_)
        with open(bstack11l111l1l1l_opy_, bstack1l1l11_opy_ (u"࠭ࡷࠨ᳘")) as f:
            json.dump(bstack11l11lll1l1_opy_, f)
    else:
        bstack1lll1llll1_opy_ = {bstack1l1l11_opy_ (u"ࠧ࡯ࡣࡰࡩ᳙ࠬ"): test_name, bstack1l1l11_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ᳚"): bstack11l1111111l_opy_, bstack1l1l11_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ᳛"): str(multiprocessing.current_process().name)}
        if bstack1l1l11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ᳜ࠧ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1lll1llll1_opy_)
  except Exception as e:
      logger.warn(bstack1l1l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡰࡺࡶࡨࡷࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽ᳝ࠣ").format(e))
def bstack1ll1lll11_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1l11_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨ᳞"))
    try:
      bstack111lllll1ll_opy_ = []
      bstack1lll1llll1_opy_ = {bstack1l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨ᳟ࠫ"): test_name, bstack1l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭᳠"): error_message, bstack1l1l11_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ᳡"): index}
      bstack11l11l1ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l11_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰ᳢ࠪ"))
      if os.path.exists(bstack11l11l1ll11_opy_):
          with open(bstack11l11l1ll11_opy_) as f:
              bstack111lllll1ll_opy_ = json.load(f)
      bstack111lllll1ll_opy_.append(bstack1lll1llll1_opy_)
      with open(bstack11l11l1ll11_opy_, bstack1l1l11_opy_ (u"ࠪࡻ᳣ࠬ")) as f:
          json.dump(bstack111lllll1ll_opy_, f)
    except Exception as e:
      logger.warn(bstack1l1l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡲࡰࡤࡲࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃ᳤ࠢ").format(e))
    return
  bstack111lllll1ll_opy_ = []
  bstack1lll1llll1_opy_ = {bstack1l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧ᳥ࠪ"): test_name, bstack1l1l11_opy_ (u"࠭ࡥࡳࡴࡲࡶ᳦ࠬ"): error_message, bstack1l1l11_opy_ (u"ࠧࡪࡰࡧࡩࡽ᳧࠭"): index}
  bstack11l11l1ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l11_opy_ (u"ࠨࡴࡲࡦࡴࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯᳨ࠩ"))
  lock_file = bstack11l11l1ll11_opy_ + bstack1l1l11_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨᳩ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11l11l1ll11_opy_):
          with open(bstack11l11l1ll11_opy_, bstack1l1l11_opy_ (u"ࠪࡶࠬᳪ")) as f:
              content = f.read().strip()
              if content:
                  bstack111lllll1ll_opy_ = json.load(open(bstack11l11l1ll11_opy_))
      bstack111lllll1ll_opy_.append(bstack1lll1llll1_opy_)
      with open(bstack11l11l1ll11_opy_, bstack1l1l11_opy_ (u"ࠫࡼ࠭ᳫ")) as f:
          json.dump(bstack111lllll1ll_opy_, f)
  except Exception as e:
    logger.warn(bstack1l1l11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡳࡱࡥࡳࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧ࠻ࠢࡾࢁࠧᳬ").format(e))
def bstack1l1ll11l11_opy_(bstack1l1ll111l_opy_, name, logger):
  try:
    bstack1lll1llll1_opy_ = {bstack1l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨ᳭ࠫ"): name, bstack1l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᳮ"): bstack1l1ll111l_opy_, bstack1l1l11_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᳯ"): str(threading.current_thread()._name)}
    return bstack1lll1llll1_opy_
  except Exception as e:
    logger.warn(bstack1l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡧ࡫ࡨࡢࡸࡨࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨᳰ").format(e))
  return
def bstack111lll1l1l1_opy_():
    return platform.system() == bstack1l1l11_opy_ (u"࡛ࠪ࡮ࡴࡤࡰࡹࡶࠫᳱ")
def bstack1l111l1lll_opy_(bstack11l11ll1l11_opy_, config, logger):
    bstack11l111ll1l1_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack11l11ll1l11_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1l1l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫࡯ࡸࡪࡸࠠࡤࡱࡱࡪ࡮࡭ࠠ࡬ࡧࡼࡷࠥࡨࡹࠡࡴࡨ࡫ࡪࡾࠠ࡮ࡣࡷࡧ࡭ࡀࠠࡼࡿࠥᳲ").format(e))
    return bstack11l111ll1l1_opy_
def bstack11l11l1l111_opy_(bstack11l111l11l1_opy_, bstack11l1111lll1_opy_):
    bstack111llll1l1l_opy_ = version.parse(bstack11l111l11l1_opy_)
    bstack11l11ll11l1_opy_ = version.parse(bstack11l1111lll1_opy_)
    if bstack111llll1l1l_opy_ > bstack11l11ll11l1_opy_:
        return 1
    elif bstack111llll1l1l_opy_ < bstack11l11ll11l1_opy_:
        return -1
    else:
        return 0
def bstack1111ll1lll_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack11l1111l11l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111llll11l1_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1l111l11_opy_(options, framework, config, bstack1ll11l1l1l_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1l1l11_opy_ (u"ࠬ࡭ࡥࡵࠩᳳ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1ll1llll11_opy_ = caps.get(bstack1l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᳴"))
    bstack111ll11llll_opy_ = True
    bstack11ll111111_opy_ = os.environ[bstack1l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᳵ")]
    bstack1ll11llll11_opy_ = config.get(bstack1l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᳶ"), False)
    if bstack1ll11llll11_opy_:
        bstack1lll1llll1l_opy_ = config.get(bstack1l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᳷"), {})
        bstack1lll1llll1l_opy_[bstack1l1l11_opy_ (u"ࠪࡥࡺࡺࡨࡕࡱ࡮ࡩࡳ࠭᳸")] = os.getenv(bstack1l1l11_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ᳹"))
        bstack11ll1ll1lll_opy_ = json.loads(os.getenv(bstack1l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ᳺ"), bstack1l1l11_opy_ (u"࠭ࡻࡾࠩ᳻"))).get(bstack1l1l11_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᳼"))
    if bstack11l1111ll11_opy_(caps.get(bstack1l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨ࡛࠸ࡉࠧ᳽"))) or bstack11l1111ll11_opy_(caps.get(bstack1l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡤࡽ࠳ࡤࠩ᳾"))):
        bstack111ll11llll_opy_ = False
    if bstack11l1l111_opy_({bstack1l1l11_opy_ (u"ࠥࡹࡸ࡫ࡗ࠴ࡅࠥ᳿"): bstack111ll11llll_opy_}):
        bstack1ll1llll11_opy_ = bstack1ll1llll11_opy_ or {}
        bstack1ll1llll11_opy_[bstack1l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᴀ")] = bstack111llll11l1_opy_(framework)
        bstack1ll1llll11_opy_[bstack1l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᴁ")] = bstack1l1ll1l11ll_opy_()
        bstack1ll1llll11_opy_[bstack1l1l11_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᴂ")] = bstack11ll111111_opy_
        bstack1ll1llll11_opy_[bstack1l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩᴃ")] = bstack1ll11l1l1l_opy_
        if bstack1ll11llll11_opy_:
            bstack1ll1llll11_opy_[bstack1l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᴄ")] = bstack1ll11llll11_opy_
            bstack1ll1llll11_opy_[bstack1l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᴅ")] = bstack1lll1llll1l_opy_
            bstack1ll1llll11_opy_[bstack1l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᴆ")][bstack1l1l11_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᴇ")] = bstack11ll1ll1lll_opy_
        if getattr(options, bstack1l1l11_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭ᴈ"), None):
            options.set_capability(bstack1l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᴉ"), bstack1ll1llll11_opy_)
        else:
            options[bstack1l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᴊ")] = bstack1ll1llll11_opy_
    else:
        if getattr(options, bstack1l1l11_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩᴋ"), None):
            options.set_capability(bstack1l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᴌ"), bstack111llll11l1_opy_(framework))
            options.set_capability(bstack1l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᴍ"), bstack1l1ll1l11ll_opy_())
            options.set_capability(bstack1l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᴎ"), bstack11ll111111_opy_)
            options.set_capability(bstack1l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᴏ"), bstack1ll11l1l1l_opy_)
            if bstack1ll11llll11_opy_:
                options.set_capability(bstack1l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᴐ"), bstack1ll11llll11_opy_)
                options.set_capability(bstack1l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᴑ"), bstack1lll1llll1l_opy_)
                options.set_capability(bstack1l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹ࠮ࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᴒ"), bstack11ll1ll1lll_opy_)
        else:
            options[bstack1l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᴓ")] = bstack111llll11l1_opy_(framework)
            options[bstack1l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᴔ")] = bstack1l1ll1l11ll_opy_()
            options[bstack1l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᴕ")] = bstack11ll111111_opy_
            options[bstack1l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᴖ")] = bstack1ll11l1l1l_opy_
            if bstack1ll11llll11_opy_:
                options[bstack1l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᴗ")] = bstack1ll11llll11_opy_
                options[bstack1l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᴘ")] = bstack1lll1llll1l_opy_
                options[bstack1l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᴙ")][bstack1l1l11_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᴚ")] = bstack11ll1ll1lll_opy_
    return options
def bstack11l11lll1ll_opy_(bstack111llll1ll1_opy_, framework):
    bstack1ll11l1l1l_opy_ = bstack1lll11l111_opy_.get_property(bstack1l1l11_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧᴛ"))
    if bstack111llll1ll1_opy_ and len(bstack111llll1ll1_opy_.split(bstack1l1l11_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪᴜ"))) > 1:
        ws_url = bstack111llll1ll1_opy_.split(bstack1l1l11_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᴝ"))[0]
        if bstack1l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩᴞ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111ll11ll11_opy_ = json.loads(urllib.parse.unquote(bstack111llll1ll1_opy_.split(bstack1l1l11_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᴟ"))[1]))
            bstack111ll11ll11_opy_ = bstack111ll11ll11_opy_ or {}
            bstack11ll111111_opy_ = os.environ[bstack1l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᴠ")]
            bstack111ll11ll11_opy_[bstack1l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᴡ")] = str(framework) + str(__version__)
            bstack111ll11ll11_opy_[bstack1l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᴢ")] = bstack1l1ll1l11ll_opy_()
            bstack111ll11ll11_opy_[bstack1l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᴣ")] = bstack11ll111111_opy_
            bstack111ll11ll11_opy_[bstack1l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᴤ")] = bstack1ll11l1l1l_opy_
            bstack111llll1ll1_opy_ = bstack111llll1ll1_opy_.split(bstack1l1l11_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᴥ"))[0] + bstack1l1l11_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᴦ") + urllib.parse.quote(json.dumps(bstack111ll11ll11_opy_))
    return bstack111llll1ll1_opy_
def bstack11ll1ll111_opy_():
    global bstack11ll1111l1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack11ll1111l1_opy_ = BrowserType.connect
    return bstack11ll1111l1_opy_
def bstack11l1llll1_opy_(framework_name):
    global bstack1lll111l1l_opy_
    bstack1lll111l1l_opy_ = framework_name
    return framework_name
def bstack1lll11ll11_opy_(self, *args, **kwargs):
    global bstack11ll1111l1_opy_
    try:
        global bstack1lll111l1l_opy_
        if bstack1l1l11_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬᴧ") in kwargs:
            kwargs[bstack1l1l11_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ᴨ")] = bstack11l11lll1ll_opy_(
                kwargs.get(bstack1l1l11_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧᴩ"), None),
                bstack1lll111l1l_opy_
            )
    except Exception as e:
        logger.error(bstack1l1l11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦᴪ").format(str(e)))
    return bstack11ll1111l1_opy_(self, *args, **kwargs)
def bstack11l111llll1_opy_(bstack11l11l1111l_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1l1l11111_opy_(bstack11l11l1111l_opy_, bstack1l1l11_opy_ (u"ࠧࠨᴫ"))
        if proxies and proxies.get(bstack1l1l11_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧᴬ")):
            parsed_url = urlparse(proxies.get(bstack1l1l11_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨᴭ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1l1l11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫᴮ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1l1l11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬᴯ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1l1l11_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ᴰ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1l1l11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᴱ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack11l1l11111_opy_(bstack11l11l1111l_opy_):
    bstack111llllll1l_opy_ = {
        bstack11l1ll1111l_opy_[bstack11l11l1l1ll_opy_]: bstack11l11l1111l_opy_[bstack11l11l1l1ll_opy_]
        for bstack11l11l1l1ll_opy_ in bstack11l11l1111l_opy_
        if bstack11l11l1l1ll_opy_ in bstack11l1ll1111l_opy_
    }
    bstack111llllll1l_opy_[bstack1l1l11_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧᴲ")] = bstack11l111llll1_opy_(bstack11l11l1111l_opy_, bstack1lll11l111_opy_.get_property(bstack1l1l11_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨᴳ")))
    bstack111lllll1l1_opy_ = [element.lower() for element in bstack11l1lllll1l_opy_]
    bstack11l11111ll1_opy_(bstack111llllll1l_opy_, bstack111lllll1l1_opy_)
    return bstack111llllll1l_opy_
def bstack11l11111ll1_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1l1l11_opy_ (u"ࠢࠫࠬ࠭࠮ࠧᴴ")
    for value in d.values():
        if isinstance(value, dict):
            bstack11l11111ll1_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack11l11111ll1_opy_(item, keys)
def bstack1l1lll1l111_opy_():
    bstack111lll1ll11_opy_ = [os.environ.get(bstack1l1l11_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡋࡏࡉࡘࡥࡄࡊࡔࠥᴵ")), os.path.join(os.path.expanduser(bstack1l1l11_opy_ (u"ࠤࢁࠦᴶ")), bstack1l1l11_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᴷ")), os.path.join(bstack1l1l11_opy_ (u"ࠫ࠴ࡺ࡭ࡱࠩᴸ"), bstack1l1l11_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᴹ"))]
    for path in bstack111lll1ll11_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1l1l11_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࠬࠨᴺ") + str(path) + bstack1l1l11_opy_ (u"ࠢࠨࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠥᴻ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1l1l11_opy_ (u"ࠣࡉ࡬ࡺ࡮ࡴࡧࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸࠦࡦࡰࡴࠣࠫࠧᴼ") + str(path) + bstack1l1l11_opy_ (u"ࠤࠪࠦᴽ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1l1l11_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࠩࠥᴾ") + str(path) + bstack1l1l11_opy_ (u"ࠦࠬࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡩࡣࡶࠤࡹ࡮ࡥࠡࡴࡨࡵࡺ࡯ࡲࡦࡦࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳ࠯ࠤᴿ"))
            else:
                logger.debug(bstack1l1l11_opy_ (u"ࠧࡉࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥ࠭ࠢᵀ") + str(path) + bstack1l1l11_opy_ (u"ࠨࠧࠡࡹ࡬ࡸ࡭ࠦࡷࡳ࡫ࡷࡩࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯࠰ࠥᵁ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1l1l11_opy_ (u"ࠢࡐࡲࡨࡶࡦࡺࡩࡰࡰࠣࡷࡺࡩࡣࡦࡧࡧࡩࡩࠦࡦࡰࡴࠣࠫࠧᵂ") + str(path) + bstack1l1l11_opy_ (u"ࠣࠩ࠱ࠦᵃ"))
            return path
        except Exception as e:
            logger.debug(bstack1l1l11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡸࡴࠥ࡬ࡩ࡭ࡧࠣࠫࢀࡶࡡࡵࡪࢀࠫ࠿ࠦࠢᵄ") + str(e) + bstack1l1l11_opy_ (u"ࠥࠦᵅ"))
    logger.debug(bstack1l1l11_opy_ (u"ࠦࡆࡲ࡬ࠡࡲࡤࡸ࡭ࡹࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠣᵆ"))
    return None
@measure(event_name=EVENTS.bstack11l1lll111l_opy_, stage=STAGE.bstack1ll11lll_opy_)
def bstack1llll11ll1l_opy_(binary_path, bstack1lll1l11111_opy_, bs_config):
    logger.debug(bstack1l1l11_opy_ (u"ࠧࡉࡵࡳࡴࡨࡲࡹࠦࡃࡍࡋࠣࡔࡦࡺࡨࠡࡨࡲࡹࡳࡪ࠺ࠡࡽࢀࠦᵇ").format(binary_path))
    bstack111ll1l1ll1_opy_ = bstack1l1l11_opy_ (u"࠭ࠧᵈ")
    bstack111ll1l1111_opy_ = {
        bstack1l1l11_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᵉ"): __version__,
        bstack1l1l11_opy_ (u"ࠣࡱࡶࠦᵊ"): platform.system(),
        bstack1l1l11_opy_ (u"ࠤࡲࡷࡤࡧࡲࡤࡪࠥᵋ"): platform.machine(),
        bstack1l1l11_opy_ (u"ࠥࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣᵌ"): bstack1l1l11_opy_ (u"ࠫ࠵࠭ᵍ"),
        bstack1l1l11_opy_ (u"ࠧࡹࡤ࡬ࡡ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠦᵎ"): bstack1l1l11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ᵏ")
    }
    bstack111lllll11l_opy_(bstack111ll1l1111_opy_)
    try:
        if binary_path:
            bstack111ll1l1111_opy_[bstack1l1l11_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᵐ")] = subprocess.check_output([binary_path, bstack1l1l11_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤᵑ")]).strip().decode(bstack1l1l11_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᵒ"))
        response = requests.request(
            bstack1l1l11_opy_ (u"ࠪࡋࡊ࡚ࠧᵓ"),
            url=bstack11lllll1ll_opy_(bstack11l1ll1ll1l_opy_),
            headers=None,
            auth=(bs_config[bstack1l1l11_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᵔ")], bs_config[bstack1l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᵕ")]),
            json=None,
            params=bstack111ll1l1111_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1l1l11_opy_ (u"࠭ࡵࡳ࡮ࠪᵖ") in data.keys() and bstack1l1l11_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡤࡠࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᵗ") in data.keys():
            logger.debug(bstack1l1l11_opy_ (u"ࠣࡐࡨࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡥ࡭ࡳࡧࡲࡺ࠮ࠣࡧࡺࡸࡲࡦࡰࡷࠤࡧ࡯࡮ࡢࡴࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠤᵘ").format(bstack111ll1l1111_opy_[bstack1l1l11_opy_ (u"ࠩࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᵙ")]))
            if bstack1l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑ࠭ᵚ") in os.environ:
                logger.debug(bstack1l1l11_opy_ (u"ࠦࡘࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡣࡶࠤࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠠࡪࡵࠣࡷࡪࡺࠢᵛ"))
                data[bstack1l1l11_opy_ (u"ࠬࡻࡲ࡭ࠩᵜ")] = os.environ[bstack1l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤ࡛ࡒࡍࠩᵝ")]
            bstack111lll11ll1_opy_ = bstack111ll11ll1l_opy_(data[bstack1l1l11_opy_ (u"ࠧࡶࡴ࡯ࠫᵞ")], bstack1lll1l11111_opy_)
            bstack111ll1l1ll1_opy_ = os.path.join(bstack1lll1l11111_opy_, bstack111lll11ll1_opy_)
            os.chmod(bstack111ll1l1ll1_opy_, 0o777) # bstack111lll1llll_opy_ permission
            return bstack111ll1l1ll1_opy_
    except Exception as e:
        logger.debug(bstack1l1l11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡳ࡫ࡷࠡࡕࡇࡏࠥࢁࡽࠣᵟ").format(e))
    return binary_path
def bstack111lllll11l_opy_(bstack111ll1l1111_opy_):
    try:
        if bstack1l1l11_opy_ (u"ࠩ࡯࡭ࡳࡻࡸࠨᵠ") not in bstack111ll1l1111_opy_[bstack1l1l11_opy_ (u"ࠪࡳࡸ࠭ᵡ")].lower():
            return
        if os.path.exists(bstack1l1l11_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡲࡷ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨᵢ")):
            with open(bstack1l1l11_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡳࡸ࠳ࡲࡦ࡮ࡨࡥࡸ࡫ࠢᵣ"), bstack1l1l11_opy_ (u"ࠨࡲࠣᵤ")) as f:
                bstack11l11l111ll_opy_ = {}
                for line in f:
                    if bstack1l1l11_opy_ (u"ࠢ࠾ࠤᵥ") in line:
                        key, value = line.rstrip().split(bstack1l1l11_opy_ (u"ࠣ࠿ࠥᵦ"), 1)
                        bstack11l11l111ll_opy_[key] = value.strip(bstack1l1l11_opy_ (u"ࠩࠥࡠࠬ࠭ᵧ"))
                bstack111ll1l1111_opy_[bstack1l1l11_opy_ (u"ࠪࡨ࡮ࡹࡴࡳࡱࠪᵨ")] = bstack11l11l111ll_opy_.get(bstack1l1l11_opy_ (u"ࠦࡎࡊࠢᵩ"), bstack1l1l11_opy_ (u"ࠧࠨᵪ"))
        elif os.path.exists(bstack1l1l11_opy_ (u"ࠨ࠯ࡦࡶࡦ࠳ࡦࡲࡰࡪࡰࡨ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧᵫ")):
            bstack111ll1l1111_opy_[bstack1l1l11_opy_ (u"ࠧࡥ࡫ࡶࡸࡷࡵࠧᵬ")] = bstack1l1l11_opy_ (u"ࠨࡣ࡯ࡴ࡮ࡴࡥࠨᵭ")
    except Exception as e:
        logger.debug(bstack1l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡭ࡥࡵࠢࡧ࡭ࡸࡺࡲࡰࠢࡲࡪࠥࡲࡩ࡯ࡷࡻࠦᵮ") + e)
@measure(event_name=EVENTS.bstack11l1ll11ll1_opy_, stage=STAGE.bstack1ll11lll_opy_)
def bstack111ll11ll1l_opy_(bstack111ll1lll11_opy_, bstack11l11l11l11_opy_):
    logger.debug(bstack1l1l11_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬ࡲࡰ࡯࠽ࠤࠧᵯ") + str(bstack111ll1lll11_opy_) + bstack1l1l11_opy_ (u"ࠦࠧᵰ"))
    zip_path = os.path.join(bstack11l11l11l11_opy_, bstack1l1l11_opy_ (u"ࠧࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࡡࡩ࡭ࡱ࡫࠮ࡻ࡫ࡳࠦᵱ"))
    bstack111lll11ll1_opy_ = bstack1l1l11_opy_ (u"࠭ࠧᵲ")
    with requests.get(bstack111ll1lll11_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1l1l11_opy_ (u"ࠢࡸࡤࠥᵳ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1l1l11_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠥᵴ"))
    with zipfile.ZipFile(zip_path, bstack1l1l11_opy_ (u"ࠩࡵࠫᵵ")) as zip_ref:
        bstack11l11111111_opy_ = zip_ref.namelist()
        if len(bstack11l11111111_opy_) > 0:
            bstack111lll11ll1_opy_ = bstack11l11111111_opy_[0] # bstack11l111lll1l_opy_ bstack11l1l1ll11l_opy_ will be bstack11l111lllll_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack11l11l11l11_opy_)
        logger.debug(bstack1l1l11_opy_ (u"ࠥࡊ࡮ࡲࡥࡴࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡧࡻࡸࡷࡧࡣࡵࡧࡧࠤࡹࡵࠠࠨࠤᵶ") + str(bstack11l11l11l11_opy_) + bstack1l1l11_opy_ (u"ࠦࠬࠨᵷ"))
    os.remove(zip_path)
    return bstack111lll11ll1_opy_
def get_cli_dir():
    bstack111lll1lll1_opy_ = bstack1l1lll1l111_opy_()
    if bstack111lll1lll1_opy_:
        bstack1lll1l11111_opy_ = os.path.join(bstack111lll1lll1_opy_, bstack1l1l11_opy_ (u"ࠧࡩ࡬ࡪࠤᵸ"))
        if not os.path.exists(bstack1lll1l11111_opy_):
            os.makedirs(bstack1lll1l11111_opy_, mode=0o777, exist_ok=True)
        return bstack1lll1l11111_opy_
    else:
        raise FileNotFoundError(bstack1l1l11_opy_ (u"ࠨࡎࡰࠢࡺࡶ࡮ࡺࡡࡣ࡮ࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡪࡴࡸࠠࡵࡪࡨࠤࡘࡊࡋࠡࡤ࡬ࡲࡦࡸࡹ࠯ࠤᵹ"))
def bstack1lll1ll111l_opy_(bstack1lll1l11111_opy_):
    bstack1l1l11_opy_ (u"ࠢࠣࠤࡊࡩࡹࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡨࡲࡶࠥࡺࡨࡦࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡯࡮ࠡࡣࠣࡻࡷ࡯ࡴࡢࡤ࡯ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠯ࠤࠥࠦᵺ")
    bstack111lll1l1ll_opy_ = [
        os.path.join(bstack1lll1l11111_opy_, f)
        for f in os.listdir(bstack1lll1l11111_opy_)
        if os.path.isfile(os.path.join(bstack1lll1l11111_opy_, f)) and f.startswith(bstack1l1l11_opy_ (u"ࠣࡤ࡬ࡲࡦࡸࡹ࠮ࠤᵻ"))
    ]
    if len(bstack111lll1l1ll_opy_) > 0:
        return max(bstack111lll1l1ll_opy_, key=os.path.getmtime) # get bstack11l111ll111_opy_ binary
    return bstack1l1l11_opy_ (u"ࠤࠥᵼ")
def bstack11ll1lll1l1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1ll11l11l11_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1ll11l11l11_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1l1lll11ll_opy_(data, keys, default=None):
    bstack1l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡗࡦ࡬ࡥ࡭ࡻࠣ࡫ࡪࡺࠠࡢࠢࡱࡩࡸࡺࡥࡥࠢࡹࡥࡱࡻࡥࠡࡨࡵࡳࡲࠦࡡࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡵࡲࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡩࡧࡴࡢ࠼ࠣࡘ࡭࡫ࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡴࡸࠠ࡭࡫ࡶࡸࠥࡺ࡯ࠡࡶࡵࡥࡻ࡫ࡲࡴࡧ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡ࡭ࡨࡽࡸࡀࠠࡂࠢ࡯࡭ࡸࡺࠠࡰࡨࠣ࡯ࡪࡿࡳ࠰࡫ࡱࡨ࡮ࡩࡥࡴࠢࡵࡩࡵࡸࡥࡴࡧࡱࡸ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡦࡨࡪࡦࡻ࡬ࡵ࠼࡚ࠣࡦࡲࡵࡦࠢࡷࡳࠥࡸࡥࡵࡷࡵࡲࠥ࡯ࡦࠡࡶ࡫ࡩࠥࡶࡡࡵࡪࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠲ࠏࠦࠠࠡࠢ࠽ࡶࡪࡺࡵࡳࡰ࠽ࠤ࡙࡮ࡥࠡࡸࡤࡰࡺ࡫ࠠࡢࡶࠣࡸ࡭࡫ࠠ࡯ࡧࡶࡸࡪࡪࠠࡱࡣࡷ࡬࠱ࠦ࡯ࡳࠢࡧࡩ࡫ࡧࡵ࡭ࡶࠣ࡭࡫ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠰ࠍࠤࠥࠦࠠࠣࠤࠥᵽ")
    if not data:
        return default
    current = data
    try:
        for key in keys:
            if isinstance(current, dict):
                current = current[key]
            elif isinstance(current, list) and isinstance(key, int):
                current = current[key]
            else:
                return default
        return current
    except (KeyError, IndexError, TypeError):
        return default