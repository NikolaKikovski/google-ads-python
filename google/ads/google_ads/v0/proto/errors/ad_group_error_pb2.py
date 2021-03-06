# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/ad_group_error.proto

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
  name='google/ads/googleads_v0/proto/errors/ad_group_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\n9google/ads/googleads_v0/proto/errors/ad_group_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xa0\x04\n\x10\x41\x64GroupErrorEnum\"\x8b\x04\n\x0c\x41\x64GroupError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1a\n\x16\x44UPLICATE_ADGROUP_NAME\x10\x02\x12\x18\n\x14INVALID_ADGROUP_NAME\x10\x03\x12%\n!ADVERTISER_NOT_ON_CONTENT_NETWORK\x10\x05\x12\x0f\n\x0b\x42ID_TOO_BIG\x10\x06\x12*\n&BID_TYPE_AND_BIDDING_STRATEGY_MISMATCH\x10\x07\x12\x18\n\x14MISSING_ADGROUP_NAME\x10\x08\x12 \n\x1c\x41\x44GROUP_LABEL_DOES_NOT_EXIST\x10\t\x12 \n\x1c\x41\x44GROUP_LABEL_ALREADY_EXISTS\x10\n\x12,\n(INVALID_CONTENT_BID_CRITERION_TYPE_GROUP\x10\x0b\x12\x38\n4AD_GROUP_TYPE_NOT_VALID_FOR_ADVERTISING_CHANNEL_TYPE\x10\x0c\x12\x39\n5ADGROUP_TYPE_NOT_SUPPORTED_FOR_CAMPAIGN_SALES_COUNTRY\x10\r\x12\x42\n>CANNOT_ADD_ADGROUP_OF_TYPE_DSA_TO_CAMPAIGN_WITHOUT_DSA_SETTING\x10\x0e\x42\xc7\x01\n\"com.google.ads.googleads.v0.errorsB\x11\x41\x64GroupErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_ADGROUPERRORENUM_ADGROUPERROR = _descriptor.EnumDescriptor(
  name='AdGroupError',
  full_name='google.ads.googleads.v0.errors.AdGroupErrorEnum.AdGroupError',
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
      name='DUPLICATE_ADGROUP_NAME', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ADGROUP_NAME', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADVERTISER_NOT_ON_CONTENT_NETWORK', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BID_TOO_BIG', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BID_TYPE_AND_BIDDING_STRATEGY_MISMATCH', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_ADGROUP_NAME', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADGROUP_LABEL_DOES_NOT_EXIST', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADGROUP_LABEL_ALREADY_EXISTS', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CONTENT_BID_CRITERION_TYPE_GROUP', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP_TYPE_NOT_VALID_FOR_ADVERTISING_CHANNEL_TYPE', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADGROUP_TYPE_NOT_SUPPORTED_FOR_CAMPAIGN_SALES_COUNTRY', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ADD_ADGROUP_OF_TYPE_DSA_TO_CAMPAIGN_WITHOUT_DSA_SETTING', index=13, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=115,
  serialized_end=638,
)
_sym_db.RegisterEnumDescriptor(_ADGROUPERRORENUM_ADGROUPERROR)


_ADGROUPERRORENUM = _descriptor.Descriptor(
  name='AdGroupErrorEnum',
  full_name='google.ads.googleads.v0.errors.AdGroupErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADGROUPERRORENUM_ADGROUPERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=638,
)

_ADGROUPERRORENUM_ADGROUPERROR.containing_type = _ADGROUPERRORENUM
DESCRIPTOR.message_types_by_name['AdGroupErrorEnum'] = _ADGROUPERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupErrorEnum = _reflection.GeneratedProtocolMessageType('AdGroupErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.ad_group_error_pb2'
  ,
  __doc__ = """Container for enum describing possible ad group errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.AdGroupErrorEnum)
  ))
_sym_db.RegisterMessage(AdGroupErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\021AdGroupErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)
