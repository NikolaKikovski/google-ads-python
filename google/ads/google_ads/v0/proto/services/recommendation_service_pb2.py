# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/recommendation_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.enums import keyword_match_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_keyword__match__type__pb2
from google.ads.google_ads.v0.proto.resources import ad_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__pb2
from google.ads.google_ads.v0.proto.resources import recommendation_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_recommendation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/recommendation_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\nCgoogle/ads/googleads_v0/proto/services/recommendation_service.proto\x12 google.ads.googleads.v0.services\x1a<google/ads/googleads_v0/proto/enums/keyword_match_type.proto\x1a\x30google/ads/googleads_v0/proto/resources/ad.proto\x1a<google/ads/googleads_v0/proto/resources/recommendation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\"1\n\x18GetRecommendationRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\x85\x01\n\x1a\x41pplyRecommendationRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12R\n\noperations\x18\x02 \x03(\x0b\x32>.google.ads.googleads.v0.services.ApplyRecommendationOperation\"\x90\x08\n\x1c\x41pplyRecommendationOperation\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12r\n\x0f\x63\x61mpaign_budget\x18\x02 \x01(\x0b\x32W.google.ads.googleads.v0.services.ApplyRecommendationOperation.CampaignBudgetParametersH\x00\x12\x62\n\x07text_ad\x18\x03 \x01(\x0b\x32O.google.ads.googleads.v0.services.ApplyRecommendationOperation.TextAdParametersH\x00\x12\x63\n\x07keyword\x18\x04 \x01(\x0b\x32P.google.ads.googleads.v0.services.ApplyRecommendationOperation.KeywordParametersH\x00\x12t\n\x11target_cpa_opt_in\x18\x05 \x01(\x0b\x32W.google.ads.googleads.v0.services.ApplyRecommendationOperation.TargetCpaOptInParametersH\x00\x1aY\n\x18\x43\x61mpaignBudgetParameters\x12=\n\x18new_budget_amount_micros\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x1a\x45\n\x10TextAdParameters\x12\x31\n\x02\x61\x64\x18\x01 \x01(\x0b\x32%.google.ads.googleads.v0.resources.Ad\x1a\xd2\x01\n\x11KeywordParameters\x12.\n\x08\x61\x64_group\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12X\n\nmatch_type\x18\x02 \x01(\x0e\x32\x44.google.ads.googleads.v0.enums.KeywordMatchTypeEnum.KeywordMatchType\x12\x33\n\x0e\x63pc_bid_micros\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x1a\x9a\x01\n\x18TargetCpaOptInParameters\x12\x36\n\x11target_cpa_micros\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x46\n!new_campaign_budget_amount_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x12\n\x10\x61pply_parameters\"k\n\x1b\x41pplyRecommendationResponse\x12L\n\x07results\x18\x01 \x03(\x0b\x32;.google.ads.googleads.v0.services.ApplyRecommendationResult\"d\n\x19\x41pplyRecommendationResult\x12\x17\n\rresource_name\x18\x01 \x01(\tH\x00\x12$\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x42\x08\n\x06result2\xac\x03\n\x15RecommendationService\x12\xbd\x01\n\x11GetRecommendation\x12:.google.ads.googleads.v0.services.GetRecommendationRequest\x1a\x31.google.ads.googleads.v0.resources.Recommendation\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v0/{resource_name=customers/*/recommendations/*}\x12\xd2\x01\n\x13\x41pplyRecommendation\x12<.google.ads.googleads.v0.services.ApplyRecommendationRequest\x1a=.google.ads.googleads.v0.services.ApplyRecommendationResponse\">\x82\xd3\xe4\x93\x02\x38\"3/v0/customers/{customer_id=*}/recommendations:apply:\x01*B\xda\x01\n$com.google.ads.googleads.v0.servicesB\x1aRecommendationServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_keyword__match__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_recommendation__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETRECOMMENDATIONREQUEST = _descriptor.Descriptor(
  name='GetRecommendationRequest',
  full_name='google.ads.googleads.v0.services.GetRecommendationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetRecommendationRequest.resource_name', index=0,
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
  serialized_start=366,
  serialized_end=415,
)


_APPLYRECOMMENDATIONREQUEST = _descriptor.Descriptor(
  name='ApplyRecommendationRequest',
  full_name='google.ads.googleads.v0.services.ApplyRecommendationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.ApplyRecommendationRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v0.services.ApplyRecommendationRequest.operations', index=1,
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
  serialized_start=418,
  serialized_end=551,
)


_APPLYRECOMMENDATIONOPERATION_CAMPAIGNBUDGETPARAMETERS = _descriptor.Descriptor(
  name='CampaignBudgetParameters',
  full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.CampaignBudgetParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_budget_amount_micros', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.CampaignBudgetParameters.new_budget_amount_micros', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1044,
  serialized_end=1133,
)

_APPLYRECOMMENDATIONOPERATION_TEXTADPARAMETERS = _descriptor.Descriptor(
  name='TextAdParameters',
  full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.TextAdParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ad', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.TextAdParameters.ad', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1135,
  serialized_end=1204,
)

_APPLYRECOMMENDATIONOPERATION_KEYWORDPARAMETERS = _descriptor.Descriptor(
  name='KeywordParameters',
  full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.KeywordParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.KeywordParameters.ad_group', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='match_type', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.KeywordParameters.match_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_micros', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.KeywordParameters.cpc_bid_micros', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1207,
  serialized_end=1417,
)

_APPLYRECOMMENDATIONOPERATION_TARGETCPAOPTINPARAMETERS = _descriptor.Descriptor(
  name='TargetCpaOptInParameters',
  full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.TargetCpaOptInParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_cpa_micros', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.TargetCpaOptInParameters.target_cpa_micros', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_campaign_budget_amount_micros', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.TargetCpaOptInParameters.new_campaign_budget_amount_micros', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1420,
  serialized_end=1574,
)

_APPLYRECOMMENDATIONOPERATION = _descriptor.Descriptor(
  name='ApplyRecommendationOperation',
  full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_budget', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.campaign_budget', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_ad', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.text_ad', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.keyword', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_cpa_opt_in', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.target_cpa_opt_in', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_APPLYRECOMMENDATIONOPERATION_CAMPAIGNBUDGETPARAMETERS, _APPLYRECOMMENDATIONOPERATION_TEXTADPARAMETERS, _APPLYRECOMMENDATIONOPERATION_KEYWORDPARAMETERS, _APPLYRECOMMENDATIONOPERATION_TARGETCPAOPTINPARAMETERS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='apply_parameters', full_name='google.ads.googleads.v0.services.ApplyRecommendationOperation.apply_parameters',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=554,
  serialized_end=1594,
)


_APPLYRECOMMENDATIONRESPONSE = _descriptor.Descriptor(
  name='ApplyRecommendationResponse',
  full_name='google.ads.googleads.v0.services.ApplyRecommendationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v0.services.ApplyRecommendationResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1596,
  serialized_end=1703,
)


_APPLYRECOMMENDATIONRESULT = _descriptor.Descriptor(
  name='ApplyRecommendationResult',
  full_name='google.ads.googleads.v0.services.ApplyRecommendationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.ApplyRecommendationResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v0.services.ApplyRecommendationResult.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='result', full_name='google.ads.googleads.v0.services.ApplyRecommendationResult.result',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1705,
  serialized_end=1805,
)

_APPLYRECOMMENDATIONREQUEST.fields_by_name['operations'].message_type = _APPLYRECOMMENDATIONOPERATION
_APPLYRECOMMENDATIONOPERATION_CAMPAIGNBUDGETPARAMETERS.fields_by_name['new_budget_amount_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_APPLYRECOMMENDATIONOPERATION_CAMPAIGNBUDGETPARAMETERS.containing_type = _APPLYRECOMMENDATIONOPERATION
_APPLYRECOMMENDATIONOPERATION_TEXTADPARAMETERS.fields_by_name['ad'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__pb2._AD
_APPLYRECOMMENDATIONOPERATION_TEXTADPARAMETERS.containing_type = _APPLYRECOMMENDATIONOPERATION
_APPLYRECOMMENDATIONOPERATION_KEYWORDPARAMETERS.fields_by_name['ad_group'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_APPLYRECOMMENDATIONOPERATION_KEYWORDPARAMETERS.fields_by_name['match_type'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_keyword__match__type__pb2._KEYWORDMATCHTYPEENUM_KEYWORDMATCHTYPE
_APPLYRECOMMENDATIONOPERATION_KEYWORDPARAMETERS.fields_by_name['cpc_bid_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_APPLYRECOMMENDATIONOPERATION_KEYWORDPARAMETERS.containing_type = _APPLYRECOMMENDATIONOPERATION
_APPLYRECOMMENDATIONOPERATION_TARGETCPAOPTINPARAMETERS.fields_by_name['target_cpa_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_APPLYRECOMMENDATIONOPERATION_TARGETCPAOPTINPARAMETERS.fields_by_name['new_campaign_budget_amount_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_APPLYRECOMMENDATIONOPERATION_TARGETCPAOPTINPARAMETERS.containing_type = _APPLYRECOMMENDATIONOPERATION
_APPLYRECOMMENDATIONOPERATION.fields_by_name['campaign_budget'].message_type = _APPLYRECOMMENDATIONOPERATION_CAMPAIGNBUDGETPARAMETERS
_APPLYRECOMMENDATIONOPERATION.fields_by_name['text_ad'].message_type = _APPLYRECOMMENDATIONOPERATION_TEXTADPARAMETERS
_APPLYRECOMMENDATIONOPERATION.fields_by_name['keyword'].message_type = _APPLYRECOMMENDATIONOPERATION_KEYWORDPARAMETERS
_APPLYRECOMMENDATIONOPERATION.fields_by_name['target_cpa_opt_in'].message_type = _APPLYRECOMMENDATIONOPERATION_TARGETCPAOPTINPARAMETERS
_APPLYRECOMMENDATIONOPERATION.oneofs_by_name['apply_parameters'].fields.append(
  _APPLYRECOMMENDATIONOPERATION.fields_by_name['campaign_budget'])
_APPLYRECOMMENDATIONOPERATION.fields_by_name['campaign_budget'].containing_oneof = _APPLYRECOMMENDATIONOPERATION.oneofs_by_name['apply_parameters']
_APPLYRECOMMENDATIONOPERATION.oneofs_by_name['apply_parameters'].fields.append(
  _APPLYRECOMMENDATIONOPERATION.fields_by_name['text_ad'])
_APPLYRECOMMENDATIONOPERATION.fields_by_name['text_ad'].containing_oneof = _APPLYRECOMMENDATIONOPERATION.oneofs_by_name['apply_parameters']
_APPLYRECOMMENDATIONOPERATION.oneofs_by_name['apply_parameters'].fields.append(
  _APPLYRECOMMENDATIONOPERATION.fields_by_name['keyword'])
_APPLYRECOMMENDATIONOPERATION.fields_by_name['keyword'].containing_oneof = _APPLYRECOMMENDATIONOPERATION.oneofs_by_name['apply_parameters']
_APPLYRECOMMENDATIONOPERATION.oneofs_by_name['apply_parameters'].fields.append(
  _APPLYRECOMMENDATIONOPERATION.fields_by_name['target_cpa_opt_in'])
_APPLYRECOMMENDATIONOPERATION.fields_by_name['target_cpa_opt_in'].containing_oneof = _APPLYRECOMMENDATIONOPERATION.oneofs_by_name['apply_parameters']
_APPLYRECOMMENDATIONRESPONSE.fields_by_name['results'].message_type = _APPLYRECOMMENDATIONRESULT
_APPLYRECOMMENDATIONRESULT.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_APPLYRECOMMENDATIONRESULT.oneofs_by_name['result'].fields.append(
  _APPLYRECOMMENDATIONRESULT.fields_by_name['resource_name'])
_APPLYRECOMMENDATIONRESULT.fields_by_name['resource_name'].containing_oneof = _APPLYRECOMMENDATIONRESULT.oneofs_by_name['result']
_APPLYRECOMMENDATIONRESULT.oneofs_by_name['result'].fields.append(
  _APPLYRECOMMENDATIONRESULT.fields_by_name['status'])
_APPLYRECOMMENDATIONRESULT.fields_by_name['status'].containing_oneof = _APPLYRECOMMENDATIONRESULT.oneofs_by_name['result']
DESCRIPTOR.message_types_by_name['GetRecommendationRequest'] = _GETRECOMMENDATIONREQUEST
DESCRIPTOR.message_types_by_name['ApplyRecommendationRequest'] = _APPLYRECOMMENDATIONREQUEST
DESCRIPTOR.message_types_by_name['ApplyRecommendationOperation'] = _APPLYRECOMMENDATIONOPERATION
DESCRIPTOR.message_types_by_name['ApplyRecommendationResponse'] = _APPLYRECOMMENDATIONRESPONSE
DESCRIPTOR.message_types_by_name['ApplyRecommendationResult'] = _APPLYRECOMMENDATIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRecommendationRequest = _reflection.GeneratedProtocolMessageType('GetRecommendationRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETRECOMMENDATIONREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.recommendation_service_pb2'
  ,
  __doc__ = """Request message for
  [RecommendationService.GetRecommendation][google.ads.googleads.v0.services.RecommendationService.GetRecommendation].
  
  
  Attributes:
      resource_name:
          The resource name of the recommendation to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetRecommendationRequest)
  ))
_sym_db.RegisterMessage(GetRecommendationRequest)

ApplyRecommendationRequest = _reflection.GeneratedProtocolMessageType('ApplyRecommendationRequest', (_message.Message,), dict(
  DESCRIPTOR = _APPLYRECOMMENDATIONREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.recommendation_service_pb2'
  ,
  __doc__ = """Request message for
  [RecommendationService.ApplyRecommendation][google.ads.googleads.v0.services.RecommendationService.ApplyRecommendation].
  
  
  Attributes:
      customer_id:
          The ID of the customer with the recommendation.
      operations:
          The list of operations to apply recommendations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ApplyRecommendationRequest)
  ))
_sym_db.RegisterMessage(ApplyRecommendationRequest)

ApplyRecommendationOperation = _reflection.GeneratedProtocolMessageType('ApplyRecommendationOperation', (_message.Message,), dict(

  CampaignBudgetParameters = _reflection.GeneratedProtocolMessageType('CampaignBudgetParameters', (_message.Message,), dict(
    DESCRIPTOR = _APPLYRECOMMENDATIONOPERATION_CAMPAIGNBUDGETPARAMETERS,
    __module__ = 'google.ads.googleads_v0.proto.services.recommendation_service_pb2'
    ,
    __doc__ = """Parameters to use when applying a campaign budget recommendation.
    
    
    Attributes:
        new_budget_amount_micros:
            New budget amount to set for target budget resource. This is a
            required field.
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ApplyRecommendationOperation.CampaignBudgetParameters)
    ))
  ,

  TextAdParameters = _reflection.GeneratedProtocolMessageType('TextAdParameters', (_message.Message,), dict(
    DESCRIPTOR = _APPLYRECOMMENDATIONOPERATION_TEXTADPARAMETERS,
    __module__ = 'google.ads.googleads_v0.proto.services.recommendation_service_pb2'
    ,
    __doc__ = """Parameters to use when applying a text ad recommendation.
    
    
    Attributes:
        ad:
            New ad to add to recommended ad group. All necessary fields
            need to be set in this message. This is a required field.
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ApplyRecommendationOperation.TextAdParameters)
    ))
  ,

  KeywordParameters = _reflection.GeneratedProtocolMessageType('KeywordParameters', (_message.Message,), dict(
    DESCRIPTOR = _APPLYRECOMMENDATIONOPERATION_KEYWORDPARAMETERS,
    __module__ = 'google.ads.googleads_v0.proto.services.recommendation_service_pb2'
    ,
    __doc__ = """Parameters to use when applying keyword recommendation.
    
    
    Attributes:
        ad_group:
            The ad group resource to add keyword to. This is a required
            field.
        match_type:
            The match type of the keyword. This is a required field.
        cpc_bid_micros:
            Optional, CPC bid to set for the keyword. If not set, keyword
            will use bid based on bidding strategy used by target ad
            group.
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ApplyRecommendationOperation.KeywordParameters)
    ))
  ,

  TargetCpaOptInParameters = _reflection.GeneratedProtocolMessageType('TargetCpaOptInParameters', (_message.Message,), dict(
    DESCRIPTOR = _APPLYRECOMMENDATIONOPERATION_TARGETCPAOPTINPARAMETERS,
    __module__ = 'google.ads.googleads_v0.proto.services.recommendation_service_pb2'
    ,
    __doc__ = """Parameters to use when applying Target CPA recommendation.
    
    
    Attributes:
        target_cpa_micros:
            Average CPA to use for Target CPA bidding strategy. This is a
            required field.
        new_campaign_budget_amount_micros:
            Optional, budget amount to set for the campaign.
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ApplyRecommendationOperation.TargetCpaOptInParameters)
    ))
  ,
  DESCRIPTOR = _APPLYRECOMMENDATIONOPERATION,
  __module__ = 'google.ads.googleads_v0.proto.services.recommendation_service_pb2'
  ,
  __doc__ = """Information about the operation to apply a recommendation and any
  parameters to customize it.
  
  
  Attributes:
      resource_name:
          The resource name of the recommendation to apply.
      apply_parameters:
          Parameters to use when applying the recommendation.
      campaign_budget:
          Optional parameters to use when applying a campaign budget
          recommendation.
      text_ad:
          Optional parameters to use when applying a text ad
          recommendation.
      keyword:
          Optional parameters to use when applying keyword
          recommendation.
      target_cpa_opt_in:
          Optional parameters to use when applying target CPA opt-in
          recommendation.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ApplyRecommendationOperation)
  ))
_sym_db.RegisterMessage(ApplyRecommendationOperation)
_sym_db.RegisterMessage(ApplyRecommendationOperation.CampaignBudgetParameters)
_sym_db.RegisterMessage(ApplyRecommendationOperation.TextAdParameters)
_sym_db.RegisterMessage(ApplyRecommendationOperation.KeywordParameters)
_sym_db.RegisterMessage(ApplyRecommendationOperation.TargetCpaOptInParameters)

ApplyRecommendationResponse = _reflection.GeneratedProtocolMessageType('ApplyRecommendationResponse', (_message.Message,), dict(
  DESCRIPTOR = _APPLYRECOMMENDATIONRESPONSE,
  __module__ = 'google.ads.googleads_v0.proto.services.recommendation_service_pb2'
  ,
  __doc__ = """Response message for
  [RecommendationService.ApplyRecommendation][google.ads.googleads.v0.services.RecommendationService.ApplyRecommendation].
  
  
  Attributes:
      results:
          Results of operations to apply recommendations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ApplyRecommendationResponse)
  ))
_sym_db.RegisterMessage(ApplyRecommendationResponse)

ApplyRecommendationResult = _reflection.GeneratedProtocolMessageType('ApplyRecommendationResult', (_message.Message,), dict(
  DESCRIPTOR = _APPLYRECOMMENDATIONRESULT,
  __module__ = 'google.ads.googleads_v0.proto.services.recommendation_service_pb2'
  ,
  __doc__ = """The result of applying a recommendation.
  
  
  Attributes:
      result:
          One of the successfully applied recommendation resource name
          or error information will be set.
      resource_name:
          Returned for successful applies.
      status:
          Returned for failed operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ApplyRecommendationResult)
  ))
_sym_db.RegisterMessage(ApplyRecommendationResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\032RecommendationServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_RECOMMENDATIONSERVICE = _descriptor.ServiceDescriptor(
  name='RecommendationService',
  full_name='google.ads.googleads.v0.services.RecommendationService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1808,
  serialized_end=2236,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRecommendation',
    full_name='google.ads.googleads.v0.services.RecommendationService.GetRecommendation',
    index=0,
    containing_service=None,
    input_type=_GETRECOMMENDATIONREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_recommendation__pb2._RECOMMENDATION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0023\0221/v0/{resource_name=customers/*/recommendations/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='ApplyRecommendation',
    full_name='google.ads.googleads.v0.services.RecommendationService.ApplyRecommendation',
    index=1,
    containing_service=None,
    input_type=_APPLYRECOMMENDATIONREQUEST,
    output_type=_APPLYRECOMMENDATIONRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0028\"3/v0/customers/{customer_id=*}/recommendations:apply:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_RECOMMENDATIONSERVICE)

DESCRIPTOR.services_by_name['RecommendationService'] = _RECOMMENDATIONSERVICE

# @@protoc_insertion_point(module_scope)
