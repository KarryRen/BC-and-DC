database_abi = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_password",
                "type": "string"
            }
        ],
        "name": "addBuyer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_card_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_card_info",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "_balance",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_totalAmount",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "_buyer_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_service_id",
                "type": "string"
            }
        ],
        "name": "addCard",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_password",
                "type": "string"
            }
        ],
        "name": "addSeller",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_service_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_service_info",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_seller_id",
                "type": "string"
            }
        ],
        "name": "addService",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "name": "buyers",
        "outputs": [
            {
                "internalType": "string",
                "name": "id_number",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "password",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "balance",
                "type": "uint256"
            },
            {
                "internalType": "uint8",
                "name": "role",
                "type": "uint8"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "name": "cards",
        "outputs": [
            {
                "internalType": "string",
                "name": "card_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "card_info",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "balance",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "totalAmount",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_id",
                "type": "string"
            }
        ],
        "name": "deleteBuyer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_card_id",
                "type": "string"
            }
        ],
        "name": "deleteCard",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_id",
                "type": "string"
            }
        ],
        "name": "deleteSeller",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_service_id",
                "type": "string"
            }
        ],
        "name": "deleteService",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getAllBuyerIds",
        "outputs": [
            {
                "internalType": "string[]",
                "name": "",
                "type": "string[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getAllCardIds",
        "outputs": [
            {
                "internalType": "string[]",
                "name": "",
                "type": "string[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getAllSellerIds",
        "outputs": [
            {
                "internalType": "string[]",
                "name": "",
                "type": "string[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getAllServiceIds",
        "outputs": [
            {
                "internalType": "string[]",
                "name": "",
                "type": "string[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_buyer_id",
                "type": "string"
            }
        ],
        "name": "getBuyerCardIds",
        "outputs": [
            {
                "internalType": "string[]",
                "name": "",
                "type": "string[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_buyer_id",
                "type": "string"
            }
        ],
        "name": "getBuyerInfo",
        "outputs": [
            {
                "internalType": "string",
                "name": "id_number",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "password",
                "type": "string"
            },
            {
                "internalType": "string[]",
                "name": "card_ids",
                "type": "string[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_card_id",
                "type": "string"
            }
        ],
        "name": "getCardInfo",
        "outputs": [
            {
                "internalType": "string",
                "name": "card_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "card_info",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "balance",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "totalAmount",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_seller_id",
                "type": "string"
            }
        ],
        "name": "getSellerInfo",
        "outputs": [
            {
                "internalType": "string",
                "name": "id_number",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "password",
                "type": "string"
            },
            {
                "internalType": "string[]",
                "name": "service_ids",
                "type": "string[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_seller_id",
                "type": "string"
            }
        ],
        "name": "getSellerServiceIds",
        "outputs": [
            {
                "internalType": "string[]",
                "name": "",
                "type": "string[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_service_id",
                "type": "string"
            }
        ],
        "name": "getServiceCardIds",
        "outputs": [
            {
                "internalType": "string[]",
                "name": "",
                "type": "string[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_service_id",
                "type": "string"
            }
        ],
        "name": "getServiceInfo",
        "outputs": [
            {
                "internalType": "string",
                "name": "service_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "service_info",
                "type": "string"
            },
            {
                "internalType": "string[]",
                "name": "card_ids",
                "type": "string[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "name": "sellers",
        "outputs": [
            {
                "internalType": "string",
                "name": "id_number",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "password",
                "type": "string"
            },
            {
                "internalType": "uint8",
                "name": "role",
                "type": "uint8"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "name": "services",
        "outputs": [
            {
                "internalType": "string",
                "name": "service_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "service_info",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_id",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "_newBalance",
                "type": "uint256"
            }
        ],
        "name": "updateBuyerBalance",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_newPassword",
                "type": "string"
            }
        ],
        "name": "updateBuyerPassword",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_card_id",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "_newBalance",
                "type": "uint256"
            }
        ],
        "name": "updateCardBalance",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_newPassword",
                "type": "string"
            }
        ],
        "name": "updateSellerPassword",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_service_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_newInfo",
                "type": "string"
            }
        ],
        "name": "updateServiceInfo",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
