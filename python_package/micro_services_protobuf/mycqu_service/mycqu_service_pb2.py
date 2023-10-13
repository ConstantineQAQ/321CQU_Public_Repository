# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: micro_services_protobuf/mycqu_service/mycqu_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from micro_services_protobuf.mycqu_service import mycqu_model_pb2 as micro__services__protobuf_dot_mycqu__service_dot_mycqu__model__pb2
from micro_services_protobuf.mycqu_service import mycqu_request_response_pb2 as micro__services__protobuf_dot_mycqu__service_dot_mycqu__request__response__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9micro_services_protobuf/mycqu_service/mycqu_service.proto\x12\rmycqu_service\x1a\x37micro_services_protobuf/mycqu_service/mycqu_model.proto\x1a\x42micro_services_protobuf/mycqu_service/mycqu_request_response.proto2\x9a\x08\n\x0cMycquFetcher\x12\x42\n\tFetchUser\x12\x1c.mycqu_service.BaseLoginInfo\x1a\x17.mycqu_service.UserInfo\x12r\n\x15\x46\x65tchEnrollCourseInfo\x12+.mycqu_service.FetchEnrollCourseInfoRequest\x1a,.mycqu_service.FetchEnrollCourseInfoResponse\x12r\n\x15\x46\x65tchEnrollCourseItem\x12+.mycqu_service.FetchEnrollCourseItemRequest\x1a,.mycqu_service.FetchEnrollCourseItemResponse\x12N\n\tFetchExam\x12\x1f.mycqu_service.FetchExamRequest\x1a .mycqu_service.FetchExamResponse\x12W\n\x0f\x46\x65tchAllSession\x12\x1c.mycqu_service.BaseLoginInfo\x1a&.mycqu_service.FetchAllSessionResponse\x12S\n\x14\x46\x65tchCurrSessionInfo\x12\x1c.mycqu_service.BaseLoginInfo\x1a\x1d.mycqu_service.CquSessionInfo\x12_\n\x13\x46\x65tchAllSessionInfo\x12\x1c.mycqu_service.BaseLoginInfo\x1a*.mycqu_service.FetchAllSessionInfoResponse\x12o\n\x14\x46\x65tchCourseTimetable\x12*.mycqu_service.FetchCourseTimetableRequest\x1a+.mycqu_service.FetchCourseTimetableResponse\x12o\n\x14\x46\x65tchEnrollTimetable\x12*.mycqu_service.FetchEnrollTimetableRequest\x1a+.mycqu_service.FetchCourseTimetableResponse\x12Q\n\nFetchScore\x12 .mycqu_service.FetchScoreRequest\x1a!.mycqu_service.FetchScoreResponse\x12J\n\x0f\x46\x65tchGpaRanking\x12\x1c.mycqu_service.BaseLoginInfo\x1a\x19.mycqu_service.GpaRanking2\xee\x01\n\x0b\x43\x61rdFetcher\x12>\n\tFetchCard\x12\x1c.mycqu_service.BaseLoginInfo\x1a\x13.mycqu_service.Card\x12L\n\nFetchBills\x12\x1c.mycqu_service.BaseLoginInfo\x1a .mycqu_service.FetchBillResponse\x12Q\n\x0e\x46\x65tchEnergyFee\x12$.mycqu_service.FetchEnergyFeeRequest\x1a\x19.mycqu_service.EnergyFees2\xc2\x01\n\x0eLibraryFetcher\x12`\n\x0f\x46\x65tchBorrowBook\x12%.mycqu_service.FetchBorrowBookRequest\x1a&.mycqu_service.FetchBorrowBookResponse\x12N\n\tRenewBook\x12\x1f.mycqu_service.RenewBookRequest\x1a .mycqu_service.RenewBookResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'micro_services_protobuf.mycqu_service.mycqu_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MYCQUFETCHER']._serialized_start=202
  _globals['_MYCQUFETCHER']._serialized_end=1252
  _globals['_CARDFETCHER']._serialized_start=1255
  _globals['_CARDFETCHER']._serialized_end=1493
  _globals['_LIBRARYFETCHER']._serialized_start=1496
  _globals['_LIBRARYFETCHER']._serialized_end=1690
# @@protoc_insertion_point(module_scope)
