<template>
  <div>
    <h2>可购买的服务卡</h2>
    <ServiceCard
      v-for="card in allCards"
      :key="card.id"
      :card="card"
      :showBuyButton="true"
      @buy="handleBuy"
    />

    <h2>我已购买的服务卡</h2>
    <ServiceCard
      v-for="card in myCards"
      :key="'my-' + card.id"
      :card="card"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useUserStore } from '../store/user'
import ServiceCard from '../components/ServiceCard.vue'

const userStore = useUserStore()
const allCards = ref([])
const myCards = ref([])

const fetchAllCards = async () => {
  const res = await axios.get('http://localhost:8000/buyer/all_cards')
  allCards.value = res.data
}

const fetchMyCards = async () => {
  const res = await axios.get(`http://localhost:8000/buyer/my_cards?buyer_id=${userStore.id_number}`)
  myCards.value = res.data
}

const handleBuy = async (cardId) => {
  const res = await axios.post('http://localhost:8000/buyer/buy_card', {
    buyer_id_number: userStore.id_number,
    card_id: cardId
  })

  if (res.data === true) {
    alert('购买成功')
    fetchMyCards()
    userStore.fetchInfo()  // 更新余额
  } else if (res.data === '余额不足') {
    alert('购买失败：余额不足')
  } else {
    alert('购买失败')
  }
}


onMounted(() => {
  fetchAllCards()
  fetchMyCards()
})
</script>
