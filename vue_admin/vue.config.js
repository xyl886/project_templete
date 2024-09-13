const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8000', // 你的后端服务地址
                changeOrigin: true,              // 允许跨域
                pathRewrite: {
                    '^/api': ''                    // 将/api前缀替换为空，匹配后端路由
                }
            }
        }
    }
})

