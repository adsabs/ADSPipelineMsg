
class Msg(object):

    def __init__(self, instance, args, kwargs):
        self.__dict__['_data'] = instance
        if kwargs:
            for k, v in kwargs.items():
                setattr(instance, k, v)


    def __str__(self):
        return self._data.SerializeToString()

    
    def __getattr__(self, key):
        if key == '_data':
            return self._data
        return getattr(self._data, key)

    def __setattr__(self, key, value):
        return setattr(self.__dict__['_data'], key, value)


    @classmethod
    def deserializer(cls, data):
        """
        Receives a serialized protocol buffer message and returns an object.
        """
        record = cls()
        record._data.ParseFromString(data)
        return record


    @classmethod
    def serializer(cls, record):
        """
        Receives an object and return a serialized protocol buffer message.
        """
        return record.serialize()


    def serialize(self):
        """
        Returns a serialized protocol buffer message
        """
        return self._data.SerializeToString()

    def is_valid(self):
        return self._data.IsInitialized()

    @property
    def data(self):
        return self._data