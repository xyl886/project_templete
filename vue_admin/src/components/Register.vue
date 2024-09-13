<template>
  <el-container
      style="height: 100vh; display: flex; align-items: center; justify-content: center; background: #f0f2f5;">
    <el-form :model="form" ref="form" label-width="80px" class="register-form">
      <el-form-item>
        <h2 style="text-align: center;">注册</h2>
      </el-form-item>
      <el-form-item  prop="username" :rules="usernameRules">
        <el-input v-model="form.username" autocomplete="off" placeholder="请输入用户名"/>
      </el-form-item>
      <el-form-item  prop="password" :rules="passwordRules">
        <el-input v-model="form.password" type="password" autocomplete="off" placeholder="请输入密码"/>
      </el-form-item>
      <el-form-item  prop="confirmPassword" :rules="confirmPasswordRules">
        <el-input v-model="form.confirmPassword" type="password" autocomplete="off" placeholder="请再次输入密码"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="register" size="medium" style="width: 100%;">注册</el-button>
      </el-form-item>
      <el-form-item style="text-align: center;">
        <span>已有账号？</span>
        <el-button type="text" @click="redirectToLogin">登录</el-button>
      </el-form-item>
    </el-form>
  </el-container>
</template>

<script>
import {register} from '@/api/user';

export default {
  data() {
    return {
      form: {
        username: '',
        password: '',
        confirmPassword: '',
      },
      usernameRules: [
        {required: true, message: '请输入用户名', trigger: 'blur'},
      ],
      passwordRules: [
        {required: true, message: '请输入密码', trigger: 'blur'},
      ],
      confirmPasswordRules: [
        {required: true, message: '请确认您的密码', trigger: 'blur'},
        {validator: this.validateConfirmPassword, trigger: 'blur'},
      ],
    };
  },
  methods: {
    validateConfirmPassword(rule, value, callback) {
      if (value !== this.form.password) {
        callback(new Error('两次输入的密码不一致'));
      } else {
        callback();
      }
    },
    async register() {
      this.$refs.form.validate(async (valid) => {
        if (valid) {
          try {
            (await register(this.form.username, this.form.password))().then(response => {
              if (response.code === 200) {
                this.$message.success('注册成功！');
                this.$router.push('/login');
              } else {
                this.$message.error('注册失败，请重试。' + response.msg);
              }
            });
          } catch (error) {
            this.$message.error('注册失败，请重试。'+ error);
            console.error('注册失败:', error);
          }
        } else {
          this.$message.error('表单校验失败，请检查输入内容。');
        }
      });
    },
    redirectToLogin() {
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
.register-form {
  width: 400px;
  padding: 40px;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.register-form:hover {
  box-shadow: 0 6px 30px rgba(0, 0, 0, 0.15);
}

.el-form-item {
  margin-bottom: 20px;
}

.el-input__inner {
  height: 40px;
  padding: 10px;
  border-radius: 6px;
}

.el-button {
  border-radius: 6px;
  font-weight: bold;
}
/deep/
.el-form-item__content{
      left: -30px;
}
.el-form-item{
  padding:0 20px
}
.el-button[type="text"] {
  font-size: 14px;
  color: #409EFF;
  padding: 0;
}

.el-container {
  background: linear-gradient(135deg, #ece9e6 0%, #ffffff 100%);
}
</style>
