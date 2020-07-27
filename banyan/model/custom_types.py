# from cement.utils.misc import is_true
# from dataclasses import dataclass
# from dataclasses_serialization.json import JSONSerializer, JSONStrSerializer
# from uuid import UUID
# from ipaddress import IPv4Address, IPv4Interface
# from semver import VersionInfo
# import datetime
# import iso8601
# from dateutil.parser import parse
# from typing import List, Dict, Union, Any
#
# JSONType = Union[List[Any], Dict[str, Any]]
#
#
# class IntString(int):
#     @classmethod
#     def from_str(cls, t: str):
#         return int(t) if t else None
#
#     def __str__(self) -> str:
#         return super().__str__()
#
#
# class WrappedDate(datetime.datetime):
#     pass
#
#
# class Iso8601Date(WrappedDate):
#     @classmethod
#     def from_str(cls, t: str):
#         return parse(t) if t else None
#
#     def __str__(self) -> str:
#         return self.isoformat()
#
#
# class NanoTimestamp(WrappedDate):
#     @classmethod
#     def from_int(cls, t):
#         return datetime.datetime.fromtimestamp(
#             int(t) / NANO) if t > 0 else None
#
#
# class BoolString(str):
#     def __bool__(self):
#         return is_true(self)
#
#     def __str__(self) -> str:
#         return str(is_true(self))
#
#
# # So many annoying date formats
#
# NANO = 1000 * 1000 * 1000
#
# JSONSerializer.register(Iso8601Date,
#                         lambda t: str(t) if t else '',
#                         lambda cls, t: Iso8601Date.from_str(t)
#                         )
#
# JSONSerializer.register(NanoTimestamp,
#                         lambda t: int(t.timestamp()) * NANO if t else 0,
#                         lambda cls, t: NanoTimestamp.from_int(t)
#                         )
#
# JSONSerializer.register(datetime.datetime,
#                         lambda t: t.isoformat() if t else '',
#                         lambda cls, t: parse(t))
#
# # JSONSerializer.register(bool,
# #                         lambda t: t,
# #                         lambda cls, t: t
# #                         )
#
# JSONSerializer.register(BoolString,
#                         lambda t: str(t),
#                         lambda cls, t: BoolString(t)
#                         )
#
# JSONSerializer.register(IntString,
#                         lambda t: t.__str__(),
#                         lambda cls, t: IntString.from_str(t)
#                         )
#
# JSONSerializer.register(UUID,
#                         lambda t: str(t) if t else '',
#                         lambda cls, t: UUID(t) if t else None
#                         )
#
# JSONSerializer.register(IPv4Address,
#                         lambda t: str(t) if t else '',
#                         lambda cls, t: IPv4Address(t) if t else None
#                         )
#
# JSONSerializer.register(IPv4Interface,
#                         lambda t: str(t) if t else '',
#                         lambda cls, t: IPv4Interface(t) if t else None
#                         )
#
# JSONSerializer.register(VersionInfo,
#                         lambda t: str(t).replace('+', '_'),
#                         lambda cls, t: VersionInfo.parse(t.replace('_', '+'))
#                         )
