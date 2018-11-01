# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/customer_client_link_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import customer_client_link_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__client__link__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/customer_client_link_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\nIgoogle/ads/googleads_v0/proto/services/customer_client_link_service.proto\x12 google.ads.googleads.v0.services\x1a\x42google/ads/googleads_v0/proto/resources/customer_client_link.proto\x1a\x1cgoogle/api/annotations.proto\"5\n\x1cGetCustomerClientLinkRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xeb\x01\n\x19\x43ustomerClientLinkService\x12\xcd\x01\n\x15GetCustomerClientLink\x12>.google.ads.googleads.v0.services.GetCustomerClientLinkRequest\x1a\x35.google.ads.googleads.v0.resources.CustomerClientLink\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/v0/{resource_name=customers/*/customerClientLinks/*}B\xde\x01\n$com.google.ads.googleads.v0.servicesB\x1e\x43ustomerClientLinkServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__client__link__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETCUSTOMERCLIENTLINKREQUEST = _descriptor.Descriptor(
  name='GetCustomerClientLinkRequest',
  full_name='google.ads.googleads.v0.services.GetCustomerClientLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetCustomerClientLinkRequest.resource_name', index=0,
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
  serialized_start=209,
  serialized_end=262,
)

DESCRIPTOR.message_types_by_name['GetCustomerClientLinkRequest'] = _GETCUSTOMERCLIENTLINKREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCustomerClientLinkRequest = _reflection.GeneratedProtocolMessageType('GetCustomerClientLinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCUSTOMERCLIENTLINKREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.customer_client_link_service_pb2'
  ,
  __doc__ = """Request message for
  [CustomerClientLinkService.GetCustomerClientLink][google.ads.googleads.v0.services.CustomerClientLinkService.GetCustomerClientLink].
  
  
  Attributes:
      resource_name:
          The resource name of the customer client link to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetCustomerClientLinkRequest)
  ))
_sym_db.RegisterMessage(GetCustomerClientLinkRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\036CustomerClientLinkServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_CUSTOMERCLIENTLINKSERVICE = _descriptor.ServiceDescriptor(
  name='CustomerClientLinkService',
  full_name='google.ads.googleads.v0.services.CustomerClientLinkService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=265,
  serialized_end=500,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCustomerClientLink',
    full_name='google.ads.googleads.v0.services.CustomerClientLinkService.GetCustomerClientLink',
    index=0,
    containing_service=None,
    input_type=_GETCUSTOMERCLIENTLINKREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__client__link__pb2._CUSTOMERCLIENTLINK,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0027\0225/v0/{resource_name=customers/*/customerClientLinks/*}')),
  ),
])
_sym_db.RegisterServiceDescriptor(_CUSTOMERCLIENTLINKSERVICE)

DESCRIPTOR.services_by_name['CustomerClientLinkService'] = _CUSTOMERCLIENTLINKSERVICE

# @@protoc_insertion_point(module_scope)