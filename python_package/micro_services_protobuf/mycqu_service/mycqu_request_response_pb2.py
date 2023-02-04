# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: micro_services_protobuf/mycqu_service/mycqu_request_response.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from micro_services_protobuf.mycqu_service import mycqu_model_pb2 as micro__services__protobuf_dot_mycqu__service_dot_mycqu__model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBmicro_services_protobuf/mycqu_service/mycqu_request_response.proto\x12\rmycqu_service\x1a\x37micro_services_protobuf/mycqu_service/mycqu_model.proto\"/\n\rBaseLoginInfo\x12\x0c\n\x04\x61uth\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"7\n\x11\x46\x65tchBillResponse\x12\"\n\x05\x62ills\x18\x01 \x03(\x0b\x32\x13.mycqu_service.Bill\"n\n\x15\x46\x65tchEnergyFeeRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x10\n\x08is_hu_xi\x18\x02 \x01(\x08\x12\x0c\n\x04room\x18\x03 \x01(\t\"F\n\x17\x46\x65tchAllSessionResponse\x12+\n\x08sessions\x18\x01 \x03(\x0b\x32\x19.mycqu_service.CquSession\"S\n\x1b\x46\x65tchAllSessionInfoResponse\x12\x34\n\rsession_infos\x18\x01 \x03(\x0b\x32\x1d.mycqu_service.CquSessionInfo\"\x8e\x01\n\x1b\x46\x65tchCourseTimetableRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12*\n\x07session\x18\x03 \x01(\x0b\x32\x19.mycqu_service.CquSession\"Y\n\x1c\x46\x65tchCourseTimetableResponse\x12\x39\n\x11\x63ourse_timetables\x18\x01 \x03(\x0b\x32\x1e.mycqu_service.CourseTimetable\"g\n\x1c\x46\x65tchEnrollCourseInfoRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x10\n\x08is_major\x18\x02 \x01(\x08\"\x9c\x02\n\x1d\x46\x65tchEnrollCourseInfoResponse\x12H\n\x06result\x18\x01 \x03(\x0b\x32\x38.mycqu_service.FetchEnrollCourseInfoResponse.ResultEntry\x1a\x42\n\x11\x45nrollCourseInfos\x12-\n\x04info\x18\x01 \x03(\x0b\x32\x1f.mycqu_service.EnrollCourseInfo\x1am\n\x0bResultEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12M\n\x05value\x18\x02 \x01(\x0b\x32>.mycqu_service.FetchEnrollCourseInfoResponse.EnrollCourseInfos:\x02\x38\x01\"s\n\x1c\x46\x65tchEnrollCourseItemRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08is_major\x18\x03 \x01(\x08\"]\n\x1d\x46\x65tchEnrollCourseItemResponse\x12<\n\x13\x65nroll_course_items\x18\x01 \x03(\x0b\x32\x1f.mycqu_service.EnrollCourseItem\"Y\n\x10\x46\x65tchExamRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x0e\n\x06stu_id\x18\x02 \x01(\t\"7\n\x11\x46\x65tchExamResponse\x12\"\n\x05\x65xams\x18\x01 \x03(\x0b\x32\x13.mycqu_service.Exam\"\\\n\x11\x46\x65tchScoreRequest\x12\x35\n\x0f\x62\x61se_login_info\x18\x01 \x01(\x0b\x32\x1c.mycqu_service.BaseLoginInfo\x12\x10\n\x08is_minor\x18\x02 \x01(\x08\":\n\x12\x46\x65tchScoreResponse\x12$\n\x06scores\x18\x01 \x03(\x0b\x32\x14.mycqu_service.Scoreb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'micro_services_protobuf.mycqu_service.mycqu_request_response_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FETCHENROLLCOURSEINFORESPONSE_RESULTENTRY._options = None
  _FETCHENROLLCOURSEINFORESPONSE_RESULTENTRY._serialized_options = b'8\001'
  _BASELOGININFO._serialized_start=142
  _BASELOGININFO._serialized_end=189
  _FETCHBILLRESPONSE._serialized_start=191
  _FETCHBILLRESPONSE._serialized_end=246
  _FETCHENERGYFEEREQUEST._serialized_start=248
  _FETCHENERGYFEEREQUEST._serialized_end=358
  _FETCHALLSESSIONRESPONSE._serialized_start=360
  _FETCHALLSESSIONRESPONSE._serialized_end=430
  _FETCHALLSESSIONINFORESPONSE._serialized_start=432
  _FETCHALLSESSIONINFORESPONSE._serialized_end=515
  _FETCHCOURSETIMETABLEREQUEST._serialized_start=518
  _FETCHCOURSETIMETABLEREQUEST._serialized_end=660
  _FETCHCOURSETIMETABLERESPONSE._serialized_start=662
  _FETCHCOURSETIMETABLERESPONSE._serialized_end=751
  _FETCHENROLLCOURSEINFOREQUEST._serialized_start=753
  _FETCHENROLLCOURSEINFOREQUEST._serialized_end=856
  _FETCHENROLLCOURSEINFORESPONSE._serialized_start=859
  _FETCHENROLLCOURSEINFORESPONSE._serialized_end=1143
  _FETCHENROLLCOURSEINFORESPONSE_ENROLLCOURSEINFOS._serialized_start=966
  _FETCHENROLLCOURSEINFORESPONSE_ENROLLCOURSEINFOS._serialized_end=1032
  _FETCHENROLLCOURSEINFORESPONSE_RESULTENTRY._serialized_start=1034
  _FETCHENROLLCOURSEINFORESPONSE_RESULTENTRY._serialized_end=1143
  _FETCHENROLLCOURSEITEMREQUEST._serialized_start=1145
  _FETCHENROLLCOURSEITEMREQUEST._serialized_end=1260
  _FETCHENROLLCOURSEITEMRESPONSE._serialized_start=1262
  _FETCHENROLLCOURSEITEMRESPONSE._serialized_end=1355
  _FETCHEXAMREQUEST._serialized_start=1357
  _FETCHEXAMREQUEST._serialized_end=1446
  _FETCHEXAMRESPONSE._serialized_start=1448
  _FETCHEXAMRESPONSE._serialized_end=1503
  _FETCHSCOREREQUEST._serialized_start=1505
  _FETCHSCOREREQUEST._serialized_end=1597
  _FETCHSCORERESPONSE._serialized_start=1599
  _FETCHSCORERESPONSE._serialized_end=1657
# @@protoc_insertion_point(module_scope)
