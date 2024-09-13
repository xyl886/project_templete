<template>
  <div id="app">
    <!-- 自定义遮罩层 -->
    <div v-if="loadingIndex" class="my-home-overlay">
      <div class="_main">
        <img class="_loading" src="./assets/loading.svg" alt="loading">
        <div class="_title">
          努力加载中...
        </div>
        <div class="_sub-title">
          初次加载资源可能需要较多时间 请耐心等待
        </div>
      </div>
    </div>
    <!-- 主内容 -->
    <router-view v-if="!loadingIndex"></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      loadingIndex: true, // 初始化时显示加载
    };
  },
  created () {
    let that = this;
    setTimeout(function () {
      that.loadingIndex = false; // 500ms 后关闭加载
    }, 500);
  },
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

/* 自定义遮罩层样式 */
.my-home-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #409EFF;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
}

._main {
  text-align: center;
}

._loading {
  width: 40px;
  margin-bottom: 20px;
}

._title {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}

._sub-title {
  font-size: 16px;
  color: #888;
}
</style>
