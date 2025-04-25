# Interface Doc

首先介绍 buyer, seller对象的成员变量，方便总览
```
Class Buyer:
  - <str> id_number: 买家的id值
  - <str> password: 买家登录密码(hash值)
  - <int> rold: 0 身份标识符
  - <list[Card]> cards: 买家办的卡

Class Seller:
  - <str> id_number: 卖家的id值
  - <str> password: 卖家登录密码(hash值)
  - <int> rold: 1 身份标识符
  - <list[Service]> services: 卖家提供的服务

Class Service:
  - <str> service_id: 服务id值
  - <str> service_info: 服务的信息
  - <list[Card]> cards: 用户开的卡

Class Card:
  - <str> card_id: 卡的id值
  - <str> card_info: 卡的信息
  - <float> balance: 余额
  - <float> totalAmount: 总充值金额
```


然后再理一下我们要实现的基础功能（接口也就在下面顺带列出）

- **注册（sign-up）功能。**分 buyer 和 seller 两种角色创建 account（身份证号/营业资质证号 + 密码 + 密码二次确认）

  ```http
  param: 
  	- <str> id_number
  	- <str> password 
  	- <str> repassword
  	- <int> role (0 for buyer, 1 for seller)
  function: 
  	- id_number 不重复
  	- password = repassword
  	- 添加账户到数据库 (不同的 role 入不同的数据库)【密码非明文，存储哈希值】
  return: True or False
  ```

- **登录（sign-in）功能**。分 buyer 和 seller 两种角色进行登录（身份证号/营业资质证号 + 密码）

  ```http
  param: 
  	- <str> id_number
  	- <str> password 
  	- <int> role (0 for buyer, 1 for seller)
  function: 
  	- id_number 在对应数据库能找到
  	- password 匹配
  return: True or False
  ```

- **seller 创建可提供服务(Services Available)。** seller 创建可提供的服务（一个 seller 可以有多个）【类似饭店创建菜单】。

  ```http
  param: 
  	- <str> id_number
  	- <str> service_id
  	- <str> service_info (服务的基本信息)
  function: 
    - service_id 不重复
    - 该行为仅限 seller (role == 1)
  	- 为服务创建合约
  return: (最后一步调用 seller 查询所有可提供服务列表 见下)
  该 id_number 下所有的 service 的 list (service_id, service_info, 充值人数, 目前已到帐金额/总充值金额)
  ```

- **buyer 账户自充值功能。** buyer 可以往自己 account 里面充钱。

  ```http
  param: 
  	- <str> id_number
  	- <double> money
  function: 
  	- 执行往账户充钱的合约
  return: 该 id_number 下的余额总数
  ```

- **buyer 服务办卡/充值功能。**buyer 可以在可用的服务列表中找到某个服务办卡/充值（一个 buyer 可以充值多个）。

  ```http
  param: 
  	- <str> id_number   # buyer id
    - <str> service_id  # 服务 id
  	- <str> card_id     # 储蓄卡 id
  	- <double> money
  function: 
  	- 执行往卡中充钱的合约
  return: (最后一步调用 buyer 查询所有卡列表功能 见下)
  该 id_number 下的 card 总 list (car_id, card_info, 余额/充值金额)
  ```

- **buyer 消费功能。**buyer 可以在自己已经充值的卡上进行操作，输入本次消费的时间、金额。

  ```http
  param: 
  	- <str> id_number
  	- <str> card_id
  	- <double> money
  function: 
  	- 执行用卡消费的合约
  return: 该 id_number 下的 card 总 list (car_id, card_info, 余额/充值金额)
  ```

- **seller 查询卡基本情况功能。**seller 可以看到享受自己提供服务的持卡用户人数 + 充值金额 + 到帐金额

  ```http
  param:
  	- <str> id_number
  function: 
  	- 查询 id_number 下的 card 总 list
  return: 该 id_number 下所有 service 下 card 的 list (service_id, card_info, 充值人数, 到帐金额/总充值金额)
  ```

- **buyer 查询卡基本情况功能**。buyer 可以看到自己充值的卡的充值金额和剩余金额

  ```http
  param:
  	- <str> id_number
  function: 
  	- 查询 id_number 下的 card 总 list
  return: 该 id_number 下所有的 card 的 list (service_id, card_id, card_info, 余额/充值金额)
  ```

- **buyer 终止卡功能。**buyer 可以自己选择 terminate 卡，卡信息消失，充值的钱全部返回 buyer 的 account。

  ```http
  param:
  	- <str> id_number
  	- <str> card_id
  function:
  	- 终止 card 合约
  return: 该 id_number 下所有的 card 的 list (service_id, card_id, card_info, 余额/充值金额)
  ```

  

