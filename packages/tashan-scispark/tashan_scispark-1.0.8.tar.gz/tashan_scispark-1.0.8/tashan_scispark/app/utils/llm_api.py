#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/8/19 15:44
# @Author : 桐
# @QQ:1041264242
# 注意事项：
"""
该文件用于调用大模型API
"""

import json
import tiktoken
import logging
from ..core.prompt import llm_base_prompt
from ..core.config import DeepSeek_Key, QwenMax_Key
from openai import OpenAI

# 配置日志记录器
logger = logging.getLogger(__name__)

# 假设DeepSeekV2模型的定价是每个token 0.0001美元
TOKEN_PRICE_USD = 0.0001
total_tokens_used = 0


def calculate_token_cost(content, model_name="gpt-3.5-turbo"):
    # 使用tiktoken库来计算token数量
    enc = tiktoken.encoding_for_model(model_name)
    tokens = enc.encode(content)
    token_count = len(tokens)
    # 计算费用
    cost_usd = token_count * TOKEN_PRICE_USD
    global total_tokens_used
    total_tokens_used += token_count
    logger.info(f"已使用总token数: {total_tokens_used}")
    return token_count, cost_usd


def call_with_deepseek(question, system_prompt=llm_base_prompt(), temperature=0.7):
    """
    调用DeepSeek API
    
    Args:
        question: 用户问题
        system_prompt: 系统提示词
        temperature: 温度参数
    
    Returns:
        API响应内容
    """
    client = DeepSeek_Key
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ]

    response = client.chat.completions.create(
        model="deepseek-chat",
        temperature=temperature,
        messages=messages
    )

    calculate_token_cost(content=question + system_prompt + response.choices[0].message.content)

    logger.info("DeepSeek API调用成功")
    return response.choices[0].message.content


def call_with_deepseek_jsonout(system_prompt, question):
    client = DeepSeek_Key

    if system_prompt == "":
        system_prompt = """The user will provide some exam text. Please parse the "question" and "answer" and output them in JSON format. 

EXAMPLE INPUT: 
Which is the highest mountain in the world? Mount Everest.

EXAMPLE JSON OUTPUT:
{
    "question": "Which is the highest mountain in the world?",
    "answer": "Mount Everest"
}"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ]

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        response_format={
            'type': 'json_object'
        }
    )
    calculate_token_cost(content=question + system_prompt + response.choices[0].message.content)
    return json.loads(response.choices[0].message.content)


def call_with_qwenmax(question, system_prompt=llm_base_prompt(), temperature=0.7):
    """
    使用通义千问API进行对话
    Args:
        question: 用户问题
        system_prompt: 系统提示词
        temperature: 温度参数
    Returns:
        str: API响应内容
    """
    client = QwenMax_Key
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ]

    try:
        response = client.chat.completions.create(
            model="qwen-max",
            temperature=temperature,
            messages=messages
        )

        calculate_token_cost(content=question + system_prompt + response.choices[0].message.content)
        logger.info("QwenMax API调用成功")
        return response.choices[0].message.content

    except Exception as e:
        logger.error(f"QwenMax API调用失败: {str(e)}")
        raise
