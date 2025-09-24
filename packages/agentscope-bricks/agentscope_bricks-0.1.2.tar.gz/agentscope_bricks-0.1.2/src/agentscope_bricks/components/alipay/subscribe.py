# -*- coding: utf-8 -*-
import os
from typing import Any, Optional
from pydantic import BaseModel, Field
from agentscope_bricks.base.component import Component
from agentscope_bricks.utils.logger_util import logger
from agentscope_bricks.components.alipay.base import (
    X_AGENT_CHANNEL,
    _create_alipay_client,
    AlipayAipaySubscribeStatusCheckRequest,
    AlipayAipaySubscribePackageInitializeRequest,
    AlipayAipaySubscribeTimesSaveRequest,
    AlipayAipaySubscribeStatusCheckResponse,
    AlipayAipaySubscribePackageInitializeResponse,
    AlipayAipaySubscribeTimesSaveResponse,
)

# 订阅计划id - 研发者在支付宝管理的订阅计划
SUBSCRIBE_PLAN_ID = os.getenv("SUBSCRIBE_PLAN_ID", "")
# 智能体名称 - 用于标识AI智能体名称
X_AGENT_NAME = os.getenv("X_AGENT_NAME", "")
# 订阅使用次数 - 用于服务提供后扣减次数设置，不设置默认为1
USE_TIMES = os.getenv("USE_TIMES", 1)


class SubscribeStatusCheckInput(BaseModel):
    """subscribe status check input schema."""

    uuid: str = Field(
        ...,
        description="账户ID",
    )


class SubscribeStatusOutput(BaseModel):
    """subscribe status check output schema."""

    subscribe_flag: bool = Field(
        ...,
        description="是否订阅,已订阅为true,否则为false",
    )
    subscribe_package: Optional[str] = Field(
        None,
        description="订阅剩余套餐描述",
    )


class SubscribePackageInitializeInput(BaseModel):
    """subscribe package initialize input schema."""

    uuid: str = Field(
        ...,
        description="账户ID",
    )


class SubscribePackageInitializeOutput(BaseModel):
    """subscribe package initialize output schema."""

    subscribe_url: Optional[str] = Field(
        None,
        description="订阅链接",
    )


class SubscribeTimesSaveInput(BaseModel):
    """subscribe times save input schema."""

    uuid: str = Field(
        ...,
        description="账户ID",
    )
    out_request_no: str = Field(
        ...,
        description="外部订单号，用来计次幂等,防止重复扣减订阅次数",
    )


class SubscribeTimesSaveOutput(BaseModel):
    """subscribe times save output schema."""

    success: bool = Field(
        ...,
        description="计次服务调用是否成功",
    )


class SubscribeCheckOrInitializeInput(BaseModel):
    """subscribe check or initialize input schema."""

    uuid: str = Field(
        ...,
        description="账户ID",
    )


class SubscribeCheckOrInitializeOutput(BaseModel):
    """subscribe check or initialize output schema."""

    subscribe_flag: bool = Field(
        ...,
        description="是否订阅,已订阅为true,否则为false",
    )
    subscribe_url: Optional[str] = Field(
        None,
        description="订阅链接，如果未订阅则返回链接",
    )


class AlipaySubscribeStatusCheck(
    Component[SubscribeStatusCheckInput, SubscribeStatusOutput],
):
    """支付宝订阅状态检查组件

    功能：
    - 判断用户是否为有效会员
    - 返回有效会员的版本信息
    - 包括有效期、剩余次数等

    主要特点：
    - 智能体订阅状态查询

    输入参数类型: SubscribeStatusCheckInput
    输出参数类型: SubscribeStatusOutput

    使用场景：
    智能体订阅付费场景

    """

    name: str = "query-alipay-subscription-status"
    description: str = "查询用户订阅状态及套餐详情"

    async def _arun(
        self,
        args: SubscribeStatusCheckInput,
        **kwargs: Any,
    ) -> SubscribeStatusOutput:
        """检查订阅状态"""
        try:
            if not SUBSCRIBE_PLAN_ID:
                raise ValueError(
                    "订阅配置错误：请设置SUBSCRIBE_PLAN_ID环境变量",
                )
            # 创建支付宝客户端实例
            alipay_client = _create_alipay_client()

            # 创建订阅状态检查请求
            request = AlipayAipaySubscribeStatusCheckRequest()
            biz_content = {
                "uuid": args.uuid,
                "plan_id": SUBSCRIBE_PLAN_ID,
                "channel": X_AGENT_CHANNEL,
            }
            request.biz_content = biz_content
            response_content = alipay_client.execute(request)
            response = AlipayAipaySubscribeStatusCheckResponse()
            response.parse_response_content(response_content)
            if response.is_success:
                is_subscribed = response.data.member_status == "VALID"
                subscribe_package_desc = None

                if is_subscribed and hasattr(
                    response.data,
                    "subscribe_member_info_d_t_o",
                ):
                    info = response.data.subscribe_member_info_d_t_o
                    package_type = info.subscribe_package_type

                    if package_type == "byCount":
                        # 计次套餐：订阅X次，还剩Y次
                        total_times = info.subscribe_times
                        left_times = info.left_times
                        subscribe_package_desc = (
                            f"订阅{total_times}次，还剩{left_times}次"
                        )
                    elif package_type == "byTime":
                        # 时间期限套餐：过期时间后过期
                        expired_date = info.expired_date
                        subscribe_package_desc = f"{expired_date}后过期"
                return SubscribeStatusOutput(
                    subscribe_flag=is_subscribed,
                    subscribe_package=subscribe_package_desc,
                )
            else:
                error_msg = (
                    f"订阅校验API返回错误: "
                    f"{response.sub_code or response.code} - "
                    f"{response.sub_msg or response.msg}"
                )
                logger.error(error_msg)
                return SubscribeStatusOutput(
                    subscribe_flag=False,
                    subscribe_package=None,
                )

        except ImportError:
            logger.error(
                "请安装官方支付宝SDK: pip install alipay-sdk-python",
            )
            return SubscribeStatusOutput(
                subscribe_flag=False,
                subscribe_package=None,
            )
        except Exception as e:
            logger.error(f"检查订阅状态失败: {str(e)}")
            return SubscribeStatusOutput(
                subscribe_flag=False,
                subscribe_package=None,
            )


class AlipaySubscribePackageInitialize(
    Component[
        SubscribePackageInitializeInput,
        SubscribePackageInitializeOutput,
    ],
):
    """支付宝订阅开通组件

    功能：
    - 返回订阅套餐的购买链接
    - 订阅计划的定价配置信息

    主要特点：
    - 智能体订阅开通

    输入参数类型: SubscribePackageInitializeInput
    输出参数类型: SubscribePackageInitializeOutput

    使用场景：
    智能体订阅付费场景

    """

    name: str = "initialize-alipay-subscription-order"
    description: str = "用户发起订阅付费，返回订阅链接"

    async def _arun(
        self,
        args: SubscribePackageInitializeInput,
        **kwargs: Any,
    ) -> SubscribePackageInitializeOutput:
        """发起订阅服务"""
        try:
            if not SUBSCRIBE_PLAN_ID or not X_AGENT_NAME:
                raise ValueError(
                    "订阅配置错误：请设置SUBSCRIBE_PLAN_ID,X_AGENT_NAME环境变量",
                )
            # 创建支付宝客户端实例
            alipay_client = _create_alipay_client()

            # 创建订阅状态检查请求
            request = AlipayAipaySubscribePackageInitializeRequest()
            biz_content = {
                "uuid": args.uuid,
                "plan_id": SUBSCRIBE_PLAN_ID,
                "channel": X_AGENT_CHANNEL,
                "agent_name": X_AGENT_NAME,
            }
            request.biz_content = biz_content
            response_content = alipay_client.execute(request)
            response = AlipayAipaySubscribePackageInitializeResponse()
            response.parse_response_content(response_content)
            if response.is_success:
                return SubscribePackageInitializeOutput(
                    subscribe_url=response.data.subscribe_url,
                )
            else:
                error_msg = (
                    f"订阅初始化API返回错误: "
                    f"{response.sub_code or response.code} - "
                    f"{response.sub_msg or response.msg}"
                )
                logger.error(error_msg)
                return SubscribePackageInitializeOutput(subscribe_url=None)

        except ImportError:
            logger.error(
                "请安装官方支付宝SDK: pip install alipay-sdk-python",
            )
            return SubscribePackageInitializeOutput(subscribe_url=None)
        except Exception as e:
            logger.error(f"发起订阅状态失败: {str(e)}")
            return SubscribePackageInitializeOutput(subscribe_url=None)


class AlipaySubscribeTimesSave(
    Component[
        SubscribeTimesSaveInput,
        SubscribeTimesSaveOutput,
    ],
):
    """支付宝订阅计次组件

    功能：
    - 针对按次付费的计费模式，记录会员用户消耗的使用次数。

    主要特点：
    - 智能体订阅计次

    输入参数类型: SubscribeTimesSaveInput
    输出参数类型: SubscribeTimesSaveOutput

    使用场景：
    智能体订阅计次场景

    """

    name: str = "times-alipay-subscription-consume"
    description: str = "用户使用服务后，记录用户使用消耗的次数"

    async def _arun(
        self,
        args: SubscribeTimesSaveInput,
        **kwargs: Any,
    ) -> SubscribeTimesSaveOutput:
        """发起订阅计次服务"""
        try:
            if not SUBSCRIBE_PLAN_ID:
                raise ValueError(
                    "订阅配置错误：请设置SUBSCRIBE_PLAN_ID环境变量",
                )
            # 创建支付宝客户端实例
            alipay_client = _create_alipay_client()

            # 创建订阅状态检查请求
            request = AlipayAipaySubscribeTimesSaveRequest()
            biz_content = {
                "uuid": args.uuid,
                "plan_id": SUBSCRIBE_PLAN_ID,
                "use_times": USE_TIMES,
                "channel": X_AGENT_CHANNEL,
                "out_request_no": args.out_request_no,
            }
            request.biz_content = biz_content
            response_content = alipay_client.execute(request)
            response = AlipayAipaySubscribeTimesSaveResponse()
            response.parse_response_content(response_content)
            if response.is_success:
                return SubscribeTimesSaveOutput(
                    success=response.data.count_success,
                )
            else:
                error_msg = (
                    f"订阅计次API返回错误: "
                    f"{response.sub_code or response.code} - "
                    f"{response.sub_msg or response.msg}"
                )
                logger.error(error_msg)
                return SubscribeTimesSaveOutput(success=False)

        except ImportError:
            logger.error(
                "请安装官方支付宝SDK: pip install alipay-sdk-python",
            )
            return SubscribeTimesSaveOutput(success=False)
        except Exception as e:
            logger.error(f"发起订阅计次失败: {str(e)}")
            return SubscribeTimesSaveOutput(success=False)


class AlipaySubscribeCheckOrInitialize(
    Component[
        SubscribeCheckOrInitializeInput,
        SubscribeCheckOrInitializeOutput,
    ],
):
    """支付宝订阅检查或初始化组件

    功能：
    - 针对按次付费的计费模式，进行订阅状态检查或初始化。

    主要特点：
    - 提供校验用户状态能力，如果已订阅直接返回状态，如果未订阅返回相关链接

    输入参数类型: SubscribeCheckOrInitializeInput
    输出参数类型: SubscribeCheckOrInitializeOutput

    使用场景：
    智能体订阅检查或初始化场景

    """

    name: str = "alipay_subscribe_check_or_initialize"
    description: str = (
        "检查用户订阅状态，如果已订阅则返回状态，如果未订阅则返回订阅链接"
    )

    async def _arun(
        self,
        args: SubscribeCheckOrInitializeInput,
        **kwargs: Any,
    ) -> SubscribeCheckOrInitializeOutput:
        """检查订阅状态或初始化订阅"""
        try:
            if not SUBSCRIBE_PLAN_ID or not X_AGENT_NAME:
                raise ValueError(
                    "订阅配置错误：请设置SUBSCRIBE_PLAN_ID,X_AGENT_NAME环境变量",
                )
            # 先检查订阅状态
            status_check = AlipaySubscribeStatusCheck()
            status_input = SubscribeStatusCheckInput(
                uuid=args.uuid,
                plan_id=SUBSCRIBE_PLAN_ID,
                channel=X_AGENT_CHANNEL,
            )
            status_output = await status_check._arun(status_input)

            # 如果检查成功且用户已订阅，直接返回状态
            if status_output.subscribe_flag:
                return SubscribeCheckOrInitializeOutput(
                    subscribe_flag=True,
                    subscribe_url=None,
                )

            # 如果未订阅，获取订阅链接
            init_component = AlipaySubscribePackageInitialize()
            init_input = SubscribePackageInitializeInput(
                uuid=args.uuid,
                plan_id=SUBSCRIBE_PLAN_ID,
                channel=X_AGENT_CHANNEL,
                agent_name=X_AGENT_NAME,
            )
            init_result = await init_component._arun(init_input)

            return SubscribeCheckOrInitializeOutput(
                subscribe_flag=False,
                subscribe_url=init_result.subscribe_url,
            )

        except ImportError:
            logger.error(
                "请安装官方支付宝SDK: pip install alipay-sdk-python",
            )
            return SubscribeCheckOrInitializeOutput(
                subscribe_flag=False,
                subscribe_url=None,
            )
        except Exception as e:
            logger.error(f"检查订阅状态或初始化订阅: {str(e)}")
            return SubscribeCheckOrInitializeOutput(
                subscribe_flag=False,
                subscribe_url=None,
            )
