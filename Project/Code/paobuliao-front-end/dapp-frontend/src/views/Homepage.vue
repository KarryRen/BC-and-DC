<template>
  <div>
    <h1>欢迎 {{ userStore.role === 'buyer' ? '买家' : '卖家' }}：{{ userStore.id_number }}</h1>
    <p>余额：{{ userStore.balance }} 元</p>

    <div>
      <input v-model="rechargeAmount" type="number" placeholder="充值金额" />
      <button @click="recharge">充值</button>
    </div>

    <BuyerPanel v-if="userStore.role === 'buyer'" />
    <SellerPanel v-else-if="userStore.role === 'seller'" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '../store/user'
import axios from 'axios'
import BuyerPanel from './BuyerPanel.vue'
import SellerPanel from './SellerPanel.vue'

const userStore = useUserStore()
const rechargeAmount = ref('')

const recharge = async () => {
  const res = await axios.post('http://localhost:8000/user/recharge', {
    id_number: userStore.id_number,
    amount: Number(rechargeAmount.value)
  })
  if (res.data === true) {
    await userStore.fetchInfo()
    rechargeAmount.value = ''
    alert('充值成功')
  } else {
    alert('充值失败')
  }
}

onMounted(() => {
  userStore.fetchInfo()
})
</script>
