import re

result = re.fullmatch(".*Motor_Control", "PDU_Motor_Control")

if result:
    print(result.string)