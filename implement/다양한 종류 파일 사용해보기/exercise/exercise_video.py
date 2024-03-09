import cv2 # pip install opencv-python

# 동영상 파일을 엽니다.
cap = cv2.VideoCapture('../assets/kitten_video.mp4')

# 동영상이 정상적으로 열렸는지 확인합니다.
if cap.isOpened():
    while True:
        # 동영상에서 프레임을 하나씩 읽습니다.
        ret, frame = cap.read()
        # 읽은 프레임이 없으면 종료합니다. (동영상의 끝)
        if not ret:
            break
        
        # 읽은 프레임을 화면에 표시합니다.
        cv2.imshow('frame', frame)
        
        # 'q' 키를 누르면 재생을 중지합니다.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 자원을 해제하고 윈도우를 모두 닫습니다.
cap.release()
cv2.destroyAllWindows()