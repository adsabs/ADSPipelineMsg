# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: denormalized_record.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import status_pb2 as status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='denormalized_record.proto',
  package='adsmsg',
  syntax='proto3',
  serialized_pb=_b('\n\x19\x64\x65normalized_record.proto\x12\x06\x61\x64smsg\x1a\x0cstatus.proto\"\x88\x0f\n\x12\x44\x65normalizedRecord\x12\x10\n\x08\x61\x62stract\x18\x01 \x01(\t\x12\x0b\n\x03\x61\x63k\x18\x02 \x01(\t\x12\x0b\n\x03\x61\x66\x66\x18\x03 \x03(\t\x12\x19\n\x11\x61lternate_bibcode\x18\x04 \x03(\t\x12\x17\n\x0f\x61lternate_title\x18\x05 \x03(\t\x12\x13\n\x0b\x61rxiv_class\x18\x06 \x03(\t\x12\x0e\n\x06\x61uthor\x18\x07 \x03(\t\x12\x14\n\x0c\x61uthor_count\x18\x08 \x01(\x05\x12\x14\n\x0c\x61uthor_facet\x18\t \x03(\t\x12\x19\n\x11\x61uthor_facet_hier\x18\x0b \x03(\t\x12\x13\n\x0b\x61uthor_norm\x18\x0c \x03(\t\x12\x13\n\x0b\x62ook_author\x18` \x03(\t\x12\x0e\n\x06\x65\x64itor\x18\x61 \x03(\t\x12\x0f\n\x07\x62ibcode\x18\r \x01(\t\x12\x10\n\x08\x62ibgroup\x18\x0e \x03(\t\x12\x16\n\x0e\x62ibgroup_facet\x18\x0f \x03(\t\x12\x0f\n\x07\x62ibstem\x18\x10 \x03(\t\x12\x15\n\rbibstem_facet\x18\x11 \x01(\t\x12\x0c\n\x04\x62ody\x18\x12 \x01(\t\x12\x10\n\x08\x63itation\x18\x13 \x03(\t\x12\x16\n\x0e\x63itation_count\x18\x14 \x01(\x04\x12\x1b\n\x13\x63itation_count_norm\x18_ \x01(\x01\x12\x17\n\x0f\x63ite_read_boost\x18\x15 \x01(\x01\x12\x16\n\x0e\x63lassic_factor\x18\x16 \x01(\x04\x12\x0f\n\x07\x63omment\x18\x17 \x03(\t\x12\x11\n\tcopyright\x18\x18 \x03(\t\x12\x10\n\x08\x64\x61tabase\x18\x19 \x03(\t\x12\x12\n\ndata_count\x18] \x01(\x05\x12\x0c\n\x04\x64\x61te\x18\x1a \x01(\t\x12\x0f\n\x07\x64octype\x18\x1d \x01(\t\x12\x1a\n\x12\x64octype_facet_hier\x18\x1e \x03(\t\x12\x0b\n\x03\x64oi\x18\x1f \x03(\t\x12\x0b\n\x03\x65id\x18  \x01(\t\x12\r\n\x05\x65mail\x18! \x03(\t\x12\x12\n\nentry_date\x18L \x01(\t\x12\x10\n\x08\x65sources\x18^ \x03(\t\x12\x10\n\x08\x66\x61\x63ility\x18\" \x03(\t\x12\x14\n\x0c\x66irst_author\x18# \x01(\t\x12\x1f\n\x17\x66irst_author_facet_hier\x18$ \x03(\t\x12\x19\n\x11\x66irst_author_norm\x18% \x01(\t\x12\x16\n\x0e\x66ulltext_ctime\x18T \x01(\t\x12\x16\n\x0e\x66ulltext_mtime\x18U \x01(\t\x12\r\n\x05grant\x18& \x03(\t\x12\x18\n\x10grant_facet_hier\x18\' \x03(\t\x12\n\n\x02id\x18( \x01(\x04\x12\x12\n\nidentifier\x18) \x03(\t\x12\x0c\n\x04isbn\x18* \x03(\t\x12\x0c\n\x04issn\x18+ \x03(\t\x12\r\n\x05issue\x18, \x01(\t\x12\x0f\n\x07keyword\x18- \x03(\t\x12\x15\n\rkeyword_facet\x18. \x03(\t\x12\x14\n\x0ckeyword_norm\x18/ \x03(\t\x12\x16\n\x0ekeyword_schema\x18\x30 \x03(\t\x12\x0c\n\x04lang\x18\x31 \x01(\t\x12\x12\n\nlinks_data\x18\x32 \x03(\t\x12\x16\n\x0emetadata_ctime\x18R \x01(\t\x12\x16\n\x0emetadata_mtime\x18S \x01(\t\x12\x15\n\rmetrics_ctime\x18X \x01(\t\x12\x15\n\rmetrics_mtime\x18Y \x01(\t\x12\r\n\x05nedid\x18O \x03(\x05\x12\x0f\n\x07nedtype\x18P \x03(\t\x12\x1d\n\x15ned_object_facet_hier\x18Q \x03(\t\x12\x14\n\x0cnonbib_ctime\x18V \x01(\t\x12\x14\n\x0cnonbib_mtime\x18W \x01(\t\x12\r\n\x05orcid\x18\x33 \x03(\t\x12\x11\n\torcid_pub\x18\x34 \x03(\t\x12\x12\n\norcid_user\x18\x35 \x03(\t\x12\x13\n\x0borcid_other\x18\x36 \x03(\t\x12\x13\n\x0borcid_ctime\x18Z \x01(\t\x12\x13\n\x0borcid_mtime\x18[ \x01(\t\x12\x0e\n\x06origin\x18\\ \x03(\t\x12\x0c\n\x04page\x18\x37 \x03(\t\x12\x12\n\npage_count\x18K \x01(\x05\x12\x12\n\npage_range\x18M \x01(\t\x12\x10\n\x08property\x18\x38 \x03(\t\x12\x0b\n\x03pub\x18\x39 \x01(\t\x12\x0f\n\x07pub_raw\x18; \x01(\t\x12\x0f\n\x07pubnote\x18: \x03(\t\x12\x0f\n\x07pubdate\x18< \x01(\t\x12\x12\n\nread_count\x18= \x01(\x05\x12\x0e\n\x06reader\x18> \x03(\t\x12\r\n\x05recid\x18? \x01(\x04\x12\x11\n\treference\x18@ \x03(\t\x12\x0e\n\x06simbid\x18\x41 \x03(\x05\x12\x10\n\x08simbtype\x18\x42 \x03(\t\x12 \n\x18simbad_object_facet_hier\x18\x43 \x03(\t\x12\x1e\n\x06status\x18J \x01(\x0e\x32\x0e.adsmsg.Status\x12\x0e\n\x06thesis\x18\x44 \x01(\t\x12\r\n\x05title\x18\x45 \x03(\t\x12\x18\n\x10update_timestamp\x18N \x01(\t\x12\x0e\n\x06vizier\x18\x46 \x03(\t\x12\x14\n\x0cvizier_facet\x18G \x03(\t\x12\x0e\n\x06volume\x18H \x01(\t\x12\x0c\n\x04year\x18I \x01(\t\x12\x0e\n\x06series\x18\x62 \x01(\t\x12\x11\n\tpublisher\x18\x63 \x01(\t\x12\x0f\n\x07version\x18\x64 \x01(\tb\x06proto3')
  ,
  dependencies=[status__pb2.DESCRIPTOR,])




_DENORMALIZEDRECORD = _descriptor.Descriptor(
  name='DenormalizedRecord',
  full_name='adsmsg.DenormalizedRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='abstract', full_name='adsmsg.DenormalizedRecord.abstract', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ack', full_name='adsmsg.DenormalizedRecord.ack', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aff', full_name='adsmsg.DenormalizedRecord.aff', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternate_bibcode', full_name='adsmsg.DenormalizedRecord.alternate_bibcode', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternate_title', full_name='adsmsg.DenormalizedRecord.alternate_title', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arxiv_class', full_name='adsmsg.DenormalizedRecord.arxiv_class', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author', full_name='adsmsg.DenormalizedRecord.author', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author_count', full_name='adsmsg.DenormalizedRecord.author_count', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author_facet', full_name='adsmsg.DenormalizedRecord.author_facet', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author_facet_hier', full_name='adsmsg.DenormalizedRecord.author_facet_hier', index=9,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author_norm', full_name='adsmsg.DenormalizedRecord.author_norm', index=10,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='book_author', full_name='adsmsg.DenormalizedRecord.book_author', index=11,
      number=96, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='editor', full_name='adsmsg.DenormalizedRecord.editor', index=12,
      number=97, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bibcode', full_name='adsmsg.DenormalizedRecord.bibcode', index=13,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bibgroup', full_name='adsmsg.DenormalizedRecord.bibgroup', index=14,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bibgroup_facet', full_name='adsmsg.DenormalizedRecord.bibgroup_facet', index=15,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bibstem', full_name='adsmsg.DenormalizedRecord.bibstem', index=16,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bibstem_facet', full_name='adsmsg.DenormalizedRecord.bibstem_facet', index=17,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='adsmsg.DenormalizedRecord.body', index=18,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='citation', full_name='adsmsg.DenormalizedRecord.citation', index=19,
      number=19, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='citation_count', full_name='adsmsg.DenormalizedRecord.citation_count', index=20,
      number=20, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='citation_count_norm', full_name='adsmsg.DenormalizedRecord.citation_count_norm', index=21,
      number=95, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cite_read_boost', full_name='adsmsg.DenormalizedRecord.cite_read_boost', index=22,
      number=21, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classic_factor', full_name='adsmsg.DenormalizedRecord.classic_factor', index=23,
      number=22, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comment', full_name='adsmsg.DenormalizedRecord.comment', index=24,
      number=23, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='copyright', full_name='adsmsg.DenormalizedRecord.copyright', index=25,
      number=24, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='database', full_name='adsmsg.DenormalizedRecord.database', index=26,
      number=25, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_count', full_name='adsmsg.DenormalizedRecord.data_count', index=27,
      number=93, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='adsmsg.DenormalizedRecord.date', index=28,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doctype', full_name='adsmsg.DenormalizedRecord.doctype', index=29,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doctype_facet_hier', full_name='adsmsg.DenormalizedRecord.doctype_facet_hier', index=30,
      number=30, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doi', full_name='adsmsg.DenormalizedRecord.doi', index=31,
      number=31, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eid', full_name='adsmsg.DenormalizedRecord.eid', index=32,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='adsmsg.DenormalizedRecord.email', index=33,
      number=33, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entry_date', full_name='adsmsg.DenormalizedRecord.entry_date', index=34,
      number=76, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esources', full_name='adsmsg.DenormalizedRecord.esources', index=35,
      number=94, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='facility', full_name='adsmsg.DenormalizedRecord.facility', index=36,
      number=34, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_author', full_name='adsmsg.DenormalizedRecord.first_author', index=37,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_author_facet_hier', full_name='adsmsg.DenormalizedRecord.first_author_facet_hier', index=38,
      number=36, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_author_norm', full_name='adsmsg.DenormalizedRecord.first_author_norm', index=39,
      number=37, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fulltext_ctime', full_name='adsmsg.DenormalizedRecord.fulltext_ctime', index=40,
      number=84, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fulltext_mtime', full_name='adsmsg.DenormalizedRecord.fulltext_mtime', index=41,
      number=85, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grant', full_name='adsmsg.DenormalizedRecord.grant', index=42,
      number=38, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grant_facet_hier', full_name='adsmsg.DenormalizedRecord.grant_facet_hier', index=43,
      number=39, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='adsmsg.DenormalizedRecord.id', index=44,
      number=40, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='adsmsg.DenormalizedRecord.identifier', index=45,
      number=41, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isbn', full_name='adsmsg.DenormalizedRecord.isbn', index=46,
      number=42, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='issn', full_name='adsmsg.DenormalizedRecord.issn', index=47,
      number=43, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='issue', full_name='adsmsg.DenormalizedRecord.issue', index=48,
      number=44, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='adsmsg.DenormalizedRecord.keyword', index=49,
      number=45, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyword_facet', full_name='adsmsg.DenormalizedRecord.keyword_facet', index=50,
      number=46, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyword_norm', full_name='adsmsg.DenormalizedRecord.keyword_norm', index=51,
      number=47, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyword_schema', full_name='adsmsg.DenormalizedRecord.keyword_schema', index=52,
      number=48, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lang', full_name='adsmsg.DenormalizedRecord.lang', index=53,
      number=49, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='links_data', full_name='adsmsg.DenormalizedRecord.links_data', index=54,
      number=50, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata_ctime', full_name='adsmsg.DenormalizedRecord.metadata_ctime', index=55,
      number=82, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata_mtime', full_name='adsmsg.DenormalizedRecord.metadata_mtime', index=56,
      number=83, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics_ctime', full_name='adsmsg.DenormalizedRecord.metrics_ctime', index=57,
      number=88, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics_mtime', full_name='adsmsg.DenormalizedRecord.metrics_mtime', index=58,
      number=89, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nedid', full_name='adsmsg.DenormalizedRecord.nedid', index=59,
      number=79, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nedtype', full_name='adsmsg.DenormalizedRecord.nedtype', index=60,
      number=80, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ned_object_facet_hier', full_name='adsmsg.DenormalizedRecord.ned_object_facet_hier', index=61,
      number=81, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nonbib_ctime', full_name='adsmsg.DenormalizedRecord.nonbib_ctime', index=62,
      number=86, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nonbib_mtime', full_name='adsmsg.DenormalizedRecord.nonbib_mtime', index=63,
      number=87, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orcid', full_name='adsmsg.DenormalizedRecord.orcid', index=64,
      number=51, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orcid_pub', full_name='adsmsg.DenormalizedRecord.orcid_pub', index=65,
      number=52, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orcid_user', full_name='adsmsg.DenormalizedRecord.orcid_user', index=66,
      number=53, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orcid_other', full_name='adsmsg.DenormalizedRecord.orcid_other', index=67,
      number=54, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orcid_ctime', full_name='adsmsg.DenormalizedRecord.orcid_ctime', index=68,
      number=90, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orcid_mtime', full_name='adsmsg.DenormalizedRecord.orcid_mtime', index=69,
      number=91, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='origin', full_name='adsmsg.DenormalizedRecord.origin', index=70,
      number=92, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page', full_name='adsmsg.DenormalizedRecord.page', index=71,
      number=55, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_count', full_name='adsmsg.DenormalizedRecord.page_count', index=72,
      number=75, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_range', full_name='adsmsg.DenormalizedRecord.page_range', index=73,
      number=77, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='property', full_name='adsmsg.DenormalizedRecord.property', index=74,
      number=56, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pub', full_name='adsmsg.DenormalizedRecord.pub', index=75,
      number=57, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pub_raw', full_name='adsmsg.DenormalizedRecord.pub_raw', index=76,
      number=59, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pubnote', full_name='adsmsg.DenormalizedRecord.pubnote', index=77,
      number=58, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pubdate', full_name='adsmsg.DenormalizedRecord.pubdate', index=78,
      number=60, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_count', full_name='adsmsg.DenormalizedRecord.read_count', index=79,
      number=61, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reader', full_name='adsmsg.DenormalizedRecord.reader', index=80,
      number=62, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recid', full_name='adsmsg.DenormalizedRecord.recid', index=81,
      number=63, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference', full_name='adsmsg.DenormalizedRecord.reference', index=82,
      number=64, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simbid', full_name='adsmsg.DenormalizedRecord.simbid', index=83,
      number=65, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simbtype', full_name='adsmsg.DenormalizedRecord.simbtype', index=84,
      number=66, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simbad_object_facet_hier', full_name='adsmsg.DenormalizedRecord.simbad_object_facet_hier', index=85,
      number=67, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.DenormalizedRecord.status', index=86,
      number=74, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thesis', full_name='adsmsg.DenormalizedRecord.thesis', index=87,
      number=68, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='adsmsg.DenormalizedRecord.title', index=88,
      number=69, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_timestamp', full_name='adsmsg.DenormalizedRecord.update_timestamp', index=89,
      number=78, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vizier', full_name='adsmsg.DenormalizedRecord.vizier', index=90,
      number=70, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vizier_facet', full_name='adsmsg.DenormalizedRecord.vizier_facet', index=91,
      number=71, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='adsmsg.DenormalizedRecord.volume', index=92,
      number=72, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='year', full_name='adsmsg.DenormalizedRecord.year', index=93,
      number=73, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='series', full_name='adsmsg.DenormalizedRecord.series', index=94,
      number=98, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publisher', full_name='adsmsg.DenormalizedRecord.publisher', index=95,
      number=99, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='adsmsg.DenormalizedRecord.version', index=96,
      number=100, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=1980,
)

_DENORMALIZEDRECORD.fields_by_name['status'].enum_type = status__pb2._STATUS
DESCRIPTOR.message_types_by_name['DenormalizedRecord'] = _DENORMALIZEDRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DenormalizedRecord = _reflection.GeneratedProtocolMessageType('DenormalizedRecord', (_message.Message,), dict(
  DESCRIPTOR = _DENORMALIZEDRECORD,
  __module__ = 'denormalized_record_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.DenormalizedRecord)
  ))
_sym_db.RegisterMessage(DenormalizedRecord)


# @@protoc_insertion_point(module_scope)
