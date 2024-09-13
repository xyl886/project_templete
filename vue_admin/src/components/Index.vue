<template>
  <el-container style="height: 100vh;">
    <!-- 顶部导航栏 -->
    <el-header class="header">
      <div class="header-left">
        <h2 style="color: #409EFF; text-align: center;">管理后台</h2>
      </div>
      <div class="header-right">
        <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">
            <img
              src="https://via.placeholder.com/40"
              alt="avatar"
              class="avatar"
            />
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="logout">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </el-header>

    <!-- 主体内容 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="200px" style="background-color: #2d3a4b;">
<!--        <div class="logo">-->
<!--          <h2 style="color: #409EFF; text-align: center;">管理后台</h2>-->
<!--        </div>-->
        <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
          @select="handleSelect"
        >
          <el-menu-item index="1" @click="currentView = 'Dashboard'">
            <i class="el-icon-menu"></i>
            <span slot="title">首页</span>
          </el-menu-item>
        </el-menu>
      </el-aside>

      <el-main>
        <component :is="currentView"></component>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>

import Dashboard from "@/components/Dashboard.vue";
import {removeToken, removeUserInfo} from "@/utils/auth";

export default {
  data() {
    return {
      currentView: 'Dashboard', // 默认显示Dashboard
    };
  },
  components: {
    Dashboard,
  },

  methods: {
    handleSelect(key, keyPath) {
      // console.log(key, keyPath);
    },
     handleCommand(command) {
      if (command === 'logout') {
        this.logout();
      }
    },
    logout() {
      // 清除 token 并跳转到登录页面
      removeToken()
      removeUserInfo()
      this.$router.push('/login');
    }
  },
};
</script>


<style scoped>
/* 顶部导航栏样式 */
.header {
  //background-color: #fff;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  //border-bottom: 1px solid #e0e6ed;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  color: #1f2d3d;
  height: 60px;
}

.avatar {
  border-radius: 50%;
  width: 40px;
  height: 40px;
  cursor: pointer;
}

.el-dropdown-link {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.header-left h2 {
  margin: 0;
}

.header-right {
  display: flex;
  align-items: center;
}

/* 侧边栏和主体内容样式 */
.el-container {
  background-color: #f5f7fa;
}

.logo {
  padding: 20px;
  background-color: #1a2b3c;
  margin-bottom: 20px;
}

.el-menu-vertical-demo {
  background-color: #1f2d3d;
  color: #fff;
}

.el-menu-vertical-demo .el-menu-item {
  color: #bfcbd9;
}

.el-menu-vertical-demo .el-menu-item.is-active {
  background-color: #409EFF;
  color: #fff;
}

.el-menu-vertical-demo .el-menu-item:hover {
  background-color: #2a3a4b;
}
</style>
