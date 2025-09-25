from __future__ import annotations
from typing import Optional, Dict, Any, TYPE_CHECKING
from datacenter_client.dto import SWIndustryCompanyListResponse

if TYPE_CHECKING:
    from ..base import BaseClient


class SWIndustryCompanyClient:
    """Client for SW-Industry-Company related endpoints."""
    def __init__(self, client: "BaseClient"):
        self._client = client

    def page_list(
        self,
        page: int = 1,
        page_size: int = 50,
        stock_code: Optional[str] = None,
        stock_name: Optional[str] = None,
        industry_code: Optional[str] = None,
        level1_industry_code: Optional[str] = None,
        level2_industry_code: Optional[str] = None,
        level3_industry_code: Optional[str] = None
    ) -> SWIndustryCompanyListResponse:
        """
        Get a paginated list of SW-industry companies.
        Corresponds to GET /sw_industry_company/page_list
        
        Args:
            page: 页码，从1开始
            page_size: 每页数量，最大1000
            stock_code: 股票代码
            stock_name: 股票名称
            industry_code: 行业代码
            level1_industry_code: 一级行业代码
            level2_industry_code: 二级行业代码
            level3_industry_code: 三级行业代码
            
        Returns:
            Dict[str, Any]: 包含申万行业公司列表和分页信息的响应
            
        Raises:
            ValueError: 当没有提供任何查询条件时
        """
        # 验证至少提供一个查询条件
        if not any([stock_code, stock_name, industry_code, level1_industry_code, level2_industry_code, level3_industry_code]):
            raise ValueError("必须提供至少一个查询条件")
        
        params: Dict[str, Any] = {"page": page, "page_size": page_size}
        if stock_code:
            params["stock_code"] = stock_code
        if stock_name:
            params["stock_name"] = stock_name
        if industry_code:
            params["industry_code"] = industry_code
        if level1_industry_code:
            params["level1_industry_code"] = level1_industry_code
        if level2_industry_code:
            params["level2_industry_code"] = level2_industry_code
        if level3_industry_code:
            params["level3_industry_code"] = level3_industry_code
        
        return SWIndustryCompanyListResponse(**self._client._request("GET", "/api/v1/sw_industry_company/page_list", params=params))

    def list(
        self,
        stock_code: Optional[str] = None,
        stock_name: Optional[str] = None,
        industry_code: Optional[str] = None,
        level1_industry_code: Optional[str] = None,
        level2_industry_code: Optional[str] = None,
        level3_industry_code: Optional[str] = None
    ) -> SWIndustryCompanyListResponse:
        """
        Get a list of SW-industry companies without pagination.
        Corresponds to GET /sw_industry_company/list
        
        Args:
            stock_code: 股票代码
            stock_name: 股票名称
            industry_code: 行业代码
            level1_industry_code: 一级行业代码
            level2_industry_code: 二级行业代码
            level3_industry_code: 三级行业代码
            
        Returns:
            Dict[str, Any]: 包含申万行业公司列表的响应
            
        Raises:
            ValueError: 当没有提供任何查询条件时
        """
        # 验证至少提供一个查询条件
        if not any([stock_code, stock_name, industry_code, level1_industry_code, level2_industry_code, level3_industry_code]):
            raise ValueError("必须提供至少一个查询条件")
        
        params: Dict[str, Any] = {}
        if stock_code:
            params["stock_code"] = stock_code
        if stock_name:
            params["stock_name"] = stock_name
        if industry_code:
            params["industry_code"] = industry_code
        if level1_industry_code:
            params["level1_industry_code"] = level1_industry_code
        if level2_industry_code:
            params["level2_industry_code"] = level2_industry_code
        if level3_industry_code:
            params["level3_industry_code"] = level3_industry_code
        
        return SWIndustryCompanyListResponse(**self._client._request("GET", "/api/v1/sw_industry_company/list", params=params))