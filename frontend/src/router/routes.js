// 第一版
// import Vue from 'vue';
// import Router from 'vue-router';
// import Home from '../views/HomePage.vue';
// import Tasks from '../views/TasksPage.vue';
// import Activity from '../views/ActivityPage.vue';
// import UserSettings from '../views/UserSettingsPage.vue';
// import ReportsView from '../views/ReportsView.vue';
//
// Vue.use(Router);
//
// export default new Router({
//   routes: [
//     { path: '/', component: Home },
//     { path: '/settings', component: UserSettings },
//     { path: '/Reports', component: ReportsView },
//     { path: '/tasks', component: Tasks },
//     { path: '/activity', component: Activity },
//   ],
// });

//第二版
// 在 router/routes.js 文件中
import ActivityPage from '@/views/ActivityPage.vue';
import DashboardPage from '@/views/DashboardPage.vue';
import HomePage from '@/views/HomePage.vue';
import ReportsView from '@/views/ReportsView.vue';
import SettingsPage from '@/views/SettingsPage.vue';
import TasksPage from '@/views/TasksPage.vue';
import UserSettingsPage from '@/views/UserSettingsPage.vue';

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/activity', name: 'Activity', component: ActivityPage },
  { path: '/dashboard', name: 'Dashboard', component: DashboardPage },
  { path: '/reports', name: 'Reports', component: ReportsView },
  { path: '/settings', name: 'Settings', component: SettingsPage },
  { path: '/tasks', name: 'Tasks', component: TasksPage },
  { path: '/user-settings', name: 'UserSettings', component: UserSettingsPage },
];

export default routes;
