<template>
  <div class="card">
    <h3>{{ card.name }}</h3>
    <p>{{ card.description }}</p>
    <p>价格：￥{{ card.price }}</p>
    <p>商家编号：{{ card.seller_id_number }}</p>
    <button v-if="showBuyButton" @click="$emit('buy', card.id)">购买</button>
  </div>
</template>

<script setup>
defineProps({
  card: Object,
  showBuyButton: {
    type: Boolean,
    default: false
  }
})
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px 0;
}
</style>
