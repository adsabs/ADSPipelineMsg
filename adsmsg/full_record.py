from msg import Msg
try:
    from google.protobuf import full_record_pb2
except ImportError:
    from protobuf import full_record_pb2

class FullRecord(Msg):

    def __init__(self):
        super(FullRecord, self).__init__()
        self._data = full_record_pb2.FullRecord()

