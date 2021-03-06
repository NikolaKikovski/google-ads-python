# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/adx_error.proto

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
  name='google/ads/googleads_v0/proto/errors/adx_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\n4google/ads/googleads_v0/proto/errors/adx_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"Q\n\x0c\x41\x64xErrorEnum\"A\n\x08\x41\x64xError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x17\n\x13UNSUPPORTED_FEATURE\x10\x02\x42\xc3\x01\n\"com.google.ads.googleads.v0.errorsB\rAdxErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_ADXERRORENUM_ADXERROR = _descriptor.EnumDescriptor(
  name='AdxError',
  full_name='google.ads.googleads.v0.errors.AdxErrorEnum.AdxError',
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
      name='UNSUPPORTED_FEATURE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=104,
  serialized_end=169,
)
_sym_db.RegisterEnumDescriptor(_ADXERRORENUM_ADXERROR)


_ADXERRORENUM = _descriptor.Descriptor(
  name='AdxErrorEnum',
  full_name='google.ads.googleads.v0.errors.AdxErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADXERRORENUM_ADXERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=169,
)

_ADXERRORENUM_ADXERROR.containing_type = _ADXERRORENUM
DESCRIPTOR.message_types_by_name['AdxErrorEnum'] = _ADXERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdxErrorEnum = _reflection.GeneratedProtocolMessageType('AdxErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _ADXERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.adx_error_pb2'
  ,
  __doc__ = """Container for enum describing possible adx errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.AdxErrorEnum)
  ))
_sym_db.RegisterMessage(AdxErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\rAdxErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)
