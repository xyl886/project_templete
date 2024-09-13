<template>
  <el-container
      class="login-container">
    <el-form :model="form" ref="form" label-width="60px" class="login-form">
      <el-form-item>
        <h2 style="text-align: center;">登录</h2>
      </el-form-item>
      <el-form-item prop="username" :rules="usernameRules">
        <el-input v-model="form.username" autocomplete="off" placeholder="请输入用户名"/>
      </el-form-item>
      <el-form-item prop="password" :rules="passwordRules">
        <el-input v-model="form.password" type="password" autocomplete="off" placeholder="请输入密码"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="login" size="medium" class="login-button">登录</el-button>
      </el-form-item>
      <el-form-item class="register-link">
        <span>还没有账户？ </span>
        <el-button type="text" @click="redirectToRegister">注册</el-button>
      </el-form-item>
    </el-form>
  </el-container>
</template>

<script>
import {login} from '@/api/user';
import {Message} from 'element-ui';
import {getToken, getUserInfo} from "@/utils/auth";

export default {
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      usernameRules: [
        {required: true, message: '请输入用户名', trigger: 'blur'},
      ],
      passwordRules: [
        {required: true, message: '请输入密码', trigger: 'blur'},
      ],
    };
  },
  created() {
    // 页面加载时检查 localStorage 中是否有 token 和 user_info
    const token = getToken();
    const userInfo = getUserInfo();
    if (token && userInfo) {
      // 如果 token 和 user_info 存在，直接跳转到首页
      this.$router.push('/index');
    }
  },
  methods: {
    async login() {
      this.$refs.form.validate(async (valid) => {
        if (valid) {
          try {
            const response = await login(this.form.username, this.form.password);
            if (response.code === 200) {
              Message.success('登录成功！');
              await this.$router.push('/index');
            } else {
              Message.error('登录失败，请检查您的凭证。' + response.msg);
            }
          } catch (error) {
            Message.error('登录失败！ ' + error);
          }
        } else {
          Message.error('表单验证失败，请检查输入内容。');
        }
      });
    },
    redirectToRegister() {
      this.$router.push('/register');
    },
  },
};
</script>

<style scoped>
/* 调整容器的布局及背景 */
.login-container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f0f2f5 0%, #e5e7eb 100%);
  padding: 20px;
}

/* 优化表单的样式 */
.login-form {
  width: 400px;
  padding: 40px;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  transition: all 0.3s ease;
}

/* 悬停时增加更强的阴影 */
.login-form:hover {
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
}

/* 调整输入框样式，增加用户体验 */
.el-input__inner {
  height: 45px;
  padding: 12px;
  font-size: 16px;
  border-radius: 6px;
}

/* 登录按钮样式优化 */
.login-button {
  width: 100%;
  height: 45px;
  font-size: 16px;
  font-weight: bold;
  border-radius: 6px;
  background: #409EFF;
  transition: background 0.3s ease;
}

.login-button:hover {
  background: #66b1ff;
}

/* 注册链接调整 */
.register-link {
  text-align: center;
  margin-top: 15px;
  color: #333;
}

.el-button[type="text"] {
  font-size: 14px;
  color: #409EFF;
  padding: 0;
}

/deep/
.el-form-item__content {
  left: -20px;
}

.el-form-item {
  padding: 0 20px
}

/* 响应式设计 */
@media (max-width: 768px) {
  .login-form {
    width: 90%;
    padding: 30px;
  }
}

@media (max-width: 480px) {
  .login-form {
    width: 100%;
    padding: 20px;
  }
}
</style>
