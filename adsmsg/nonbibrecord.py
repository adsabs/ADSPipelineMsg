from .msg import Msg
from .protobuf import nonbibrecord_pb2
from google.protobuf.json_format import MessageToJson
import json

class NonBibRecord(Msg):

    def __init__(self, *args, **kwargs):
        super(NonBibRecord, self).__init__(nonbibrecord_pb2.NonBibRecord(), args, kwargs)


class NonBibRecordList(Msg):

    def __init__(self, *args, **kwargs):
        if 'nonbib_records' in kwargs:
            tmp = [NonBibRecord(**x)._data for x in kwargs['nonbib_records']]
            kwargs['metrics_records'] = tmp
        super(NonBibRecordList, self).__init__(nonbibrecord_pb2.NonBibRecordList(), args, kwargs)


def protobufToNonBibRecord(pbuf):
    """use with elements in NonBibRecordList.nonbib_records

    converts nonbibrecord_pb2.NonBibRecord to our NonBibRecord wrapper
    """
    tmp_string = MessageToJson(pbuf)
    tmp_dict = json.loads(tmp_string)
    tmp_nonbib = NonBibRecord(**tmp_dict)
    return tmp_nonbib

