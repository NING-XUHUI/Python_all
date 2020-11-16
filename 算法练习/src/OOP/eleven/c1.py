# 枚举

from enum import Enum
from enum import IntEnum,unique

@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class VIP2(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.YELLOW.value)
print(type(VIP.GREEN))
print(VIP['GREEN'])

# for v in VIP:
#     print(v)

if VIP.GREEN == 2:
    print("a")

for v in VIP.__members__.items():
    print(v)

