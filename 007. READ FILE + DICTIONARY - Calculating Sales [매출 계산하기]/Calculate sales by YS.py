''' 1개월의 일자별 매출 내역을 통해 월 평균 매출을 계산하는 코드 '''

with open('data/chicken.txt', 'r') as data:
    sum = 0 # 매출 합계 계산을 위한 변수
    days = 0 # 영업일을 counting 하기 위한 변수
    
    for i in data:
        lined = (i.strip()).split()
            # data에서 화이트 스페이스 제거(strip) + 날짜와 가격 분리(split)하여 lined 리스트에 저장
        sum += int(lined[1])
            # 가격만 다 더하여 sum 변수에 총 매출 저장
            # 외부 파일에서 읽어온 데이터는 str 형태이므로, int형으로 casting 해주어야 함.
            # lined[0]에는 해당 매출이 발생한 날짜가, lined[1]에는 해당 일자의 매출이 저장됨.
            
        days += 1
            # 월별 총 날짜 수 계산을 위해 반복문 1회마다 일자 +1 증가
    
    print (sum / days)
        # 평균 매출 : 총 매출 / 영업일

''' ------ 동작 설명 ------
1. 이미 txt 파일로 존재하고 있는 일자별 매출 내역 파일을 불러온다.
2. for문을 통해 한줄씩 입력되어 있는 매출에 대하여 화이트 스페이스 제거 및 내용 분리 작업을 거친다.
3. 분리한 내용에서 매출만 숫자로 변환하여 sum 변수에 저장한다.
4. 최종적인 sum의 값을 영업일로 나누어 계산한다.

 ------ 해결이 오래걸린 이유 ------

 우선 코드가 길어졌던 이유는, (i.strip()).split()와 같이 한번에 실행할 수 있는 내용을
 lined = i.strip() / lined2 = lined.split()와 같이 불필요하게 나누어서 수행했기 때문이다.
 해당 문제는 동시수행이 가능함을 알고 수정했다.

 그리고 어떻게 문제를 해결할 것인지에 대해서는 구상을 완료했지만,
 그것을 구현하는 과정에 있어서 sum 변수에 매출을 전체 더하는 방법에 애를 먹었었다. '''
