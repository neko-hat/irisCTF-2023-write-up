import zlib

target = b'x\x9c\xcb,\xca,N.I\xab.\xc9\xc8,\x8e7,\x8eOIM3\xcc3,1\xce\xa9\x8c7\x89/\xa8,\xc90\xc8\x8bO\xcc)2L\xcf(\xa9\x05\x00\x83\x0c\x10\xf9'

flag = zlib.decompress(target)
print(flag)