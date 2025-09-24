import json
from operator import contains
import traceback
from typing import Optional, Dict, Any, List
from alibabacloud_eci20180808.client import Client as EciClient
from alibabacloud_eci20180808.models import (
    CreateContainerGroupRequest,
    DescribeContainerGroupsRequest,
    CreateContainerGroupRequestContainer,
    CreateContainerGroupRequestImageRegistryCredential,
    CreateContainerGroupRequestTag,
    CreateContainerGroupRequest,
)
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models
from pixelarraylib.monitor.feishu import Feishu

feishu_alert = Feishu("devtoolkit服务报警")


class ECIUtils:
    def __init__(self, region_id: str, access_key_id: str, access_key_secret: str):
        """
        description:
            初始化ECI工具类
        parameters:
            region_id(str): 地域ID
            access_key_id(str): 访问密钥ID
            access_key_secret(str): 访问密钥Secret
        """
        self.region_id = region_id
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.client = self._create_client()

    def _create_client(self) -> EciClient:
        """
        description:
            创建ECI客户端
        return:
            EciClient: ECI客户端实例
        """
        config = open_api_models.Config(
            access_key_id=self.access_key_id,
            access_key_secret=self.access_key_secret,
            region_id=self.region_id,
            endpoint=f"eci.{self.region_id}.aliyuncs.com",
        )
        return EciClient(config)

    def create_container_group(
        self,
        container_group_name: str,
        acr_region_id: str,
        acr_credentials: Dict,
        images: List[Dict[str, Any]],
        instance_type: str = "ecs.c1.small",
        zone_id: str = "a",
        restart_policy: str = "Always",
    ):
        """
        description:
            创建容器组
        parameters:
            container_group_name(str): 容器组名称
            acr_region_id(str): ACR地域ID
            acr_credentials(Dict): ACR凭证
            images(List[Dict[str, Any]]): 镜像列表
            instance_type(str): 实例类型
            zone_id(str): 可用区ID
            restart_policy(str): 重启策略
        return:
            dict: 创建结果
            success(bool): 是否成功
        """
        containers = []
        for image in images:
            container_0 = CreateContainerGroupRequestContainer(
                name=image["repository_name"],
                image=f"pixelarrayai-registry-vpc.{acr_region_id}.cr.aliyuncs.com/{image['namespace_name']}/{image['repository_name']}:latest",
            )
            containers.append(container_0)

        image_registry_credentials = [
            CreateContainerGroupRequestImageRegistryCredential(
                password=acr_credentials["password"],
                server=f"pixelarrayai-registry-vpc.{acr_region_id}.cr.aliyuncs.com",
                user_name=acr_credentials["user_name"],
            )
        ]

        tag_0 = CreateContainerGroupRequestTag(key="team", value="pixelarrayai")
        create_container_group_request = CreateContainerGroupRequest(
            region_id=self.region_id,
            zone_id=f"{self.region_id}-{zone_id}",
            container_group_name=container_group_name,
            restart_policy=restart_policy,
            cpu=1,
            memory=2,
            resource_group_id="rg-acfm3aqovjsymaa",
            dns_policy="Default",
            instance_type=instance_type,
            active_deadline_seconds=600,
            spot_strategy="SpotAsPriceGo",
            host_name="ecitest",
            tag=[tag_0],
            image_registry_credential=image_registry_credentials,
            termination_grace_period_seconds=60,
            container=[container_0],
            auto_match_image_cache=False,
            share_process_namespace=True,
            schedule_strategy="VSwitchOrdered",
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            response = self.client.create_container_group_with_options(
                create_container_group_request, runtime
            )
            return response.body.to_map(), True
        except Exception as error:
            feishu_alert.send(f"创建容器组失败: {error}")
            return {}, False

    def describe_container_group(self, container_group_id: str):
        """
        description:
            查询容器组
        parameters:
            container_group_id(str): 容器组ID
        return:
            dict: 查询结果
        """
        try:
            describe_container_groups_request = DescribeContainerGroupsRequest(
                container_group_id=container_group_id
            )
            runtime = util_models.RuntimeOptions()
            response = self.client.describe_container_groups_with_options(
                describe_container_groups_request, runtime
            )
            return response.body.to_map()
        except Exception as error:
            feishu_alert.send(f"查询容器组失败: {error}")
            return {}

    def list_container_groups(self):
        """
        description:
            查询容器组列表
        parameters:
            None
        return:
            dict: 查询结果
        """
        try:
            list_container_groups_request = ListContainerGroupsRequest()
            runtime = util_models.RuntimeOptions()
            response = self.client.list_container_groups_with_options(
                list_container_groups_request, runtime
            )
            return response.body.to_map()
        except Exception as error:
            feishu_alert.send(f"查询容器组列表失败: {error}")
            return {}
