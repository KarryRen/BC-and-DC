// @Author : Kai Ren
// @Time   : 2025.03.21
// @Comment: The entrance of the whole application.

// basic APP import
import {createApp} from 'vue'
import App from './App.vue'
// element plus import
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import locale from 'element-plus/dist/locale/zh-cn'
// append css
import './assets/main.scss'

// Step 1. Creat the APP
const app = createApp(App)

// Step 2. Use Element Plus to set APP
app.use(ElementPlus, {locale})

// Step 3. Run the APP
app.mount('#app')
