phone_book =  ["123","3123"]
def solution(phone_book):
    answer = True
    phone_book.sort() # 숫자대로 정렬
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            return False

    return answer
print(solution(phone_book))