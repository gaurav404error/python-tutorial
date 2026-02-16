f = open("test.txt", 'w')

print('File Name: ', f.name)

print('File Mode: ', f.mode)

print('Is file readable: ', f.readable())

print('Is file Writable: ', f.writable())

print('Is file closed: ', f.closed)

f.close()

print('Is file closed: ', f.closed)

print("")