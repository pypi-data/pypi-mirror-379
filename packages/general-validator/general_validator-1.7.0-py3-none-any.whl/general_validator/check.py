# -*- coding:utf-8 -*-
from .logger import log_debug, log_info, log_warning, log_error
from .base import BaseValidator
from .engine import ValidationEngine, ValidationResult, ValidationError, perform_item_wise_conditional_check, get_nested_value, parse_and_validate


"""
General-Validator check系列数据校验函数 - 核心极简通用数据校验函数

check系列函数始终返回布尔值结果，适用场景：
- 流程控制：`if`、`while` 等控制结构
- 高频调用：性能敏感的场景
- 简洁判断：只需要知道成功或失败
- 快速筛选：大批量数据的快速过滤
"""


def check(data, *validations, max_fail=None, fast_fail=True, output_format="summary", mode="bool", context=None) -> ValidationResult:
    """
    极简通用数据校验函数
    
    :param data: 要校验的数据
    :param validations: 校验规则，支持多种简洁格式
    :param max_fail: 失败阈值
        - None: 严格模式，一个失败全部失败（默认）
        - int: 每个规则最多允许N个失败
        - float: 每个规则最多允许N%失败率

    :param fast_fail: 快速失败，默认True
    :param output_format: 校验结果输出格式：summary/detail/dict
    :param mode: 校验结果返回模式
        - "assert": 断言模式，成功返回ValidationResult，失败抛ValidationError
        - "dict": 字典模式，成功/失败都返回结构化字典
        - "bool": 布尔模式，成功返回True，失败返回False（默认）

    :param context: 上下文对象，用于累积校验结果（链式调用时使用）
    :return: bool | dict | ValidationResult: 根据mode参数返回不同类型
    :raises: ValidationError: 校验失败时抛出（mode="assert"时）
    :raises ValueError: 当mode参数不支持、校验规则格式错误、数据结构异常时抛出
    :raises RuntimeError: 当校验过程中出现系统异常时抛出
    
    用法示例：
    1. 默认非空校验 - 最简形式
    check(response, "data.product.id", "data.product.name")
    
    2. 带校验器的形式
    check(response, "data.product.id > 0", "data.product.price >= 10.5")
    
    3. 混合校验
    check(response, 
          "data.product.id",           # 默认非空
          "data.product.price > 0",    # 大于0
          "status_code == 200")        # 等于200
    
    4. 列表批量校验 - 通配符
    check(response, "data.productList.*.id", "data.productList.*.name")
    
    5. 嵌套列表校验
    check(response, "data.productList.*.purchasePlan.*.id > 0")
    """
    # 使用核心引擎执行校验
    engine = ValidationEngine()
    context = engine.execute(data, validations, max_fail, fast_fail, context=context, output_format=output_format)
    
    # 构建详细结果
    result = context.build_detailed_result()
    
    # 根据 mode 参数决定返回类型
    if mode == "assert":
        # 断言模式：成功返回ValidationResult，失败抛ValidationError（默认）
        if result.success:
            return result
        else:
            raise ValidationError(result, output_format=output_format)
    elif mode == "dict":
        # 字典模式：成功/失败都返回结构化数据
        return result.to_dict()
    elif mode == "bool":
        # 布尔模式：只返回成功/失败状态
        return result.success
    else:
        raise ValueError(f"不支持的mode值: {mode}，支持的值: 'assert', 'dict', 'bool'")


def check_not_empty(data, *validations, max_fail=None, fast_fail=True, output_format="summary", mode="bool") -> ValidationResult:
    """
    专门的非空校验
    
    :param data: 要校验的数据
    :param validations: 校验规则，支持多种简洁格式
    :param max_fail: 失败阈值
        - None: 严格模式，一个失败全部失败（默认）
        - int: 每个规则最多允许N个失败
        - float: 每个规则最多允许N%失败率

    :param fast_fail: 快速失败，默认True
    :param output_format: 校验结果输出格式：summary/detail/dict
    :param mode: 校验结果返回模式
        - "assert": 断言模式，成功返回ValidationResult，失败抛ValidationError
        - "dict": 字典模式，成功/失败都返回结构化字典
        - "bool": 布尔模式，成功返回True，失败返回False（默认）

    :return: bool | dict | ValidationResult: 根据mode参数返回不同类型
    :raises: ValidationError: 当mode="assert"且校验失败时抛出
    :raises: Exception: 当参数错误或数据结构异常时抛出异常
    """
    return check(data, *validations, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode=mode)


def check_when(data, condition, *then, max_fail=None, fast_fail=True, output_format="summary", mode="bool", context=None) -> ValidationResult:
    """
    严格条件校验 - 所有匹配项都满足条件时才执行then校验（第一种语义）
    
    语义说明：
    1. 对所有数据项进行条件校验
    2. 如果所有数据项都满足条件，就执行then规则校验
    3. 如果任一数据项不满足条件，就跳过整个then校验（返回成功）
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
    :param mode: 校验结果返回模式
        - "assert": 断言模式，成功返回ValidationResult，失败抛ValidationError
        - "dict": 字典模式，成功/失败都返回结构化字典
        - "bool": 布尔模式，成功返回True，失败返回False（默认）

    :param context: 上下文对象，用于累积校验结果（链式调用时使用）

    :return: bool | dict | ValidationResult: 根据mode参数返回不同类型
    :raises: ValidationError: 当mode="assert"且校验失败时抛出
    :raises: Exception: 当参数错误或数据结构异常时抛出异常
    
    用法示例：
    1. 单个then校验 - 当status为active时，price必须大于0
    check_when(data, "status == 'active'", "price > 0")
    
    2. 多个then校验 - 当type为premium时，features字段不能为空且price必须大于100
    check_when(data, "type == 'premium'", "features", "price > 100")
    
    3. 批量校验 - 当status为active时，多个字段都必须校验通过
    check_when(data, "status == 'active'",
               "price > 0",
               "name",
               "description",
               "category != 'test'")
    
    4. 支持通配符 - 当所有产品状态为active时，价格都必须大于0且名称不能为空
    check_when(data, "products.*.status == 'active'",
               "products.*.price > 0",
               "products.*.name")
    
    5. 混合条件校验 - 当用户为VIP时，多个权限字段都必须校验
    check_when(data, "user.level == 'vip'",
               "user.permissions.download == true",
               "user.permissions.upload == true",
               "user.quota > 1000")

    注意：
    1. 当条件满足时，所有then校验都必须通过才算成功
    2. 当条件不满足时，跳过所有then校验（返回True）
    """
    # 参数验证
    if not then:
        raise ValueError("至少需要提供一个then校验规则")
    
    log_info(f"开始严格条件校验 - 数据长度: {len(data)}, then规则数: {len(then)}")
    log_debug(f"校验规则: check_when({condition}) then({', '.join(str(rule) for rule in then)})")
    log_debug(f"失败阈值: {'默认严格模式' if max_fail is None else max_fail}")
    
    try:
        # 检查条件是否满足（条件检查不计入统计）
        condition_result = parse_and_validate(data, condition, context=None)
        
        # 条件不成立，跳过then校验
        if not condition_result:
            msg = f"条件不成立: check_when({condition}), 跳过then校验"
            log_warning(msg)
            result = ValidationResult(success=True, total_rules=0, passed_rules=0, failed_rules=0, summary=msg, fast_fail=fast_fail, output_format=output_format)
            if mode == "assert":
                return result
            elif mode == "dict":
                return result.to_dict()
            elif mode == "bool":
                return True
            else:
                raise ValueError(f"不支持的mode值: {mode}，支持的值: 'assert', 'dict', 'bool'")

        # 条件成立，直接调用check函数校验then规则。这样每个then规则自然成为独立的统计维度
        log_debug(f"条件成立: check_when({condition}), 执行then校验")
        return check(data, *then, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode=mode, context=context)
    except ValidationError as e:
        log_error(f"❌ 严格条件校验失败: check_when({condition}) - '{str(e)}'")
        raise
    except Exception as e:
        log_error(f"❌ 严格条件校验出现异常: check_when({condition}) - '{str(e)}'")
        raise


def check_when_each(data, condition, *then, max_fail=None, fast_fail=True, output_format="summary", mode="bool", context=None) -> ValidationResult:
    """
    逐项条件校验 - 对指定路径下的每个数据项分别进行条件+then检查（第二种语义）
    
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
    :param mode: 校验结果返回模式
        - "assert": 断言模式，成功返回ValidationResult，失败抛ValidationError
        - "dict": 字典模式，成功/失败都返回结构化字典
        - "bool": 布尔模式，成功返回True，失败返回False（默认）

    :param context: 上下文对象，用于累积校验结果（链式调用时使用）

    :return: bool | dict | ValidationResult: 根据mode参数返回不同类型
    :raises: ValidationError: 当mode="assert"且校验失败时抛出
    :raises: Exception: 当参数错误或数据结构异常时抛出异常
    
    示例用法：
    1. 基础用法 - 直接使用路径表达式，无需预提取列表
    check_when_each(data, "users.*.status == 'active'", "users.*.score > 70")
    
    2. 多个then规则 - 活跃VIP用户必须有名字且分数大于80
    check_when_each(data, "users.*.status == 'active'", "users.*.name", "users.*.score > 80")
    
    3. 深度嵌套场景 - 支持复杂路径表达式
    check_when_each(response, "data.regions.*.cities.*.status == 'active'", "data.regions.*.cities.*.population > 0")
    
    4. 阈值模式 - 允许30%的活跃用户分数不达标
    check_when_each(data, "users.*.status == 'active'", "users.*.score > 70", max_fail=0.3)
    """
    # 参数验证
    if not then:
        raise ValueError("至少需要提供一个then校验规则")
    
    log_info(f"开始逐项条件校验 - 数据长度: {len(data)}, then规则数: {len(then)}")
    log_debug(f"校验规则: check_when_each({condition}) then({', '.join(str(rule) for rule in then)})")
    log_debug(f"失败阈值: {'默认严格模式' if max_fail is None else max_fail}")
    
    try:
        return perform_item_wise_conditional_check(data, condition, then, max_fail, fast_fail, context=context, output_format=output_format, mode=mode)
    except ValidationError as e:
        log_error(f"❌ 逐项条件校验失败: check_when_each({condition}) - '{str(e)}'")
        raise
    except Exception as e:
        log_error(f"❌ 逐项条件校验出现异常: check_when_each({condition}) - '{str(e)}'")
        raise



def check_list_when(data_list, condition, *then, max_fail=None, fast_fail=True, output_format="summary", mode="bool", context=None) -> ValidationResult:
    """
    列表逐项条件校验 - check_when_each函数的简化版，专门用于列表数据

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
    :param mode: 校验结果返回模式
        - "assert": 断言模式，成功返回ValidationResult，失败抛ValidationError
        - "dict": 字典模式，成功/失败都返回结构化字典
        - "bool": 布尔模式，成功返回True，失败返回False（默认）

    :param context: 上下文对象，用于累积校验结果（链式调用时使用）

    :return: bool | dict | ValidationResult: 根据mode参数返回不同类型
    :raises: ValidationError: 当mode="assert"且校验失败时抛出
    :raises: Exception: 当参数错误或数据结构异常时抛出异常
    
    用法示例：
    1. 基础用法 - 对用户列表，活跃用户的分数必须大于70
    users = [
        {"name": "张三", "status": "active", "score": 85},
        {"name": "李四", "status": "active", "score": 65},  # 条件满足但then失败
        {"name": "王五", "status": "inactive", "score": 70}  # 条件不满足，跳过
    ]
    check_list_when(users, "status == 'active'", "score > 70")

    2. 多个then规则 - 活跃用户必须有名字且分数大于80
    check_list_when(users, "status == 'active'", "name", "score > 80")

    3. 阈值模式 - 允许30%的活跃用户分数不达标
    check_list_when(users, "status == 'active'", "score > 70", max_fail=0.3)

    适用场景：
    - list of dict 列表数据结构
    - 需要对列表中符合条件的数据项进行个别校验
    - 希望统计满足条件的数据项中then规则的失败率
    """
    # 参数验证
    if not isinstance(data_list, list):
        raise TypeError(f"data_list必须是列表，当前类型: {type(data_list)}")

    if not then:
        raise ValueError("至少需要提供一个then校验规则")

    log_info(f"开始列表逐项条件校验 - 列表长度: {len(data_list)}, then规则数: {len(then)}")
    log_debug(f"校验规则: check_list_when({condition}) then({', '.join(str(rule) for rule in then)})")
    log_debug(f"失败阈值: {'默认严格模式' if max_fail is None else max_fail}")

    try:
        return perform_item_wise_conditional_check(data_list, condition, then, max_fail, fast_fail, context=context, output_format=output_format, mode=mode)
    except ValidationError as e:
        log_error(f"❌ 列表逐项条件校验失败: check_list_when({condition}) - '{str(e)}'")
        raise
    except Exception as e:
        log_error(f"❌ 列表逐项条件校验出现异常: check_list_when({condition}) - '{str(e)}'")
        raise


def check_list(data_list, *validations, max_fail=None, fast_fail=True, output_format="summary", mode="bool", **named_validations) -> ValidationResult:
    """
    列表数据批量校验

    :param data_list: 数据列表
    :param validations: 字段校验规则（默认非空校验，同时支持符号表达式校验和字典格式参数校验）
    :param max_fail: 失败阈值
        - None: 严格模式，一个失败全部失败（默认）
        - int: 每个规则最多允许N个失败
        - float: 每个规则最多允许N%失败率

    :param fast_fail: 快速失败，默认True
    :param output_format: 校验结果输出格式：summary/detail/dict
    :param mode: 校验结果返回模式
        - "assert": 断言模式，成功返回ValidationResult，失败抛ValidationError
        - "dict": 字典模式，成功/失败都返回结构化字典
        - "bool": 布尔模式，成功返回True，失败返回False（默认）


    :param named_validations: 具名字段校验规则 field_name="validator expression"}
    :return: bool | dict | ValidationResult: 根据mode参数返回不同类型
    :raises: ValidationError: 当mode="assert"且校验失败时抛出
    :raises: TypeError: 当data_list不是列表时抛出
    
    用法示例：
    # 默认非空校验
    check_list(productList, "id", "name", "price")
    
    # 带校验器
    check_list(productList, "name", id="> 0", price=">= 0")
    或
    check_list(productList, "name", "id > 0", "price >= 0")
    
    # 混合使用
    check_list(productList, "name", "description", id="> 0", status="== 'active'")
    或
    check_list(productList, "name", "description", "id > 0", "status == 'active'")
    """
    total_fields = len(validations) + len(named_validations)
    log_info(f"列表数据批量校验 - 列表长度: {len(data_list) if isinstance(data_list, list) else '未知'}, 字段数: {total_fields}")
    log_debug(f"非空校验字段: {list(validations)}")
    log_debug(f"带校验器字段: {dict(named_validations)}")
    
    if not isinstance(data_list, list):
        raise TypeError(f"data_list必须是列表，当前类型: {type(data_list)}")
    
    # 构建校验规则
    rules = []
    # 默认非空校验的字段
    for field in validations:
        rules.append(f"*.{field}")
    # 带校验器的字段
    for field, validator_expr in named_validations.items():
        rules.append(f"*.{field} {validator_expr}")
    
    return check(data_list, *rules, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode=mode)


def check_nested(data, list_field, nested_field, *validations, max_fail=None, fast_fail=True, output_format="summary", mode="bool") -> ValidationResult:
    """
    嵌套列表数据批量校验

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
    :param mode: 校验结果返回模式
        - "assert": 断言模式，成功返回ValidationResult，失败抛ValidationError
        - "dict": 字典模式，成功/失败都返回结构化字典
        - "bool": 布尔模式，成功返回True，失败返回False（默认）

    :param named_validations: 具名字段校验规则 field_name="validator expression"}
    :return: ValidationResult | dict | bool: 根据mode参数返回不同类型
    :raises: ValidationError: 当mode="assert"且校验失败时抛出
    :raises: ValueError: 当列表路径不存在、嵌套对象不存在或为空时抛出
    
    用法示例：
    1. 默认非空校验
    check_nested(response, "data.productList", "purchasePlan", "id", "name")
    
    2. 带校验器
    check_nested(response, "data.productList", "purchasePlan", "id > 0", "amount >= 100")
    """
    log_info(f"嵌套列表数据批量校验 - 路径: {list_field}.*.{nested_field}, 字段数: {len(validations)}")
    log_debug(f"列表路径: {list_field}")
    log_debug(f"嵌套对象路径: {nested_field}")
    log_debug(f"字段校验规则: {list(validations)}")
    
    main_list = get_nested_value(data, list_field)
    if isinstance(main_list, list) and len(main_list) > 0:
        nested_obj = main_list[0].get(nested_field)
        if not nested_obj:
            raise ValueError(f"check_nested校验时嵌套对象 {nested_field} 不存在或为空")
    else:
        raise ValueError(f"check_nested校验时列表路径 {list_field} 的值不是列表或为空列表")

    # 构建校验规则
    rules = []
    for validation in validations:
        if isinstance(nested_obj, list):
            rules.append(f"{list_field}.*.{nested_field}.*.{validation}")
        elif isinstance(nested_obj, dict):
            rules.append(f"{list_field}.*.{nested_field}.{validation}")
        else:
            raise ValueError(f"check_nested校验时嵌套对象 {nested_field} 不是列表或字典")

    return check(data, *rules, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode=mode)


class DataChecker(BaseValidator):
    """链式调用数据校验器 - 继承BaseValidator类"""
    
    def validate(self, max_fail=None, fast_fail=True, output_format="summary", mode="bool") -> ValidationResult:
        """
        执行校验，默认返回布尔值结果
        
        :param max_fail: 失败阈值
            - None: 严格模式，一个失败全部失败（默认）
            - int: 每个规则最多允许N个失败
            - float: 每个规则最多允许N%失败率

        :param fast_fail: 快速失败，默认True
        :param output_format: 校验结果输出格式：summary/detail/dict
        :param mode: 校验结果返回模式
        - "assert": 断言模式，成功返回ValidationResult，失败抛ValidationError
        - "dict": 字典模式，成功/失败都返回结构化字典
        - "bool": 布尔模式，成功返回True，失败返回False（默认）

        :param named_validations: 具名字段校验规则 field_name="validator expression"}
        :return: bool | dict | ValidationResult: 根据mode参数返回不同类型
        :raises: ValidationError: 当mode="assert"且校验失败时抛出
        """
        return check(self.data, *self.rules, max_fail=max_fail, fast_fail=fast_fail, output_format=output_format, mode=mode)


def checker(data):
    """创建数据校验器 - 增强版，支持详细结果返回"""
    return DataChecker(data)