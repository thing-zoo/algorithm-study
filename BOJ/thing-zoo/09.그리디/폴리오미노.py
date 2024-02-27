board = input()
answer = board.replace('XXXX', 'AAAA')
answer = answer.replace('XX', 'BB')
print(answer if 'X' not in answer else -1)