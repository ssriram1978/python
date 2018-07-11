import os
class open_close_manipulate_files():
    def __init__(self,filename):
        self.filename=filename

    def read_text(self):
        output=[]
        with open(self.filename,mode='r') as f:
            for lines in f:
                print(lines)
                output.append(lines)
        return output

    def read_bytes(self):
        output=[]
        with open(self.filename,mode='rb') as f:
            for lines in f:
                print(lines)
                output.append(lines)
        return output

    def prepare_string_buffer(self,start,end):
        return ','.join([str(x) for x in range(start,end)])

    def write_text(self,start,end):
        string_array=self.prepare_string_buffer(start,end)
        with open(self.filename, mode='w') as f:
            f.write(string_array)

    def write_bytes(self,start,end):
        string_array=self.prepare_string_buffer(start,end)
        with open(self.filename, mode='wb') as f:
            f.write(string_array.encode(encoding='utf-8'))

    def byte_array_manipulation(self,start,end):
        string_array = self.prepare_string_buffer(start, end)
        byte_array=bytearray(string_array.encode(encoding='utf-8'))
        print("byte_array before manipulation={}".format(byte_array))
        byte_array[1]=ord('S')
        byte_array[2] = ord('*')
        print("byte_array after manipulation={}".format(byte_array))

    def example_of_readinto_operation(self):
        data=None
        with open(self.filename, mode='rb') as f:
            for lines in f:
                data = bytearray(os.path.getsize(self.filename))
                f.readinto(data)
        print(data)


print("----------Demonstrating how to open,close and manipulate usage.-----------")
obj5 = open_close_manipulate_files("sriram.txt")
print("obj5.write_text(1,10)")
obj5.write_text(1, 10)
print("obj5.perform_read_operation()")
obj5.read_text()
print("obj5.write_bytes(1,10)")
obj5.write_bytes(1, 10)
print("obj5.perform_read_operation()")
obj5.read_bytes()
print("obj5.example_of_readinto_operation()")
obj5.example_of_readinto_operation()
obj5.byte_array_manipulation(1, 10)
