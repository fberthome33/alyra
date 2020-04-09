import datetime

max_value_four_bytes = bytearray.fromhex("FFFFFFFF");
max_value_four_bytes_int = int.from_bytes(max_value_four_bytes, byteorder='little')



dateRef1970 = datetime.datetime(1970,1,1);
dateMax = dateRef1970 + datetime.timedelta(0, max_value_four_bytes_int);

print("number max sur 4 octets=", max_value_four_bytes_int);
#number max sur 4 octets= 4294967295
print("date max=", str(dateMax));
#date max= 2106-02-07 06:28:15