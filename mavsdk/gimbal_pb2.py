# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gimbal/gimbal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gimbal/gimbal.proto',
  package='mavsdk.rpc.gimbal',
  syntax='proto3',
  serialized_options=b'\n\020io.mavsdk.gimbalB\013GimbalProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13gimbal/gimbal.proto\x12\x11mavsdk.rpc.gimbal\";\n\x15SetPitchAndYawRequest\x12\x11\n\tpitch_deg\x18\x01 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x02 \x01(\x02\"P\n\x16SetPitchAndYawResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\"D\n\x0eSetModeRequest\x12\x32\n\x0bgimbal_mode\x18\x01 \x01(\x0e\x32\x1d.mavsdk.rpc.gimbal.GimbalMode\"I\n\x0fSetModeResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\"X\n\x15SetRoiLocationRequest\x12\x14\n\x0clatitude_deg\x18\x01 \x01(\x01\x12\x15\n\rlongitude_deg\x18\x02 \x01(\x01\x12\x12\n\naltitude_m\x18\x03 \x01(\x02\"P\n\x16SetRoiLocationResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\"\xca\x01\n\x0cGimbalResult\x12\x36\n\x06result\x18\x01 \x01(\x0e\x32&.mavsdk.rpc.gimbal.GimbalResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"n\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x10\n\x0cRESULT_ERROR\x10\x02\x12\x12\n\x0eRESULT_TIMEOUT\x10\x03\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x04*B\n\nGimbalMode\x12\x1a\n\x16GIMBAL_MODE_YAW_FOLLOW\x10\x00\x12\x18\n\x14GIMBAL_MODE_YAW_LOCK\x10\x01\x32\xb5\x02\n\rGimbalService\x12g\n\x0eSetPitchAndYaw\x12(.mavsdk.rpc.gimbal.SetPitchAndYawRequest\x1a).mavsdk.rpc.gimbal.SetPitchAndYawResponse\"\x00\x12R\n\x07SetMode\x12!.mavsdk.rpc.gimbal.SetModeRequest\x1a\".mavsdk.rpc.gimbal.SetModeResponse\"\x00\x12g\n\x0eSetRoiLocation\x12(.mavsdk.rpc.gimbal.SetRoiLocationRequest\x1a).mavsdk.rpc.gimbal.SetRoiLocationResponse\"\x00\x42\x1f\n\x10io.mavsdk.gimbalB\x0bGimbalProtob\x06proto3'
)

_GIMBALMODE = _descriptor.EnumDescriptor(
  name='GimbalMode',
  full_name='mavsdk.rpc.gimbal.GimbalMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GIMBAL_MODE_YAW_FOLLOW', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GIMBAL_MODE_YAW_LOCK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=707,
  serialized_end=773,
)
_sym_db.RegisterEnumDescriptor(_GIMBALMODE)

GimbalMode = enum_type_wrapper.EnumTypeWrapper(_GIMBALMODE)
GIMBAL_MODE_YAW_FOLLOW = 0
GIMBAL_MODE_YAW_LOCK = 1


_GIMBALRESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.gimbal.GimbalResult.Result',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_TIMEOUT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNSUPPORTED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=595,
  serialized_end=705,
)
_sym_db.RegisterEnumDescriptor(_GIMBALRESULT_RESULT)


_SETPITCHANDYAWREQUEST = _descriptor.Descriptor(
  name='SetPitchAndYawRequest',
  full_name='mavsdk.rpc.gimbal.SetPitchAndYawRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pitch_deg', full_name='mavsdk.rpc.gimbal.SetPitchAndYawRequest.pitch_deg', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaw_deg', full_name='mavsdk.rpc.gimbal.SetPitchAndYawRequest.yaw_deg', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=101,
)


_SETPITCHANDYAWRESPONSE = _descriptor.Descriptor(
  name='SetPitchAndYawResponse',
  full_name='mavsdk.rpc.gimbal.SetPitchAndYawResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gimbal_result', full_name='mavsdk.rpc.gimbal.SetPitchAndYawResponse.gimbal_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=183,
)


_SETMODEREQUEST = _descriptor.Descriptor(
  name='SetModeRequest',
  full_name='mavsdk.rpc.gimbal.SetModeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gimbal_mode', full_name='mavsdk.rpc.gimbal.SetModeRequest.gimbal_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=253,
)


_SETMODERESPONSE = _descriptor.Descriptor(
  name='SetModeResponse',
  full_name='mavsdk.rpc.gimbal.SetModeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gimbal_result', full_name='mavsdk.rpc.gimbal.SetModeResponse.gimbal_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=328,
)


_SETROILOCATIONREQUEST = _descriptor.Descriptor(
  name='SetRoiLocationRequest',
  full_name='mavsdk.rpc.gimbal.SetRoiLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude_deg', full_name='mavsdk.rpc.gimbal.SetRoiLocationRequest.latitude_deg', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude_deg', full_name='mavsdk.rpc.gimbal.SetRoiLocationRequest.longitude_deg', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitude_m', full_name='mavsdk.rpc.gimbal.SetRoiLocationRequest.altitude_m', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=330,
  serialized_end=418,
)


_SETROILOCATIONRESPONSE = _descriptor.Descriptor(
  name='SetRoiLocationResponse',
  full_name='mavsdk.rpc.gimbal.SetRoiLocationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gimbal_result', full_name='mavsdk.rpc.gimbal.SetRoiLocationResponse.gimbal_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=500,
)


_GIMBALRESULT = _descriptor.Descriptor(
  name='GimbalResult',
  full_name='mavsdk.rpc.gimbal.GimbalResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.gimbal.GimbalResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.gimbal.GimbalResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GIMBALRESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=705,
)

_SETPITCHANDYAWRESPONSE.fields_by_name['gimbal_result'].message_type = _GIMBALRESULT
_SETMODEREQUEST.fields_by_name['gimbal_mode'].enum_type = _GIMBALMODE
_SETMODERESPONSE.fields_by_name['gimbal_result'].message_type = _GIMBALRESULT
_SETROILOCATIONRESPONSE.fields_by_name['gimbal_result'].message_type = _GIMBALRESULT
_GIMBALRESULT.fields_by_name['result'].enum_type = _GIMBALRESULT_RESULT
_GIMBALRESULT_RESULT.containing_type = _GIMBALRESULT
DESCRIPTOR.message_types_by_name['SetPitchAndYawRequest'] = _SETPITCHANDYAWREQUEST
DESCRIPTOR.message_types_by_name['SetPitchAndYawResponse'] = _SETPITCHANDYAWRESPONSE
DESCRIPTOR.message_types_by_name['SetModeRequest'] = _SETMODEREQUEST
DESCRIPTOR.message_types_by_name['SetModeResponse'] = _SETMODERESPONSE
DESCRIPTOR.message_types_by_name['SetRoiLocationRequest'] = _SETROILOCATIONREQUEST
DESCRIPTOR.message_types_by_name['SetRoiLocationResponse'] = _SETROILOCATIONRESPONSE
DESCRIPTOR.message_types_by_name['GimbalResult'] = _GIMBALRESULT
DESCRIPTOR.enum_types_by_name['GimbalMode'] = _GIMBALMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetPitchAndYawRequest = _reflection.GeneratedProtocolMessageType('SetPitchAndYawRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPITCHANDYAWREQUEST,
  '__module__' : 'gimbal.gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetPitchAndYawRequest)
  })
_sym_db.RegisterMessage(SetPitchAndYawRequest)

SetPitchAndYawResponse = _reflection.GeneratedProtocolMessageType('SetPitchAndYawResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPITCHANDYAWRESPONSE,
  '__module__' : 'gimbal.gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetPitchAndYawResponse)
  })
_sym_db.RegisterMessage(SetPitchAndYawResponse)

SetModeRequest = _reflection.GeneratedProtocolMessageType('SetModeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETMODEREQUEST,
  '__module__' : 'gimbal.gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetModeRequest)
  })
_sym_db.RegisterMessage(SetModeRequest)

SetModeResponse = _reflection.GeneratedProtocolMessageType('SetModeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETMODERESPONSE,
  '__module__' : 'gimbal.gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetModeResponse)
  })
_sym_db.RegisterMessage(SetModeResponse)

SetRoiLocationRequest = _reflection.GeneratedProtocolMessageType('SetRoiLocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETROILOCATIONREQUEST,
  '__module__' : 'gimbal.gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetRoiLocationRequest)
  })
_sym_db.RegisterMessage(SetRoiLocationRequest)

SetRoiLocationResponse = _reflection.GeneratedProtocolMessageType('SetRoiLocationResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETROILOCATIONRESPONSE,
  '__module__' : 'gimbal.gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetRoiLocationResponse)
  })
_sym_db.RegisterMessage(SetRoiLocationResponse)

GimbalResult = _reflection.GeneratedProtocolMessageType('GimbalResult', (_message.Message,), {
  'DESCRIPTOR' : _GIMBALRESULT,
  '__module__' : 'gimbal.gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.GimbalResult)
  })
_sym_db.RegisterMessage(GimbalResult)


DESCRIPTOR._options = None

_GIMBALSERVICE = _descriptor.ServiceDescriptor(
  name='GimbalService',
  full_name='mavsdk.rpc.gimbal.GimbalService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=776,
  serialized_end=1085,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetPitchAndYaw',
    full_name='mavsdk.rpc.gimbal.GimbalService.SetPitchAndYaw',
    index=0,
    containing_service=None,
    input_type=_SETPITCHANDYAWREQUEST,
    output_type=_SETPITCHANDYAWRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetMode',
    full_name='mavsdk.rpc.gimbal.GimbalService.SetMode',
    index=1,
    containing_service=None,
    input_type=_SETMODEREQUEST,
    output_type=_SETMODERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetRoiLocation',
    full_name='mavsdk.rpc.gimbal.GimbalService.SetRoiLocation',
    index=2,
    containing_service=None,
    input_type=_SETROILOCATIONREQUEST,
    output_type=_SETROILOCATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GIMBALSERVICE)

DESCRIPTOR.services_by_name['GimbalService'] = _GIMBALSERVICE

# @@protoc_insertion_point(module_scope)
