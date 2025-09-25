#!/usr/bin/env python3


import os
import time

from mcp.server.fastmcp import FastMCP


# 创建 MCP 服务器实例
mcp = FastMCP("kbase-mcp-server",
              dependencies=["requests", "ffmpeg-python", "tqdm", "dashscope"])





@mcp.tool()
def fetch_external_data(page_num: int = 1, page_size: int = 20) -> str:
    """
    获取外部数据
    
    参数:
    - page_num: 页码，默认为1
    - page_size: 每页数量，默认为20
    
    返回:
    - API响应结果的字符串形式
    """
    import requests
    
    url = f'https://v2.fangcloud.com/aiapi/knowledgeDataCollect/externaDataCollectpage?_={int(time.time()*1000)}'
    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://v2.fangcloud.com',
        'Pragma': 'no-cache',
        'Referer': 'https://v2.fangcloud.com/console/gather/external',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    # 从环境变量获取API密钥
    kbase_key = os.getenv('KBASE_KEY')
    if not kbase_key:
        raise ValueError("未设置环境变量 KBASE_KEY，请在配置中添加知识库密钥")

    if not isinstance(kbase_key, str):
        # 如果是集合或其他类型，转换为字符串
        kbase_key = str(kbase_key)

    cookies = {
        'cookie': kbase_key
    }
    
    data = {
        "pageNum": page_num,
        "pageSize": page_size
    }
    
    try:
        response = requests.post(url, headers=headers, cookies=cookies, json=data)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"请求失败: {str(e)}"


@mcp.tool()
def push_ai_qa_to_library(question: str, content: str) -> str:
    """
    将AI问答内容推送到知识库

    参数:
    - question: 问题
    - content: 回答内容

    返回:
    - API响应结果的字符串形式
    """
    import requests
    import time

    url = f'https://ask.fangcloud.com/kbase/library/pushAiQaToLibrary?_={int(time.time() * 1000)}'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ask.fangcloud.com',
        'Pragma': 'no-cache',
        'Priority': 'u=1, i',
        'Referer': 'https://ask.fangcloud.com/kbase-web/v4/index/kbase',
        'RequestToken': 'SMSPEwTv0TcWEP6z18EwiNInLrJcIAllygNad0Fp',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'ewogICJpdiIgOiAiYm5Lc281MTVweHMwbGRoNFAzL0xFQT09IiwKICAidmFsdWUiIDogIndOellCeEFMMmRxOVN3TDhQNjVjQXAwZG9USnBzZ0RYd1RYRXVGU2FtN3lIaldodkVKVHRZcWlXRDBNdVdMQUlBbXk2QXhNTXdkVG5BYlhNSlpTN253PT0iLAogICJtYWMiIDogImI1Zjk1ZjhiMTc1ZjVkMzI0MjVmOTZhYWRjMzhjYTc1OGY1YWY3Yzc4N2QwNDQ5OTIzNzVlZTY4ZTk1MzI2MGIiCn0='
    }

    # 从环境变量获取API密钥
    kbase_key = os.getenv('KBASE_KEY')
    if not kbase_key:
        raise ValueError("未设置环境变量 KBASE_KEY，请在配置中添加知识库密钥")

    if not isinstance(kbase_key, str):
        # 如果是集合或其他类型，转换为字符串
        kbase_key = str(kbase_key)

    cookies = {
        'cookie': kbase_key
    }

    library_id = os.getenv('LIBRARY_ID')

    data = {
        "libraryId": library_id,
        "documentId": 0,
        "qaInfo": {
            "question": question,
            "content": content
        }
    }

    try:
        response = requests.post(url, headers=headers, cookies=cookies, json=data)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"请求失败: {str(e)}"


@mcp.tool()
def add_web_data_book(web_url: str, model: int = 2) -> str:
    """
    将网页内容添加到知识库

    参数:
    - web_url: 网页URL
    - model: 模型类型，默认为2

    返回:
    - API响应结果的字符串形式
    """
    import requests
    import time
    import os

    # 生成时间戳
    timestamp = int(time.time() * 1000)
    url = f'https://ask.fangcloud.com/kbase/book/addWebDataBook?_={timestamp}'

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://ask.fangcloud.com',
        'Pragma': 'no-cache',
        'Priority': 'u=1, i',
        'Referer': 'https://ask.fangcloud.com/kbase-web/v4/index/kbase',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    # 从环境变量获取API密钥
    kbase_key = os.getenv('KBASE_KEY')
    if not kbase_key:
        raise ValueError("未设置环境变量 KBASE_KEY，请在配置中添加知识库密钥")

    if not isinstance(kbase_key, str):
        # 如果是集合或其他类型，转换为字符串
        kbase_key = str(kbase_key)

    cookies = {
        'cookie': kbase_key
    }

    library_id = os.getenv('LIBRARY_ID')


    # 请求数据
    data = {
        "webUrl": web_url,
        "model": model,
        "libraryId": library_id
    }


    try:
        response = requests.post(url, headers=headers, cookies=cookies, json=data)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"请求失败: {str(e)}"
    except Exception as e:
        return f"发生错误: {str(e)}"


@mcp.tool()
def push_pdf_link_to_library(pdf_link: str, pdf_file_name: str) -> str:
    """
    根据PDF链接下载PDF文件到知识库

    参数:
    - pdf_link: PDF文件的URL链接
    - pdf_file_name: PDF文件名称

    返回:
    - API响应结果的字符串形式
    """
    import requests
    import time
    import os

    url = f'https://ask.fangcloud.com/kbase/library/pushPdfLinkToLibrary?_={int(time.time() * 1000)}'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ask.fangcloud.com',
        'Pragma': 'no-cache',
        'Priority': 'u=1, i',
        'Referer': 'https://ask.fangcloud.com/kbase-web/v4/index/kbase',
        'RequestToken': 'SMSPEwTv0TcWEP6z18EwiNInLrJcIAllygNad0Fp',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'ewogICJpdiIgOiAiYm5Lc281MTVweHMwbGRoNFAzL0xFQT09IiwKICAidmFsdWUiIDogIndOellCeEFMMmRxOVN3TDhQNjVjQXAwZG9USnBzZ0RYd1RYRXVGU2FtN3lIaldodkVKVHRZcWlXRDBNdVdMQUlBbXk2QXhNTXdkVG5BYlhNSlpTN253PT0iLAogICJtYWMiIDogImI1Zjk1ZjhiMTc1ZjVkMzI0MjVmOTZhYWRjMzhjYTc1OGY1YWY3Yzc4N2QwNDQ5OTIzNzVlZTY4ZTk1MzI2MGIiCn0='
    }

    # 从环境变量获取API密钥
    kbase_key = os.getenv('KBASE_KEY')
    if not kbase_key:
        raise ValueError("未设置环境变量 KBASE_KEY，请在配置中添加知识库密钥")

    if not isinstance(kbase_key, str):
        # 如果是集合或其他类型，转换为字符串
        kbase_key = str(kbase_key)

    cookies = {
        'cookie': kbase_key
    }

    # 如果没有传入library_id，则从环境变量获取

    library_id = os.getenv('LIBRARY_ID')
    if not library_id:
        raise ValueError("未设置环境变量 LIBRARY_ID，请在配置中添加知识库ID")

    data = {
        "pdfLink": pdf_link,
        "pdfFileName": pdf_file_name,
        "libraryId": library_id
    }

    try:
        response = requests.post(url, headers=headers, cookies=cookies, json=data)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"请求失败: {str(e)}"


@mcp.tool()
def push_pdf_link_to_library_local(pdf_link: str, pdf_file_name: str) -> str:
    """
    通过本地工具根据PDF链接下载PDF文件到知识库

    参数:
    - pdf_link: PDF文件的URL链接
    - pdf_file_name: PDF文件名称

    返回:
    - API响应结果的字符串形式
    """
    import requests
    import time
    import os

    url = f'https://ask.fangcloud.com/kbase/library/pushPdfLinkToLibrary?_={int(time.time() * 1000)}'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ask.fangcloud.com',
        'Pragma': 'no-cache',
        'Priority': 'u=1, i',
        'Referer': 'https://ask.fangcloud.com/kbase-web/v4/index/kbase',
        'RequestToken': 'SMSPEwTv0TcWEP6z18EwiNInLrJcIAllygNad0Fp',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'ewogICJpdiIgOiAiYm5Lc281MTVweHMwbGRoNFAzL0xFQT09IiwKICAidmFsdWUiIDogIndOellCeEFMMmRxOVN3TDhQNjVjQXAwZG9USnBzZ0RYd1RYRXVGU2FtN3lIaldodkVKVHRZcWlXRDBNdVdMQUlBbXk2QXhNTXdkVG5BYlhNSlpTN253PT0iLAogICJtYWMiIDogImI1Zjk1ZjhiMTc1ZjVkMzI0MjVmOTZhYWRjMzhjYTc1OGY1YWY3Yzc4N2QwNDQ5OTIzNzVlZTY4ZTk1MzI2MGIiCn0='
    }

    # 从环境变量获取API密钥
    kbase_key = ("device_token=0c4be4b62e5c22af69b481e136ea5cb6; __root_domain_v=.fangcloud.com; "
                 "_qddaz=QD.553549197110339; _c_WBKFRo=7bGUYvSfNsAJHOxfvYNeQtvxJPttAq5VkYL43LtB; "
                 "Qs_lvt_389248=1752138520%2C1752231249%2C1757313098; "
                 "Qs_pv_389248=153042335511384480%2C1997181492032253000%2C1340866863378764000; "
                 "Hm_lvt_05713beafc7f9b26f552d1d194d915d2=1757313099; lang=zh-CN; "
                 "Hm_lvt_762d2bc251bef4b42a758268dc7edda3=1756436725,1756799141,1756887504,1758011822; "
                 "HMACCOUNT=7C58F7722482AAD1; is_ai_cloud_enabled=always; "
                 "XSRF-TOKEN=ewogICJpdiIgOiAiWUxHUGRJYUs2ZnNWZDd4TTh2Y3RVZz09IiwKICAidmFsdWUiIDogImNvbW9qUDZvejVhdHdTbmIzcW1ML2tyVVVUajhTNXBhdWZLNnZLZElOaWhGWFBydlAwY1Q1TmhCUTZtNUMxaUFQa3JFSXVGU1c5TjJZNzNrOWZkRC9RPT0iLAogICJtYWMiIDogImM5ZWRiOTNkZDkzYmI3YjU4NTg3ZGQ1YjFhNTRmZjU5OTRlZWUwNGNjYThmMzlkZDkzZDFiNGU1MDM2OTc1ODIiCn0=; Hm_lpvt_762d2bc251bef4b42a758268dc7edda3=1758714399; __DC_sid=99099662.1201538987649830100.1758720140284.705; __DC_monitor_count=20; __DC_gid=99099662.309057045.1747825944390.1758720140660.501; fc_session=eyJpdiI6InF4WTJZajA2XC80SFo2MW93WGRUZzhnPT0iLCJ2YWx1ZSI6InBhYmxxdWd3UG5wRlRkYWhkZWVybzlvYzlvRG9UZ1JsY2kzQ0RQZ1F1a1wvQ3NFZG5RN3ZhcFRick1jZUhxcXp4NEhXeFF3aWJWRzBscytBdDFTVjRTQT09IiwibWFjIjoiZWQxM2RkMDE1ZjdkNTZlZGI0ZTczNzFmNDNjYjkwMGM2OWFhNjgzNDIyNTdmYjM5YzFjNWQxYTNmNDc1MjdhZSJ9; ab_test=1")
    if not kbase_key:
        raise ValueError("未设置环境变量 KBASE_KEY，请在配置中添加知识库密钥")

    if not isinstance(kbase_key, str):
        # 如果是集合或其他类型，转换为字符串
        kbase_key = str(kbase_key)

    cookies = {
        'cookie': kbase_key
    }

    # 如果没有传入library_id，则从环境变量获取

    library_id = "e415104edb9897a3aa4b8223cfc37599"

    data = {
        "pdfLink": pdf_link,
        "pdfFileName": pdf_file_name,
        "libraryId": library_id
    }

    try:
        response = requests.post(url, headers=headers, cookies=cookies, json=data)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"请求失败: {str(e)}"

def main():
    """启动MCP服务器"""
    mcp.run()


if __name__ == "__main__":
    main()