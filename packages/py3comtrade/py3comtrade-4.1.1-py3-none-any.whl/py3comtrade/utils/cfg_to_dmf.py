#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

from py3comtrade.dispose.channel_name import parser_phase

if __name__ == '__main__':
    # 清理并加载数据到DataFrame
    df = pd.read_csv(r"D:\codeArea\gitee\comtradeOfPython\通道名称汇总.csv", encoding='gbk')
    pn = parser_phase("220kVI母 Ua")
    print(pn)
