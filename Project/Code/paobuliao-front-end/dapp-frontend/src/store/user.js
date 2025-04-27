import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore('user', {
    state: () => ({
        id_number: '',
        role: '',  // 'buyer' or 'seller'
        balance: 0
    }),
    actions: {
        async fetchInfo() {
            if (this.id_number) {
                const res = await axios.get(`http://localhost:8000/user/info?id_number=${this.id_number}`)
                this.balance = res.data.balance
                this.role = res.data.role
            }
        }
    }
})
