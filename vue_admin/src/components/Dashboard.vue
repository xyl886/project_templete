<template>
  <el-container style="padding: 20px;">
    <el-row>
      <el-col :span="24">
        <h1>Dashboard</h1>
        <el-card>
          <h2>Welcome to your dashboard, {{ username }}!</h2>
          <!-- Add more dashboard content here -->
        </el-card>
      </el-col>
    </el-row>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      username: '',
    };
  },
  created() {
    // Assuming token is stored in localStorage and user data can be fetched
    const token = localStorage.getItem('token');
    if (token) {
      // Fetch user data or other dashboard-related information
      // For demonstration, we'll just set the username directly
      this.username = 'User'; // Replace with actual user data fetch
    } else {
      this.$router.push('/login');
    }
  },
};
</script>

<style scoped>
.dashboard {
  padding: 20px;
}
</style>
