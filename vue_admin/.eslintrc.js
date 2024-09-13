module.exports = {
  extends: ['eslint:recommended', 'plugin:vue/essential'],
  env: {
    node: true, // 添加 Node.js 环境
    browser: true, // 添加浏览器环境
  },
  rules: {
    'no-useless-catch': 'warn',
    'vue/multi-word-component-names': 'off',
    'no-unused-vars': ['warn', { 'argsIgnorePattern': '^_' }],
    'no-undef': 'off' // 可以选择关闭 no-undef 规则，或添加其他规则
  },
};
