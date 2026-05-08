<template>
  <div id="app">
    <nav class="nav-bar">
      <router-link to="/" data-testid="nav-expenses">소비기록</router-link>
      <router-link to="/statistics" data-testid="nav-statistics">통계</router-link>
      <router-link to="/settings" data-testid="nav-settings">설정</router-link>
    </nav>
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f5f5f5; }
.nav-bar { display: flex; background: #fff; border-bottom: 1px solid #e0e0e0; padding: 12px 16px; gap: 24px; }
.nav-bar a { text-decoration: none; color: #666; font-weight: 500; padding: 8px 16px; border-radius: 8px; }
.nav-bar a.router-link-active { color: #1976d2; background: #e3f2fd; }
.main-content { max-width: 960px; margin: 0 auto; padding: 16px; }
</style>
