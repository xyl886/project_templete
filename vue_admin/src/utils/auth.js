const TokenKey = 'token'
const userInfoKey = 'userInfo'

export function getToken() {
    return localStorage.getItem(TokenKey)
}

export function setToken(token) {
    return localStorage.setItem(TokenKey, token)
}

export function removeToken() {
    return localStorage.removeItem(TokenKey)
}

export function setUserInfo(userInfo) {
    return localStorage.setItem(userInfoKey, JSON.stringify(userInfo))
}

export function getUserInfo() {
    return JSON.parse(localStorage.getItem(userInfoKey))
}

export function removeUserInfo() {
    return localStorage.removeItem(userInfoKey)
}