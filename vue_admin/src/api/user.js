import request from "@/utils/request";

export const ADMIN_API = '/admin';

// 用户登录
export const login = (username, password) => {
    return request({
        url: `${ADMIN_API}/login`,
        method: 'post',
        data: {
            username,
            password
        }
    });
};

// 用户注册
export const register = (username, password) => {
    return request({
        url: `${ADMIN_API}/register`,
        method: 'post',
        data: {
            username,
            password
        }
    });
};
