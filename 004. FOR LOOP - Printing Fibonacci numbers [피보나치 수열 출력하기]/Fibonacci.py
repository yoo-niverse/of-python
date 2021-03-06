''' 피보나치 수열의 공식 : A(3) = A(2) + A(1)'''

i = 1 # 피보나치 수열의 초항 = 1
current = 1 # A(3), 즉 계산하고자 하는 현재 항을 의미
prev = 0 # A(2), 계산하고자 하는 항의 직전 항 의미

while i < 51: # 1에서 50까지 피보나치 수열의 항을 차례로 출력하는 문제 
    i += 1
        # i는 각 항에 대한 numbering을 하는 요소
    print(current)
        # 직전 항과 전전 항의 합으로 구성된 현재 항 current 출력
        
    tmp = prev
        # tmp라는 변수에 이전항의 값을 저장
    prev = current
        # prev(이전) 변수에는 현재 항의 값을 저장
    current = tmp + prev
        # 직전 항(prev)와 전전 항(tmp)의 값을 더하여 새로운 항(current)의 값 계산가능

''' --------- 동작설명 ---------
1. i를 증가시키며 50번째 항까지 동작 수행
2. 가장 초기에는 A(1) = 1 / A(2) = 1로 동작을 시작함
3. tmp 변수는 current의 값을 prev로, prev의 값을 tmp로 옮겨 새로운 current를 계산하기 위한 '임시저장소'용 변수

 --------- 해결에 오랜 시간이 소요된 이유 ---------

 최초시도에서는 tmp 변수를 구상하지 못하고 단순히 이전항(prev)와 최초항(current)만 생각하였음.
 때문에 각 값을 특정 리스트에 저장하여 연산을 수행하려하다보니 코드가 복잡해지고, 오류가 발생하였고
 불현 듯 임시저장소의 필요성을 떠올리며 문제를 해결할 수 있게 되었음. '''
    
    
