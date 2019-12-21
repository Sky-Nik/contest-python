# https://www.hackerrank.com/challenges/security-message-space-and-ciphertext-space/problem
print(''.join(map(lambda c: str((int(c) + 1) % 10), list(input()))))
