private_key = "a986431b2d487c5d5a0bb24eb122be05c23f9e221ed71f5bf1d9af7b4d23c6c4"

account = w3.eth.account.from_key(private_key)
account_address = account.address


class DataBase:
    def __init__(self):
        contract_address = "0x5876144a769c19463b65916cf05209c1cf1ae575"
        contract_address = Web3.to_checksum_address(contract_address)  # 转换为 checksum 地址
        self.contract = w3.eth.contract(address=contract_address, abi=database_abi)
        self.base_tx = {
            'from': account_address,
            'gas': 500000,
            'gasPrice': w3.to_wei('0.025', 'gwei'),
            'nonce': w3.eth.get_transaction_count(account_address),
            'chainId': 42161
        }

    def addBuyer(self, id: str, password: str):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)
        transaction = self.contract.functions.addBuyer(id, password).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def addCard(self, card_id: str, card_info: str, balance: int, totalAmount: int, buyer_id: str, service_id: str):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)

        transaction = self.contract.functions.addCard(
            card_id, card_info, balance, totalAmount, buyer_id, service_id).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def addSeller(self, id: str, password: str):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)
        transaction = self.contract.functions.addSeller(id, password).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def addService(self, service_id: str, service_info: str, seller_id: str):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)

        transaction = self.contract.functions.addService(
            service_id, service_info, seller_id).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def updateBuyerBalance(self, buyer_id: str, new_balance: int):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)

        transaction = self.contract.functions.updateBuyerBalance(buyer_id, new_balance).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def updateBuyerPassword(self, id: str, new_password: str):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)

        transaction = self.contract.functions.updateBuyerPassword(id, new_password).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def updateSellerPassword(self, id: str, new_password: str):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)

        transaction = self.contract.functions.updateSellerPassword(id, new_password).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def updateServiceInfo(self, service_id: str, new_info: str):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)

        transaction = self.contract.functions.updateServiceInfo(service_id, new_info).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def deleteBuyer(self, buyer_id: str):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)

        transaction = self.contract.functions.deleteBuyer(buyer_id).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def deleteCard(self, card_id: str):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)

        transaction = self.contract.functions.deleteCard(card_id).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def deleteSeller(self, seller_id: str):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)

        transaction = self.contract.functions.deleteSeller(seller_id).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def deleteService(self, service_id: str):
        self.base_tx['nonce'] = w3.eth.get_transaction_count(account_address)

        transaction = self.contract.functions.deleteService(service_id).build_transaction(self.base_tx)
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"交易已发送，tx hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"交易完成，区块: {receipt.blockNumber}")

    def getAllBuyerIds(self):
        buyer_ids = self.contract.functions.getAllBuyerIds().call()
        print(f"所有买家 ID: {buyer_ids}")
        return buyer_ids

    def getAllSellerIds(self):
        seller_ids = self.contract.functions.getAllSellerIds().call()
        print(f"所有卖家 ID: {seller_ids}")
        return seller_ids

    def getAllServiceIds(self):
        service_ids = self.contract.functions.getAllServiceIds().call()
        return service_ids

    def get_buyer_info(self, buyer_id):
        buyer_info = self.contract.functions.getBuyerInfo(buyer_id).call()
        return buyer_info
    # 获取 Seller 详细信息

    def get_seller_info(self, seller_id):
        seller_info = self.contract.functions.getSellerInfo(seller_id).call()
        return seller_info

    # 获取 Service 详细信息
    def get_service_info(self, service_id):
        service_info = self.contract.functions.getServiceInfo(service_id).call()
        return service_info

    # 获取 Card 详细信息
    def get_card_info(self, card_id):
        card_info = self.contract.functions.getCardInfo(card_id).call()
        return card_info

    def sign_up(self, id_number: str, password: str, repassword: str, role: int) -> bool:
        # 检查密码是否一致
        if password != repassword:
            print("❌ 两次密码不一致")
            return False

        # 获取所有已存在的用户
        if role == 0:
            all_ids = self.getAllBuyerIds()
        elif role == 1:
            all_ids = self.getAllSellerIds()
        else:
            print("❌ 角色必须是 0 (buyer) 或 1 (seller)")
            return False

        # 检查 ID 是否已存在
        if id_number in all_ids:
            print("❌ 该用户已存在")
            return False

        # 生成密码哈希（SHA-256）
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # 上链
        try:
            if role == 0:
                self.addBuyer(id_number, password_hash)
            else:
                self.addSeller(id_number, password_hash)
            print("✅ 注册成功")
            return True
        except Exception as e:
            print(f"❌ 注册失败: {e}")
            return False

    def sign_in(self, id_number: str, password: str, role: int) -> bool:
        try:
            # 将用户输入的密码哈希成与链上匹配的格式（bytes32）
            hashed_input_password = hashlib.sha256(password.encode()).hexdigest()

            if role == 0:
                # Buyer 登录
                buyer = self.contract.functions.buyers(id_number).call()
                if buyer[0] == "":  # id_number 为空表示未找到
                    print("Buyer 不存在")
                    return False

                stored_hashed_password = buyer[1]  # password
                return hashed_input_password == stored_hashed_password.lower()

            elif role == 1:
                # Seller 登录
                seller = self.contract.functions.sellers(id_number).call()
                if seller[0] == "":
                    print("Seller 不存在")
                    return False

                stored_hashed_password = seller[1]
                return hashed_input_password == stored_hashed_password.lower()

            else:
                print("无效角色")
                return False

        except Exception as e:
            print(f"登录失败，原因: {str(e)}")
            return False

    def create_service(self, id_number: str, service_id: str, service_info: str, role: int):
        try:
            # 身份检查：只能 seller 操作
            if role != 1:
                print("只有 seller 可以添加服务")
                return []

            # service_id 不重复检查（假设合约已实现 getAllServiceIds）
            all_services = self.getAllServiceIds()
            if service_id in all_services:
                print("服务 ID 已存在")
                return []

            # 添加服务
            self.addService(service_id, service_info, id_number)

            # 获取该 seller 下所有服务
            return self.get_services_by_seller(id_number)

        except Exception as e:
            print(f"添加服务失败: {e}")
            return []

    def get_services_by_seller(self, seller_id: str):
        try:
            # 合约需支持函数 getSellerServiceIds(seller_id) -> string[]
            service_ids = self.contract.functions.getSellerServiceIds(seller_id).call()
            service_list = []
            for sid in service_ids:
                # 合约函数 getService(service_id) -> (service_info, seller_id, recharge_count, received_amount, total_amount)
                info = self.get_service_info(sid)

                service_list.append(info)

            return service_list

        except Exception as e:
            print(f"获取服务失败: {e}")
            return []

     # 充值买家账户
    def rechargeBuyerAccount(self, id_number: str, money: float):
        try:
            # 首先获取买家的当前余额
            buyer_info = self.contract.functions.getBuyerInfo(id_number).call()
            if not buyer_info:
                print("❌ 找不到该买家")
                return None

            # 转账
            self.updateBuyerBalance(id_number, money)

            # 返回充值后买家的总余额

            return self.get_buyer_info(id_number)

        except Exception as e:
            print(f"充值失败，原因: {str(e)}")
            return None


dapi = DataBase()
