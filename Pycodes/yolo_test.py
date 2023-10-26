import os
from ultralytics import YOLO
import copy
import f_yolov8 as v8
import cv2
import numpy as np

# 폴더 경로 설정
folder_paths = '/Users/leejungbin/Desktop/codes/Deepi/pyenv/sample_pics/'
src = ['/Users/leejungbin/Desktop/codes/Deepi/pyenv/sample_pics/Unknown.jpeg']

# 폴더 내 .jpeg 파일 경로 수집
paths = os.listdir(folder_paths)
for path in paths:
    if path.endswith(('.jpeg')):
        src.append(os.path.join(folder_paths, path))

# YOLO 모델 초기화
model = YOLO('./weights/yolov8n-seg.pt')

# 각 이미지에 대해 예측 및 결과 처리
results = model(
    source=src[0],
    save=True,
    save_txt=True,
    save_crop=True,
    project='project',
    name='name'
)

# 예측 결과 가져오기
result = results[0]

# 객체 탐지 및 세그멘테이션 결과 처리
d_img1, Segmentations = v8.inference(result)  # Segmentation

# 객체 세그멘테이션 정보 추출
segmentation_data = Segmentations['pol']
class_indices = Segmentations['class']

# 객체 별로 세그멘테이션 마스크 생성
segmentation_masks = []
for i in range(len(segmentation_data)):
    polygon_points = segmentation_data[i]  # 객체의 다각형 점 좌표
    class_index = class_indices[i]  # 객체의 클래스 인덱스
    
    # 클래스 별로 다른 색상 사용 (예: 클래스 0은 빨간색, 클래스 1은 파란색 등)
    color = (0, 0, 255) if class_index == 0 else (0, 255, 0)  # 여기서는 클래스 0과 1에 대해 빨간색과 녹색 사용
    
    # 이미지 크기와 같은 빈 마스크 생성
    height, width = d_img1.shape[:2]
    mask = np.zeros((height, width, 3), dtype=np.uint8)
    
    # 객체의 다각형을 마스킹
    cv2.fillPoly(mask, [np.array(polygon_points, dtype=np.int32)], color)
    
    segmentation_masks.append(mask)

# 세그멘테이션된 객체를 합친다
segmentation_result = np.zeros((height, width, 3), dtype=np.uint8)
for mask in segmentation_masks:
    segmentation_result = cv2.add(segmentation_result, mask)

# 세그멘테이션 결과 이미지 표시
cv2.imshow('Segmentation Result', segmentation_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
