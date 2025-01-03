# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: lms.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'lms.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tlms.proto\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"=\n\rLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x0c\n\x04role\x18\x03 \x01(\t\"\x1e\n\rLogoutRequest\x12\r\n\x05token\x18\x01 \x01(\t\"!\n\x0eStatusResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"N\n\x10PostQueryRequest\x12\x12\n\nstudent_id\x18\x01 \x01(\t\x12\x12\n\nquery_text\x18\x02 \x01(\t\x12\x12\n\nllm_answer\x18\x03 \x01(\t\"3\n\x0ePostQueryReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x10\n\x08query_id\x18\x02 \x01(\x05\"$\n\x11GetQueriesRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"?\n\x05Query\x12\x10\n\x08query_id\x18\x01 \x01(\x05\x12\x12\n\nquery_text\x18\x02 \x01(\t\x12\x10\n\x08response\x18\x03 \x01(\t\"*\n\x0fGetQueriesReply\x12\x17\n\x07queries\x18\x01 \x03(\x0b\x32\x06.Query\"@\n\x15RespondToQueryRequest\x12\x10\n\x08query_id\x18\x01 \x01(\x05\x12\x15\n\rresponse_text\x18\x02 \x01(\t\"&\n\x13RespondToQueryReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"G\n\x13PostMaterialRequest\x12\x16\n\x0ematerial_title\x18\x01 \x01(\t\x12\x18\n\x10material_content\x18\x02 \x01(\t\"<\n\x14PostMaterialResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x13\n\x0bmaterial_id\x18\x02 \x01(\x05\"W\n\x0e\x43ourseMaterial\x12\x13\n\x0bmaterial_id\x18\x01 \x01(\x05\x12\x16\n\x0ematerial_title\x18\x02 \x01(\t\x12\x18\n\x10material_content\x18\x03 \x01(\t\"\x1b\n\x19GetCourseMaterialsRequest\"=\n\x17GetCourseMaterialsReply\x12\"\n\tmaterials\x18\x01 \x03(\x0b\x32\x0f.CourseMaterial\"Q\n\x15PostAssignmentRequest\x12\x18\n\x10\x61ssignment_title\x18\x01 \x01(\t\x12\x1e\n\x16\x61ssignment_description\x18\x02 \x01(\t\"=\n\x13PostAssignmentReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rassignment_id\x18\x02 \x01(\x05\"\x17\n\x15GetAssignmentsRequest\"]\n\nAssignment\x12\x15\n\rassignment_id\x18\x01 \x01(\x05\x12\x18\n\x10\x61ssignment_title\x18\x02 \x01(\t\x12\x1e\n\x16\x61ssignment_description\x18\x03 \x01(\t\"7\n\x13GetAssignmentsReply\x12 \n\x0b\x61ssignments\x18\x01 \x03(\x0b\x32\x0b.Assignment\"`\n\x17SubmitAssignmentRequest\x12\x15\n\rassignment_id\x18\x01 \x01(\x05\x12\x12\n\nstudent_id\x18\x02 \x01(\t\x12\x1a\n\x12submission_content\x18\x03 \x01(\t\"(\n\x15SubmitAssignmentReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x17\n\x15GetSubmissionsRequest\"S\n\nSubmission\x12\x15\n\rassignment_id\x18\x01 \x01(\x05\x12\x12\n\nstudent_id\x18\x02 \x01(\t\x12\x1a\n\x12submission_content\x18\x03 \x01(\t\"7\n\x13GetSubmissionsReply\x12 \n\x0bsubmissions\x18\x01 \x03(\x0b\x32\x0b.Submission\"d\n\x16GradeSubmissionRequest\x12\x15\n\rassignment_id\x18\x01 \x01(\x05\x12\x12\n\nstudent_id\x18\x02 \x01(\t\x12\r\n\x05grade\x18\x03 \x01(\t\x12\x10\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\x04 \x01(\t\"\'\n\x14GradeSubmissionReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\'\n\x11ViewGradesRequest\x12\x12\n\nstudent_id\x18\x01 \x01(\t\"S\n\x05Grade\x12\x15\n\rassignment_id\x18\x01 \x01(\x05\x12\x12\n\nstudent_id\x18\x02 \x01(\t\x12\r\n\x05grade\x18\x03 \x01(\t\x12\x10\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\x04 \x01(\t\")\n\x0fViewGradesReply\x12\x16\n\x06grades\x18\x01 \x03(\x0b\x32\x06.Grade\"b\n\x12RequestVoteRequest\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61ndidateId\x18\x02 \x01(\x05\x12\x14\n\x0clastLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0blastLogTerm\x18\x04 \x01(\x05\"8\n\x13RequestVoteResponse\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0bvoteGranted\x18\x02 \x01(\x08\"\x93\x01\n\x14\x41ppendEntriesRequest\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x10\n\x08leaderId\x18\x02 \x01(\x05\x12\x14\n\x0cprevLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0bprevLogTerm\x18\x04 \x01(\x05\x12\x1a\n\x07\x65ntries\x18\x05 \x03(\x0b\x32\t.LogEntry\x12\x14\n\x0cleaderCommit\x18\x06 \x01(\x05\"6\n\x15\x41ppendEntriesResponse\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\"&\n\x12LeaderAnnouncement\x12\x10\n\x08leaderId\x18\x01 \x01(\t\"5\n\x08LogEntry\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x1b\n\x0bgrade_entry\x18\x02 \x01(\x0b\x32\x06.Grade\"\x07\n\x05\x45mpty\"\x0f\n\rLeaderRequest\"#\n\x0eLeaderResponse\x12\x11\n\tis_leader\x18\x01 \x01(\x08\x32\xe2\x07\n\x03LMS\x12&\n\x05Login\x12\r.LoginRequest\x1a\x0e.LoginResponse\x12)\n\x06Logout\x12\x0e.LogoutRequest\x1a\x0f.StatusResponse\x12/\n\tPostQuery\x12\x11.PostQueryRequest\x1a\x0f.PostQueryReply\x12\x32\n\nGetQueries\x12\x12.GetQueriesRequest\x1a\x10.GetQueriesReply\x12>\n\x0eRespondToQuery\x12\x16.RespondToQueryRequest\x1a\x14.RespondToQueryReply\x12\x41\n\x12PostCourseMaterial\x12\x14.PostMaterialRequest\x1a\x15.PostMaterialResponse\x12J\n\x12GetCourseMaterials\x12\x1a.GetCourseMaterialsRequest\x1a\x18.GetCourseMaterialsReply\x12>\n\x0ePostAssignment\x12\x16.PostAssignmentRequest\x1a\x14.PostAssignmentReply\x12>\n\x0eGetAssignments\x12\x16.GetAssignmentsRequest\x1a\x14.GetAssignmentsReply\x12\x44\n\x10SubmitAssignment\x12\x18.SubmitAssignmentRequest\x1a\x16.SubmitAssignmentReply\x12>\n\x0eGetSubmissions\x12\x16.GetSubmissionsRequest\x1a\x14.GetSubmissionsReply\x12\x41\n\x0fGradeSubmission\x12\x17.GradeSubmissionRequest\x1a\x15.GradeSubmissionReply\x12\x32\n\nViewGrades\x12\x12.ViewGradesRequest\x1a\x10.ViewGradesReply\x12.\n\x0b\x43heckLeader\x12\x0e.LeaderRequest\x1a\x0f.LeaderResponse\x12\x38\n\x0bRequestVote\x12\x13.RequestVoteRequest\x1a\x14.RequestVoteResponse\x12>\n\rAppendEntries\x12\x15.AppendEntriesRequest\x1a\x16.AppendEntriesResponse\x12-\n\x0e\x41nnounceLeader\x12\x13.LeaderAnnouncement\x1a\x06.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lms_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LOGINREQUEST']._serialized_start=13
  _globals['_LOGINREQUEST']._serialized_end=63
  _globals['_LOGINRESPONSE']._serialized_start=65
  _globals['_LOGINRESPONSE']._serialized_end=126
  _globals['_LOGOUTREQUEST']._serialized_start=128
  _globals['_LOGOUTREQUEST']._serialized_end=158
  _globals['_STATUSRESPONSE']._serialized_start=160
  _globals['_STATUSRESPONSE']._serialized_end=193
  _globals['_POSTQUERYREQUEST']._serialized_start=195
  _globals['_POSTQUERYREQUEST']._serialized_end=273
  _globals['_POSTQUERYREPLY']._serialized_start=275
  _globals['_POSTQUERYREPLY']._serialized_end=326
  _globals['_GETQUERIESREQUEST']._serialized_start=328
  _globals['_GETQUERIESREQUEST']._serialized_end=364
  _globals['_QUERY']._serialized_start=366
  _globals['_QUERY']._serialized_end=429
  _globals['_GETQUERIESREPLY']._serialized_start=431
  _globals['_GETQUERIESREPLY']._serialized_end=473
  _globals['_RESPONDTOQUERYREQUEST']._serialized_start=475
  _globals['_RESPONDTOQUERYREQUEST']._serialized_end=539
  _globals['_RESPONDTOQUERYREPLY']._serialized_start=541
  _globals['_RESPONDTOQUERYREPLY']._serialized_end=579
  _globals['_POSTMATERIALREQUEST']._serialized_start=581
  _globals['_POSTMATERIALREQUEST']._serialized_end=652
  _globals['_POSTMATERIALRESPONSE']._serialized_start=654
  _globals['_POSTMATERIALRESPONSE']._serialized_end=714
  _globals['_COURSEMATERIAL']._serialized_start=716
  _globals['_COURSEMATERIAL']._serialized_end=803
  _globals['_GETCOURSEMATERIALSREQUEST']._serialized_start=805
  _globals['_GETCOURSEMATERIALSREQUEST']._serialized_end=832
  _globals['_GETCOURSEMATERIALSREPLY']._serialized_start=834
  _globals['_GETCOURSEMATERIALSREPLY']._serialized_end=895
  _globals['_POSTASSIGNMENTREQUEST']._serialized_start=897
  _globals['_POSTASSIGNMENTREQUEST']._serialized_end=978
  _globals['_POSTASSIGNMENTREPLY']._serialized_start=980
  _globals['_POSTASSIGNMENTREPLY']._serialized_end=1041
  _globals['_GETASSIGNMENTSREQUEST']._serialized_start=1043
  _globals['_GETASSIGNMENTSREQUEST']._serialized_end=1066
  _globals['_ASSIGNMENT']._serialized_start=1068
  _globals['_ASSIGNMENT']._serialized_end=1161
  _globals['_GETASSIGNMENTSREPLY']._serialized_start=1163
  _globals['_GETASSIGNMENTSREPLY']._serialized_end=1218
  _globals['_SUBMITASSIGNMENTREQUEST']._serialized_start=1220
  _globals['_SUBMITASSIGNMENTREQUEST']._serialized_end=1316
  _globals['_SUBMITASSIGNMENTREPLY']._serialized_start=1318
  _globals['_SUBMITASSIGNMENTREPLY']._serialized_end=1358
  _globals['_GETSUBMISSIONSREQUEST']._serialized_start=1360
  _globals['_GETSUBMISSIONSREQUEST']._serialized_end=1383
  _globals['_SUBMISSION']._serialized_start=1385
  _globals['_SUBMISSION']._serialized_end=1468
  _globals['_GETSUBMISSIONSREPLY']._serialized_start=1470
  _globals['_GETSUBMISSIONSREPLY']._serialized_end=1525
  _globals['_GRADESUBMISSIONREQUEST']._serialized_start=1527
  _globals['_GRADESUBMISSIONREQUEST']._serialized_end=1627
  _globals['_GRADESUBMISSIONREPLY']._serialized_start=1629
  _globals['_GRADESUBMISSIONREPLY']._serialized_end=1668
  _globals['_VIEWGRADESREQUEST']._serialized_start=1670
  _globals['_VIEWGRADESREQUEST']._serialized_end=1709
  _globals['_GRADE']._serialized_start=1711
  _globals['_GRADE']._serialized_end=1794
  _globals['_VIEWGRADESREPLY']._serialized_start=1796
  _globals['_VIEWGRADESREPLY']._serialized_end=1837
  _globals['_REQUESTVOTEREQUEST']._serialized_start=1839
  _globals['_REQUESTVOTEREQUEST']._serialized_end=1937
  _globals['_REQUESTVOTERESPONSE']._serialized_start=1939
  _globals['_REQUESTVOTERESPONSE']._serialized_end=1995
  _globals['_APPENDENTRIESREQUEST']._serialized_start=1998
  _globals['_APPENDENTRIESREQUEST']._serialized_end=2145
  _globals['_APPENDENTRIESRESPONSE']._serialized_start=2147
  _globals['_APPENDENTRIESRESPONSE']._serialized_end=2201
  _globals['_LEADERANNOUNCEMENT']._serialized_start=2203
  _globals['_LEADERANNOUNCEMENT']._serialized_end=2241
  _globals['_LOGENTRY']._serialized_start=2243
  _globals['_LOGENTRY']._serialized_end=2296
  _globals['_EMPTY']._serialized_start=2298
  _globals['_EMPTY']._serialized_end=2305
  _globals['_LEADERREQUEST']._serialized_start=2307
  _globals['_LEADERREQUEST']._serialized_end=2322
  _globals['_LEADERRESPONSE']._serialized_start=2324
  _globals['_LEADERRESPONSE']._serialized_end=2359
  _globals['_LMS']._serialized_start=2362
  _globals['_LMS']._serialized_end=3356
# @@protoc_insertion_point(module_scope)
