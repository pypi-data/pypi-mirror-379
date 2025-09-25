#!/usr/bin/env python3
"""
Tushare MCP Server - 聚合股票数据接口
基于 Tushare 数据接口的 MCP 服务器，提供全面的中国金融市场数据
"""

import asyncio
import os
import ssl
from typing import List, Optional
import pandas as pd
import tushare as ts
from datetime import datetime, timedelta

from mcp.server import Server, InitializationOptions
import mcp.server.stdio
import mcp.types as types


class TushareDataProvider:
    """Tushare 数据提供器 - 聚合股票相关接口"""
    
    def __init__(self, token: Optional[str] = None):
        """初始化 Tushare 连接"""
        self.token = token
        if self.token:
            ts.set_token(self.token)
            self.pro = ts.pro_api()
            print("✅ Tushare Token has been set.")
        else:
            self.pro = None
            print("⚠️ Tushare Token is not set, using free interface (limited functionality).")
    
    # ================ 基础股票数据接口 ================
    
    def get_stock_basic(self, exchange: str = '', list_status: str = 'L') -> pd.DataFrame:
        """获取股票基本信息"""
        try:
            if self.pro:
                return self.pro.stock_basic(exchange=exchange, list_status=list_status)
            else:
                return ts.get_stock_basics()
        except Exception as e:
            print(f"获取股票基本信息失败: {e}")
            return pd.DataFrame()
    
    def get_daily_data(self, ts_code: str, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取日线行情"""
        try:
            if self.pro:
                return self.pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            else:
                symbol = ts_code.split('.')[0]
                return ts.get_hist_data(symbol, start=start_date, end=end_date)
        except Exception as e:
            print(f"获取日线数据失败: {e}")
            return pd.DataFrame()
    
    def get_realtime_quotes(self, ts_codes: List[str]) -> pd.DataFrame:
        """获取实时行情"""
        try:
            if self.pro:
                codes_str = ','.join(ts_codes)
                return self.pro.query('daily_basic', ts_code=codes_str, trade_date=datetime.now().strftime('%Y%m%d'))
            else:
                symbols = [code.split('.')[0] for code in ts_codes]
                return ts.get_realtime_quotes(symbols)
        except Exception as e:
            print(f"获取实时行情失败: {e}")
            return pd.DataFrame()
    

    
    # ================ 市场数据接口 ================
    
    def get_top_list(self, trade_date: str = '') -> pd.DataFrame:
        """获取龙虎榜数据"""
        try:
            if self.pro:
                if not trade_date:
                    trade_date = datetime.now().strftime('%Y%m%d')
                return self.pro.top_list(trade_date=trade_date)
            else:
                print("龙虎榜数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取龙虎榜数据失败: {e}")
            return pd.DataFrame()
    
    def get_money_flow(self, ts_code: str = '', trade_date: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取资金流向数据"""
        try:
            if self.pro:
                if ts_code:
                    return self.pro.moneyflow(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)
                else:
                    return self.pro.moneyflow_hsgt(trade_date=trade_date, start_date=start_date, end_date=end_date)
            else:
                print("资金流向数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取资金流向数据失败: {e}")
            return pd.DataFrame()
    
    def get_concept_detail(self, concept_name: str = '') -> pd.DataFrame:
        """获取概念股详情"""
        try:
            if self.pro:
                if concept_name:
                    concepts = self.pro.concept()
                    concept_match = concepts[concepts['name'].str.contains(concept_name, na=False)]
                    if not concept_match.empty:
                        concept_code = concept_match.iloc[0]['code']
                        return self.pro.concept_detail(id=concept_code)
                else:
                    return self.pro.concept()
            else:
                print("概念股数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取概念股数据失败: {e}")
            return pd.DataFrame()
    
    def get_margin_detail(self, trade_date: str = '', exchange_id: str = '') -> pd.DataFrame:
        """获取融资融券数据"""
        try:
            if self.pro:
                if not trade_date:
                    trade_date = datetime.now().strftime('%Y%m%d')
                return self.pro.margin_detail(trade_date=trade_date, exchange_id=exchange_id)
            else:
                print("融资融券数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取融资融券数据失败: {e}")
            return pd.DataFrame()
    
    def get_block_trade(self, trade_date: str = '') -> pd.DataFrame:
        """获取大宗交易数据"""
        try:
            if self.pro:
                if not trade_date:
                    trade_date = datetime.now().strftime('%Y%m%d')
                return self.pro.block_trade(trade_date=trade_date)
            else:
                print("大宗交易数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取大宗交易数据失败: {e}")
            return pd.DataFrame()
    
    def get_fund_basic(self, market: str = 'E') -> pd.DataFrame:
        """获取基金基本信息"""
        try:
            if self.pro:
                return self.pro.fund_basic(market=market)
            else:
                print("基金数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取基金数据失败: {e}")
            return pd.DataFrame()
    
    # ================ 财务数据接口 ================
    
    def get_financial_data(self, ts_code: str, period: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取财务数据"""
        try:
            if self.pro:
                return self.pro.income(ts_code=ts_code, period=period, start_date=start_date, end_date=end_date)
            else:
                print("财务数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取财务数据失败: {e}")
            return pd.DataFrame()
    
    def get_index_data(self, ts_code: str, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取指数行情"""
        try:
            if self.pro:
                return self.pro.index_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            else:
                # Free API uses different codes for indices
                index_code_map = {
                    '000300.SH': 'hs300',
                    '000016.SH': 'sz50',
                    '000001.SH': 'sh',
                    '399001.SZ': 'sz',
                    '399006.SZ': 'cyb',
                }
                symbol = index_code_map.get(ts_code)
                if symbol:
                    # Monkey-patch for pandas.DataFrame.append for tushare compatibility
                    _original_append = getattr(pd.DataFrame, 'append', None)
                    # Replace append with concat if it's missing (pandas >= 2.0)
                    if _original_append is None:
                        pd.DataFrame.append = lambda self, other, ignore_index=False: pd.concat([self, other], ignore_index=ignore_index)

                    try:
                        # Skip SSL certificate verification for macOS compatibility
                        ssl._create_default_https_context = ssl._create_unverified_context
                        # For indices, get_k_data is used. The parameter is 'end'.
                        return ts.get_k_data(symbol, start=start_date, end=end_date)
                    finally:
                        # Clean up the monkey-patch
                        if _original_append is None:
                            delattr(pd.DataFrame, 'append')
                        else:
                            # Restore original append if it existed
                            pd.DataFrame.append = _original_append
                else:
                    print(f"免费接口不支持或未映射指数 {ts_code}。")
                    return pd.DataFrame()
        except Exception as e:
            print(f"获取指数数据失败: {e}")
            return pd.DataFrame()
    
    # ================ ETF和指数数据接口 ================

    def get_etf_basic(self) -> pd.DataFrame:
        """获取 ETF 基本信息"""
        try:
            if self.pro:
                return self.pro.fund_basic(market='E')
            else:
                print("ETF 基本信息需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取 ETF 基本信息失败: {e}")
            return pd.DataFrame()

    def get_etf_daily(self, ts_code: str, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取 ETF 日线行情"""
        try:
            if self.pro:
                return self.pro.fund_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            else:
                print("ETF 日线行情需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取 ETF 日线行情失败: {e}")
            return pd.DataFrame()

    
    def get_etf_basic(self, market: str = 'E') -> pd.DataFrame:
        """获取ETF基本信息"""
        try:
            if self.pro:
                return self.pro.fund_basic(market=market, fund_type='ETF')
            else:
                print("ETF数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取ETF基本信息失败: {e}")
            return pd.DataFrame()
    
    def get_etf_daily(self, ts_code: str, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取ETF日线行情"""
        try:
            if self.pro:
                return self.pro.fund_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            else:
                print("ETF行情数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取ETF行情失败: {e}")
            return pd.DataFrame()

    def get_etf_index(self, ts_code: str, pub_date: str = '', base_date: str = '') -> pd.DataFrame:
        """获取ETF基准指数列表信息"""
        try:
            if self.pro:
                return self.pro.etf_index(ts_code=ts_code, pub_date=pub_date, base_date=base_date)
            else:
                print("ETF基准指数列表信息需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取ETF基准指数列表信息失败: {e}")
            return pd.DataFrame()

    def get_fund_adj(self, ts_code: str, trade_date: str = '', start_date: str = '', end_date: str = '', offset: str = '', limit: str = '') -> pd.DataFrame:
        """获取基金复权因子"""
        try:
            if self.pro:
                return self.pro.fund_adj(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date, offset=offset, limit=limit)
            else:
                print("基金复权因子需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取基金复权因子失败: {e}")
            return pd.DataFrame()

    def get_stk_mins(self, ts_code: str, freq: str, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取ETF分钟数据"""
        try:
            if self.pro:
                return self.pro.stk_mins(ts_code=ts_code, freq=freq, start_date=start_date, end_date=end_date)
            else:
                print("ETF分钟数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取ETF分钟数据失败: {e}")
            return pd.DataFrame()
    
    def get_index_basic(self, market: str = '') -> pd.DataFrame:
        """获取指数基本信息"""
        try:
            if self.pro:
                return self.pro.index_basic(market=market)
            else:
                print("指数基本信息需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取指数基本信息失败: {e}")
            return pd.DataFrame()
    
    def get_index_weight(self, index_code: str, trade_date: str = '') -> pd.DataFrame:
        """获取指数成分股权重"""
        try:
            if self.pro:
                if not trade_date:
                    trade_date = datetime.now().strftime('%Y%m%d')
                return self.pro.index_weight(index_code=index_code, trade_date=trade_date)
            else:
                print("指数成分股权重需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取指数成分股权重失败: {e}")
            return pd.DataFrame()
    
    # ================ 债券数据接口 ================
    
    def get_bond_basic(self, ts_code: str = '') -> pd.DataFrame:
        """获取债券基本信息"""
        try:
            if self.pro:
                return self.pro.bond_basic(ts_code=ts_code)
            else:
                print("债券数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取债券基本信息失败: {e}")
            return pd.DataFrame()
    
    def get_bond_daily(self, ts_code: str, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取债券日线行情"""
        try:
            if self.pro:
                return self.pro.bond_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            else:
                print("债券行情数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取债券行情失败: {e}")
            return pd.DataFrame()
    
    def get_cb_basic(self) -> pd.DataFrame:
        """获取可转债基本信息"""
        try:
            if self.pro:
                return self.pro.cb_basic()
            else:
                print("可转债数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取可转债基本信息失败: {e}")
            return pd.DataFrame()
    
    def get_cb_daily(self, ts_code: str, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取可转债日线行情"""
        try:
            if self.pro:
                return self.pro.cb_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            else:
                print("可转债行情数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取可转债行情失败: {e}")
            return pd.DataFrame()
    
    # ================ 扩展基金数据接口 ================
    
    def get_fund_daily(self, ts_code: str, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取基金净值数据"""
        try:
            if self.pro:
                return self.pro.fund_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            else:
                print("基金净值数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取基金净值失败: {e}")
            return pd.DataFrame()
    
    def get_fund_portfolio(self, ts_code: str, period: str = '') -> pd.DataFrame:
        """获取基金持仓数据"""
        try:
            if self.pro:
                return self.pro.fund_portfolio(ts_code=ts_code, period=period)
            else:
                print("基金持仓数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取基金持仓失败: {e}")
            return pd.DataFrame()
    
    def get_fund_rating(self, ts_code: str = '') -> pd.DataFrame:
        """获取基金评级数据"""
        try:
            if self.pro:
                return self.pro.fund_rating(ts_code=ts_code)
            else:
                print("基金评级数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取基金评级失败: {e}")
            return pd.DataFrame()
    
    # ================ 宏观经济数据接口 ================
    
    def get_gdp_data(self, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取GDP数据"""
        try:
            if self.pro:
                return self.pro.cn_gdp(start_date=start_date, end_date=end_date)
            else:
                print("GDP数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取GDP数据失败: {e}")
            return pd.DataFrame()
    
    def get_cpi_data(self, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取CPI数据"""
        try:
            if self.pro:
                return self.pro.cn_cpi(start_date=start_date, end_date=end_date)
            else:
                print("CPI数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取CPI数据失败: {e}")
            return pd.DataFrame()
    
    def get_interest_rate(self, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取利率数据"""
        try:
            if self.pro:
                return self.pro.shibor(start_date=start_date, end_date=end_date)
            else:
                print("利率数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取利率数据失败: {e}")
            return pd.DataFrame()
    
    def get_exchange_rate(self, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取汇率数据"""
        try:
            if self.pro:
                return self.pro.fx_daily(start_date=start_date, end_date=end_date)
            else:
                print("汇率数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取汇率数据失败: {e}")
            return pd.DataFrame()
    
    def get_pmi_data(self, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取PMI数据"""
        try:
            if self.pro:
                return self.pro.cn_pmi(start_date=start_date, end_date=end_date)
            else:
                print("PMI数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取PMI数据失败: {e}")
            return pd.DataFrame()
    
    def get_money_supply(self, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取货币供应量数据"""
        try:
            if self.pro:
                return self.pro.cn_m(start_date=start_date, end_date=end_date)
            else:
                print("货币供应量数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取货币供应量数据失败: {e}")
            return pd.DataFrame()

    def get_balance_sheet(self, ts_code: str = '', period: str = '', start_date: str = '', end_date: str = '', is_vip: bool = False) -> pd.DataFrame:
        """获取资产负债表"""
        try:
            if self.pro:
                if is_vip:
                    return self.pro.balancesheet_vip(period=period)
                else:
                    return self.pro.balancesheet(ts_code=ts_code, period=period, start_date=start_date, end_date=end_date)
            else:
                print("资产负债表数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取资产负债表失败: {e}")
            return pd.DataFrame()

    def get_cash_flow(self, ts_code: str = '', period: str = '', start_date: str = '', end_date: str = '', is_vip: bool = False) -> pd.DataFrame:
        """获取现金流量表"""
        try:
            if self.pro:
                if is_vip:
                    return self.pro.cashflow_vip(period=period)
                else:
                    return self.pro.cashflow(ts_code=ts_code, period=period, start_date=start_date, end_date=end_date)
            else:
                print("现金流量表数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取现金流量表失败: {e}")
            return pd.DataFrame()

    def get_fina_indicator(self, ts_code: str, start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取财务指标数据"""
        try:
            if self.pro:
                return self.pro.fina_indicator(ts_code=ts_code, start_date=start_date, end_date=end_date)
            else:
                print("财务指标数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取财务指标数据失败: {e}")
            return pd.DataFrame()

    def get_fina_mainbz(self, ts_code: str = '', period: str = '', type: str = '', is_vip: bool = False) -> pd.DataFrame:
        """获取主营业务构成"""
        try:
            if self.pro:
                if is_vip:
                    return self.pro.fina_mainbz_vip(period=period, type=type)
                else:
                    return self.pro.fina_mainbz(ts_code=ts_code, period=period, type=type)
            else:
                print("主营业务构成数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取主营业务构成失败: {e}")
            return pd.DataFrame()

    def get_weekly_data(self, ts_code: str = '', trade_date: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取周线行情"""
        try:
            if self.pro:
                return self.pro.weekly(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)
            else:
                print("周线行情数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取周线行情失败: {e}")
            return pd.DataFrame()

    def get_monthly_data(self, ts_code: str = '', trade_date: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取月线行情"""
        try:
            if self.pro:
                return self.pro.monthly(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)
            else:
                print("月线行情数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取月线行情失败: {e}")
            return pd.DataFrame()

    def get_daily_basic(self, ts_code: str = '', trade_date: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取每日指标"""
        try:
            if self.pro:
                return self.pro.daily_basic(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)
            else:
                print("每日指标数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取每日指标失败: {e}\n")
            return pd.DataFrame()

    def get_adj_factor(self, ts_code: str = '', trade_date: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取复权因子"""
        try:
            if self.pro:
                return self.pro.adj_factor(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)
            else:
                print("复权因子数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取复权因子失败: {e}\n")
            return pd.DataFrame()

    def get_suspend_d(self, ts_code: str = '', trade_date: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取停复牌信息"""
        try:
            if self.pro:
                return self.pro.suspend_d(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)
            else:
                print("停复牌信息需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取停复牌信息失败: {e}\n")
            return pd.DataFrame()

    def get_limit_list(self, trade_date: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取涨跌停价格"""
        try:
            if self.pro:
                return self.pro.limit_list(trade_date=trade_date, start_date=start_date, end_date=end_date)
            else:
                print("涨跌停价格数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取涨跌停价格失败: {e}\n")
            return pd.DataFrame()

    def get_moneyflow_ind_dc(self, trade_date: str = '', content_type: str = '') -> pd.DataFrame:
        """获取东财概念及行业板块资金流向"""
        try:
            if self.pro:
                return self.pro.moneyflow_ind_dc(trade_date=trade_date, content_type=content_type)
            else:
                print("东财概念及行业板块资金流向数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取东财概念及行业板块资金流向失败: {e}")
            return pd.DataFrame()

    def get_moneyflow_ind_ths(self, trade_date: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取同花顺行业资金流向"""
        try:
            if self.pro:
                return self.pro.moneyflow_ind_ths(trade_date=trade_date, start_date=start_date, end_date=end_date)
            else:
                print("同花顺行业资金流向数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取同花顺行业资金流向失败: {e}")
            return pd.DataFrame()

    def get_moneyflow_mkt_dc(self, trade_date: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取大盘资金流向"""
        try:
            if self.pro:
                return self.pro.moneyflow_mkt_dc(trade_date=trade_date, start_date=start_date, end_date=end_date)
            else:
                print("大盘资金流向数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取大盘资金流向失败: {e}")
            return pd.DataFrame()

    def get_dc_hot(self, trade_date: str = '', market: str = '', hot_type: str = '', is_new: str = 'Y') -> pd.DataFrame:
        """获取东方财富热板"""
        try:
            if self.pro:
                return self.pro.dc_hot(trade_date=trade_date, market=market, hot_type=hot_type, is_new=is_new)
            else:
                print("东方财富热板数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取东方财富热板失败: {e}")
            return pd.DataFrame()

    def get_dc_daily(self, ts_code: str = '', trade_date: str = '', start_date: str = '', end_date: str = '', idx_type: str = '') -> pd.DataFrame:
        """获取东财概念板块行情"""
        try:
            if self.pro:
                return self.pro.dc_daily(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date, idx_type=idx_type)
            else:
                print("东财概念板块行情数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取东财概念板块行情失败: {e}")
            return pd.DataFrame()

    def get_dc_index(self, ts_code: str = '', name: str = '', trade_date: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取东方财富概念板块"""
        try:
            if self.pro:
                return self.pro.dc_index(ts_code=ts_code, name=name, trade_date=trade_date, start_date=start_date, end_date=end_date)
            else:
                print("东方财富概念板块数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取东方财富概念板块失败: {e}")
            return pd.DataFrame()

    def get_dc_member(self, ts_code: str = '', con_code: str = '', trade_date: str = '') -> pd.DataFrame:
        """获取东方财富板块成分"""
        try:
            if self.pro:
                return self.pro.dc_member(ts_code=ts_code, con_code=con_code, trade_date=trade_date)
            else:
                print("东方财富板块成分数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取东方财富板块成分失败: {e}")
            return pd.DataFrame()

    def get_daily_info(self, trade_date: str = '', ts_code: str = '', exchange: str = '', start_date: str = '', end_date: str = '', fields: str = '') -> pd.DataFrame:
        """获取市场交易统计"""
        try:
            if self.pro:
                return self.pro.daily_info(trade_date=trade_date, ts_code=ts_code, exchange=exchange, start_date=start_date, end_date=end_date, fields=fields)
            else:
                print("市场交易统计数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取市场交易统计失败: {e}")
            return pd.DataFrame()

    def get_sz_daily_info(self, trade_date: str = '', ts_code: str = '', start_date: str = '', end_date: str = '') -> pd.DataFrame:
        """获取深圳市场每日交易概况"""
        try:
            if self.pro:
                return self.pro.sz_daily_info(trade_date=trade_date, ts_code=ts_code, start_date=start_date, end_date=end_date)
            else:
                print("深圳市场每日交易概况数据需要 Tushare Pro 权限")
                return pd.DataFrame()
        except Exception as e:
            print(f"获取深圳市场每日交易概况失败: {e}")
            return pd.DataFrame()


# 创建 MCP 服务器
server = Server("tushare-mcp-server")

# 全局数据提供器, 将在初始化时创建
data_provider: Optional[TushareDataProvider] = None


@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """列出所有可用的工具"""
    return [
        # 基础股票数据
        types.Tool(
            name="get_stock_basic",
            description="获取股票基本信息列表",
            inputSchema={
                "type": "object",
                "properties": {
                    "exchange": {
                        "type": "string",
                        "description": "交易所代码：SSE-上交所，SZSE-深交所，空为全部",
                        "default": ""
                    },
                    "list_status": {
                        "type": "string", 
                        "description": "上市状态：L-上市，D-退市，P-暂停上市",
                        "default": "L"
                    }
                }
            }
        ),
        types.Tool(
            name="get_daily_data",
            description="获取股票日线行情数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "股票代码，如 000001.SZ"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD 格式",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string", 
                        "description": "结束日期 YYYYMMDD 格式",
                        "default": ""
                    }
                },
                "required": ["ts_code"]
            }
        ),
        types.Tool(
            name="get_weekly_data",
            description="获取A股周线行情",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "TS代码 (二选一)",
                        "default": ""
                    },
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (二选一)",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_monthly_data",
            description="获取A股月线行情",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "TS代码 (二选一)",
                        "default": ""
                    },
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (二选一)",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_daily_basic",
            description="获取A股每日指标",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "TS代码 (二选一)",
                        "default": ""
                    },
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (二选一)",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_adj_factor",
            description="获取复权因子",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "TS代码 (可选)",
                        "default": ""
                    },
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (可选)",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_suspend_d",
            description="获取停复牌信息",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "TS代码 (可选)",
                        "default": ""
                    },
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (可选)",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_limit_list",
            description="获取涨跌停价格",
            inputSchema={
                "type": "object",
                "properties": {
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (可选)",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期",
                        "default": ""
                    }
                }
            }
        ),        types.Tool(
            name="get_moneyflow_ind_dc",
            description="获取东财概念及行业板块资金流向",
            inputSchema={
                "type": "object",
                "properties": {
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "content_type": {
                        "type": "string",
                        "description": "类型：industry-行业, concept-概念, region-地域",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_moneyflow_ind_ths",
            description="获取同花顺行业资金流向",
            inputSchema={
                "type": "object",
                "properties": {
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 (YYYYMMDD)",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_moneyflow_mkt_dc",
            description="获取大盘资金流向",
            inputSchema={
                "type": "object",
                "properties": {
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 (YYYYMMDD)",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_dc_hot",
            description="获取东方财富热板",
            inputSchema={
                "type": "object",
                "properties": {
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "market": {
                        "type": "string",
                        "description": "市场类型 (A股市场, ETF基金, 港股市场, 美股市场)",
                        "default": ""
                    },
                    "hot_type": {
                        "type": "string",
                        "description": "热点类型 (人气榜, 飙升榜)",
                        "default": ""
                    },
                    "is_new": {
                        "type": "string",
                        "description": "是否最新 (Y/N)",
                        "default": "Y"
                    }
                }
            }
        ),
        types.Tool(
            name="get_dc_daily",
            description="获取东财概念板块行情",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "板块代码",
                        "default": ""
                    },
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "idx_type": {
                        "type": "string",
                        "description": "板块类型 (concept, industry, region)",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_dc_index",
            description="获取东方财富概念板块",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "板块代码",
                        "default": ""
                    },
                    "name": {
                        "type": "string",
                        "description": "板块名称",
                        "default": ""
                    },
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 (YYYYMMDD)",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_dc_member",
            description="获取东方财富板块成分",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "板块代码",
                        "default": ""
                    },
                    "con_code": {
                        "type": "string",
                        "description": "成分股代码",
                        "default": ""
                    },
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (YYYYMMDD)",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_daily_info",
            description="获取市场交易统计",
            inputSchema={
                "type": "object",
                "properties": {
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "ts_code": {
                        "type": "string",
                        "description": "板块代码",
                        "default": ""
                    },
                    "exchange": {
                        "type": "string",
                        "description": "交易所 (SH, SZ)",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "fields": {
                        "type": "string",
                        "description": "指定字段",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_sz_daily_info",
            description="获取深圳市场每日交易概况",
            inputSchema={
                "type": "object",
                "properties": {
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "ts_code": {
                        "type": "string",
                        "description": "板块代码",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 (YYYYMMDD)",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 (YYYYMMDD)",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_realtime_quotes",
            description="获取股票实时行情",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_codes": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "股票代码列表，如 ['000001.SZ', '000002.SZ']"
                    }
                },
                "required": ["ts_codes"]
            }
        ),
        
        # 市场数据
        types.Tool(
            name="get_top_list",
            description="获取龙虎榜数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 YYYYMMDD，默认为今日",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_money_flow",
            description="获取资金流向数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "股票代码，如 000001.SZ（可选，不填则获取沪深港通资金流向）",
                        "default": ""
                    },
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 YYYYMMDD，默认为今日",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_concept_detail",
            description="获取概念股详情",
            inputSchema={
                "type": "object",
                "properties": {
                    "concept_name": {
                        "type": "string",
                        "description": "概念名称，如'人工智能'、'新能源'等（可选，不填则获取所有概念）",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_margin_detail",
            description="获取融资融券数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 YYYYMMDD，默认为今日",
                        "default": ""
                    },
                    "exchange_id": {
                        "type": "string",
                        "description": "交易所代码：SSE-上交所，SZSE-深交所（可选）",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_block_trade",
            description="获取大宗交易数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 YYYYMMDD，默认为今日",
                        "default": ""
                    }
                }
            }
        ),
        
        # 财务和基金数据
        types.Tool(
            name="get_financial_data",
            description="获取上市公司财务数据（需要Pro权限）",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "股票代码，如 000001.SZ"
                    },
                    "period": {
                        "type": "string",
                        "description": "报告期 YYYYMMDD",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD", 
                        "default": ""
                    }
                },
                "required": ["ts_code"]
            }
        ),
        types.Tool(
            name="get_balance_sheet",
            description="获取资产负债表数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "股票代码，如 000001.SZ",
                        "default": ""
                    },
                    "period": {
                        "type": "string",
                        "description": "报告期 YYYYMMDD",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    },
                    "is_vip": {
                        "type": "boolean",
                        "description": "是否使用VIP接口获取所有公司季度数据",
                        "default": False
                    }
                }
            }
        ),
        types.Tool(
            name="get_cash_flow",
            description="获取现金流量表数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "股票代码，如 000001.SZ",
                        "default": ""
                    },
                    "period": {
                        "type": "string",
                        "description": "报告期 YYYYMMDD",
                        "default": ""
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    },
                    "is_vip": {
                        "type": "boolean",
                        "description": "是否使用VIP接口获取所有公司季度数据",
                        "default": False
                    }
                }
            }
        ),
        types.Tool(
            name="get_fina_indicator",
            description="获取财务指标数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "股票代码，如 000001.SZ"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                },
                "required": ["ts_code"]
            }
        ),
        types.Tool(
            name="get_fina_mainbz",
            description="获取主营业务构成数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "股票代码，如 000001.SZ",
                        "default": ""
                    },
                    "period": {
                        "type": "string",
                        "description": "报告期 YYYYMMDD",
                        "default": ""
                    },
                    "type": {
                        "type": "string",
                        "description": "类型 P产品 D地区 I行业",
                        "default": ""
                    },
                    "is_vip": {
                        "type": "boolean",
                        "description": "是否使用VIP接口获取所有公司季度数据",
                        "default": False
                    }
                }
            }
        ),
        types.Tool(
            name="get_fund_basic",
            description="获取基金基本信息",
            inputSchema={
                "type": "object",
                "properties": {
                    "market": {
                        "type": "string",
                        "description": "市场类型：E-场内基金，O-场外基金",
                        "default": "E"
                    }
                }
            }
        ),
        
        # 指数数据
        types.Tool(
            name="get_index_data",
            description="获取指数行情数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "指数代码，如 000001.SH（上证指数）"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                },
                "required": ["ts_code"]
            }
        ),
        types.Tool(
            name="get_market_summary",
            description="获取市场概况（主要指数当日表现）",
            inputSchema={
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "查询日期 YYYYMMDD，默认为今日",
                        "default": ""
                    }
                }
            }
        ),
        
        # ================ ETF和指数数据工具 ================
        types.Tool(
            name="get_etf_basic",
            description="获取ETF基本信息",
            inputSchema={
                "type": "object",
                "properties": {
                    "market": {
                        "type": "string",
                        "description": "市场类型：E-场内基金，O-场外基金",
                        "default": "E"
                    }
                }
            }
        ),
        types.Tool(
            name="get_etf_daily",
            description="获取ETF日线行情数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "ETF代码，如 510050.SH"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                },
                "required": ["ts_code"]
            }
        ),
        types.Tool(
            name="get_index_basic",
            description="获取指数基本信息",
            inputSchema={
                "type": "object",
                "properties": {
                    "market": {
                        "type": "string",
                        "description": "市场类型：MSCI-MSCI指数，CSI-中证指数，SSE-上交所指数，SZSE-深交所指数",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_index_weight",
            description="获取指数成分股权重",
            inputSchema={
                "type": "object",
                "properties": {
                    "index_code": {
                        "type": "string",
                        "description": "指数代码，如 000300.SH（沪深300）"
                    },
                    "trade_date": {
                        "type": "string",
                        "description": "交易日期 YYYYMMDD，默认为今日",
                        "default": ""
                    }
                },
                "required": ["index_code"]
            }
        ),
        
        # ================ 债券数据工具 ================
        types.Tool(
            name="get_bond_basic",
            description="获取债券基本信息",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "债券代码（可选，不填则获取所有债券）",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_bond_daily",
            description="获取债券日线行情数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "债券代码"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                },
                "required": ["ts_code"]
            }
        ),
        types.Tool(
            name="get_cb_basic",
            description="获取可转债基本信息",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        types.Tool(
            name="get_cb_daily",
            description="获取可转债日线行情数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "可转债代码"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                },
                "required": ["ts_code"]
            }
        ),
        
        # ================ 扩展基金数据工具 ================
        types.Tool(
            name="get_fund_daily",
            description="获取基金净值数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "基金代码"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                },
                "required": ["ts_code"]
            }
        ),
        types.Tool(
            name="get_fund_portfolio",
            description="获取基金持仓数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "基金代码"
                    },
                    "period": {
                        "type": "string",
                        "description": "报告期 YYYYMMDD",
                        "default": ""
                    }
                },
                "required": ["ts_code"]
            }
        ),
        types.Tool(
            name="get_fund_rating",
            description="获取基金评级数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "ts_code": {
                        "type": "string",
                        "description": "基金代码（可选，不填则获取所有基金评级）",
                        "default": ""
                    }
                }
            }
        ),
        
        # ================ 宏观经济数据工具 ================
        types.Tool(
            name="get_gdp_data",
            description="获取GDP数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_cpi_data",
            description="获取CPI数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_interest_rate",
            description="获取利率数据（SHIBOR）",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_exchange_rate",
            description="获取汇率数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_pmi_data",
            description="获取PMI数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="get_money_supply",
            description="获取货币供应量数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "开始日期 YYYYMMDD",
                        "default": ""
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期 YYYYMMDD",
                        "default": ""
                    }
                }
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> List[types.TextContent]:
    """处理工具调用"""
    if data_provider is None:
        return [types.TextContent(type="text", text="错误: TushareDataProvider 未初始化。请确保服务器已正确初始化。")]
    try:
        # 基础股票数据
        if name == "get_stock_basic":
            exchange = arguments.get("exchange", "")
            list_status = arguments.get("list_status", "L")
            df = data_provider.get_stock_basic(exchange=exchange, list_status=list_status)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到股票基本信息")]
            
            result = f"📊 **股票基本信息** (共{len(df)}只)\n\n"
            result += "| 代码 | 名称 | 行业 | 地区 | 上市日期 |\n"
            result += "|------|------|------|------|----------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('industry', 'N/A')} | {row.get('area', 'N/A')} | {row.get('list_date', 'N/A')} |\n"
            
            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 只股票"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_daily_data":
            ts_code = arguments["ts_code"]
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_daily_data(ts_code=ts_code, start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text=f"未获取到 {ts_code} 的日线数据")]
            
            result = f"📈 **{ts_code} 日线行情** (共{len(df)}条记录)\n\n"
            result += "| 日期 | 开盘 | 最高 | 最低 | 收盘 | 成交量 |\n"
            result += "|------|------|------|------|------|--------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('trade_date', row.name)} | {row.get('open', 'N/A')} | {row.get('high', 'N/A')} | {row.get('low', 'N/A')} | {row.get('close', 'N/A')} | {row.get('vol', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]

        elif name == "get_weekly_data":
            ts_code = arguments.get("ts_code", "")
            trade_date = arguments.get("trade_date", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_weekly_data(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到周线行情数据")]

            result = f"📈 **周线行情** (共{len(df)}条记录)\n\n"
            result += "| 股票代码 | 交易日期 | 开盘 | 最高 | 最低 | 收盘 | 成交量 |\n"
            result += "|----------|----------|------|------|------|------|--------|\n"

            for _, row in df.head(10).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('trade_date', 'N/A')} | {row.get('open', 'N/A')} | {row.get('high', 'N/A')} | {row.get('low', 'N/A')} | {row.get('close', 'N/A')} | {row.get('vol', 'N/A')} |\n"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_monthly_data":
            ts_code = arguments.get("ts_code", "")
            trade_date = arguments.get("trade_date", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_monthly_data(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到月线行情数据")]

            result = f"📈 **月线行情** (共{len(df)}条记录)\n\n"
            result += "| 股票代码 | 交易日期 | 开盘 | 最高 | 最低 | 收盘 | 成交量 |\n"
            result += "|----------|----------|------|------|------|------|--------|\n"

            for _, row in df.head(10).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('trade_date', 'N/A')} | {row.get('open', 'N/A')} | {row.get('high', 'N/A')} | {row.get('low', 'N/A')} | {row.get('close', 'N/A')} | {row.get('vol', 'N/A')} |\n"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_daily_basic":
            ts_code = arguments.get("ts_code", "")
            trade_date = arguments.get("trade_date", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_daily_basic(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到每日指标数据")]

            result = f"📈 **每日指标** (共{len(df)}条记录)\n\n"
            result += "| 股票代码 | 交易日期 | 总市值 | 市盈率 | 市净率 |\n"
            result += "|----------|----------|--------|--------|--------|\n"

            for _, row in df.head(10).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('trade_date', 'N/A')} | {row.get('total_mv', 'N/A')} | {row.get('pe', 'N/A')} | {row.get('pb', 'N/A')} |\n"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_adj_factor":
            ts_code = arguments.get("ts_code", "")
            trade_date = arguments.get("trade_date", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_adj_factor(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到复权因子数据")]

            result = f"📊 **复权因子** (共{len(df)}条记录)\n\n"
            result += "| 股票代码 | 交易日期 | 复权因子 |\n"
            result += "|----------|----------|----------|\n"

            for _, row in df.head(10).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('trade_date', 'N/A')} | {row.get('adj_factor', 'N/A')} |\n"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_suspend_d":
            ts_code = arguments.get("ts_code", "")
            trade_date = arguments.get("trade_date", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_suspend_d(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到停复牌信息")]

            result = f"📊 **停复牌信息** (共{len(df)}条记录)\n\n"
            result += "| 股票代码 | 停牌日期 | 复牌日期 | 停牌原因 |\n"
            result += "|----------|----------|----------|----------|\n"

            for _, row in df.head(10).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('suspend_date', 'N/A')} | {row.get('resume_date', 'N/A')} | {row.get('suspend_reason', 'N/A')} |\n"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_limit_list":
            trade_date = arguments.get("trade_date", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_limit_list(trade_date=trade_date, start_date=start_date, end_date=end_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到涨跌停价格数据")]

            result = f"📊 **涨跌停价格** (共{len(df)}条记录)\n\n"
            result += "| 股票代码 | 交易日期 | 涨停价 | 跌停价 |\n"
            result += "|----------|----------|----------|----------|\n"

            for _, row in df.head(10).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('trade_date', 'N/A')} | {row.get('up_limit', 'N/A')} | {row.get('down_limit', 'N/A')} |\n"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_moneyflow_ind_dc":
            trade_date = arguments.get("trade_date", "")
            content_type = arguments.get("content_type", "")
            df = data_provider.get_moneyflow_ind_dc(trade_date=trade_date, content_type=content_type)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到东财概念及行业板块资金流向数据")]

            result = f"📊 **东财概念及行业板块资金流向** (共{len(df)}条记录)\n\n"
            result += "| 交易日期 | 板块名称 | 主力净流入 | 涨跌幅 |\n"
            result += "|----------|----------|------------|---------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('trade_date', 'N/A')} | {row.get('name', 'N/A')} | {row.get('net_amount', 'N/A')} | {row.get('pct_change', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_moneyflow_ind_ths":
            trade_date = arguments.get("trade_date", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_moneyflow_ind_ths(trade_date=trade_date, start_date=start_date, end_date=end_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到同花顺行业资金流向数据")]

            result = f"📊 **同花顺行业资金流向** (共{len(df)}条记录)\n\n"
            result += "| 交易日期 | 行业名称 | 主力净流入 | 涨跌幅 |\n"
            result += "|----------|----------|------------|---------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('trade_date', 'N/A')} | {row.get('industry', 'N/A')} | {row.get('net_amount', 'N/A')} | {row.get('pct_change', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_moneyflow_mkt_dc":
            trade_date = arguments.get("trade_date", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_moneyflow_mkt_dc(trade_date=trade_date, start_date=start_date, end_date=end_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到大盘资金流向数据")]

            result = f"📊 **大盘资金流向** (共{len(df)}条记录)\n\n"
            result += "| 交易日期 | 上证收盘 | 上证涨跌 | 深证收盘 | 深证涨跌 | 主力净流入 |\n"
            result += "|----------|----------|----------|----------|----------|------------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('trade_date', 'N/A')} | {row.get('close_sh', 'N/A')} | {row.get('pct_change_sh', 'N/A')} | {row.get('close_sz', 'N/A')} | {row.get('pct_change_sz', 'N/A')} | {row.get('net_amount', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_dc_hot":
            trade_date = arguments.get("trade_date", "")
            market = arguments.get("market", "")
            hot_type = arguments.get("hot_type", "")
            is_new = arguments.get("is_new", "Y")
            df = data_provider.get_dc_hot(trade_date=trade_date, market=market, hot_type=hot_type, is_new=is_new)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到东方财富热板数据")]

            result = f"📊 **东方财富热板** (共{len(df)}条记录)\n\n"
            result += "| 股票代码 | 股票名称 | 排名 | 涨跌幅 | 最新价 |\n"
            result += "|----------|----------|------|---------|--------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('ts_name', 'N/A')} | {row.get('rank', 'N/A')} | {row.get('pct_change', 'N/A')} | {row.get('current_price', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_dc_daily":
            ts_code = arguments.get("ts_code", "")
            trade_date = arguments.get("trade_date", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            idx_type = arguments.get("idx_type", "")
            df = data_provider.get_dc_daily(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date, idx_type=idx_type)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到东财概念板块行情数据")]

            result = f"📊 **东财概念板块行情** (共{len(df)}条记录)\n\n"
            result += "| 板块代码 | 交易日期 | 收盘 | 开盘 | 最高 | 最低 | 涨跌幅 |\n"
            result += "|----------|----------|------|------|------|------|---------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('trade_date', 'N/A')} | {row.get('close', 'N/A')} | {row.get('open', 'N/A')} | {row.get('high', 'N/A')} | {row.get('low', 'N/A')} | {row.get('pct_change', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_dc_index":
            ts_code = arguments.get("ts_code", "")
            name = arguments.get("name", "")
            trade_date = arguments.get("trade_date", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_dc_index(ts_code=ts_code, name=name, trade_date=trade_date, start_date=start_date, end_date=end_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到东方财富概念板块数据")]

            result = f"📊 **东方财富概念板块** (共{len(df)}条记录)\n\n"
            result += "| 板块代码 | 板块名称 | 领涨股 | 涨跌幅 | 总市值 | 换手率 | 上涨家数 | 下跌家数 |\n"
            result += "|----------|----------|----------|---------|--------|----------|----------|----------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('leading', 'N/A')} | {row.get('pct_change', 'N/A')} | {row.get('total_mv', 'N/A')} | {row.get('turnover_rate', 'N/A')} | {row.get('up_num', 'N/A')} | {row.get('down_num', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_dc_member":
            ts_code = arguments.get("ts_code", "")
            con_code = arguments.get("con_code", "")
            trade_date = arguments.get("trade_date", "")
            df = data_provider.get_dc_member(ts_code=ts_code, con_code=con_code, trade_date=trade_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到东方财富板块成分数据")]

            result = f"📊 **东方财富板块成分** (共{len(df)}条记录)\n\n"
            result += "| 板块代码 | 成分股代码 | 成分股名称 | 交易日期 |\n"
            result += "|----------|------------|------------|----------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('con_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('trade_date', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_daily_info":
            trade_date = arguments.get("trade_date", "")
            ts_code = arguments.get("ts_code", "")
            exchange = arguments.get("exchange", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            fields = arguments.get("fields", "")
            df = data_provider.get_daily_info(trade_date=trade_date, ts_code=ts_code, exchange=exchange, start_date=start_date, end_date=end_date, fields=fields)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到市场交易统计数据")]

            result = f"📊 **市场交易统计** (共{len(df)}条记录)\n\n"
            result += "| 交易日期 | 板块代码 | 板块名称 | 总市值 | 市盈率 |\n"
            result += "|----------|----------|----------|--------|--------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('trade_date', 'N/A')} | {row.get('ts_code', 'N/A')} | {row.get('ts_name', 'N/A')} | {row.get('total_mv', 'N/A')} | {row.get('pe', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]

        elif name == "get_sz_daily_info":
            trade_date = arguments.get("trade_date", "")
            ts_code = arguments.get("ts_code", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_sz_daily_info(trade_date=trade_date, ts_code=ts_code, start_date=start_date, end_date=end_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到深圳市场每日交易概况数据")]

            result = f"📊 **深圳市场每日交易概况** (共{len(df)}条记录)\n\n"
            result += "| 交易日期 | 板块代码 | 股票数量 | 成交金额 | 总市值 |\n"
            result += "|----------|----------|----------|----------|--------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('trade_date', 'N/A')} | {row.get('ts_code', 'N/A')} | {row.get('count', 'N/A')} | {row.get('amount', 'N/A')} | {row.get('total_mv', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_realtime_quotes":
            ts_codes = arguments["ts_codes"]
            df = data_provider.get_realtime_quotes(ts_codes)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到实时行情数据")]
            
            result = f"⚡ **实时行情** (共{len(df)}只股票)\n\n"
            result += "| 代码 | 当前价 | 涨跌幅 | 成交量 | 换手率 |\n"
            result += "|------|--------|--------|--------|--------|\n"
            
            for _, row in df.iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('close', 'N/A')} | {row.get('pct_chg', 'N/A')}% | {row.get('vol', 'N/A')} | {row.get('turnover_rate', 'N/A')}% |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        # 市场数据
        elif name == "get_top_list":
            trade_date = arguments.get("trade_date", "")
            df = data_provider.get_top_list(trade_date=trade_date)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到龙虎榜数据")]
            
            result = f"🐉 **龙虎榜数据** ({trade_date or '今日'})\n\n"
            result += "| 股票代码 | 股票名称 | 涨跌幅 | 成交额 |\n"
            result += "|----------|----------|--------|--------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('pct_chg', 'N/A')}% | {row.get('amount', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_money_flow":
            ts_code = arguments.get("ts_code", "")
            trade_date = arguments.get("trade_date", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_money_flow(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到资金流向数据")]
            
            result = f"💰 **资金流向数据** ({trade_date or '今日'})\n\n"
            result += "| 日期 | 主力净流入 | 超大单净流入 |\n"
            result += "|------|------------|-------------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('trade_date', 'N/A')} | {row.get('net_mf_amount', 'N/A')} | {row.get('net_mf_amount_xl', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_concept_detail":
            concept_name = arguments.get("concept_name", "")
            df = data_provider.get_concept_detail(concept_name=concept_name)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到概念股数据")]
            
            if concept_name:
                result = f"💡 **'{concept_name}' 概念股详情**\n\n"
                result += "| 股票代码 | 股票名称 | 行业 |\n"
                result += "|----------|----------|------|\n"
                
                for _, row in df.head(20).iterrows():
                    result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('industry', 'N/A')} |\n"
            else:
                result = f"💡 **所有概念板块**\n\n"
                result += "| 概念代码 | 概念名称 |\n"
                result += "|----------|----------|\n"
                
                for _, row in df.head(20).iterrows():
                    result += f"| {row.get('code', 'N/A')} | {row.get('name', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_margin_detail":
            trade_date = arguments.get("trade_date", "")
            exchange_id = arguments.get("exchange_id", "")
            df = data_provider.get_margin_detail(trade_date=trade_date, exchange_id=exchange_id)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到融资融券数据")]
            
            result = f"📊 **融资融券数据** ({trade_date or '今日'})\n\n"
            result += "| 股票代码 | 股票名称 | 融资余额 | 融券余额 |\n"
            result += "|----------|----------|----------|----------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('rzye', 'N/A')} | {row.get('rqye', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_block_trade":
            trade_date = arguments.get("trade_date", "")
            df = data_provider.get_block_trade(trade_date=trade_date)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到大宗交易数据")]
            
            result = f"📦 **大宗交易数据** ({trade_date or '今日'})\n\n"
            result += "| 股票代码 | 股票名称 | 成交价 | 成交量 | 成交额 |\n"
            result += "|----------|----------|--------|--------|--------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('price', 'N/A')} | {row.get('vol', 'N/A')} | {row.get('amount', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_financial_data":
            ts_code = arguments["ts_code"]
            period = arguments.get("period", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_financial_data(ts_code=ts_code, period=period, start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text=f"未获取到 {ts_code} 的财务数据（可能需要Pro权限）")]
            
            result = f"💰 **{ts_code} 财务数据**\n\n"
            result += "| 报告期 | 营业收入 | 净利润 | 总资产 |\n"
            result += "|--------|----------|--------|--------|\n"
            
            for _, row in df.head(5).iterrows():
                result += f"| {row.get('end_date', 'N/A')} | {row.get('total_revenue', 'N/A')} | {row.get('n_income', 'N/A')} | {row.get('total_assets', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_balance_sheet":
            ts_code = arguments.get("ts_code", "")
            period = arguments.get("period", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            is_vip = arguments.get("is_vip", False)
            df = data_provider.get_balance_sheet(ts_code=ts_code, period=period, start_date=start_date, end_date=end_date, is_vip=is_vip)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到资产负债表数据")]

            result = f"📊 **资产负债表数据** (共{len(df)}条记录)\n\n"
            result += "| 股票代码 | 报告期 | 总资产 | 总负债 | 股东权益 |\n"
            result += "|----------|----------|----------|----------|----------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('end_date', 'N/A')} | {row.get('total_assets', 'N/A')} | {row.get('total_liab', 'N/A')} | {row.get('total_hldr_eqy_inc_min_int', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_cash_flow":
            ts_code = arguments.get("ts_code", "")
            period = arguments.get("period", "")
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            is_vip = arguments.get("is_vip", False)
            df = data_provider.get_cash_flow(ts_code=ts_code, period=period, start_date=start_date, end_date=end_date, is_vip=is_vip)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到现金流量表数据")]

            result = f"📊 **现金流量表数据** (共{len(df)}条记录)\n\n"
            result += "| 股票代码 | 报告期 | 经营活动现金流 | 投资活动现金流 | 筹资活动现金流 |\n"
            result += "|----------|----------|----------------|----------------|----------------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('end_date', 'N/A')} | {row.get('n_cashflow_act', 'N/A')} | {row.get('n_cashflow_inv_act', 'N/A')} | {row.get('n_cashflow_fin_act', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_fina_indicator":
            ts_code = arguments["ts_code"]
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_fina_indicator(ts_code=ts_code, start_date=start_date, end_date=end_date)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到财务指标数据")]

            result = f"📊 **财务指标数据** (共{len(df)}条记录)\n\n"
            result += "| 股票代码 | 报告期 | ROE | 资产负债率 | 毛利率 |\n"
            result += "|----------|----------|-----|------------|---------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('end_date', 'N/A')} | {row.get('roe', 'N/A')} | {row.get('debt_to_assets', 'N/A')} | {row.get('gross_margin', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_fina_mainbz":
            ts_code = arguments.get("ts_code", "")
            period = arguments.get("period", "")
            type = arguments.get("type", "")
            is_vip = arguments.get("is_vip", False)
            df = data_provider.get_fina_mainbz(ts_code=ts_code, period=period, type=type, is_vip=is_vip)

            if df.empty:
                return [types.TextContent(type="text", text="未获取到主营业务构成数据")]

            result = f"📊 **主营业务构成数据** (共{len(df)}条记录)\n\n"
            result += "| 股票代码 | 报告期 | 业务项目 | 业务收入 | 业务利润 |\n"
            result += "|----------|----------|----------|----------|----------|\n"

            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('end_date', 'N/A')} | {row.get('bz_item', 'N/A')} | {row.get('bz_sales', 'N/A')} | {row.get('bz_profit', 'N/A')} |\n"

            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 条记录"

            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_fund_basic":
            market = arguments.get("market", "E")
            df = data_provider.get_fund_basic(market=market)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到基金数据")]
            
            market_name = "场内基金" if market == "E" else "场外基金"
            result = f"💼 **{market_name}基本信息** (共{len(df)}只)\n\n"
            result += "| 基金代码 | 基金名称 | 基金类型 | 管理人 |\n"
            result += "|----------|----------|----------|--------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('fund_type', 'N/A')} | {row.get('management', 'N/A')} |\n"
            
            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 只基金"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_index_data":
            ts_code = arguments["ts_code"]
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_index_data(ts_code=ts_code, start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text=f"未获取到指数 {ts_code} 的数据")]
            
            result = f"📊 **指数 {ts_code} 行情**\n\n"
            result += "| 日期 | 开盘 | 最高 | 最低 | 收盘 | 成交量 |\n"
            result += "|------|------|------|------|------|--------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('trade_date', row.name)} | {row.get('open', 'N/A')} | {row.get('high', 'N/A')} | {row.get('low', 'N/A')} | {row.get('close', 'N/A')} | {row.get('vol', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_market_summary":
            date = arguments.get("date", datetime.now().strftime('%Y%m%d'))
            
            # 获取主要指数数据
            major_indices = [
                ("000001.SH", "上证指数"),
                ("399001.SZ", "深证成指"), 
                ("399006.SZ", "创业板指"),
                ("000300.SH", "沪深300")
            ]
            
            result = f"📊 **市场概况** ({date})\n\n"
            result += "| 指数 | 最新价 | 涨跌幅 | 成交量 |\n"
            result += "|------|--------|--------|--------|\n"
            
            for code, name in major_indices:
                df = data_provider.get_index_data(ts_code=code, start_date=date, end_date=date)
                if not df.empty:
                    row = df.iloc[0]
                    result += f"| {name} | {row.get('close', 'N/A')} | {row.get('pct_chg', 'N/A')}% | {row.get('vol', 'N/A')} |\n"
                else:
                    result += f"| {name} | N/A | N/A | N/A |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        # ================ ETF和指数数据工具处理 ================
        elif name == "get_etf_basic":
            market = arguments.get("market", "E")
            df = data_provider.get_etf_basic(market=market)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到ETF数据")]
            
            market_name = "场内ETF" if market == "E" else "场外ETF"
            result = f"📊 **{market_name}基本信息** (共{len(df)}只)\n\n"
            result += "| ETF代码 | ETF名称 | 基金类型 | 管理人 |\n"
            result += "|---------|---------|----------|--------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('fund_type', 'N/A')} | {row.get('management', 'N/A')} |\n"
            
            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 只ETF"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_etf_daily":
            ts_code = arguments["ts_code"]
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_etf_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text=f"未获取到 {ts_code} 的ETF行情数据")]
            
            result = f"📈 **{ts_code} ETF行情** (共{len(df)}条记录)\n\n"
            result += "| 日期 | 开盘 | 最高 | 最低 | 收盘 | 成交量 |\n"
            result += "|------|------|------|------|------|--------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('trade_date', 'N/A')} | {row.get('open', 'N/A')} | {row.get('high', 'N/A')} | {row.get('low', 'N/A')} | {row.get('close', 'N/A')} | {row.get('vol', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_index_basic":
            market = arguments.get("market", "")
            df = data_provider.get_index_basic(market=market)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到指数基本信息")]
            
            result = f"📊 **指数基本信息** (共{len(df)}个指数)\n\n"
            result += "| 指数代码 | 指数名称 | 市场 | 发布机构 |\n"
            result += "|----------|----------|------|----------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('market', 'N/A')} | {row.get('publisher', 'N/A')} |\n"
            
            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 个指数"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_index_weight":
            index_code = arguments["index_code"]
            trade_date = arguments.get("trade_date", "")
            df = data_provider.get_index_weight(index_code=index_code, trade_date=trade_date)
            
            if df.empty:
                return [types.TextContent(type="text", text=f"未获取到指数 {index_code} 的成分股权重")]
            
            result = f"⚖️ **{index_code} 成分股权重** ({trade_date or '最新'})\n\n"
            result += "| 股票代码 | 股票名称 | 权重(%) |\n"
            result += "|----------|----------|----------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('con_code', 'N/A')} | {row.get('con_name', 'N/A')} | {row.get('weight', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        # ================ 债券数据工具处理 ================
        elif name == "get_bond_basic":
            ts_code = arguments.get("ts_code", "")
            df = data_provider.get_bond_basic(ts_code=ts_code)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到债券数据")]
            
            result = f"🏦 **债券基本信息** (共{len(df)}只债券)\n\n"
            result += "| 债券代码 | 债券名称 | 债券类型 | 发行日期 |\n"
            result += "|----------|----------|----------|----------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('bond_type', 'N/A')} | {row.get('issue_date', 'N/A')} |\n"
            
            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 只债券"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_bond_daily":
            ts_code = arguments["ts_code"]
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_bond_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text=f"未获取到 {ts_code} 的债券行情数据")]
            
            result = f"📈 **{ts_code} 债券行情** (共{len(df)}条记录)\n\n"
            result += "| 日期 | 开盘 | 最高 | 最低 | 收盘 | 成交量 |\n"
            result += "|------|------|------|------|------|--------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('trade_date', 'N/A')} | {row.get('open', 'N/A')} | {row.get('high', 'N/A')} | {row.get('low', 'N/A')} | {row.get('close', 'N/A')} | {row.get('vol', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_cb_basic":
            df = data_provider.get_cb_basic()
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到可转债数据")]
            
            result = f"🔄 **可转债基本信息** (共{len(df)}只)\n\n"
            result += "| 转债代码 | 转债名称 | 正股代码 | 正股名称 |\n"
            result += "|----------|----------|----------|----------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('cb_name', 'N/A')} | {row.get('stk_code', 'N/A')} | {row.get('stk_name', 'N/A')} |\n"
            
            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 只可转债"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_cb_daily":
            ts_code = arguments["ts_code"]
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_cb_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text=f"未获取到 {ts_code} 的可转债行情数据")]
            
            result = f"📈 **{ts_code} 可转债行情** (共{len(df)}条记录)\n\n"
            result += "| 日期 | 开盘 | 最高 | 最低 | 收盘 | 成交量 |\n"
            result += "|------|------|------|------|------|--------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('trade_date', 'N/A')} | {row.get('open', 'N/A')} | {row.get('high', 'N/A')} | {row.get('low', 'N/A')} | {row.get('close', 'N/A')} | {row.get('vol', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        # ================ 扩展基金数据工具处理 ================
        elif name == "get_fund_daily":
            ts_code = arguments["ts_code"]
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_fund_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text=f"未获取到 {ts_code} 的基金净值数据")]
            
            result = f"📊 **{ts_code} 基金净值** (共{len(df)}条记录)\n\n"
            result += "| 日期 | 单位净值 | 累计净值 | 日增长率 |\n"
            result += "|------|----------|----------|----------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('trade_date', 'N/A')} | {row.get('nav', 'N/A')} | {row.get('acc_nav', 'N/A')} | {row.get('daily_return', 'N/A')}% |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_fund_portfolio":
            ts_code = arguments["ts_code"]
            period = arguments.get("period", "")
            df = data_provider.get_fund_portfolio(ts_code=ts_code, period=period)
            
            if df.empty:
                return [types.TextContent(type="text", text=f"未获取到 {ts_code} 的基金持仓数据")]
            
            result = f"💼 **{ts_code} 基金持仓** ({period or '最新'})\n\n"
            result += "| 股票代码 | 股票名称 | 持仓比例(%) | 市值(万元) |\n"
            result += "|----------|----------|-------------|------------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('mkv_ratio', 'N/A')} | {row.get('mkv', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_fund_rating":
            ts_code = arguments.get("ts_code", "")
            df = data_provider.get_fund_rating(ts_code=ts_code)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到基金评级数据")]
            
            result = f"⭐ **基金评级数据** (共{len(df)}只基金)\n\n"
            result += "| 基金代码 | 基金名称 | 评级机构 | 评级 | 评级日期 |\n"
            result += "|----------|----------|----------|------|----------|\n"
            
            for _, row in df.head(20).iterrows():
                result += f"| {row.get('ts_code', 'N/A')} | {row.get('name', 'N/A')} | {row.get('rating_agency', 'N/A')} | {row.get('rating', 'N/A')} | {row.get('rating_date', 'N/A')} |\n"
            
            if len(df) > 20:
                result += f"\n... 还有 {len(df) - 20} 只基金"
            
            return [types.TextContent(type="text", text=result)]
        
        # ================ 宏观经济数据工具处理 ================
        elif name == "get_gdp_data":
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_gdp_data(start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到GDP数据")]
            
            result = f"📊 **GDP数据** (共{len(df)}条记录)\n\n"
            result += "| 季度 | GDP(亿元) | 同比增长(%) | 环比增长(%) |\n"
            result += "|------|-----------|-------------|-------------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('quarter', 'N/A')} | {row.get('gdp', 'N/A')} | {row.get('gdp_yoy', 'N/A')} | {row.get('gdp_qoq', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_cpi_data":
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_cpi_data(start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到CPI数据")]
            
            result = f"📊 **CPI数据** (共{len(df)}条记录)\n\n"
            result += "| 月份 | CPI | 同比增长(%) | 环比增长(%) |\n"
            result += "|------|-----|-------------|-------------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('month', 'N/A')} | {row.get('cpi', 'N/A')} | {row.get('cpi_yoy', 'N/A')} | {row.get('cpi_mom', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_interest_rate":
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_interest_rate(start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到利率数据")]
            
            result = f"📊 **SHIBOR利率数据** (共{len(df)}条记录)\n\n"
            result += "| 日期 | 隔夜 | 1周 | 2周 | 1月 | 3月 |\n"
            result += "|------|------|-----|-----|-----|-----|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('date', 'N/A')} | {row.get('on', 'N/A')} | {row.get('1w', 'N/A')} | {row.get('2w', 'N/A')} | {row.get('1m', 'N/A')} | {row.get('3m', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_exchange_rate":
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_exchange_rate(start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到汇率数据")]
            
            result = f"📊 **汇率数据** (共{len(df)}条记录)\n\n"
            result += "| 日期 | 美元/人民币 | 欧元/人民币 | 日元/人民币 |\n"
            result += "|------|-------------|-------------|-------------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('trade_date', 'N/A')} | {row.get('usdcny', 'N/A')} | {row.get('eurcny', 'N/A')} | {row.get('jpycny', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_pmi_data":
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_pmi_data(start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到PMI数据")]
            
            result = f"📊 **PMI数据** (共{len(df)}条记录)\n\n"
            result += "| 月份 | 制造业PMI | 非制造业PMI | 综合PMI |\n"
            result += "|------|-----------|-------------|----------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('month', 'N/A')} | {row.get('pmi', 'N/A')} | {row.get('nmi', 'N/A')} | {row.get('cpi', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        elif name == "get_money_supply":
            start_date = arguments.get("start_date", "")
            end_date = arguments.get("end_date", "")
            df = data_provider.get_money_supply(start_date=start_date, end_date=end_date)
            
            if df.empty:
                return [types.TextContent(type="text", text="未获取到货币供应量数据")]
            
            result = f"📊 **货币供应量数据** (共{len(df)}条记录)\n\n"
            result += "| 月份 | M0(亿元) | M1(亿元) | M2(亿元) | M1同比(%) | M2同比(%) |\n"
            result += "|------|----------|----------|----------|-----------|-----------|\n"
            
            for _, row in df.head(10).iterrows():
                result += f"| {row.get('month', 'N/A')} | {row.get('m0', 'N/A')} | {row.get('m1', 'N/A')} | {row.get('m2', 'N/A')} | {row.get('m1_yoy', 'N/A')} | {row.get('m2_yoy', 'N/A')} |\n"
            
            return [types.TextContent(type="text", text=result)]
        
        else:
            return [types.TextContent(type="text", text=f"未知工具: {name}")]
    
    except Exception as e:
        return [types.TextContent(type="text", text=f"执行工具 {name} 时发生错误: {str(e)}")]


async def main():
    """主函数, 设置并运行 MCP 服务器"""
    token = os.getenv('TUSHARE_TOKEN')
    if not token:
        print("⚠️  未设置 TUSHARE_TOKEN 环境变量，功能将受限。")
        print("   请访问 https://tushare.pro/ 注册以获取 Token。")
    
    # 在服务器运行前初始化 data_provider
    global data_provider
    data_provider = TushareDataProvider(token)
    
    # 运行服务器
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            initialization_options=InitializationOptions(
                server_name="tushare-mcp-server",
                server_version="0.1.4",
                capabilities={}
            )
        )

def cli_main():
    """命令行入口函数"""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n服务器已关闭。")

if __name__ == "__main__":
    cli_main()
