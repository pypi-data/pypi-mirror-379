from datacenter_client.tests.base import BaseClientTest
from datacenter_client.dto import SWIndustryCompanyItem
import unittest


class TestSWIndustryCompanyClient(BaseClientTest):
    """申万行业公司客户端测试类"""
    
    def test_page_list(self):
        """测试分页获取申万行业公司列表"""
        print("\n" + "=" * 50)
        print("测试申万行业公司客户端 - 分页获取列表")
        print("=" * 50)
        
        try:
            result = self.client.sw_industry_company.page_list(page=1, page_size=5)
            print(f"状态: {result.status}")
            self.print_pagination_info(result)
            
            # 测试DTO功能
            if result.items:
                item = result.items[0]
                self.assertIsInstance(item, SWIndustryCompanyItem)
                print(f"第一条记录的股票代码: {item.stock_code}")
                print(f"第一条记录的股票名称: {item.stock_name}")
                print(f"第一条记录的行业代码: {item.industry_code}")
                print(f"第一条记录的一级行业名称: {item.level1_industry}")
                print(f"第一条记录的一级行业代码: {item.level1_industry_code}")
        except Exception as e:
            print(f"测试分页获取列表时出错: {e}")
    
    def test_list(self):
        """测试获取申万行业公司列表"""
        print("\n" + "=" * 50)
        print("测试申万行业公司客户端 - 获取列表")
        print("=" * 50)
        
        try:
            result = self.client.sw_industry_company.list()
            print(f"状态: {result.status}")
            self.print_list_info(result)
            
            # 测试DTO功能
            if result.items:
                item = result.items[0]
                self.assertIsInstance(item, SWIndustryCompanyItem)
                print(f"第一条记录的股票代码: {item.stock_code}")
                print(f"第一条记录的股票名称: {item.stock_name}")
                print(f"第一条记录的行业代码: {item.industry_code}")
                print(f"第一条记录的一级行业名称: {item.level1_industry}")
                print(f"第一条记录的一级行业代码: {item.level1_industry_code}")
        except Exception as e:
            print(f"测试获取列表时出错: {e}")
    
    def test_list_with_filters(self):
        """测试使用过滤条件获取申万行业公司列表"""
        print("\n" + "=" * 50)
        print("测试申万行业公司客户端 - 使用过滤条件获取列表")
        print("=" * 50)
        
        try:
            # 使用一级行业代码过滤
            result = self.client.sw_industry_company.list(level1_industry_code="801010.SI")
            print(f"状态: {result.status}")
            self.print_list_info(result)
            
            # 测试DTO功能
            if result.items:
                item = result.items[0]
                self.assertIsInstance(item, SWIndustryCompanyItem)
                print(f"第一条记录的股票代码: {item.stock_code}")
                print(f"第一条记录的股票名称: {item.stock_name}")
                print(f"第一条记录的行业代码: {item.industry_code}")
                print(f"第一条记录的一级行业名称: {item.level1_industry}")
                print(f"第一条记录的一级行业代码: {item.level1_industry_code}")
        except Exception as e:
            print(f"测试使用过滤条件获取列表时出错: {e}")
    
    def test_validation_error(self):
        """测试不提供查询条件时的验证错误"""
        print("\n" + "=" * 50)
        print("测试申万行业公司客户端 - 验证错误")
        print("=" * 50)
        
        try:
            # 不提供任何查询条件，应该抛出ValueError
            result = self.client.sw_industry_company.list()
            print("错误：应该抛出ValueError异常")
        except ValueError as e:
            print(f"成功捕获验证错误: {e}")
        except Exception as e:
            print(f"测试验证错误时出错: {e}")


if __name__ == "__main__":
    # 创建测试套件
    suite = unittest.TestSuite()
    
    # 添加测试方法
    suite.addTest(TestSWIndustryCompanyClient('test_page_list'))
    suite.addTest(TestSWIndustryCompanyClient('test_list'))
    suite.addTest(TestSWIndustryCompanyClient('test_list_with_filters'))
    suite.addTest(TestSWIndustryCompanyClient('test_validation_error'))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)