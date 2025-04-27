<script setup lang="ts">
import { useUserStore } from '../store/user'
import NavBar from '../components/NavBar.vue'
const userStore = useUserStore()
</script>
<template>
  <div>
    <NavBar />
    <h2>欢迎：{{ userStore.id_number }} ({{ userStore.role === 0 ? "买家" : "卖家" }})</h2>

    <div v-if="userStore.role === 1">
      <router-link to="/seller"><button>创建服务卡</button></router-link>
    </div>
    <div v-else-if="userStore.role === 0">
      <router-link to="/buyer"><button>购买服务卡</button></router-link>
    </div>
  </div>
</template>
