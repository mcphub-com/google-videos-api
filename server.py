import os
import requests
from typing import Union, Literal, Annotated
from mcp.server import FastMCP
from pydantic import Field
from fastmcp import FastMCP
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 创建 MCP 服务器实例
mcp = FastMCP('google-videos-server')

# SerpAPI 配置
SERPAPI_URL = "https://serpapi.com/search?engine=google_videos"
SERPAPI_KEY = os.getenv("SERP_API_KEY")

@mcp.tool()
def search_videos(
    q: Annotated[str, Field(description="搜索查询内容，支持高级语法如 inurl:, site:, intitle: 等" )],
    location: Annotated[Union[str, None], Field(description="Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The location and uule parameters can't be used together. It is recommended to specify location at the city level in order to simulate a real user’s search. If location is omitted, the search may take on the location of the proxy.")] = None,
    tbs: Annotated[Union[str, None], Field(description="高级搜索参数（例如按日期、时长过滤）")] = None,
    safe: Annotated[Union[Literal["active", "off"], None], Field(description="成人内容过滤，'active' 或 'off'")] = "active",
    nfpr: Annotated[Union[int, None], Field(description="是否排除拼写纠正结果（1=是, 0=否）")] = None,
    filter: Annotated[Union[int, None], Field(description="结果过滤（1=启用, 0=禁用）")] = None,
    start: Annotated[Union[int, None], Field(description="分页偏移量（例如 0=第一页, 10=第二页）")] = 0,
    num: Annotated[Union[int, None], Field(description="返回结果数量（10-100）")] = 10,
    device: Annotated[Union[Literal["desktop", "tablet", "mobile"], None], Field(description="设备类型")] = "desktop",
    no_cache: Annotated[Union[bool, None], Field(description="是否禁用缓存")] = False,
    async_mode: Annotated[Union[bool, None], Field(description="是否异步获取结果（需使用 Searches Archive API 获取）")] = False
):
    """
    使用 Google Videos API 搜索视频结果
    返回包含视频标题、链接、缩略图、时长等信息的结构化数据
    """

    if location:
        q = q + ", location: %s"%location
    # 构建请求负载
    payload = {
        'engine': "google_videos",
        'api_key': SERPAPI_KEY,
        'q': q,
        'tbs': tbs,
        'safe': safe,
        'nfpr': nfpr,
        'filter': filter,
        'start': start,
        'num': num,
        'device': device,
        'no_cache': str(no_cache).lower(),
        'async': str(async_mode).lower()
    }
    
    # 移除空值参数
    payload = {k: v for k, v in payload.items() if v is not None}
    
    # 发送请求到 SerpAPI
    response = requests.get(SERPAPI_URL, params=payload)
    response.raise_for_status()  # 检查HTTP错误
    
    return response.json()

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")