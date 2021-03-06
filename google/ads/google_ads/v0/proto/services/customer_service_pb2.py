# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/customer_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import customer_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/customer_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\n=google/ads/googleads_v0/proto/services/customer_service.proto\x12 google.ads.googleads.v0.services\x1a\x36google/ads/googleads_v0/proto/resources/customer.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"+\n\x12GetCustomerRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\" \n\x1eListAccessibleCustomersRequest\"9\n\x1fListAccessibleCustomersResponse\x12\x16\n\x0eresource_names\x18\x01 \x03(\t2\xfd\x02\n\x0f\x43ustomerService\x12\x99\x01\n\x0bGetCustomer\x12\x34.google.ads.googleads.v0.services.GetCustomerRequest\x1a+.google.ads.googleads.v0.resources.Customer\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v0/{resource_name=customers/*}\x12\xcd\x01\n\x17ListAccessibleCustomers\x12@.google.ads.googleads.v0.services.ListAccessibleCustomersRequest\x1a\x41.google.ads.googleads.v0.services.ListAccessibleCustomersResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v0/customers:listAccessibleCustomersB\xd4\x01\n$com.google.ads.googleads.v0.servicesB\x14\x43ustomerServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_GETCUSTOMERREQUEST = _descriptor.Descriptor(
  name='GetCustomerRequest',
  full_name='google.ads.googleads.v0.services.GetCustomerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetCustomerRequest.resource_name', index=0,
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
  serialized_start=217,
  serialized_end=260,
)


_LISTACCESSIBLECUSTOMERSREQUEST = _descriptor.Descriptor(
  name='ListAccessibleCustomersRequest',
  full_name='google.ads.googleads.v0.services.ListAccessibleCustomersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=262,
  serialized_end=294,
)


_LISTACCESSIBLECUSTOMERSRESPONSE = _descriptor.Descriptor(
  name='ListAccessibleCustomersResponse',
  full_name='google.ads.googleads.v0.services.ListAccessibleCustomersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_names', full_name='google.ads.googleads.v0.services.ListAccessibleCustomersResponse.resource_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=296,
  serialized_end=353,
)

DESCRIPTOR.message_types_by_name['GetCustomerRequest'] = _GETCUSTOMERREQUEST
DESCRIPTOR.message_types_by_name['ListAccessibleCustomersRequest'] = _LISTACCESSIBLECUSTOMERSREQUEST
DESCRIPTOR.message_types_by_name['ListAccessibleCustomersResponse'] = _LISTACCESSIBLECUSTOMERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCustomerRequest = _reflection.GeneratedProtocolMessageType('GetCustomerRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCUSTOMERREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """Request message for
  [CustomerService.GetCustomer][google.ads.googleads.v0.services.CustomerService.GetCustomer].
  
  
  Attributes:
      resource_name:
          The resource name of the customer to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetCustomerRequest)
  ))
_sym_db.RegisterMessage(GetCustomerRequest)

ListAccessibleCustomersRequest = _reflection.GeneratedProtocolMessageType('ListAccessibleCustomersRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTACCESSIBLECUSTOMERSREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """Request message for
  [CustomerService.ListAccessibleCustomers][google.ads.googleads.v0.services.CustomerService.ListAccessibleCustomers].
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ListAccessibleCustomersRequest)
  ))
_sym_db.RegisterMessage(ListAccessibleCustomersRequest)

ListAccessibleCustomersResponse = _reflection.GeneratedProtocolMessageType('ListAccessibleCustomersResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTACCESSIBLECUSTOMERSRESPONSE,
  __module__ = 'google.ads.googleads_v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """Response message for
  [CustomerService.ListAccessibleCustomers][google.ads.googleads.v0.services.CustomerService.ListAccessibleCustomers].
  
  
  Attributes:
      resource_names:
          Resource name of customers directly accessible by the user
          authenticating the call.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ListAccessibleCustomersResponse)
  ))
_sym_db.RegisterMessage(ListAccessibleCustomersResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\024CustomerServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_CUSTOMERSERVICE = _descriptor.ServiceDescriptor(
  name='CustomerService',
  full_name='google.ads.googleads.v0.services.CustomerService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=356,
  serialized_end=737,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCustomer',
    full_name='google.ads.googleads.v0.services.CustomerService.GetCustomer',
    index=0,
    containing_service=None,
    input_type=_GETCUSTOMERREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__pb2._CUSTOMER,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002!\022\037/v0/{resource_name=customers/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='ListAccessibleCustomers',
    full_name='google.ads.googleads.v0.services.CustomerService.ListAccessibleCustomers',
    index=1,
    containing_service=None,
    input_type=_LISTACCESSIBLECUSTOMERSREQUEST,
    output_type=_LISTACCESSIBLECUSTOMERSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\'\022%/v0/customers:listAccessibleCustomers')),
  ),
])
_sym_db.RegisterServiceDescriptor(_CUSTOMERSERVICE)

DESCRIPTOR.services_by_name['CustomerService'] = _CUSTOMERSERVICE

# @@protoc_insertion_point(module_scope)
