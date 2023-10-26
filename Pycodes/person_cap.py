import cv2
from ultralytics import YOLO
import numpy as np

cap = cv2.VideoCapture('/Users/leejungbin/Desktop/codes/Deepi/pyenv/sample_pics/IMG_1562.MOV')

model = YOLO("./weights/yolov8m.pt")

# 파일에 좌표 정보를 저장할 파일명
output_file = 'object_coordinates.txt'

# 텍스트 파일을 쓰기 모드로 열고 파일 핸들을 얻습니다.
with open(output_file, 'w') as file:
    while True:
        # cap.read()를 통해 파일을 불러온다.
        ret, frame = cap.read()
        # ret이 True로 기본 설정이 되어 있고 읽을 동영상의 프레임이 더이상 없을 경우 False로 처리 된다.
        if not ret:
            break
        
        # 동영상의 각 프레임을 학습시킨 결과를 results 안에 넣는다.
        results = model(frame)
        # result는 결과를 가르킨다.
        result = results[0]

        # filtered boxes and classes를 저장하기 위한 리스트를 생성한다.
        filtered_boxes = []
        filtered_classes = []

        # result는 각 프레임에서 탐지된 객체의 결과가 담겨 있는데, 이때 conf(Confidence)를 idx(index), conf(Conficdence)로 가져온다.
        # 즉  result.boxex.conf라는 리스트의 각 원소와 인덱스를 추출한다. 
        for idx, conf in enumerate(result.boxes.conf):
            if conf > 0.5:
                bbox = result.boxes.xyxy[idx] # 
                cls = result.boxes.cls[idx] # 해당 클래스에 매핑된 번호
                name = result.names[cls.item()] # 클래스의 이름을 추출

                (x, y, x2, y2) = bbox
                x, y, x2, y2 = int(x), int(y), int(x2), int(y2)

                filtered_boxes.append((x, y, x2, y2))
                filtered_classes.append(int(cls))


        for (x, y, x2, y2), cls in zip(filtered_boxes, filtered_classes):
            cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 225), 2)
            cv2.putText(frame, name, (x, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 225), 2)

            # 좌표 정보를 텍스트 파일에 기록
            line = f"Object Class: {name}, x: {x}, y: {y}, x2: {x2}, y2: {y2}\n"
            file.write(line)

        cv2.imshow("Img", frame)
        key = cv2.waitKey(1)  # 1ms 대기로 변경하여 비디오가 자동으로 진행
        # 'Esc' 키를 누르면 종료
        if key == 27:
            break

# 파일 핸들을 닫습니다.
file.close()

cap.release()
cv2.destroyAllWindows()
