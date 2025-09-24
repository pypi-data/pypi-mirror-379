import hashlib
import json
import os
import sys
import argparse
from typing import Any, Dict, List, Optional
import requests
from mcp.server.fastmcp import FastMCP
from enum import Enum

class ConfigKeys(Enum):
    """环境变量配制键"""
    APP_KEY = "APP_KEY"
    APP_SECRET = "APP_SECRET"
    AMAP_MAPS_API_KEY = "AMAP_MAPS_API_KEY"

class ApiEndpoints(Enum):
    """请求地址"""
    BASEURL = "http://openapi.test.yunzhanxinxi.com"
    #BASEURL = "https://openapi.yunzhanxinxi.com"
    CATEGORY_LIST = "/api/product-square/category"
    GET_PRODUCT_SQUARE_LIST = "/api/product-square/list"

    @staticmethod
    def build_url(path: Enum, params: Dict[str, Any] = None) -> str:
        """构建完整URL"""
        url = f"{ApiEndpoints.BASEURL.value}{path.value}"
        if params:
            param_str = "&".join([f"{key}={value}" for key, value in params.items()])
            url = f"{url}?{param_str}"
        return url

def get_env_variable(env_key: str) -> str:
    """从环境变量获取指定值"""
    env_key = os.getenv(env_key)
    if not env_key:
        raise ValueError(f"{env_key} environment variable is required")
    return env_key

APP_KEY = get_env_variable(ConfigKeys.APP_KEY.value)
APP_SECRET = get_env_variable(ConfigKeys.APP_SECRET.value)
AMAP_MAPS_API_KEY = get_env_variable(ConfigKeys.AMAP_MAPS_API_KEY.value)

mcp = FastMCP("amap-maps")

def get_sign(app_secret: str, params: Dict[str, Any] = None) -> str:
    """
    根据指定规则生成签名

    签名规则:
    1. 将所有参数按键名的字母顺序排序
    2. 拼接参数格式为 key=value，多个参数用&连接
    3. 前后加上app_secret
    4. 进行MD5加密得到签名

    Args:
        app_secret: 应用密钥
        params: 需要签名的参数字典

    Returns:
        str: 签名结果
    """
    if params is None:
        params = {}

    # 复制参数，避免修改原参数
    sign_params = params.copy()

    # 如果存在sign字段，需要移除
    if 'sign' in sign_params:
        del sign_params['sign']

    # 按键名ASCII升序排序
    sorted_keys = sorted(sign_params.keys())

    # 拼接参数字符串
    param_strings = []
    for key in sorted_keys:
        value = sign_params[key]
        # 如果值是字典类型，需要转换为JSON字符串（无空格）
        if isinstance(value, dict):
            value_str = json.dumps(value, separators=(',', ':'), ensure_ascii=False)
        else:
            value_str = str(value)
        param_strings.append(f"{key}={value_str}")

    # 拼接所有参数
    params_str = "&".join(param_strings)

    # 前后加上app_secret
    sign_string = f"{app_secret}{params_str}{app_secret}"

    # MD5加密
    md5_hash = hashlib.md5(sign_string.encode('utf-8'))
    return md5_hash.hexdigest()

@mcp.tool()
def get_category_list()-> Dict[str, Any]:
    """获取所有分类"""
    try:
        # 准备签名参数
        sign_params = {
            "app_key": APP_KEY
            # 可以添加其他需要的参数，如timestamp等
        }
        query_params = {
            "app_key": APP_KEY,
            "sign": get_sign(APP_SECRET, sign_params)
        }
        response = requests.get(
            ApiEndpoints.build_url(ApiEndpoints.CATEGORY_LIST,query_params),
        )
        response.raise_for_status()
        data = response.json()
        if data["code"] != 0:
            return {"error": f"Get category list failed: {data.get('msg') or data.get('status')}"}
        return {
            "list": data.get("data", [])
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_product_square_list(
        category_id: int = 0,
        page_num: int = 1,
        page_size: int = 10,
        sort_name: str = "price",
        sort_type: str = "asc",
        search_text: str = "",
        longitude: str = "",
        latitude: str = "",
        price_floor: int = 0,
        price_cap: int = 0,
        sku_ids: str = ""
) -> Dict[str, Any]:
    """获取选品列表

    Args:
        category_id: 分类ID
        page_num: 页码
        page_size: 每页数量
        sort_name: 排序字段
        sort_type: 排序类型
        search_text: 搜索文本
        longitude: 经度
        latitude: 纬度
        price_floor: 价格下限
        price_cap: 价格上限
        sku_ids: SKU ID列表
    """
    try:
        # 准备请求参数
        request_data = {
            "app_key": APP_KEY,
            "source": 1,
            "platform": 1,
            "bizLine": 0,
            "searchText": search_text,
            "search_id": "",
            "sortName": sort_name,
            "sortType": sort_type,
            "listTopiId": category_id,
            "page": page_num,
            "pageSize": page_size,
            "longitude": longitude,
            "latitude": latitude,
            "priceFloor": price_floor,
            "priceCap": price_cap,
            "skuIds": sku_ids
        }

        # 生成签名（不包含sign字段本身）
        sign_params = request_data.copy()
        request_data["sign"] = get_sign(APP_SECRET, sign_params)

        # 发送POST请求
        url = f"{ApiEndpoints.BASEURL.value}{ApiEndpoints.GET_PRODUCT_SQUARE_LIST.value}"
        response = requests.post(
            url,
            json=request_data  # 使用json参数发送JSON数据
        )
        response.raise_for_status()
        data = response.json()

        if data["code"] != 0:
            return {"error": f"Get product square list failed: {data.get('msg') or data.get('status')}"}

        return {
            "list": data.get("list", []),
            "search_id": data.get("search_id", ""),
            "has_next": data.get("has_next", page_num),
            "page_size": data.get("page_size", page_size)
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Amap MCP Server")
    parser.add_argument('transport', nargs='?', default='streamable-http', choices=['stdio', 'sse', 'streamable-http'],
                        help='Transport type (stdio, sse, or streamable-http)')
    args = parser.parse_args()

    # Run the MCP server with the specified transport
    mcp.run(transport=args.transport)