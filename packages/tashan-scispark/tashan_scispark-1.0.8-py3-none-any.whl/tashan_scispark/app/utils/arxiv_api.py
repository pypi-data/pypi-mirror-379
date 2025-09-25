#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/9/21 23:07
# @Author : 桐
# @QQ:1041264242
# 注意事项：
import arxiv
import json
import logging

# 配置日志记录器
logger = logging.getLogger(__name__)


def get_authors(authors, first_author=False):
    if not first_author:
        output = ", ".join(str(author) for author in authors)
    else:
        output = authors[0]
    return output


def get_papers(query="astronomy", max_results=2):
    """
    @param topic: str
    @param query: str
    @return paper_with_code: dict
    """

    paper_list = []

    search_engine = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    for result in search_engine.results():
        paper_id = result.entry_id
        paper_title = result.title
        paper_pdf = result.pdf_url
        paper_doi = result.doi
        paper_abstract = result.summary.replace("\n", " ")
        paper_authors = get_authors(result.authors)
        primary_category = result.primary_category
        publish_time = result.published.date().isoformat()

        data = {"topic": query,
                "title": paper_title,
                "id": paper_id,
                "doi": paper_doi,
                "pdf": paper_pdf,
                "abstract": paper_abstract,
                "authors": paper_authors,
                "category": primary_category,
                "time": publish_time}

        paper_list.append(data)

    return paper_list


def search_paper(Keywords, Limit=2):
    """
    搜索学术论文
    
    Args:
        Keywords: 关键词列表
        Limit: 每个关键词的论文数量限制
    
    Returns:
        data_collector: 论文数据列表
    """
    data_collector = []

    for keyword in Keywords:
        logger.info(f"检索与技术实体相关的论文: {keyword}")
        data_collector += get_papers(query=keyword, max_results=Limit)
        logger.debug(f"当前收集的论文数据: {len(data_collector)} 篇")
        logger.info(f"检索与技术实体相关的论文: {keyword} 状态:完成!")
    return data_collector
