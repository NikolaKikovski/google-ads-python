# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/account_budget_proposal_status.proto

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
  name='google/ads/googleads_v0/proto/enums/account_budget_proposal_status.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\nHgoogle/ads/googleads_v0/proto/enums/account_budget_proposal_status.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\xaa\x01\n\x1f\x41\x63\x63ountBudgetProposalStatusEnum\"\x86\x01\n\x1b\x41\x63\x63ountBudgetProposalStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x11\n\rAPPROVED_HELD\x10\x03\x12\x0c\n\x08\x41PPROVED\x10\x04\x12\r\n\tCANCELLED\x10\x05\x12\x0c\n\x08REJECTED\x10\x06\x42\xd1\x01\n!com.google.ads.googleads.v0.enumsB AccountBudgetProposalStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_ACCOUNTBUDGETPROPOSALSTATUSENUM_ACCOUNTBUDGETPROPOSALSTATUS = _descriptor.EnumDescriptor(
  name='AccountBudgetProposalStatus',
  full_name='google.ads.googleads.v0.enums.AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus',
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
      name='PENDING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPROVED_HELD', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPROVED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECTED', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=144,
  serialized_end=278,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTBUDGETPROPOSALSTATUSENUM_ACCOUNTBUDGETPROPOSALSTATUS)


_ACCOUNTBUDGETPROPOSALSTATUSENUM = _descriptor.Descriptor(
  name='AccountBudgetProposalStatusEnum',
  full_name='google.ads.googleads.v0.enums.AccountBudgetProposalStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACCOUNTBUDGETPROPOSALSTATUSENUM_ACCOUNTBUDGETPROPOSALSTATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=278,
)

_ACCOUNTBUDGETPROPOSALSTATUSENUM_ACCOUNTBUDGETPROPOSALSTATUS.containing_type = _ACCOUNTBUDGETPROPOSALSTATUSENUM
DESCRIPTOR.message_types_by_name['AccountBudgetProposalStatusEnum'] = _ACCOUNTBUDGETPROPOSALSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountBudgetProposalStatusEnum = _reflection.GeneratedProtocolMessageType('AccountBudgetProposalStatusEnum', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTBUDGETPROPOSALSTATUSENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.account_budget_proposal_status_pb2'
  ,
  __doc__ = """Message describing AccountBudgetProposal statuses.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.AccountBudgetProposalStatusEnum)
  ))
_sym_db.RegisterMessage(AccountBudgetProposalStatusEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB AccountBudgetProposalStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
