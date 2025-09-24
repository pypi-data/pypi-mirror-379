import os
from dotenv import load_dotenv
cwd_path = os.getcwd()
print(f'cwd: {cwd_path}')
dotenv_path = f'{cwd_path}/.env'
print(f'dotenv_path: {dotenv_path}')
load_dotenv(dotenv_path=dotenv_path)

from awe.mq.mq_listener import MQListener
from awe.mq.mq_producer import MQProducer
from awe.clients.comfyui_client import ComfyUIClient

class AWE:

  def __init__(self, 
    comfyui_host="",
    comfyui_port="",
  ):
    self.comfyui_host = comfyui_host
    self.comfyui_port = comfyui_port
    os.environ['COMFYUI_HOST'] = f'{comfyui_host}'
    os.environ['COMFYUI_PORT'] = f'{comfyui_port}'

  def start(self):
    # 1. 初始化 ComfyUI Client
    self.comfyui_client = ComfyUIClient(self.comfyui_host, self.comfyui_port)
    self.comfyui_client.connect()
    # 2. 启动 MQ Listener
    self.mq_listener = MQListener(callback=self.comfyui_client.run)
    self.mq_listener.start()
    # 3. 初始化 MQ Producer
    self.mq_producer = MQProducer()
    # 4. 监听 comfyui_client 的 progress 事件
    self.comfyui_client.on_progress(self.mq_producer.send_progress_message)
    # 5. 监听 comfyui_client 的 error 事件
    self.comfyui_client.on_error(self.mq_producer.send_error_message)
    # 6. 监听 comfyui_client 的 complete 事件
    self.comfyui_client.on_complete(self.mq_producer.send_complete_message)
