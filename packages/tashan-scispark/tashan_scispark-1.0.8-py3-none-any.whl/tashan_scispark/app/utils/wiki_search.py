#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/7 14:06
# @Author : 桐
# @QQ:1041264242
# 注意事项：

import json
import re
import time
import logging
import requests
from ..core.config import Proxies

# 配置日志记录器
logger = logging.getLogger(__name__)


# 用于获取Wikipedia上的简介内容
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def get_description(text):
    """
    从搜索结果中提取描述信息
    
    Args:
        text: 搜索结果数据
    
    Returns:
        descriptions: 描述信息列表
    """
    descriptions = []

    try:
        for item in text['search']:
            descriptions.append(item['description'])
        logger.debug(f"成功提取 {len(descriptions)} 个描述")
    except Exception as e:
        logger.warning(f"描述信息为空或提取失败: {str(e)}")

    logger.debug("get_description 完成!")
    return descriptions


def get_wikipedia_intro(entity_data, lang):
    wikipedia_intro = ''
    if 'sitelinks' in entity_data and f'{lang}wiki' in entity_data['sitelinks']:
        wikipedia_title = entity_data['sitelinks'][f'{lang}wiki']['title']
        wikipedia_url = 'https://en.wikipedia.org/w/api.php' if lang == 'en' else 'https://zh.wikipedia.org/w/api.php'
        wikipedia_params = {
            'action': 'query',
            'format': 'json',
            'titles': wikipedia_title,
            'prop': 'extracts',
            'exintro': True,
            'explaintext': True,
            'converttitles': True
        }
        while True:
            try:
                wikipedia_response = requests.get(wikipedia_url, wikipedia_params)
                break
            except requests.exceptions.RequestException as e:
                logger.warning("获取Wikipedia文章内容错误，等待60s后重试...")
                time.sleep(60)

        wikipedia_data = wikipedia_response.json()
        page_id = next(iter(wikipedia_data['query']['pages']))
        wikipedia_intro = wikipedia_data['query']['pages'][page_id]['extract']
        wikipedia_intro = remove_html_tags(wikipedia_intro)
    return wikipedia_intro


def search(query, language='en', limit=3):
    url = "https://www.wikidata.org/w/api.php"

    params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'search': {query},  # 搜索文本
        'language': {language},  # 查询语言（英文）
        'type': 'item',
        'limit': {limit}  # 返回最大数目
    }

    # 访问
    get = requests.get(url=url, params=params, proxies=Proxies)
    # 转为json数据
    re_json = get.json()

    return re_json


def search_detailed(id, language='en'):
    """
    根据实体ID获取详细信息
    
    Args:
        id: 实体ID
        language: 查询语言，默认为英文
    
    Returns:
        re_json: 详细信息的JSON数据
    """
    url = "https://www.wikidata.org/w/api.php"

    params = {
        'ids': {id},  # 实体id,可多个，比如'Q123|Q456'
        'action': 'wbgetentities',
        'format': 'json',
        'language': {language},
    }

    # 访问
    get = requests.get(url=url, params=params, proxies=Proxies)
    # 转为json数据
    re_json = get.json()

    # 使用logger记录详细信息，而不是直接打印到stdout
    try:
        description = re_json["entities"][id]["descriptions"]["en"]
        logger.debug(f"实体 {id} 的描述信息: {json.dumps(description, ensure_ascii=False, indent=2)}")
    except KeyError as e:
        logger.warning(f"无法获取实体 {id} 的描述信息: {str(e)}")

    return re_json

# print(get_description(search("Astrophysics",limit=1)))
