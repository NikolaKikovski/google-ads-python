# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/conversion_action_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import conversion_action_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_conversion__action__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/conversion_action_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\nFgoogle/ads/googleads_v0/proto/services/conversion_action_service.proto\x12 google.ads.googleads.v0.services\x1a?google/ads/googleads_v0/proto/resources/conversion_action.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"3\n\x1aGetConversionActionRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\x86\x01\n\x1eMutateConversionActionsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12O\n\noperations\x18\x02 \x03(\x0b\x32;.google.ads.googleads.v0.services.ConversionActionOperation\"\xf9\x01\n\x19\x43onversionActionOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x45\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x33.google.ads.googleads.v0.resources.ConversionActionH\x00\x12\x45\n\x06update\x18\x02 \x01(\x0b\x32\x33.google.ads.googleads.v0.resources.ConversionActionH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"r\n\x1fMutateConversionActionsResponse\x12O\n\x07results\x18\x02 \x03(\x0b\x32>.google.ads.googleads.v0.services.MutateConversionActionResult\"5\n\x1cMutateConversionActionResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xc5\x03\n\x17\x43onversionActionService\x12\xc5\x01\n\x13GetConversionAction\x12<.google.ads.googleads.v0.services.GetConversionActionRequest\x1a\x33.google.ads.googleads.v0.resources.ConversionAction\";\x82\xd3\xe4\x93\x02\x35\x12\x33/v0/{resource_name=customers/*/conversionActions/*}\x12\xe1\x01\n\x17MutateConversionActions\x12@.google.ads.googleads.v0.services.MutateConversionActionsRequest\x1a\x41.google.ads.googleads.v0.services.MutateConversionActionsResponse\"A\x82\xd3\xe4\x93\x02;\"6/v0/customers/{customer_id=*}/conversionActions:mutate:\x01*B\xdc\x01\n$com.google.ads.googleads.v0.servicesB\x1c\x43onversionActionServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_conversion__action__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_GETCONVERSIONACTIONREQUEST = _descriptor.Descriptor(
  name='GetConversionActionRequest',
  full_name='google.ads.googleads.v0.services.GetConversionActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetConversionActionRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=288,
)


_MUTATECONVERSIONACTIONSREQUEST = _descriptor.Descriptor(
  name='MutateConversionActionsRequest',
  full_name='google.ads.googleads.v0.services.MutateConversionActionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.MutateConversionActionsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v0.services.MutateConversionActionsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=425,
)


_CONVERSIONACTIONOPERATION = _descriptor.Descriptor(
  name='ConversionActionOperation',
  full_name='google.ads.googleads.v0.services.ConversionActionOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v0.services.ConversionActionOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v0.services.ConversionActionOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v0.services.ConversionActionOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v0.services.ConversionActionOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v0.services.ConversionActionOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=428,
  serialized_end=677,
)


_MUTATECONVERSIONACTIONSRESPONSE = _descriptor.Descriptor(
  name='MutateConversionActionsResponse',
  full_name='google.ads.googleads.v0.services.MutateConversionActionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v0.services.MutateConversionActionsResponse.results', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=679,
  serialized_end=793,
)


_MUTATECONVERSIONACTIONRESULT = _descriptor.Descriptor(
  name='MutateConversionActionResult',
  full_name='google.ads.googleads.v0.services.MutateConversionActionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.MutateConversionActionResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=795,
  serialized_end=848,
)

_MUTATECONVERSIONACTIONSREQUEST.fields_by_name['operations'].message_type = _CONVERSIONACTIONOPERATION
_CONVERSIONACTIONOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CONVERSIONACTIONOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_conversion__action__pb2._CONVERSIONACTION
_CONVERSIONACTIONOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_conversion__action__pb2._CONVERSIONACTION
_CONVERSIONACTIONOPERATION.oneofs_by_name['operation'].fields.append(
  _CONVERSIONACTIONOPERATION.fields_by_name['create'])
_CONVERSIONACTIONOPERATION.fields_by_name['create'].containing_oneof = _CONVERSIONACTIONOPERATION.oneofs_by_name['operation']
_CONVERSIONACTIONOPERATION.oneofs_by_name['operation'].fields.append(
  _CONVERSIONACTIONOPERATION.fields_by_name['update'])
_CONVERSIONACTIONOPERATION.fields_by_name['update'].containing_oneof = _CONVERSIONACTIONOPERATION.oneofs_by_name['operation']
_CONVERSIONACTIONOPERATION.oneofs_by_name['operation'].fields.append(
  _CONVERSIONACTIONOPERATION.fields_by_name['remove'])
_CONVERSIONACTIONOPERATION.fields_by_name['remove'].containing_oneof = _CONVERSIONACTIONOPERATION.oneofs_by_name['operation']
_MUTATECONVERSIONACTIONSRESPONSE.fields_by_name['results'].message_type = _MUTATECONVERSIONACTIONRESULT
DESCRIPTOR.message_types_by_name['GetConversionActionRequest'] = _GETCONVERSIONACTIONREQUEST
DESCRIPTOR.message_types_by_name['MutateConversionActionsRequest'] = _MUTATECONVERSIONACTIONSREQUEST
DESCRIPTOR.message_types_by_name['ConversionActionOperation'] = _CONVERSIONACTIONOPERATION
DESCRIPTOR.message_types_by_name['MutateConversionActionsResponse'] = _MUTATECONVERSIONACTIONSRESPONSE
DESCRIPTOR.message_types_by_name['MutateConversionActionResult'] = _MUTATECONVERSIONACTIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetConversionActionRequest = _reflection.GeneratedProtocolMessageType('GetConversionActionRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCONVERSIONACTIONREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.conversion_action_service_pb2'
  ,
  __doc__ = """Request message for [ConversionActionService.GetConversionAction].
  
  
  Attributes:
      resource_name:
          The resource name of the conversion action to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetConversionActionRequest)
  ))
_sym_db.RegisterMessage(GetConversionActionRequest)

MutateConversionActionsRequest = _reflection.GeneratedProtocolMessageType('MutateConversionActionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECONVERSIONACTIONSREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.conversion_action_service_pb2'
  ,
  __doc__ = """Request message for [ConversionActionService.MutateConversionActions].
  
  
  Attributes:
      customer_id:
          The ID of the customer whose conversion actions are being
          modified.
      operations:
          The list of operations to perform on individual conversion
          actions.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateConversionActionsRequest)
  ))
_sym_db.RegisterMessage(MutateConversionActionsRequest)

ConversionActionOperation = _reflection.GeneratedProtocolMessageType('ConversionActionOperation', (_message.Message,), dict(
  DESCRIPTOR = _CONVERSIONACTIONOPERATION,
  __module__ = 'google.ads.googleads_v0.proto.services.conversion_action_service_pb2'
  ,
  __doc__ = """A single operation (create, update, remove) on a conversion action.
  
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          conversion action.
      update:
          Update operation: The conversion action is expected to have a
          valid resource name.
      remove:
          Remove operation: A resource name for the removed conversion
          action is expected, in this format:  ``customers/{customer_id}
          /conversionActions/{conversion_action_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ConversionActionOperation)
  ))
_sym_db.RegisterMessage(ConversionActionOperation)

MutateConversionActionsResponse = _reflection.GeneratedProtocolMessageType('MutateConversionActionsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECONVERSIONACTIONSRESPONSE,
  __module__ = 'google.ads.googleads_v0.proto.services.conversion_action_service_pb2'
  ,
  __doc__ = """Response message for conversion action mutate.
  
  
  Attributes:
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateConversionActionsResponse)
  ))
_sym_db.RegisterMessage(MutateConversionActionsResponse)

MutateConversionActionResult = _reflection.GeneratedProtocolMessageType('MutateConversionActionResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECONVERSIONACTIONRESULT,
  __module__ = 'google.ads.googleads_v0.proto.services.conversion_action_service_pb2'
  ,
  __doc__ = """The result for the conversion action mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateConversionActionResult)
  ))
_sym_db.RegisterMessage(MutateConversionActionResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\034ConversionActionServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_CONVERSIONACTIONSERVICE = _descriptor.ServiceDescriptor(
  name='ConversionActionService',
  full_name='google.ads.googleads.v0.services.ConversionActionService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=851,
  serialized_end=1304,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetConversionAction',
    full_name='google.ads.googleads.v0.services.ConversionActionService.GetConversionAction',
    index=0,
    containing_service=None,
    input_type=_GETCONVERSIONACTIONREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_conversion__action__pb2._CONVERSIONACTION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0025\0223/v0/{resource_name=customers/*/conversionActions/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='MutateConversionActions',
    full_name='google.ads.googleads.v0.services.ConversionActionService.MutateConversionActions',
    index=1,
    containing_service=None,
    input_type=_MUTATECONVERSIONACTIONSREQUEST,
    output_type=_MUTATECONVERSIONACTIONSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002;\"6/v0/customers/{customer_id=*}/conversionActions:mutate:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_CONVERSIONACTIONSERVICE)

DESCRIPTOR.services_by_name['ConversionActionService'] = _CONVERSIONACTIONSERVICE

# @@protoc_insertion_point(module_scope)
