from ultralytics import YOLO

# Load a model
model = YOLO('/Users/leejungbin/Desktop/codes/Deepi/weights/yolov8n.pt')  # pretrained YOLOv8n model


# return a list of Results objects
image_paths = ['/Users/leejungbin/Desktop/codes/Deepi/pyenv/sample_pics/office.jpeg', '/Users/leejungbin/Desktop/codes/Deepi/pyenv/sample_pics/people_in.jpeg']
# results = model(image_paths, stream= True) # return a list of Results objects
result = model.predict(image_paths, save=True, imgsz=320, conf=0.5)

# Process results list
for result in result:
    boxes = result.boxes.xyxy  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    names = model.names

    
    clist= result[0].boxes.cls
    cls = set()
    for cno in clist:
        cls.add(model.names[int(cno)])

    print(cls)



