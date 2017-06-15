# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metrics.proto

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
  name='metrics.proto',
  package='adsmsg',
  syntax='proto2',
  serialized_pb=_b('\n\rmetrics.proto\x12\x06\x61\x64smsg\"\xe5\x02\n\rMetricsRecord\x12\x0f\n\x07\x62ibcode\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x10\n\x08refereed\x18\x03 \x01(\x08\x12\x14\n\x0crn_citations\x18\x04 \x01(\x02\x12\x18\n\x10rn_citation_data\x18\x05 \x01(\t\x12\x11\n\tdownloads\x18\x06 \x03(\x05\x12\r\n\x05reads\x18\x07 \x03(\x05\x12\x14\n\x0c\x61n_citations\x18\x08 \x01(\x02\x12\x1d\n\x15refereed_citation_num\x18\t \x01(\x05\x12\x14\n\x0c\x63itation_num\x18\n \x01(\x05\x12\x15\n\rreference_num\x18\x0b \x01(\x05\x12\x11\n\tcitations\x18\x0c \x03(\t\x12\x1a\n\x12refereed_citations\x18\r \x03(\t\x12\x12\n\nauthor_num\x18\x0e \x01(\x05\x12\x1d\n\x15\x61n_refereed_citations\x18\x0f \x01(\x02\x12\x0f\n\x07modtime\x18\x10 \x01(\t\"C\n\x11MetricsRecordList\x12.\n\x0fmetrics_records\x18\x01 \x03(\x0b\x32\x15.adsmsg.MetricsRecord')
)




_METRICSRECORD = _descriptor.Descriptor(
  name='MetricsRecord',
  full_name='adsmsg.MetricsRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bibcode', full_name='adsmsg.MetricsRecord.bibcode', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='adsmsg.MetricsRecord.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refereed', full_name='adsmsg.MetricsRecord.refereed', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rn_citations', full_name='adsmsg.MetricsRecord.rn_citations', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rn_citation_data', full_name='adsmsg.MetricsRecord.rn_citation_data', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='downloads', full_name='adsmsg.MetricsRecord.downloads', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reads', full_name='adsmsg.MetricsRecord.reads', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='an_citations', full_name='adsmsg.MetricsRecord.an_citations', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refereed_citation_num', full_name='adsmsg.MetricsRecord.refereed_citation_num', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='citation_num', full_name='adsmsg.MetricsRecord.citation_num', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_num', full_name='adsmsg.MetricsRecord.reference_num', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='citations', full_name='adsmsg.MetricsRecord.citations', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refereed_citations', full_name='adsmsg.MetricsRecord.refereed_citations', index=12,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author_num', full_name='adsmsg.MetricsRecord.author_num', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='an_refereed_citations', full_name='adsmsg.MetricsRecord.an_refereed_citations', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modtime', full_name='adsmsg.MetricsRecord.modtime', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=383,
)


_METRICSRECORDLIST = _descriptor.Descriptor(
  name='MetricsRecordList',
  full_name='adsmsg.MetricsRecordList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics_records', full_name='adsmsg.MetricsRecordList.metrics_records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=452,
)

_METRICSRECORDLIST.fields_by_name['metrics_records'].message_type = _METRICSRECORD
DESCRIPTOR.message_types_by_name['MetricsRecord'] = _METRICSRECORD
DESCRIPTOR.message_types_by_name['MetricsRecordList'] = _METRICSRECORDLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetricsRecord = _reflection.GeneratedProtocolMessageType('MetricsRecord', (_message.Message,), dict(
  DESCRIPTOR = _METRICSRECORD,
  __module__ = 'metrics_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.MetricsRecord)
  ))
_sym_db.RegisterMessage(MetricsRecord)

MetricsRecordList = _reflection.GeneratedProtocolMessageType('MetricsRecordList', (_message.Message,), dict(
  DESCRIPTOR = _METRICSRECORDLIST,
  __module__ = 'metrics_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.MetricsRecordList)
  ))
_sym_db.RegisterMessage(MetricsRecordList)


# @@protoc_insertion_point(module_scope)
