<template>
  <div>
    <h2>创建服务卡</h2>
    <form @submit.prevent="createService">
      <input v-model="name" placeholder="服务名称" required />
      <input v-model="price" type="number" placeholder="价格" required />
      <textarea v-model="description" placeholder="服务描述" required></textarea>
      <button type="submit">创建</button>
    </form>

    <h3>我发布的服务卡</h3>
    <div v-for="card in cards" :key="card.id" class="card">
      <ServiceCard :card="card" />
      <button @click="fetchBuyers(card.id)">查看购买者</button>

      <ul v-if="buyers[card.id]">
        <li v-for="buyer in buyers[card.id]" :key="buyer.id_number">
          买家编号：{{ buyer.id_number }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useUserStore } from '../store/user'
import ServiceCard from '../components/ServiceCard.vue'

const userStore = useUserStore()

const name = ref('')
const price = ref('')
const description = ref('')
const cards = ref([])
const buyers = ref({})

const fetchMyServices = async () => {
  const res = await axios.get(`http://localhost:8000/seller/cards?id_number=${userStore.id_number}`)
  cards.value = res.data
}

const createService = async () => {
  const res = await axios.post('http://localhost:8000/seller/create_card', {
    seller_id_number: userStore.id_number,
    name: name.value,
    price: price.value,
    description: description.value,
  })
  if (res.data === true) {
    await fetchMyServices()
    name.value = price.value = description.value = ''
  }
}

const fetchBuyers = async (cardId) => {
  if (!buyers.value[cardId]) {
    const res = await axios.get(`http://localhost:8000/seller/buyers_of_card?card_id=${cardId}`)
    buyers.value[cardId] = res.data
  }
}

onMounted(fetchMyServices)
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 15px 0;
}
</style>
