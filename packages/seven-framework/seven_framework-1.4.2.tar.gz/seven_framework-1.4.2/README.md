

<!--
 * @Author: ChenXiaolei
 * @Date: 2021-09-08 11:32:28
 * @LastEditTime: 2025-09-24 15:19:15
 * @LastEditors: ChenXiaolei
 * @Description: 
-->

# seven_framework

## 天志互联Python开发库

### 1.4.2 更新内容
* base_model添加update_table允许使用order by语句

### 1.4.1 更新内容
* base_model优化add_update_whole_entity方法，修复关键词报错的问题

### 1.4.0 更新内容
* 安全升级，参数过滤sql、xss命令注入

### 1.3.12 更新内容
* mysql不输入print错误日志

### 1.3.11 更新内容
* 增加powerjob帮助类

### 1.3.10 更新内容
* mysql支持不配置连接池
* codding url_encode 过滤+号

### 1.3.9 更新内容
* 优化MongoDB帮助类

### 1.3.8 更新内容
* 优化MongoDB帮助类

### 1.3.7 更新内容
* 优化MongoDB帮助类

### 1.3.6 更新内容
* 优化MongoDB帮助类

### 1.3.5 更新内容
* 增加MongoDB帮助类

### 1.3.4 更新内容
* 屏蔽nacos获取配置后的具体配置信息

### 1.3.3 更新内容
* nacos配置获取优化

### 1.3.2 更新内容
* nacos配置获取优化，支持鉴权

### 1.3.1 更新内容
* nacos配置获取优化，支持鉴权

### 1.3.0 更新内容
* 增加nacos云端配置拉取

### 1.2.11 更新内容
* base_model add_values允许主键传入

### 1.2.10 更新内容
* 优化TimeHelper

### 1.2.9 更新内容
* 优化base_console

### 1.2.8 更新内容
* 控制台支持扩展config配置 如 config_jd.json

### 1.2.7 更新内容
* 支持扩展config配置 如 config_jd.json

### 1.2.6 更新内容
* 优化monitor支持扩展config配置

### 1.2.5 更新内容
* 优化monitor支持redis集群检测

### 1.2.4 更新内容
* monitor支持redis集群检测

### 1.2.3 更新内容
* monitor支持redis集群检测

### 1.2.2 更新内容
* redis集群帮助类优化

### 1.2.1 更新内容
* 增加redis集群帮助类

### 1.1.51 更新内容
* ESHelper增加get方法

### 1.1.50 更新内容
* ESHelper增加count方法

### 1.1.49 更新内容
* ESHelper增加字典类型的配置文件

### 1.1.48 更新内容
* TimeHelper->format_time_to_timestamp 支持输出毫秒级别时间戳

### 1.1.47 更新内容
* MySQLHelper增加透传参数

### 1.1.46 更新内容
* lisence异常调试

### 1.1.45 更新内容
* lisence异常调试

### 1.1.44 更新内容
* lisence异常调试

### 1.1.43 更新内容
* lisence异常调试

### 1.1.42 更新内容
* lisence异常时打印日志

### 1.1.41 更新内容
* lisence异常时打印目录结构树

### 1.1.40 更新内容
* 处理base_model->update_list 排除更新字段为str时无效的bug

### 1.1.39 更新内容
* 处理base_model->update_entity 排除更新字段为str时无效的bug

### 1.1.38 更新内容
* 日志内容兼容字典类型

### 1.1.37 更新内容
* CryptoHelper 计算目录哈希函数优化

### 1.1.36 更新内容
* base_tornado添加lisence检查

### 1.1.35 更新内容
* CryptoHelper 增加目录哈希计算函数

### 1.1.34 更新内容
* COS新增以数据流形式上传Object

### 1.1.33 更新内容
* 修复is_this_month 每月最后一天为False的BUG

### 1.1.32 更新内容
* 更新SignHelper 对json格式的兼容处理,去除json的空格.

### 1.1.31 更新内容
* 限制urllib3版本号

### 1.1.30 更新内容
* 优化base_model的update_entity兼容数据库关键字

### 1.1.29 更新内容
* 优化filter_check_params过滤器
* 添加企业微信帮助类方法

### 1.1.28 更新内容
* 修复数据库分页查询时 分页模式=next时的bug

### 1.1.27 更新内容
* RedisHelper 参数调整

### 1.1.26 更新内容
* 配合k8s monitor异常时返回httpstatus=500

### 1.1.25 更新内容
* RedisHelper 兼容redis6.0以后版本,增加username配置项

### 1.1.24 更新内容
* 增加微信帮助类

### 1.1.23 更新内容
* 增加memcached帮助类

### 1.1.22 更新内容
* 优化企业微信帮助类

### 1.1.21 更新内容
* 更新企业微信帮助类
* 新增文件MD5计算

### 1.1.20 更新内容
* OSHelper->copy_tree 支持is_cover是否覆盖文件选项

### 1.1.19 更新内容
* 修复SignHelper传参BUG

### 1.1.18 更新内容
* mysql base_model 增加字段反引号,兼容字段使用关键字的情况

### 1.1.17 更新内容
* 处理base_model get_dict_page_list next时返回实体的bug

### 1.1.16 更新内容
* 兼容timestamp_to_format_time 无法处理毫秒的问题

### 1.1.15 更新内容
* 与bos冲突 调整pycryptodome 初始要求>=3.8.0

### 1.1.14 更新内容
* base_model 分页相关方法增加分页计数模式可选参数

### 1.1.13 更新内容
* CryptoHelper增加RSA相关函数
* SignHelper增加RSA签名函数

### 1.1.12 更新内容
* 修复get_last_day_of_the_month() 12月份异常的bug 

### 1.1.11 更新内容
* SignHelper增加签名串链接字符
* 修改base_handler 增加config配置is_check_xsrf 不默认验证

### 1.1.10 更新内容
* 修复sign参数为数字的报错情况

### 1.1.9 更新内容
* 增加http patch方法

### 1.1.8 更新内容
* 增加os功能
* 处理MySQL事务OperationalError或者是InternalError异常堵塞的问题

### 1.1.7 更新内容
* 修复aws s3 bug

### 1.1.6 更新内容
* 新增消息队列帮助类(RabbitMQ、RocketMQ)

### 1.1.5 更新内容
* mysql事务日志修复

### 1.1.4 更新内容
* 添加消息队列 RabbitMQ、RocketMQ帮助类

### 1.1.3 更新内容
* 修复mysql事务回滚的bug

### 1.1.1 更新内容
* redis支持ssl

### 1.1.0 更新内容
* 修改base_handler:filter_check_params参数过滤器在获取post/application/json参数后,增加同时去获取query参数
* base_model update_table、del_entity 添加limit可选参数

### 1.0.135 更新内容
* 优化mysql事务没记录日志的问题

### 1.0.134 更新内容
* 添加AWS S3存储支持
* MySQLHelper _add_sql_log添加详细日志

### 1.0.133 更新内容
* HTTPHelper 添加put delete options head patch方法

### 1.0.132 更新内容
* 新增ip解析帮助类
* 添加百度云媒体信息获取方法

### 1.0.131 更新内容
* 新增os.py 文件/文件夹操作类
* base_handler加上返回文件流函数
* 默认线程连接池数量调整为5000,并且支持配置读取(thread_pool_count)

### 1.0.130 更新内容
* base_model 增加add_values(insert...values(),();)函数;
* base_model add函数增加可选返回值(自增ID或影响行数)扩展参数;
* base_model 增加add_update_whole_entity函数,用于遇到唯一键时全量更新的函数;
* mysql.py commit_transaction 添加返回详细的元组信息参数

### 1.0.129 更新内容
* 处理路由传参未透传接收问题

### 1.0.128 更新内容
* Monitor接口监控不参与日志记录

### 1.0.127 更新内容
* base_model limit支持整形

### 1.0.126 更新内容
* 日志配置添加log_console,用于控制日志是否需要输出在控制台上

### 1.0.125 更新内容
* 添加通用签名装饰器
* 更新百度SDK版本号

### 1.0.124 更新内容
* 添加百度云存储BOS组件
* base_model update_entity添加排除更新字段
* log未配置报错问题修复

### 1.0.123 更新内容
* 添加日志备份时间

### 1.0.122 更新内容
* 处理了日志存储配置开关无效的bug
* 优化redis字符串返回byte类型的配置

### 1.0.121 更新内容
* 处理文本日志不记录request_code的问题;
* dict添加不定字典的合并函数;

### 1.0.120 更新内容
* 添加本地文件读写帮助类 file->LocalFileHelper

### 1.0.119 更新内容
* mysql日志记录格式调整

### 1.0.118 更新内容
* TimeHelper增加格式时间转换函数

### 1.0.117 更新内容
* 框架整理发布

### 1.0.116 更新内容
* tornado handler自带monitor.py

### 1.0.115 更新内容
* log优化
* clickhouse帮助类

### 1.0.114 更新内容
* log日志配置修改,添加redis日志存储

### 1.0.113 更新内容
* 增加JsonHelper json_dumps()  常用格式的反序列化

### 1.0.112 更新内容
* 优化SignHelper公共加密类

### 1.0.111 更新内容
* 优化SignHelper公共加密类

### 1.0.110 更新内容
* 优化pymysql暗改转移方法

### 1.0.108 更新内容
* 添加腾讯云对象存储

### 1.0.107 更新内容
* 兼容base_model get_total时传groupby时报错的问题

### 1.0.106 更新内容
* 添加阿里oss2依赖

### 1.0.105 更新内容
* 添加阿里oss2帮助类

### 1.0.104 更新内容
* 优化file添加金山云(KS3)存储帮助类

### 1.0.102 更新内容
* file添加金山云(KS3)存储帮助类
* 调整filter_check_params 方法兼容application/json为空时自动再查找普通参数

### 1.0.101 更新内容
* http_log增加打印公共返回字段

### 1.0.100 更新内容
* 修复mysql update bug

### 1.0.99 更新内容
* 修复mysql bug

### 1.0.98 更新内容
* 优化Timehelper 关于本周/月/年 第一天及最后一天时间,以及指定日期的对比函数

### 1.0.96 更新内容
* 新增Timehelper 关于本周/月/年 第一天及最后一天时间,以及指定日期的对比函数
* 优化mysql 传参如果不为list的情况下,参数为0报错的bug

### 1.0.95 更新内容
* 新增CSVHelper

### 1.0.94 更新内容
* 优化base_model 解决get_entity_by_id id=0报错的BUG

### 1.0.93 更新内容
* 优化base_model

### 1.0.92 更新内容
* 修改base_model 更新数据库未影响行数时返回False

### 1.0.91 更新内容
* DBUtils 高版本写法变更,依赖版本调整

### 1.0.90 更新内容
* TimeHelper 增加时间差集计算

### 1.0.89 更新内容
* 优化企业微信帮助类

### 1.0.88 更新内容
* 优化企业微信帮助类

### 1.0.87 更新内容
* 添加企业微信帮助类
* 添加公共签名帮助类
* 兼容http post请求

### 1.0.86 更新内容
* 修改毫秒级时间戳

### 1.0.85 更新内容
* 添加毫秒级时间戳

### 1.0.84 更新内容
* 修复redis db=0是异常的bug

### 1.0.83 更新内容
* 修复http post json请求bug

### 1.0.82 更新内容
* 修复redis添加init参数bug

### 1.0.81 更新内容
* Redis添加init参数,可直接指定配置字典即可

### 1.0.80 更新内容
* 优化sha256加密方法

### 1.0.79 更新内容
* 添加sha256加密方法

### 1.0.78 更新内容
* TimeHelper添加更改格式化时间格式的方法

### 1.0.77 更新内容
* log入库时间戳格式调整

### 1.0.75 更新内容
* 事务添加导出sql语句方法

### 1.0.74 更新内容
* 优化mysql事务

### 1.0.73 更新内容
* base_model增加update_list方法

### 1.0.72 更新内容
* 优化DbTransaction 事务类

### 1.0.71 更新内容
* 优化DbTransaction 事务类

### 1.0.70 更新内容
* 增加DbTransaction 事务类

### 1.0.69 更新内容
* 修复base_model BUG

### 1.0.68 更新内容
* 修改企业微信通知添加项目产生的错误

### 1.0.67 更新内容
* base_model 增加事务处理

### 1.0.66 更新内容
* 添加框架依赖

### 1.0.65 更新内容
* 添加框架依赖

### 1.0.64 更新内容
* 增加excel帮助类
* 增加二维码帮助类

### 1.0.63 更新内容
* 修改file->ufile cdn前缀问题

### 1.0.62 更新内容
* base_model 修改page_list函数的count()字段

### 1.0.61 更新内容
* log记录数据库添加record_time字段
* base_handler->get_params 添加是否去除前后空格选填参数

### 1.0.60 更新内容
* base_model conver_type修改

### 1.0.59 更新内容
* 企业微信通知加项目名称

### 1.0.58 更新内容
* 修改host处理

### 1.0.57 更新内容
* 修改log写入数据库转义问题

### 1.0.56 更新内容
* 优化base_model 分页函数

### 1.0.55 更新内容
* 优化全局异常报错处理

### 1.0.54 更新内容
* 优化mysql连接

### 1.0.53 更新内容
* 添加DBUtils依赖

### 1.0.52 更新内容
* 优化mysqlhelper 连接池
* basemodel配合mysql修改

### 1.0.51 更新内容
* 修改urlencode bug

### 1.0.50 更新内容
* 优化log添加数据库记录

### 1.0.49 更新内容
* log添加数据库记录
* ufile.py 改名为 file.py
* file.py 添加ufile 下载文件方法

### 1.0.48 更新内容
* 优化filter_check_params

### 1.0.47 更新内容
* JsonEncoder 支持decimal类型

### 1.0.46 更新内容
* 修复ufile bug

### 1.0.45 更新内容
* 修复ufile包名冲突的问题

### 1.0.44 更新内容
* 增加ufile封装

### 1.0.43 更新内容
* 修复企业微信通知bug
* 修改prepare的http请求信息支持json参数

### 1.0.42 更新内容
* @filter_check_params支持接收json传参

### 1.0.41 更新内容
* 添加testing环境配置

### 1.0.40 更新内容
* 修复已知BUG

### 1.0.39 更新内容
* 添加企业微信报警(notice.py)
* 修改base_handler内filter_check_params装饰器无需输入可选参数

### 1.0.38 更新内容
* 修复引用

### 1.0.37 更新内容
* 修复json bytes转码BUG
* base_handler 添加body参数转dict函数

### 1.0.36 更新内容
* 修复http请求控制台日志bug

### 1.0.35 更新内容
* 添加http请求控制台日志

### 1.0.33 更新内容
* 添加base_tornado

### 1.0.31 更新内容
* 添加coding帮助类

### 1.0.30 更新内容
* 添加依赖源

### 1.0.29 更新内容
* 优化base_model 增加seven_framework架引用

### 1.0.27 更新内容
* 增加控制台基础引用 base_console

### 1.0.26 更新内容
* 优化CryptoHelper 编码问题
* 增加CryptoHelper 针对bytes的md5加密
* 优化BaseHandler body转实体方法

### 1.0.25 更新内容
* CryptoHelper增加sha1加密

### 1.0.24 更新内容
* base_handler增加request_body_to_entity方法

### 1.0.23 更新内容
* 优化base_handler get_param 空值也返回默认值

### 1.0.22 更新内容
* 优化base_handler filter_check_params 装饰器,允许不检查必填参数

### 1.0.20 更新内容
* 优化MysqlHelper

### 1.0.19 更新内容
* 将MysqlHelper 的condition参数 拆开为 where/group_by/order_by/limit 参数
* 将MysqlHelper及base_model 增加事务执行函数transaction_execute

### 1.0.18 更新内容
* 解决base_api_handler的初始化bug

### 1.0.17 更新内容
* 优化框架结构
* 修改CryptoHelper 的 AES加解密方法