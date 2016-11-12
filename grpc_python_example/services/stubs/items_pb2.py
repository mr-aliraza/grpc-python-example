# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: items.proto

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
  name='items.proto',
  package='grpc_python_example',
  syntax='proto3',
  serialized_pb=_b('\n\x0bitems.proto\x12\x13grpc_python_example\".\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x1c\n\x0eGetItemRequest\x12\n\n\x02id\x18\x01 \x01(\x05\":\n\x0fGetItemResponse\x12\'\n\x04item\x18\x01 \x01(\x0b\x32\x19.grpc_python_example.Item2d\n\nItemMaster\x12V\n\x07GetItem\x12#.grpc_python_example.GetItemRequest\x1a$.grpc_python_example.GetItemResponse\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='grpc_python_example.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc_python_example.Item.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='grpc_python_example.Item.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='grpc_python_example.Item.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=36,
  serialized_end=82,
)


_GETITEMREQUEST = _descriptor.Descriptor(
  name='GetItemRequest',
  full_name='grpc_python_example.GetItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc_python_example.GetItemRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=84,
  serialized_end=112,
)


_GETITEMRESPONSE = _descriptor.Descriptor(
  name='GetItemResponse',
  full_name='grpc_python_example.GetItemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='grpc_python_example.GetItemResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=114,
  serialized_end=172,
)

_GETITEMRESPONSE.fields_by_name['item'].message_type = _ITEM
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['GetItemRequest'] = _GETITEMREQUEST
DESCRIPTOR.message_types_by_name['GetItemResponse'] = _GETITEMRESPONSE

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:grpc_python_example.Item)
  ))
_sym_db.RegisterMessage(Item)

GetItemRequest = _reflection.GeneratedProtocolMessageType('GetItemRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETITEMREQUEST,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:grpc_python_example.GetItemRequest)
  ))
_sym_db.RegisterMessage(GetItemRequest)

GetItemResponse = _reflection.GeneratedProtocolMessageType('GetItemResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETITEMRESPONSE,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:grpc_python_example.GetItemResponse)
  ))
_sym_db.RegisterMessage(GetItemResponse)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class ItemMasterStub(object):
  """Manages item data.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetItem = channel.unary_unary(
        '/grpc_python_example.ItemMaster/GetItem',
        request_serializer=GetItemRequest.SerializeToString,
        response_deserializer=GetItemResponse.FromString,
        )


class ItemMasterServicer(object):
  """Manages item data.
  """

  def GetItem(self, request, context):
    """Get an item by id.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ItemMasterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetItem': grpc.unary_unary_rpc_method_handler(
          servicer.GetItem,
          request_deserializer=GetItemRequest.FromString,
          response_serializer=GetItemResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc_python_example.ItemMaster', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaItemMasterServicer(object):
  """Manages item data.
  """
  def GetItem(self, request, context):
    """Get an item by id.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaItemMasterStub(object):
  """Manages item data.
  """
  def GetItem(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Get an item by id.
    """
    raise NotImplementedError()
  GetItem.future = None


def beta_create_ItemMaster_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('grpc_python_example.ItemMaster', 'GetItem'): GetItemRequest.FromString,
  }
  response_serializers = {
    ('grpc_python_example.ItemMaster', 'GetItem'): GetItemResponse.SerializeToString,
  }
  method_implementations = {
    ('grpc_python_example.ItemMaster', 'GetItem'): face_utilities.unary_unary_inline(servicer.GetItem),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_ItemMaster_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('grpc_python_example.ItemMaster', 'GetItem'): GetItemRequest.SerializeToString,
  }
  response_deserializers = {
    ('grpc_python_example.ItemMaster', 'GetItem'): GetItemResponse.FromString,
  }
  cardinalities = {
    'GetItem': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'grpc_python_example.ItemMaster', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)