
# pip install openxlab #安装

# pip install -U openxlab #版本升级

import os
from dotenv import load_dotenv
load_dotenv()

import openxlab
openxlab.login(ak=os.getenv('Access_Key'), sk=os.getenv('Secret_Key')) #进行登录，输入对应的AK/SK

from openxlab.dataset import info
info(dataset_repo='OpenDriveLab/OpenLane-V2') #数据集信息及文件列表查看

# from openxlab.dataset import get
# get(dataset_repo='OpenDriveLab/OpenLane-V2', target_path='download_dataset')  # 数据集下载

from openxlab.dataset import download
download(dataset_repo='OpenDriveLab/OpenLane-V2',source_path='/README.md', target_path='download_dataset') #数据集文件下载
# download(dataset_repo='OpenDriveLab/OpenLane-V2',source_path='/metafile.yaml', target_path='download_dataset') #数据集文件下载
# download(dataset_repo='OpenDriveLab/OpenLane-V2',source_path='/raw/OpenLane-V2_subset_A_image_0.tar', target_path='download_dataset') #数据集文件下载
# download(dataset_repo='OpenDriveLab/OpenLane-V2',source_path='/raw/OpenLane-V2_subset_A_info-ls.tar', target_path='download_dataset') #数据集文件下载
# download(dataset_repo='OpenDriveLab/OpenLane-V2',source_path='/raw/OpenLane-V2_subset_A_info.tar', target_path='download_dataset') #数据集文件下载
