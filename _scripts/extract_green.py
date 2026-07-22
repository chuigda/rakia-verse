"""从地图图片中抠出绿色区域的轮廓，输出为透明背景 PNG。"""

import sys
import cv2
import numpy as np

def extract_green_contours(input_path: str, output_path: str):
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        print(f"无法读取图片: {input_path}")
        sys.exit(1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 绿色范围 (宽松一点，覆盖图中的绿)
    lower_green = np.array([30, 80, 80])
    upper_green = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # 形态学操作去噪
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    # 找轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 只保留面积较大的轮廓（过滤噪点）
    min_area = 500
    contours = [c for c in contours if cv2.contourArea(c) > min_area]

    # 在透明背景上绘制轮廓
    h, w = img.shape[:2]
    result = np.zeros((h, w, 4), dtype=np.uint8)
    cv2.drawContours(result, contours, -1, (0, 0, 0, 255), 2)

    cv2.imwrite(output_path, result)
    print(f"已保存 {len(contours)} 个轮廓到: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python extract_green.py <输入图片> [输出图片]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "green_contours.png"
    extract_green_contours(input_file, output_file)
