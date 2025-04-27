<template>
  <div>
    <h2>注册账号</h2>
    <form @submit.prevent="handleRegister">
      <input v-model="id_number" placeholder="身份证号/营业执照号" required />
      <input v-model="password" type="password" placeholder="密码" required />
      <input v-model="repassword" type="password" placeholder="确认密码" required />
      <select v-model="role">
        <option disabled value="">请选择身份</option>
        <option value="0">买家</option>
        <option value="1">卖家</option>
      </select>
      <button type="submit">注册</button>
    </form>
    <p>{{ msg }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const id_number = ref('')
const password = ref('')
const repassword = ref('')
const role = ref('')
const msg = ref('')
const router = useRouter()

const handleRegister = async () => {
  try {
    const res = await axios.post('http://localhost:8000/register', {
      id_number: id_number.value,
      password: password.value,
      repassword: repassword.value,
      role: parseInt(role.value)
    })
    if (res.data === true) {
      msg.value = '注册成功，跳转登录...'
      setTimeout(() => router.push('/login'), 1000)
    } else {
      msg.value = '注册失败，请检查输入'
    }
  } catch (err) {
    msg.value = '注册异常'
  }
}
</script>
