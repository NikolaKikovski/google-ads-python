# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/bidding_strategy_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/enums/bidding_strategy_type.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n?google/ads/googleads_v0/proto/enums/bidding_strategy_type.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\xbf\x02\n\x17\x42iddingStrategyTypeEnum\"\xa3\x02\n\x13\x42iddingStrategyType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x10\n\x0c\x45NHANCED_CPC\x10\x02\x12\x0e\n\nMANUAL_CPC\x10\x03\x12\x0e\n\nMANUAL_CPM\x10\x04\x12\x0e\n\nMANUAL_CPV\x10\r\x12\x18\n\x14MAXIMIZE_CONVERSIONS\x10\n\x12\x1d\n\x19MAXIMIZE_CONVERSION_VALUE\x10\x0b\x12\x15\n\x11PAGE_ONE_PROMOTED\x10\x05\x12\x0f\n\x0bPERCENT_CPC\x10\x0c\x12\x0e\n\nTARGET_CPA\x10\x06\x12\x18\n\x14TARGET_OUTRANK_SHARE\x10\x07\x12\x0f\n\x0bTARGET_ROAS\x10\x08\x12\x10\n\x0cTARGET_SPEND\x10\tB\xc9\x01\n!com.google.ads.googleads.v0.enumsB\x18\x42iddingStrategyTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_BIDDINGSTRATEGYTYPEENUM_BIDDINGSTRATEGYTYPE = _descriptor.EnumDescriptor(
  name='BiddingStrategyType',
  full_name='google.ads.googleads.v0.enums.BiddingStrategyTypeEnum.BiddingStrategyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENHANCED_CPC', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MANUAL_CPC', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MANUAL_CPM', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MANUAL_CPV', index=5, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMIZE_CONVERSIONS', index=6, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMIZE_CONVERSION_VALUE', index=7, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAGE_ONE_PROMOTED', index=8, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERCENT_CPC', index=9, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_CPA', index=10, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_OUTRANK_SHARE', index=11, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_ROAS', index=12, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_SPEND', index=13, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=127,
  serialized_end=418,
)
_sym_db.RegisterEnumDescriptor(_BIDDINGSTRATEGYTYPEENUM_BIDDINGSTRATEGYTYPE)


_BIDDINGSTRATEGYTYPEENUM = _descriptor.Descriptor(
  name='BiddingStrategyTypeEnum',
  full_name='google.ads.googleads.v0.enums.BiddingStrategyTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BIDDINGSTRATEGYTYPEENUM_BIDDINGSTRATEGYTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=418,
)

_BIDDINGSTRATEGYTYPEENUM_BIDDINGSTRATEGYTYPE.containing_type = _BIDDINGSTRATEGYTYPEENUM
DESCRIPTOR.message_types_by_name['BiddingStrategyTypeEnum'] = _BIDDINGSTRATEGYTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BiddingStrategyTypeEnum = _reflection.GeneratedProtocolMessageType('BiddingStrategyTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _BIDDINGSTRATEGYTYPEENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.bidding_strategy_type_pb2'
  ,
  __doc__ = """Container for enum describing possible bidding strategy types.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.BiddingStrategyTypeEnum)
  ))
_sym_db.RegisterMessage(BiddingStrategyTypeEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\030BiddingStrategyTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
