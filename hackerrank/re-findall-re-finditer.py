# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
import re
s = '\n'.join(re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', input()))
print(s if s else -1)
