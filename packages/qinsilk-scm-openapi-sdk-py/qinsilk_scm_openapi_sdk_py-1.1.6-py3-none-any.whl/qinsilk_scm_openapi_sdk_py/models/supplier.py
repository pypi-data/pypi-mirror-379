"""
供应商相关的API请求和响应模型
"""
from .base import BaseRequest, BaseResponse


class SupplierSaveDTO:
    """供应商保存数据传输对象"""
    
    def __init__(self, supplier_name=None, supplier_type=None, status=None, id=None, code=None, 
                 supplier_name_py=None, virtual_storehouse_id=None, cellphone=None, level_id=None, 
                 province_id=None, city_id=None, county_id=None, address=None, show_order=None, 
                 remark=None, bank=None, bank_account=None, bank_account_id=None, bank_remark=None):
        self.supplier_name = supplier_name  # 供应商名称（必填）
        self.supplier_type = supplier_type  # 供应商类型（必填）
        self.status = status  # 状态（必填）
        self.id = id
        self.code = code
        self.supplier_name_py = supplier_name_py
        self.virtual_storehouse_id = virtual_storehouse_id
        self.cellphone = cellphone
        self.level_id = level_id
        self.province_id = province_id
        self.city_id = city_id
        self.county_id = county_id
        self.address = address
        self.show_order = show_order
        self.remark = remark
        self.bank = bank
        self.bank_account = bank_account
        self.bank_account_id = bank_account_id
        self.bank_remark = bank_remark

    def to_dict(self):
        return {
            'supplierName': self.supplier_name,
            'supplierType': self.supplier_type,
            'status': self.status,
            'id': self.id,
            'code': self.code,
            'supplierNamePy': self.supplier_name_py,
            'virtualStorehouseId': self.virtual_storehouse_id,
            'cellphone': self.cellphone,
            'levelId': self.level_id,
            'provinceId': self.province_id,
            'cityId': self.city_id,
            'countyId': self.county_id,
            'address': self.address,
            'showOrder': self.show_order,
            'remark': self.remark,
            'bank': self.bank,
            'bankAccount': self.bank_account,
            'bankAccountId': self.bank_account_id,
            'bankRemark': self.bank_remark
        }


class SupplierDetail:
    """供应商详情"""
    
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.id = data.get('id')
        self.supplier_name = data.get('supplierName')
        self.code = data.get('code')
        self.supplier_name_py = data.get('supplierNamePy')
        self.supplier_type = data.get('supplierType')
        self.virtual_storehouse = data.get('virtualStorehouse')
        self.virtual_storehouse_id = data.get('virtualStorehouseId')
        self.cellphone = data.get('cellphone')
        self.level_id = data.get('levelId')
        self.province_id = data.get('provinceId')
        self.city_id = data.get('cityId')
        self.county_id = data.get('countyId')
        self.address = data.get('address')
        self.show_order = data.get('showOrder')
        self.status = data.get('status')
        self.remark = data.get('remark')
        self.bank = data.get('bank')
        self.bank_account = data.get('bankAccount')
        self.bank_account_id = data.get('bankAccountId')
        self.bank_remark = data.get('bankRemark')


class SupplierSaveRequest(BaseRequest):
    """新增供应商请求"""
    
    def __init__(self):
        super().__init__()
        self.supplier_save_dto = None

    def get_api_url(self):
        return 'api/open/supplier/base/add'

    def get_version(self):
        return "1.0"
    
    def response_class(self):
        return SupplierDetailResponse
    
    def get_request_body(self):
        if self.supplier_save_dto:
            return {"supplierSaveDto": self.supplier_save_dto.to_dict()}
        return {}


class SupplierDetailRequest(BaseRequest):
    """供应商详情请求"""
    
    def __init__(self):
        super().__init__()
        self.supplier_id = None

    def get_api_url(self):
        return 'api/open/supplier/base/get'

    def get_version(self):
        return "1.0"
    
    def response_class(self):
        return SupplierDetailResponse
    
    def get_request_body(self):
        return {"supplierId": self.supplier_id}


class SupplierListRequest(BaseRequest):
    """供应商列表请求"""
    
    def __init__(self):
        super().__init__()
        self.supplier_name = None
        self.code = None
        self.page = 1
        self.size = 10

    def get_api_url(self):
        return 'api/open/supplier/base/list'

    def get_version(self):
        return "1.0"
    
    def response_class(self):
        return SupplierListResponse
    
    def get_request_body(self):
        body = {
            "page": self.page,
            "size": self.size
        }
        if self.supplier_name:
            body["supplierName"] = self.supplier_name
        if self.code:
            body["code"] = self.code
        return body


class SupplierDetailResponse(BaseResponse):
    """供应商详情响应"""
    
    def __init__(self, response_data=None):
        super().__init__(response_data)
        if response_data and 'data' in response_data:
            self.data = SupplierDetail(response_data['data'])
        else:
            self.data = None


class SupplierListResponse(BaseResponse):
    """供应商列表响应"""
    
    def __init__(self, response_data=None):
        super().__init__(response_data)
        if response_data and 'data' in response_data:
            self.data = [SupplierDetail(item) for item in response_data['data']]
        else:
            self.data = []