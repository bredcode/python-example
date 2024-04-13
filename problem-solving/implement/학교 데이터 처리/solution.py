with open('./data.csv') as file:
  students = []
  # 1. csv 파일을 불러와 리스트에 저장한다
  for line in file.readlines():
    # 이때 각 리스트별 마지막 줄에 개행(\n)은 제거한다.
    line = line.replace("\n","")
    # 2. 각 리스트별 문자열을 리스트로 변환한다.
    line = line.split(",")
    students.append(line)


  studentB = []
  totalB = []
  for student in students:
    # 3. 지역코드가 B인 자료에 대해
    if student[-1] == "B":
      studentB.append(student)
      # '국어+영어'의 결과로
      totalB.append(int(student[2]) + int(student[3]))
  
  # 내림차순 정렬했을 때
  totalB = list(reversed(sorted(totalB)))
  # 다섯 번째 학번을 출력
  for student in studentB:
    if int(student[2]) + int(student[3]) == totalB[4]:
      print(student[0])


  count = 0
  for student in students:
    # 성취도가 A 또는 B인 자료에 대해
    if student[-2] == "A" or student[-2] == "B":
      # 총점이 200점 이상인 학생 중
      if int(student[-4]) >= 200:
        # 이름이 팰린드롬으로 구성 된 학생이 몇명인지 구하시오
        if student[1] == student[1][::-1]:
          count+=1
  print(count)

  
  

  
  