<template>
  <nav>
    <router-link to="/login">登录</router-link> |
    <router-link to="/register">注册</router-link> |
    <router-link to="/dashboard">主页</router-link>
  </nav>
</template>

<script setup>
</script>

<style scoped>
nav {
  padding: 10px;
  background: #e8e8e8;
}
nav a {
  margin: 0 10px;
}
</style>
