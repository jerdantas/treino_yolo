from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(data='/home/dantas/VA/treino_yolo/and/data.yaml', epochs=40)
results = model.val()  # evaluate model performance on the validation set

pred = input('Predict')
results = model("/home/dantas/and_project/AND/AND/images/2112-00086.png")  # predict on an image

print(results)