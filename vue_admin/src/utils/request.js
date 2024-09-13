import axios from 'axios'
import store from '@/store'
import {getToken, removeToken, setToken, setUserInfo} from "@/utils/auth";
import {Message} from "element-ui";
import {ADMIN_API} from "@/api/user";

// console.log(process.env.VUE_APP_BASE_API)
// create an axios instance
const service = axios.create({
    baseURL: process.env.VUE_APP_BASE_API,
    timeout: 36000 // request timeout
})

// request interceptor
service.interceptors.request.use(
    config => {

        //do something before request is sent
        let token = getToken()
        if (token != null) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config
    },
    error => {
        // do something with request error
        console.log(error) // for debug
        return Promise.reject(error)
    }
)

// response interceptor
service.interceptors.response.use(
    /**
     * If you want to get http information such as headers or status
     * Please return  response => response
     */

    /**
     * Determine the request status by custom code
     * Here is just an example
     * You can also judge the status by HTTP Status Code
     */
    response => {
        const res = response.data
        // if the custom code is not 20000, it is judged as an error.

        if (res.code !== 200) {
            if (res.code === 401) {
                removeToken()
                sessionStorage.removeItem("user")
                store.state.userInfo = null
                store.state.loginFlag = true
            }
            if (res.code === 403) {
                Message({
                    message: res.msg,
                    type: 'error',
                    duration: 5 * 1000
                })
            }
            return Promise.reject(new Error(res.msg || 'Error'))
        } else {
            //如果是登录接口，则保存请求头里的token
            if (response.config.url === ADMIN_API + 'login' && response.config.method === 'post') {
                const token = String(response.headers['authorization']).split(' ')[1];
                setToken(token);
                const user_info = res.userinfo
                setUserInfo(user_info)
            }
            return res
        }
    },
    error => {
        console.log('err' + error) // for debug
        return Promise.reject(error)
    }
)

export default service