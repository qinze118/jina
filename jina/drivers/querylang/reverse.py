from typing import Iterable

from .. import BaseRecursiveDriver

if False:
    from ...proto import jina_pb2


class ReverseQL(BaseRecursiveDriver):
    def apply_all(self, docs: Iterable['jina_pb2.Document'], *args, **kwargs):
        docs.reverse()


class ReverseMatchesQL(BaseRecursiveDriver):
    def apply_all(self, docs: Iterable['jina_pb2.Document'], *args, **kwargs):
        docs.matches.reverse()
