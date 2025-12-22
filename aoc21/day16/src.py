lines = open("input.txt").read().strip()

hex2bit  = {"0":"0000","1":"0001","2":"0010","3":"0011",
            "4":"0100","5":"0101","6":"0110","7":"0111",
            "8":"1000","9":"1001","A":"1010","B":"1011",
            "C":"1100","D":"1101","E":"1110","F":"1111"}
bits = "".join([hex2bit[h] for h in lines])

def bin2dec(b_string):
    n_bits = len(b_string)
    s = 0
    for i in range(n_bits):
        s+= 2**(n_bits-i-1)*int(b_string[i])
    return s

def parseVersion(bits):
    return bin2dec(bits[:3]),bits[3:]

def parseTypeID(bits):
    return bin2dec(bits[:3]),bits[3:]

def parseNumber(bits):
    b_string = ""
    while bits[0] == "1":
        b_string+=bits[1:5]
        bits =bits[5:]
    b_string += bits[1:5]
    bits = bits[5:]
    return bin2dec(b_string),bits

def parseOperater(type_id,bits):
    sum_version = 0
    nums = []
    if bits[0] == "0":
        n_bits = bin2dec(bits[1:16])
        sub_bits = bits[16:16+n_bits]
        while "1" in sub_bits:
            n,version,sub_bits = parsePacket(sub_bits)
            if n >=0: 
                nums.append(n)
            sum_version+=version
        bits = bits[16+n_bits:]
            
    elif bits[0] == "1":
        n_packets = bin2dec(bits[1:12])
        bits = bits[12:]
        for i in range(n_packets):
            n,version,bits = parsePacket(bits)
            if n >=0: 
                nums.append(n)
            sum_version += version

    match type_id:
        case 0:
            n = sum(nums)
        case 1:
            n = 1
            for x in nums:
                n*=x
        case 2:
            n = min(nums)
        case 3:
            n = max(nums)
        case 5:
            n = nums[0]>nums[1]
        case 6:
            n = nums[0]<nums[1]
        case 7:
            n = nums[0]==nums[1]

    return n,sum_version,bits
    
def parsePacket(bits):
    sum_version = 0
    number = -1
    version_packet,bits= parseVersion(bits)
    sum_version+=version_packet
    type_id, bits = parseTypeID(bits)
   
    if type_id != 4:
        number,version_subpackets,bits = parseOperater(type_id,bits)
        sum_version += version_subpackets
    else:
        number,bits = parseNumber(bits)

    return number,sum_version,bits

ans2,ans1,bits = parsePacket(bits)

print(ans1)
print(ans2)