from abc import ABC, abstractmethod

class DataSourceInterface(ABC):
    @abstractmethod
    def get_datasource_name(self):
        """数据源名称"""
        pass

    @abstractmethod
    def get_datasource_meta_vector(self):
        """数据源名称"""
        pass

    @abstractmethod
    def get_port_tags(self):
        """获取产品标签"""
        pass

    @abstractmethod
    def get_port_inds(self):
        """获取产品相关指标列表"""
        pass

    @abstractmethod
    def get_asset_tags(self):
        """获取资产标签列表"""
        pass

    @abstractmethod
    def get_asset_inds(self):
        """获取资产持仓指标列表"""
        pass

    @abstractmethod
    def get_basic_inds(self):
        """获取基础列指标"""
        pass

    @abstractmethod
    def get_data(self, run_method: str, data_subject: str, sec_ids: list=[], port_ids: list=[],
             tags: list=[], inds: list=[], start_date = None, end_date = None, penetrate=None):
        """获取持仓数据"""
        pass

    @abstractmethod
    def get_repository_inds(self, run_method: str, repository: str, ind_list: list, params: dict):
        """获取指标库内的相关指标数据"""
        pass

    @abstractmethod
    def get_repository_metadata(self, rep_list: list):
        """获取指标库的元数据"""
        pass

    @abstractmethod
    def get_all_repository_metadata(self):
        """一次性获取所有指标库的元数据"""
        pass

    @abstractmethod
    def get_repository_params(self, rep_list: list):
        """获取指标库的所需的参数元数据"""
        pass

    @abstractmethod
    def get_repository_inds_meta(self, rep_dict: dict):
        """获取指标库的指标的元数据"""
        pass

