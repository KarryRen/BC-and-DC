module.exports = {
    lintOnSave: false, //关闭eslint语法检查配置
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8888', // 这里后台的地址模拟的;应该填写你们真实的后台接口
                ws: false,
                changOrigin: true, // 允许跨域
                pathRewrite: {'^/api': ''}  // 路径重写，请求的时候使用这个api就可以
            }
        }
    }
}
