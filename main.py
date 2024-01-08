from ultralytics import YOLO

model = YOLO('ultralytics/models/v8/yolov8n.yaml')
model.train(**{'cfg': 'ultralytics/yolo/cfg/default.yaml'})

#model = YOLO('runs/detect/train14/weights/best.pt')
#model.val(name='val_n_wiouv3_DCNall')

#model = YOLO('runs/detect/train6/weights/best.pt')
#model = YOLO('runs/detect/n_wiou_DCN_83.9/weights/best.pt')
#model.predict(source = '/home/yxy/ga/yolov8/ultralytics-main/data/pred', conf = 0.6, name = 'test_n', save_txt = True, save = True, hide_conf = False, line_thickness=1)