# Copyright (c) 2021 Julien Floret
# Copyright (c) 2021 Robin Jarry
# SPDX-License-Identifier: BSD-3-Clause

import json
import logging
from pathlib import Path
from typing import Callable, Dict, Iterator

from .tag import Tag
from .util import SubDir


LOG = logging.getLogger(__name__)


# --------------------------------------------------------------------------------------
class Branch(SubDir):
    """
    TODO
    """

    ROOT_DIR = "branches"

    @classmethod
    def parent_path(cls, parent: "ArtifactRepository") -> Path:
        return parent.path() / cls.ROOT_DIR

    def url_bit(self) -> str:
        return f"branches/{self.name}"

    def get_tags(self, access_cb: Callable[[str], bool] = None) -> Iterator[Tag]:
        for t in Tag.all(self):
            if access_cb is not None and not access_cb(t.url()):
                continue
            yield t

    def get_tag(
        self,
        name: str,
        access_cb: Callable[[str], bool] = None,
        filter_names: list[str] = None,
    ) -> Tag:
        if name in ("latest", "stable", "oldstable"):
            tags = list(self.get_tags(access_cb))
            if filter_names:
                tags = [tag for tag in tags if tag.name in filter_names]
            tags.sort(key=Tag.creation_date, reverse=True)
            first = True
            for t in tags:
                if name == "latest":
                    return t
                if t.is_stable():
                    if name == "stable" or not first:
                        return t
                    first = False
            raise FileNotFoundError(name)
        return Tag(self, name)

    def _policy_path(self) -> Path:
        return self._path / ".cleanup_policy"

    def set_cleanup_policy(self, max_daily_tags: int, max_released_tags: int):
        policy = {
            "max_daily_tags": max_daily_tags,
            "max_released_tags": max_released_tags,
        }
        self._policy_path().write_text(json.dumps(policy))

    def get_cleanup_policy(self) -> Dict[str, int]:
        try:
            policy = json.loads(self._policy_path().read_text())
        except (OSError, ValueError):
            policy = {}
        for field in "max_daily_tags", "max_released_tags":
            if field not in policy:
                policy[field] = 0
        return policy

    def delete(self):
        if not self.exists():
            raise FileNotFoundError()
        for t in self.get_tags():
            if t.is_locked():
                raise OSError(f"Tag {t.name} is locked")
            if t.is_released():
                raise OSError(f"Tag {t.name} is released, unrelease it first")
        for t in self.get_tags():
            t.delete()
        self.root().rmtree(self._path)
