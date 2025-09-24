input1 = """/home/admin/workspace/aop_lab/smRmhcotBg/lora_rank16_bf16-step00008.safetensors
/home/admin/workspace/aop_lab/smRmhcotBg/lora_rank16_bf16-step00016.safetensors
/home/admin/workspace/aop_lab/smRmhcotBg/lora_rank16_bf16-step00024.safetensors
/home/admin/workspace/aop_lab/smRmhcotBg/lora_rank16_bf16-step00032.safetensors"""

input2 = "smRmhcotBg"

import json

def extract_relative_file_paths(file_paths, folder_name):
    """
    提取相对于指定文件夹的文件路径
    
    Args:
        file_paths: 多行字符串，每行是一个完整的文件路径
        folder_name: 目标文件夹名称
    
    Returns:
        list: 相对于目标文件夹的文件路径列表
    """
    relative_paths = []
    for line in file_paths.strip().split('\n'):
        if folder_name in line:
            relative_path = line.split(folder_name + '/')[-1]
            relative_paths.append(f"{folder_name}/{relative_path}")
        else:
            relative_paths.append(line)  # 如果不包含folder_name，则保持原样
    return json.dumps(relative_paths)

output = extract_relative_file_paths(input1, input2)
print(output) 