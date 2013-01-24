# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='login.proto',
  package='pbauth',
  serialized_pb='\n\x0blogin.proto\x12\x06pbauth\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\"\x81\x01\n\rLoginResponse\x12\x30\n\x06status\x18\x01 \x02(\x0e\x32 .pbauth.LoginResponse.StatusType\x12\x0e\n\x06userId\x18\x02 \x01(\x05\".\n\nStatusType\x12\x0b\n\x07SUCCESS\x10\x00\x12\x13\n\x0f\x41\x43\x43OUNT_INVALID\x10\x01')



_LOGINRESPONSE_STATUSTYPE = descriptor.EnumDescriptor(
  name='StatusType',
  full_name='pbauth.LoginResponse.StatusType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ACCOUNT_INVALID', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=159,
  serialized_end=205,
)


_LOGINREQUEST = descriptor.Descriptor(
  name='LoginRequest',
  full_name='pbauth.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='username', full_name='pbauth.LoginRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='password', full_name='pbauth.LoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=23,
  serialized_end=73,
)


_LOGINRESPONSE = descriptor.Descriptor(
  name='LoginResponse',
  full_name='pbauth.LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='pbauth.LoginResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='userId', full_name='pbauth.LoginResponse.userId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOGINRESPONSE_STATUSTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=76,
  serialized_end=205,
)

_LOGINRESPONSE.fields_by_name['status'].enum_type = _LOGINRESPONSE_STATUSTYPE
_LOGINRESPONSE_STATUSTYPE.containing_type = _LOGINRESPONSE;
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE

class LoginRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGINREQUEST
  
  # @@protoc_insertion_point(class_scope:pbauth.LoginRequest)

class LoginResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGINRESPONSE
  
  # @@protoc_insertion_point(class_scope:pbauth.LoginResponse)

# @@protoc_insertion_point(module_scope)