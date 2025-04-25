// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MarketplaceDatabase {
    struct Card {
        string card_id;
        string card_info;
        uint256 balance;
        uint256 totalAmount;
    }

    struct Service {
        string service_id;
        string service_info;
        string[] card_ids; // 卡片关联
    }

    struct Buyer {
        string id_number;
        string password;
        uint256 balance; // 买家的余额
        uint8 role; // 0 = buyer
        string[] card_ids;
    }

    struct Seller {
        string id_number;
        string password;
        uint8 role; // 1 = seller
        string[] service_ids;
    }
    string[] private buyerIds;
    string[] private sellerIds;
    string[] private serviceIds; // ✅ 所有服务 ID 记录
    string[] private cardIds;
    // 数据存储
    mapping(string => Buyer) public buyers;
    mapping(string => Seller) public sellers;
    mapping(string => Service) public services;
    mapping(string => Card) public cards;

    // ========== Buyer ==========
    function addBuyer(string memory _id, string memory _password) public {
        require(bytes(buyers[_id].id_number).length == 0, "Buyer exists");
        buyers[_id] = Buyer({
            id_number: _id,
            password: _password,
            balance: 0, // 初始余额为0
            role: 0, // 角色标识符
            card_ids: new string[](0)
        });
        buyerIds.push(_id); // <- 记录 ID
    }
    function getBuyerInfo(string memory _buyer_id) public view returns (
        string memory id_number,
        string memory password,
        string[] memory card_ids,
        uint256 balance
    ) {
        require(bytes(buyers[_buyer_id].id_number).length > 0, "Buyer not found");
        Buyer storage b = buyers[_buyer_id];
        return (b.id_number, b.password, b.card_ids, b.balance);
    }
    function updateBuyerPassword(string memory _id, string memory _newPassword) public {
        require(bytes(buyers[_id].id_number).length > 0, "Buyer not found");
        buyers[_id].password = _newPassword;
    }
    function updateBuyerBalance(string memory _id, uint256 _newBalance) public {
        require(bytes(buyers[_id].id_number).length > 0, "Buyer not found");
        buyers[_id].balance = _newBalance;
    }

    function deleteBuyer(string memory _id) public {
        require(bytes(buyers[_id].id_number).length > 0, "Buyer not found");
        delete buyers[_id];
    }

    // ========== Seller ==========
    function addSeller(string memory _id, string memory _password) public {
        require(bytes(sellers[_id].id_number).length == 0, "Seller exists");
        sellers[_id] = Seller({
            id_number: _id,
            password: _password,
            role: 1, // 角色标识符
            service_ids: new string[](0) // 初始化服务ID为空
        });
        sellerIds.push(_id); // <- 记录 ID
    }
    function getSellerInfo(string memory _seller_id) public view returns (
        string memory id_number,
        string memory password,
        string[] memory service_ids
    ) {
        require(bytes(sellers[_seller_id].id_number).length > 0, "Seller not found");
        Seller storage s = sellers[_seller_id];
        return (s.id_number, s.password, s.service_ids);
    }
    function updateSellerPassword(string memory _id, string memory _newPassword) public {
        require(bytes(sellers[_id].id_number).length > 0, "Seller not found");
        sellers[_id].password = _newPassword;
    }

    function deleteSeller(string memory _id) public {
        require(bytes(sellers[_id].id_number).length > 0, "Seller not found");
        delete sellers[_id];
    }

    // ========== Service ==========
    function addService(string memory _service_id, string memory _service_info, string memory _seller_id) public {
        require(bytes(services[_service_id].service_id).length == 0, "Service exists");
        services[_service_id] = Service({
            service_id: _service_id,
            service_info: _service_info,
            card_ids: new string[](0)  // 初始化服务对应的卡片ID为空
        });
        sellers[_seller_id].service_ids.push(_service_id);  // 将服务 ID 加入卖家的服务列表
        serviceIds.push(_service_id); // ✅ 加入总列表
    }
    function getServiceInfo(string memory _service_id) public view returns (
        string memory service_id,
        string memory service_info,
        string[] memory card_ids
    ) {
        require(bytes(services[_service_id].service_id).length > 0, "Service not found");
        Service storage s = services[_service_id];
        return (s.service_id, s.service_info, s.card_ids);
    }
    function updateServiceInfo(string memory _service_id, string memory _newInfo) public {
        require(bytes(services[_service_id].service_id).length > 0, "Service not found");
        services[_service_id].service_info = _newInfo;
    }

    function deleteService(string memory _service_id) public {
        require(bytes(services[_service_id].service_id).length > 0, "Service not found");
        delete services[_service_id];
    }

    // ========== Card ==========
    function addCard(string memory _card_id, string memory _card_info, uint256 _balance, uint256 _totalAmount, string memory _buyer_id, string memory _service_id) public {
        require(bytes(cards[_card_id].card_id).length == 0, "Card exists");
        cards[_card_id] = Card(_card_id, _card_info, _balance, _totalAmount);
        buyers[_buyer_id].card_ids.push(_card_id);
        services[_service_id].card_ids.push(_card_id);
        cardIds.push(_card_id); // ✅ 记录卡片 ID
    }
    function getCardInfo(string memory _card_id) public view returns (
        string memory card_id,
        string memory card_info,
        uint256 balance,
        uint256 totalAmount
    ) {
        require(bytes(cards[_card_id].card_id).length > 0, "Card not found");
        Card storage c = cards[_card_id];
        return (c.card_id, c.card_info, c.balance, c.totalAmount);
    }
    function updateCardBalance(string memory _card_id, uint256 _newBalance) public {
        require(bytes(cards[_card_id].card_id).length > 0, "Card not found");
        cards[_card_id].balance = _newBalance;
    }

    function deleteCard(string memory _card_id) public {
        require(bytes(cards[_card_id].card_id).length > 0, "Card not found");
        delete cards[_card_id];
    }

    // ========== 查询辅助 ==========
    function getBuyerCardIds(string memory _buyer_id) public view returns (string[] memory) {
        return buyers[_buyer_id].card_ids;
    }

    function getSellerServiceIds(string memory _seller_id) public view returns (string[] memory) {
        return sellers[_seller_id].service_ids;
    }

    function getServiceCardIds(string memory _service_id) public view returns (string[] memory) {
        return services[_service_id].card_ids;
    }
    function getAllSellerIds() public view returns (string[] memory) {
        return sellerIds;
    }
    function getAllBuyerIds() public view returns (string[] memory) {
    return buyerIds;
    }

    function getAllServiceIds() public view returns (string[] memory) {
        return serviceIds;
    }
    function getAllCardIds() public view returns (string[] memory) {
        return cardIds;
    }
}