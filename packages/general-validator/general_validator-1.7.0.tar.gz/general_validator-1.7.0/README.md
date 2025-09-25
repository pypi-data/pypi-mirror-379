# General-Validator

<p align="center">
  <img src="https://img.shields.io/badge/version-1.6.0-brightgreen" alt="Version">
  <img src="https://img.shields.io/badge/python-3.7%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/core-极简通用-orange" alt="Core">
</p>

> **一个校验函数，多种高级特性，无限应用场景： 🌍 [English Documentation](README-EN.md)** | **🇨🇳 [中文完整文档](README-CN.md)**

一款极简通用数据校验器，专为批量复杂数据校验场景设计，通过极简的校验语法、灵活的阈值机制、强大的联合校验功能，让数据校验变得简单而强大！🚀


## ✨ 核心优势

- 🎯 **极简调用**: `check(data, "field > 0")` 一个入口函数搞定所有校验场景
- 🔥 **默认非空**: `check(data, "field1", "field2")` 默认非空，简洁易懂
- 🌟 **直观语法**: `"field > 0"` 近乎自然语言表达，拒绝复杂配置
- 🔗 **通配符链式**: `"*.profile.*.score > 60"` 实现无限深度批量校验
- 🔄 **联合规则校验**: 支持 &&（AND）和 ||（OR）逻辑操作符
- ⚙️ **失败阈值控制**: 严格模式/数量阈值/比率阈值灵活切换
- 🎭 **多种返回模式**: 内置三种返回模式`'mode=bool|assert|dict'`，满足不同场景
- 🎮 **性能优先**: 内置快速失败参数`'fast_fail=True|False'`，按需设置
- 🔍 **链式调用**: 内置40+常用链式校验函数，一链到底
- 💪 **专项便捷**: `check_when`、`check_list`、`check_nested` 等专项优化函数
- 🧠 **智能解析**: 支持自动推断数据类型和校验操作符解析



## 🚀 核心理念：一个函数，极简语法，无限可能

### ⚡ 一键安装

```shell
pip install general-validator
```

### 💡 一个 check 函数搞定所有场景

```python
from general_validator import check

# 基础校验 - 最简洁的方式
data = {"name": "Alice", "age": 25, "email": "alice@example.com"}

# 一行代码搞定复杂校验
if check(data, "name", "age > 18", "email *= '@'"):
    print("数据有效，继续处理")

# 批量数据校验 - 通配符链式取值
users = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
if check(users, "*.name", "*.age > 18"):
    print("所有用户数据有效")

# 阈值控制 - 允许部分失败
if check(users, "*.age > 21", max_fail=0.3):  # 允许30%失败
    print("大部分用户符合要求")
```


## 📊 五大核心特性

基于一个 **check** 函数，衍生出强大的数据校验生态：

### 1️⃣ **专项便捷** - 基于 check 衍生的专项函数

```python
from general_validator import check_when, check_when_each, check_list, check_nested

# 非空数据校验 - 数据字段非空校验
check_not_empty(user, "name", "age", "email")

# 列表专项校验 - 专门优化的列表校验
check_list(products, "id > 0", "name", "price > 0")

# 嵌套数据校验 - 深度嵌套结构校验
check_nested(complex_data, nested_rules)

# 条件校验 - 满足条件时才校验
check_when(orders, "amount > 100", "verified == true")

# 逐项条件校验 - 每个满足条件的项都要校验  
check_when_each(users, "status == 'active'", "score > 70")

# 逐项列表条件校验 - 每个列表项都有校验
check_list_when(users, "level == 'vip'", "discount == 0.88")
```

### 2️⃣ **多种模式** - 基于 mode 参数的不同返回形式

```python
from general_validator import check, ValidationError

# 布尔模式（默认）- 快速判断
result = check(data, rules, mode="bool")  # True/False

# 断言模式 - 精确错误定位
try:
    check(data, rules, mode="assert")  # 基于assert理念「失败即异常」：成功返回结果，失败抛异常
except ValidationError as e:
    print(f"错误: {e}")

# 字典模式 - 详细分析报告
result = check(data, rules, mode="dict")  # 详细字典信息
print(f"成功率: {result['success_rate']:.1%}")
```

### 3️⃣ **极简语法** - 近乎自然语言的校验表达

```python
# 默认非空校验
check(data, "name", "email", "phone")

# 直观的比较操作
check(data, "age > 18", "score >= 60", "price < 1000")

# 字符串匹配校验  
check(data, "email *= '@'", "phone ^= '13'", "name #>= 2")

# 复杂逻辑条件
check(data, "status == 'active' && verified == true || admin == true")
```

### 4️⃣ **强大特性** - 批量处理和智能控制

```python
from general_validator import check, checker

# 通配符链式取值 - 无限深度批量校验
check(data, "users.*.profile.*.settings.*.enabled == true")

# 阈值控制 - 灵活的失败容忍度
check(batch, rules, max_fail=5)      # 最多5个失败
check(batch, rules, max_fail=0.1)    # 最多10%失败率

# 快速失败控制 - 性能优化
check(large_data, rules, fast_fail=True)   # 遇到失败立即停止

# 链式调用 - 优雅的流式API
checker(data).not_empty("name").greater_than("age", 18).validate()
```

### 5️⃣ **便捷 API** - 基于 mode 参数衍生的不同系列 API

| 功能 | check系列 (默认布尔模式) | validate系列 (断言模式) | inspect系列 (字典模式) |
|------|-----------------|----------------------|---------------------|
| 基础校验 | `check()` | `validate()` | `inspect()` |
| 非空校验 | `check_not_empty()` | `validate_not_empty()` | `inspect_not_empty()` |
| 条件校验 | `check_when()` | `validate_when()` | `inspect_when()` |
| 逐项条件 | `check_when_each()` | `validate_when_each()` | `inspect_when_each()` |
| 列表条件 | `check_list_when()` | `validate_list_when()` | `inspect_list_when()` |
| 列表校验 | `check_list()` | `validate_list()` | `inspect_list()` |
| 嵌套校验 | `check_nested()` | `validate_nested()` | `inspect_nested()` |
| 链式调用 | `checker().validate()` | `validator().validate()` | `inspector().validate()` |


```python
from general_validator import inspect, validate, ValidationError, checker, validator, inspector

# 需要快速验证？check 系列函数（即 mode="bool"）
result = check(data, "field1", "field2 > 0")

# 需要失败即异常？validate 系列函数（即 mode="assert"）
try:
    validate(data, "field1", "field2 > 0")  # 失败抛异常，成功返回详情
except ValidationError as e:
    handle_detailed_error(e)

# 需要详细数据分析？inspect 系列（即 mode="dict"）
result = inspect(batch_data, quality_rules)
api_response = {
    "quality_score": result["success_rate"],
    "failed_count": len(result["failed_fields"]),
    "details": result
}

# 不同链式调用风格
checker(data).not_empty("name").greater_than("age", 18).validate()     # → bool
validator(data).not_empty("name").greater_than("age", 18).validate()   # → ValidationResult
inspector(data).not_empty("name").greater_than("age", 18).validate()   # → dict
```


## 🔧 内置强大直观的操作符

| 分类 | 操作符 | 示例 |
|----------|-----------|----------|
| **比较** | `==`, `!=`, `>`, `>=`, `<`, `<=` | `"age > 18"`, `"status == 'active'"` |
| **字符串** | `*=`, `^=`, `$=`, `~=` | `"email *= '@'"`, `"url ^= 'https://'"` |
| **长度** | `#>`, `#<`, `#=`, `#>=`, `#<=` | `"password #>= 8"`, `"name #< 50"` |
| **逻辑** | `&&`, `||` | `"active && premium"`, `"admin || vip"` |
| **类型** | `@=` | `"age @= 'int'"`, `"data @= 'dict'"` |
| **默认** | 默认非空校验 | `"name"`, `"email"` (非空字段) |

更多详情与用法参考：[校验器和操作符](docs/api-reference/operators.md)

## 🔗 内置丰富直观的流式接口

| 方法 | 描述 | 示例 |
|------|------|------|
| `not_empty(*paths)` | 批量非空校验 | `.not_empty("name", "email")` |
| `equals(path, value)` | 等于校验 | `.equals("status", "active")` |
| `not_equals(path, value)` | 不等于校验 | `.not_equals("status", "banned")` |
| `starts_with(path, prefix)` | 开头校验 | `.starts_with("url", "https://")` |
| `ends_with(path, suffix)` | 结尾校验 | `.ends_with("email", "@company.com")` |
| `contains(path, substring)` | 包含校验 | `.contains("description", "product")` |
| `matches_regex(path, pattern)` | 正则校验 | `.matches_regex("phone", r"^\+1\d{10}$")` |
| `is_email(path)` | 邮箱格式校验 | `.is_email("email")` |
| `is_url(path)` | URL格式校验 | `.is_url("website")` |
| `is_type(path, type_name)` | 通用类型校验 | `.is_type("age", "int")` |
| `is_string(path)` | 字符串类型 | `.is_string("name")` |
| `is_number(path)` | 数字类型 | `.is_number("price")` |
| `is_integer(path)` | 整数类型 | `.is_integer("count")` |
| `is_boolean(path)` | 布尔类型 | `.is_boolean("active")` |
| `is_list(path)` | 列表类型 | `.is_list("tags")` |
| `is_dict(path)` | 字典类型 | `.is_dict("config")` |
| `greater_than(path, value)` | 大于校验 | `.greater_than("age", 18)` |
| `greater_equal(path, value)` | 大于等于校验 | `.greater_equal("score", 60)` |
| `less_than(path, value)` | 小于校验 | `.less_than("age", 100)` |
| `less_equal(path, value)` | 小于等于校验 | `.less_equal("discount", 0.5)` |
| `between(path, min_val, max_val)` | 范围校验 | `.between("age", 18, 65)` |
| `is_positive(path)` | 正数校验 | `.is_positive("amount")` |
| `is_negative(path)` | 负数校验 | `.is_negative("balance")` |
| `length_equals(path, length)` | 长度等于 | `.length_equals("code", 6)` |
| `length_greater_than(path, length)` | 长度大于 | `.length_greater_than("password", 8)` |
| `length_less_than(path, length)` | 长度小于 | `.length_less_than("title", 100)` |
| `length_between(path, min_len, max_len)` | 长度范围 | `.length_between("name", 2, 50)` |
| `when(condition, *then)` | 严格条件校验 | `.when("status == 'active'", "score > 70")` |
| `when_each(condition, *then)` | 逐项条件校验 | `.when_each("*.level == 'vip'", "*.credits > 1000")` |
| `list_when(condition, *then)` | 列表专用条件校验：when_each的简化版 | `.list_when("level == 'vip'", "credits > 1000")` |

更多详情与用法参考：[链式调用API](docs/api-reference/operators.md)


## 🎭 实战场景演示

### 🛠️ API自动化测试 - 结合[HttpRunner](https://github.com/httprunner/httprunner)工具实现极速高效批量自动化测试，让自动化效率飞起来

```yaml
name: 用户数据接口测试

request:
  url: /api/users
  method: GET

validate:
  # 第一层：基础结构（必须通过）
  - eq:
    - ${check(body, "status_code == 200", "id", "username", "password", "created_at")}
    - True
  # 第二层：业务字段（允许少量异常）
  - eq:
    - ${check(body, "email *= @", "phone ~= '^1[3-9]\\d{9}$", "profile", max_fail=0.01)}
    - True
  # 第三层：可选字段（更宽松）
  - eq:
    - ${check(body, "avatar $= png", "bio ^= 'https://'", "preferences #> 10", max_fail=0.1)}
    - True
```

### 🔗 API接口开发 - 一个 check 函数的三层应用

```python
@app.route('/api/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    
    # ⚡ 第一层：快速入口校验
    if not check(user_data, "username", "email", "age"):
        return jsonify({"error": "缺少必要字段"}), 400
    
    # 🎯 第二层：业务规则校验  
    if not check(user_data, "username #>= 3", "age >= 18", "email *= '@'"):
        return jsonify({"error": "数据格式不符合要求"}), 400
    
    # 📊 第三层：详细质量分析（需要时）
    quality = inspect(user_data, "phone #>= 10", "profile.bio")
    if quality["success_rate"] < 0.8:
        logger.warning(f"用户信息完整度较低: {quality['success_rate']:.1%}")
    
    user = create_user_account(user_data)
    return jsonify({"success": True, "user": user})
```

### 📊 数据质量监控 - 阶梯式质量控制

```python
def monitor_daily_batch(batch_data):
    """基于 check 函数的多层质量监控"""
    
    # 🚨 第一道防线：严格质量门控  
    if not check(batch_data, "*.user_id > 0", "*.email *= '@'", max_fail=0.01):
        alert_critical("数据质量严重异常，停止处理")
        return "BLOCKED"
    
    # ⚠️  第二道防线：业务质量检查
    business_ok = check_when_each(batch_data, 
                                 "user_type == 'premium'", 
                                 "credit_score > 600")
    if not business_ok:
        logger.warning("高级用户数据质量异常")
    
    # 📈 第三道防线：全面质量分析
    quality_report = inspect(batch_data, 
                           "*.phone #>= 10", 
                           "*.address",
                           "*.profile.complete == true")
    
    save_quality_metrics({
        "date": datetime.now().date(),
        "quality_score": quality_report["success_rate"],
        "total_records": len(batch_data)
    })
    
    return "PROCESSED"
```

### ⚙️ 业务规则引擎 - 条件化智能校验

```python
def process_orders(orders):
    """基于 check 系列的业务规则引擎"""
    
    # 🎯 基础数据完整性
    if not check(orders, "*.id > 0", "*.customer_id", "*.amount > 0"):
        raise DataError("订单基础数据不完整")
    
    # 💳 高价值订单特殊处理
    high_value_orders = [o for o in orders if o.get("amount", 0) > 1000]
    if high_value_orders:
        check_when_each(high_value_orders, 
                       "amount > 1000", 
                       "verified_address", "risk_score < 0.3")
    
    # 🌍 国际订单合规检查
    international_orders = [o for o in orders if o.get("country") != "CN"]  
    if international_orders:
        check_list(international_orders, 
                  "customs_form", "tax_calculated", "shipping_method")
    
    # 🎁 VIP客户优惠资格
    vip_orders = [o for o in orders if o.get("customer_level") == "vip"]
    if vip_orders and check_list(vip_orders, "loyalty_points >= 1000"):
        apply_vip_discount(vip_orders)
    
    return process_all_orders(orders)
```


## 🎉 立即开始

### 1. 快速安装
```bash
pip install general-validator
```

### 2. 从一个 check 函数开始
```python
from general_validator import check

# 🎯 基础校验 - 一行搞定
data = {"name": "Alice", "age": 25, "email": "alice@example.com"}
if check(data, "name", "age > 18", "email *= '@'"):
    print("数据有效！")
```

### 3. 探索 check 函数的强大能力
```python
# 🌟 批量数据校验
users = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 17}]
data_ok = check(users, "*.name", "*.age > 18", max_fail=0.5)  # 允许50%失败

# ⚙️ 条件校验：专项函数更便捷
from general_validator import check_when_each
check_when_each(users, "age >= 18", "email *= '@'")  # 成年用户才检查邮箱

# 🔄 需要更多信息？试试其他模式
from general_validator import validate, inspect
validate(data, rules)  # 断言模式：失败抛异常，便于调试
inspect(data, rules)   # 字典模式：返回详细分析，适合API
```

### 4. 立即在项目中使用
```python
# 替换你的复杂校验逻辑
# Before: 复杂的 if-else 判断
# After: 简洁的一行代码
if check(request.json, "user_id > 0", "action", "timestamp"):
    process_request()
```


## 🆚 与传统方案对比

| 特性对比 | General-Validator | 传统校验方案 |
|---------|------------------|-------------|
| **入口复杂度** | ⭐⭐⭐⭐⭐ 一个 check 函数 | ⭐⭐ 多个库、多种语法 |
| **学习成本** | ⭐⭐⭐⭐⭐ 零学习成本 | ⭐⭐ 学习复杂配置规则 |
| **代码简洁** | `check(data, "field > 0")` | 需要编写大量判断判断 |
| **批量处理** | `"*.field"` 通配符批量一次搞定 | 需要手动循环遍历 |
| **错误定位** | 精确到具体字段路径 | 难以定位问题源头 |
| **扩展能力** | 专项函数 + 多种模式 | 功能固定，难以扩展 |
| **阈值控制** | 内置严格模式、比率模式、数量模式 | 需要手动实现逻辑 |
| **性能优化** | 内置短路求值优化、快速失败 | 需要手动优化 |

### 🎯 一个函数的强大生态

**传统方案**：需要学习多个库的不同语法
```python
# ❌ 传统方式 - 复杂且分散
import jsonschema, cerberus, marshmallow
schema1 = {...}  # jsonschema语法
schema2 = {...}  # cerberus语法  
schema3 = {...}  # marshmallow语法
```

**General-Validator**：一个 check 函数搞定所有场景
```python
# ✅ 一个函数 - 简洁且统一
from general_validator import check
check(data, "field1", "field2 > 0")        # 基础校验
check(data, rules, max_fail=0.1)            # 阈值控制
check_when(data, condition, requirements)   # 条件校验
```

### 🎪 使用场景

- ✅ **接口测试**: API 响应数据校验
- ✅ **数据质量监控**: 批量数据完整性检查
- ✅ **业务规则验证**: 复杂条件下的数据校验
- ✅ **配置一致性**: 微服务配置校验
- ✅ **数据迁移**: 导入数据格式校验


## 📚 完整文档导航

| 📖 文档分类 | 描述 | 适合人群 |
|-----------|------|---------|
| [🚀 快速入门](docs/quick-start.md) | 15分钟掌握 check 函数精髓 | 新用户 |
| [📋 API参考](docs/api-reference/README.md) | check 系列完整函数文档 | 开发者 |
| [⚡ 高级特性](docs/advanced-features/README.md) | 通配符、阈值、链式调用等 | 进阶用户 |
| [🎪 场景应用](docs/scenarios/README.md) | 实际业务场景最佳实践 | 解决方案 |
| [🎯 模式指南](docs/mode-guide/README.md) | check/validate/inspect 模式详解 | 特殊需求 |
| [🏆 最佳实践](docs/best-practices/README.md) | 性能优化和使用建议 | 所有用户 |


## 🤝 社区与支持

- ⭐ **GitHub**: [给项目点星](https://github.com/zhuifengshen/general-validator)
- 🐛 **问题反馈**: [提交Issue](https://github.com/zhuifengshen/general-validator/issues)
- 💬 **讨论交流**: [GitHub Discussions](https://github.com/zhuifengshen/general-validator/discussions)
- 📧 **使用示例**: 查看项目 `docs/usage/` 目录

## 📄 开源协议

MIT License - 商用友好，自由使用

---

<p align="center">
  <strong>让数据校验变得简单、智能、强大！ 🚀</strong>
  <br><br>
  <strong>一个函数，多种特性，无限可能</strong>
  <br><br>
  <a href="docs/quick-start.md">🎊 立即开始</a> •
  <a href="docs/api-reference/README.md">🎯 API 指南</a> •
  <a href="docs/scenarios/README.md">💡 场景案例</a>
</p>

---
