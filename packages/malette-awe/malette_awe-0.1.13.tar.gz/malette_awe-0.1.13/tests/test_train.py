import json
input1 = """{
  "success": true,
  "total_files": 8,
  "success_count": 8,
  "failed_count": 0,
  "bucket": "industryai",
  "endpoint": "oss-cn-beijing.aliyuncs.com",
  "domain": "oss-cn-beijing.aliyuncs.com",
  "make_public": false,
  "results": [
    {
      "success": true,
      "index": 0,
      "object_key": "ddesignpro/flux-lora-train/lora_1753761253.png",
      "etag": "09AE83695B746189B684847A3F1A921F",
      "request_id": "688845E57AB4F03838BB76C6",
      "content_type": "image/png",
      "size": 1376532,
      "oss_url": "ddesignpro/flux-lora-train/lora_1753761253.png",
      "public_url": "http://industryai.oss-cn-beijing.aliyuncs.com/ddesignpro%2Fflux-lora-train%2Flora_1753761253.png?OSSAccessKeyId=LTAI5tCv9DpB7gYic1oGsAyv&Expires=1753764855&Signature=1U1r8cTP1VYEc7WW67iCZlTmCZU%3D",
      "type": "image"
    },
    {
      "success": true,
      "index": 1,
      "object_key": "ddesignpro/flux-lora-train/lora_1753761255.png",
      "etag": "34131193560049065BF63751A0013781",
      "request_id": "688845E77AB4F038384A85C6",
      "content_type": "image/png",
      "size": 1359114,
      "oss_url": "ddesignpro/flux-lora-train/lora_1753761255.png",
      "public_url": "http://industryai.oss-cn-beijing.aliyuncs.com/ddesignpro%2Fflux-lora-train%2Flora_1753761255.png?OSSAccessKeyId=LTAI5tCv9DpB7gYic1oGsAyv&Expires=1753764856&Signature=gbPJ1jNfsh6xVI3Gf0ahpRRrzxw%3D",
      "type": "image"
    },
    {
      "success": true,
      "index": 2,
      "object_key": "ddesignpro/flux-lora-train/lora_1753761256.png",
      "etag": "EBAF438B45410BA990D2B850976C416B",
      "request_id": "688845E97AB4F038382191C6",
      "content_type": "image/png",
      "size": 1319964,
      "oss_url": "ddesignpro/flux-lora-train/lora_1753761256.png",
      "public_url": "http://industryai.oss-cn-beijing.aliyuncs.com/ddesignpro%2Fflux-lora-train%2Flora_1753761256.png?OSSAccessKeyId=LTAI5tCv9DpB7gYic1oGsAyv&Expires=1753764858&Signature=%2BzV7jndGMyWQImxwvfOeW%2BOxdN8%3D",
      "type": "image"
    },
    {
      "success": true,
      "index": 3,
      "object_key": "ddesignpro/flux-lora-train/lora_1753761258.png",
      "etag": "12FF4126B1F05132A437F5C0A0C1637A",
      "request_id": "688845EA7AB4F03838439FC6",
      "content_type": "image/png",
      "size": 1475810,
      "oss_url": "ddesignpro/flux-lora-train/lora_1753761258.png",
      "public_url": "http://industryai.oss-cn-beijing.aliyuncs.com/ddesignpro%2Fflux-lora-train%2Flora_1753761258.png?OSSAccessKeyId=LTAI5tCv9DpB7gYic1oGsAyv&Expires=1753764860&Signature=J%2FYU0e3Joy4Wo8pkLiEjo6gk5TM%3D",
      "type": "image"
    },
    {
      "success": true,
      "index": 0,
      "object_key": "ddesignpro/flux-lora-train/lora_1753761260.safetensors",
      "etag": "DDEEF7151A9800919D763EBBCAC93595",
      "request_id": "688845EC7AB4F03838A0ABC6",
      "content_type": "",
      "size": 153272016,
      "oss_url": "ddesignpro/flux-lora-train/lora_1753761260.safetensors",
      "public_url": "http://industryai.oss-cn-beijing.aliyuncs.com/ddesignpro%2Fflux-lora-train%2Flora_1753761260.safetensors?OSSAccessKeyId=LTAI5tCv9DpB7gYic1oGsAyv&Expires=1753764972&Signature=%2BWHLvORgi8NzAPo5gprKBaW9lTk%3D",
      "type": "file"
    },
    {
      "success": true,
      "index": 1,
      "object_key": "ddesignpro/flux-lora-train/lora_1753761372.safetensors",
      "etag": "D441210FD4F60DF9CC6F49E6DB723568",
      "request_id": "6888465C7AB4F038385DACCA",
      "content_type": "",
      "size": 153272016,
      "oss_url": "ddesignpro/flux-lora-train/lora_1753761372.safetensors",
      "public_url": "http://industryai.oss-cn-beijing.aliyuncs.com/ddesignpro%2Fflux-lora-train%2Flora_1753761372.safetensors?OSSAccessKeyId=LTAI5tCv9DpB7gYic1oGsAyv&Expires=1753765051&Signature=A2fh05VVjtNXLhZf3G3H6AJiayc%3D",
      "type": "file"
    },
    {
      "success": true,
      "index": 2,
      "object_key": "ddesignpro/flux-lora-train/lora_1753761451.safetensors",
      "etag": "8FFE44EF5DE08F7C8F1A0DC79CEDCE26",
      "request_id": "688846AB7AB4F03838C56DCD",
      "content_type": "",
      "size": 153272016,
      "oss_url": "ddesignpro/flux-lora-train/lora_1753761451.safetensors",
      "public_url": "http://industryai.oss-cn-beijing.aliyuncs.com/ddesignpro%2Fflux-lora-train%2Flora_1753761451.safetensors?OSSAccessKeyId=LTAI5tCv9DpB7gYic1oGsAyv&Expires=1753765137&Signature=%2BC9tXMXdAzjIUBGJo5LL2meYF8U%3D",
      "type": "file"
    },
    {
      "success": true,
      "index": 3,
      "object_key": "ddesignpro/flux-lora-train/lora_1753761537.safetensors",
      "etag": "EF7B3EB9E7F88445D331BCE9ECA12349",
      "request_id": "688847017AB4F03838A16BD0",
      "content_type": "",
      "size": 153272016,
      "oss_url": "ddesignpro/flux-lora-train/lora_1753761537.safetensors",
      "public_url": "http://industryai.oss-cn-beijing.aliyuncs.com/ddesignpro%2Fflux-lora-train%2Flora_1753761537.safetensors?OSSAccessKeyId=LTAI5tCv9DpB7gYic1oGsAyv&Expires=1753765220&Signature=f95s2vjnTiEx%2FdXIuVonCCGAfOQ%3D",
      "type": "file"
    }
  ]
}"""
input2 = """[
  "0.27611368894577026",
  "0.2764444053173065",
  "0.2533600330352783",
  "0.5105385184288025"
]"""
input3 = """["smRmhcotBg/lora_rank16_bf16-step00008.safetensors", "smRmhcotBg/lora_rank16_bf16-step00016.safetensors", "smRmhcotBg/lora_rank16_bf16-step00024.safetensors", "smRmhcotBg/lora_rank16_bf16-step00032.safetensors"]"""

def transform_upload_result(upload_data, local_file_paths):
    """
    将OSS上传结果转换为按LoRA文件分组的结构
    
    Args:
        upload_data: 原始上传结果数据（dict或JSON字符串）
    
    Returns:
        dict: 转换后的数据结构
    """
    
    # 检查数据有效性
    if not upload_data.get('success', False) or not upload_data.get('results'):
        return {
            "success": False,
            "data": []
        }
    
    results = upload_data['results']
    
    # 分离图片文件和LoRA文件
    image_files = [item for item in results if item.get('type') == 'image']
    lora_files = [item for item in results if item.get('type') == 'file' and 
                  item.get('object_key', '').endswith('.safetensors')]
    
    # 构建转换后的数据
    data = []
    
    # 按LoRA文件分组
    index = -1
    for lora_file in lora_files:
        index += 1
        # 根据 index 获取对应的本地文件路径
        local_file_path = local_file_paths[index]

        lora_item = {
            "loraFilePath": lora_file.get('oss_url', ''),
            "loraFileUrl": lora_file.get('public_url', ''),
            "localFilePath": local_file_path,
            "size": lora_file.get('size', 0),
            "images": []
        }
        
        # 为每个LoRA文件添加对应的图片
        # 这里使用简单的索引对应关系，你可以根据实际需求调整匹配逻辑
        lora_index = lora_file.get('index', 0)
        
        # 找到对应索引的图片文件
        matching_images = [img for img in image_files if img.get('index') == lora_index]
        
        for image in matching_images:
            image_item = {
                "imageFilePath": image.get('oss_url', ''),
                "imageFileUrl": image.get('public_url', '')
            }
            lora_item["images"].append(image_item)
        
        data.append(lora_item)
    
    return {
        "success": True,
        "data": {
          "loras": data,
          "loss": []
        }
    }

try:
  input3 = json.loads(input3)
except Exception as e:
  print("not json")
  input3 = input3.strip().split('\n')

output = transform_upload_result(json.loads(input1), input3)
output['data']['loss'] = json.loads(input2)


print(json.dumps(output, indent=2))