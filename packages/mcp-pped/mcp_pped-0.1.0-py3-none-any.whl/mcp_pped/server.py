from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction
import cv2
from IPython.display import Image
from mcp.server.fastmcp.server import FastMCP
import math
import json
mcp = FastMCP("PPEDet")
# 算术工具组
@mcp.tool()

def PPED(src: str) -> str:
    """执行个人防护检测"""
    model_path = "best.pt"
    # imge = "test_img/6.jpg"

    detection_model = AutoDetectionModel.from_pretrained(
        model_type="ultralytics",
        model_path=model_path,
        confidence_threshold=0.15,
        device="cuda:0",  # or 'cuda:0'
    )

    img = src

    result = get_sliced_prediction(
        img,
        detection_model,
        slice_height=256,
        slice_width=256,
        overlap_height_ratio=0.2,
        overlap_width_ratio=0.2,
    )

    resultliet = []
    object_prediction_list = result.object_prediction_list
    for i in object_prediction_list:
        print()
        resultliet.append({"bbox": i.bbox.box, "mask": i.mask, "score": i.score.value, "name": i.category.name})
    result_str = json.dumps(resultliet, ensure_ascii=False)

    # result.export_visuals(export_dir="./")
    #images = Image("result.jpg")


    return result_str





if __name__ == "__main__":
    #print("start")
    mcp.run(transport="stdio")