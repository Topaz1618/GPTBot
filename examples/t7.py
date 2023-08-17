import paddle
from paddle.vision.transforms import Resize
from paddledet.models import FasterRCNN
from paddledet.datasets import Dataset
from paddledet.transforms import Normalize

# 加载预训练的Faster RCNN模型
model = FasterRCNN()
model.load_state_dict(paddle.load("faster_rcnn_model.pdparams"))

# 加载并预处理图像
image = paddle.vision.imread("output_1.jpg")
transform = paddle.vision.transforms.Compose([
    Resize(target_size=(800, 800)),
    Normalize()
])
image = transform(image)

# 设置模型为评估模式
model.eval()

# 进行表格方框的检测
with paddle.no_grad():
    outputs = model.predict(image.unsqueeze(0))

# 获取检测结果
boxes = outputs[0]['boxes'].numpy()
scores = outputs[0]['scores'].numpy()

# 绘制方框
import cv2
image = cv2.imread("table_image.jpg")
for box in boxes:
    x1, y1, x2, y2 = box
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 显示结果图像
cv2.imshow("Table Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()