# -*- coding:utf-8 -*-
from .check import check, check_not_empty, check_when, check_when_each, check_list_when, check_list, check_nested, DataChecker

"""
General-Validator validate系列数据校验函数 - check系列函数的断言模式别名，方便调用，同时保持完全向后兼容

validate系列函数遵循assert“失败即异常”的理念，校验成功时返回ValidationResult，校验失败时抛出ValidationError，适用场景：
- 需要精确错误定位的数据验证场景
- 异常驱动的错误处理逻辑
- 详细失败信息的调试场景
- 数据质量监控和分析
"""

def validate(data, *validations, max_fail=None, fast_fail=True, output_format="summary"):
    """
    极简数据校验入口函数 - check函数的断言模式别名
    
    :param data: 要校验的数据
    :param validations: 校验规则，支持多种简洁格式
    :param max_fail: 失败阈值
        - None: 严格模式，一个失败全部失败（默认，保持完全兼容性）
        - int: 每个规则最多允许N个失败 (如 max_fail=3)
        - float: 每个规则最多允许N%失败率 (如 max_fail=0.1 表示10%)

    :param output_format: 校验结果输出格式：summary/detail/dict
    :return: ValidationResult: 校验成功时返回ValidationResult对象
    :raises: ValidationError: 校验失败时抛出ValidationError对象
    
    用法示例：
    1. 成功场景 - 获取详细校验结果
    try:
        result = validate(data, "field1", "field2 > 0", "field3")
        print(f"校验成功: {result.summary}")
        print(f"共校验了 {result.total_rules} 个规则，全部通过")
        
        # 查看每个规则的执行详情
        for rule_result in result.rule_results:
            print(f"规则 '{rule_result.rule}': {rule_result.passed_fields}/{rule_result.total_fields} 字段通过")
    
    2. 失败场景 - 快速定位问题根源
    except ValidationError as e:
        print(f"校验失败: {str(e)}")
        
        # 快速定位：第一个失败的规则和字段
        first_failed_rule = e.get_first_failed_rule()
        first_failed_field = e.get_first_failed_field()
        if first_failed_field:
            print(f"首个失败: {first_failed_field.field_path} -> {first_failed_field.message}")
        
        # 详细分析：遍历所有失败项
        for rule_result in e.result.get_failed_rules():
            print(f"失败规则: {rule_result.rule}")
            for field_result in [f for f in rule_result.field_results if not f.success]:
                print(f"  - {field_result.field_path}: 期望{field_result.expect_value}, 实际{field_result.actual_value}")
    
    3. 阈值模式 - 灵活的质量控制
    try:
        result = validate(data, "users.*.id > 0", "users.*.name", max_fail=0.1)  # 允许10%失败
        print(f"校验通过: {result.summary}")
        if result.execution_mode == "threshold":
            print("在可接受的质量范围内")
    except ValidationError as e:
        print(f"质量不达标: {e}")
        print(f"失败率超过了设定的阈值 ({e.result.max_fail_info})")
    """
    return check(data, *validations, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode="assert")


def validate_not_empty(data, *validations, max_fail=None, fast_fail=True, output_format="summary"):
    """
    专门的非空校验 - check_not_empty函数的断言模式别名

    :param data: 待校验的数据
    :param validations: 校验规则，支持多种简洁格式
    :param max_fail: 失败阈值
    :param fast_fail: 快速失败，默认True
    :param output_format: 校验结果输出格式：summary/detail/dict
    :return: ValidationResult: 校验成功时返回ValidationResult对象
    :raises: ValidationError: 校验失败时抛出ValidationError对象

    用法示例：
    try:
        result = validate_not_empty(data, "field1", "field2")
        print(f"非空校验成功: {result}")
    except ValidationError as e:
        print(f"非空校验失败: {e}")
    """
    return check_not_empty(data, *validations, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode="assert")


def validate_when(data, condition, *then, max_fail=None, fast_fail=True, output_format="summary"):
    """
    严格条件校验 - check_when函数的断言模式别名

    语义说明：
    1. 对所有数据项进行条件校验
    2. 如果所有数据项都满足条件，就执行then规则校验
    3. 如果任一数据项不满足条件，就跳过整个then校验
    4. 每个then规则有独立的统计维度
    
    :param data: 要校验的数据
    :param condition: 条件表达式，支持所有校验器语法
    :param then: then表达式，支持所有校验器语法，可传入多个校验规则
    :param max_fail: 失败阈值
        - None: 严格模式，一个失败全部失败（默认）
        - int: 每个规则最多允许N个失败
        - float: 每个规则最多允许N%失败率

    :param fast_fail: 快速失败，默认True
    :param output_format: 校验结果输出格式：summary/detail/dict
    :return: ValidationResult: 校验成功时返回ValidationResult对象
    :raises: ValidationError: 校验失败时抛出ValidationError对象
    
    用法示例：
    try:
        result = validate_when(data, "products.*.status == 'active'", "products.*.price > 0")
        print(f"条件校验成功: {result}")
    except ValidationError as e:
        print(f"条件校验失败: {e}")
    """
    return check_when(data, condition, *then, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode="assert")


def validate_when_each(data, condition, *then, max_fail=None, fast_fail=True, output_format="summary"):
    """
    逐项条件校验 - check_when_each函数的断言模式别名
    
    语义说明：
    1. 通过路径表达式定位要检查的数据项列表
    2. 对每个数据项分别进行条件检查
    3. 对满足条件的数据项执行then规则校验，不满足则跳过
    4. 每个then规则按照满足条件的数据项独立统计失败率
    
    :param data: 要校验的数据（任意类型）
    :param condition: 条件表达式，使用路径表达式，如 "users.*.status == 'active'"
    :param then: then规则，使用路径表达式，如 "users.*.score > 70"，可传入多个校验规则
    :param max_fail: 失败阈值
        - None: 严格模式，一个失败全部失败（默认）
        - int: 每个规则最多允许N个失败
        - float: 每个规则最多允许N%失败率
    :param fast_fail: 快速失败，默认True
    :param output_format: 校验结果输出格式：summary/detail/dict
    :return: ValidationResult: 校验成功时返回ValidationResult对象
    :raises: ValidationError: 校验失败时抛出ValidationError对象

    用法示例：
    try:
        result = validate_when_each(data, "users.*.status == 'active'", "users.*.score > 70")
        print(f"逐项校验成功: {result}")
    except ValidationError as e:
        print(f"逐项校验失败: {e}")
    """
    return check_when_each(data, condition, *then, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode="assert")


def validate_list_when(data_list, condition, *then, max_fail=None, fast_fail=True, output_format="summary"):
    """
    列表逐项条件校验 - check_list_when函数的断言模式别名

    语义说明：
    1. 针对数据项列表，对每个数据项分别进行条件检查
    2. 对满足条件的数据项执行then规则校验，不满足则跳过
    3. 每个then规则按照满足条件的数据项独立统计失败率
    4. 每个then规则的失败率 = (满足条件但then失败的数据项数) / (满足条件的数据项总数)

    :param data_list: 要校验的数据列表
    :param condition: 条件表达式，支持所有校验器语法
    :param then: then表达式，支持所有校验器语法，可传入多个校验规则
    :param max_fail: 失败阈值
        - None: 严格模式，一个失败全部失败（默认）
        - int: 每个规则最多允许N个失败
        - float: 每个规则最多允许N%失败率

    :param fast_fail: 快速失败，默认True
    :param output_format: 校验结果输出格式：summary/detail/dict
    :return: ValidationResult: 校验成功时返回ValidationResult对象
    :raises: ValidationError: 校验失败时抛出ValidationError对象

    用法示例：
    try:
        users = [{"name": "张三", "status": "active", "score": 85}, ...]
        result = validate_list_when(users, "status == 'active'", "score > 70")
        print(f"列表条件校验成功: {result}")
    except ValidationError as e:
        print(f"列表条件校验失败: {e}")
    """
    return check_list_when(data_list, condition, *then, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode="assert")


def validate_list(data_list, *validations, max_fail=None, fast_fail=True, output_format="summary", **named_validations):
    """
    列表数据批量校验 - check_list函数的断言模式别名
    
    :param data_list: 数据列表
    :param validations: 字段校验规则（默认非空校验，同时支持符号表达式校验和字典格式参数校验）
    :param max_fail: 失败阈值
        - None: 严格模式，一个失败全部失败（默认）
        - int: 每个规则最多允许N个失败
        - float: 每个规则最多允许N%失败率
    :param fast_fail: 快速失败，默认True
    :param named_validations: 具名字段校验规则 field_name="validator expression"}
    :param output_format: 校验结果输出格式：summary/detail/dict
    :return: ValidationResult: 校验成功时返回ValidationResult对象
    :raises: ValidationError: 校验失败时抛出ValidationError对象
    
    用法示例：
    try:
        result = validate_list(products, "id", "name", "price > 0", max_fail=2)
        print(f"列表校验成功: {result}")
    except ValidationError as e:
        print(f"列表校验失败: {e}")
    """
    return check_list(data_list, *validations, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode="assert", **named_validations)


def validate_nested(data, list_field, nested_field, *validations, max_fail=None, fast_fail=True, output_format="summary"):
    """
    嵌套列表数据批量校验 - check_nested函数的断言模式别名
    
    :param data: 要校验的数据
    :param list_field: 列表路径
    :param nested_field: 嵌套对象字段名，支持列表或字典对象
    :param validations: 字段校验规则
    :param max_fail: 失败阈值
        - None: 严格模式，一个失败全部失败（默认）
        - int: 每个规则最多允许N个失败
        - float: 每个规则最多允许N%失败率

    :param fast_fail: 快速失败，默认True
    :param output_format: 校验结果输出格式：summary/detail/dict
    :return: ValidationResult: 校验成功时返回ValidationResult对象
    :raises: ValidationError: 校验失败时抛出ValidationError对象
    
    用法示例：
    try:
        result = validate_nested(response, "data.productList", "purchasePlan", "id > 0", "amount >= 100")
        print(f"嵌套列表校验成功: {result}")
    except ValidationError as e:
        print(f"嵌套列表校验失败: {e}")
    """
    return check_nested(data, list_field, nested_field, *validations, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode="assert")


class DataValidator(DataChecker):
    """链式调用数据校验器 - 继承DataChecker类"""
    
    def validate(self, max_fail=None, fast_fail=True, output_format="summary"):
        """重写DataChecker.validate方法，执行校验，校验成功时返回ValidationResult对象，校验失败时抛出ValidationError对象
        
        :param max_fail: 失败阈值
            - None: 严格模式，一个失败全部失败（默认）
            - int: 每个规则最多允许N个失败
            - float: 每个规则最多允许N%失败率
        :param fast_fail: 快速失败，默认True
        :param output_format: 校验结果输出格式：summary/detail/dict
        :return: ValidationResult: 校验成功时返回ValidationResult对象
        :raises: ValidationError: 校验失败时抛出ValidationError对象

        用法示例：
        try:
            result = validator(data)\
                .not_empty("field1", "field2")\
                .greater_than("field3", 0)\
                .validate(max_fail=0.1)
            print(f"链式校验成功: {result.summary}")
        except ValidationError as e:
            print(f"链式校验失败: {e}")
        """
        return super().validate(max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode="assert")


def validator(data):
    """创建数据校验器 - checker函数的别名"""
    return DataValidator(data)