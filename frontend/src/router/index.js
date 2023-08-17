import { createRouter, createWebHistory } from 'vue-router';
import ActivityFeed from '@/components/pages/AppActivityFeed.vue';
import Settings from '@/views/UserSettingsPage.vue';
import ReportsView from "@/views/ReportsView.vue";
import Home from "@/views/HomePage.vue";
import Tasks from "@/views/TasksPage.vue";
import Activity from "@/views/ActivityPage.vue";


const routes = [
    { path: '/', component: Home },
    { path: '/settings', component: Settings },
    { path: '/reports', component: ReportsView }, // 注意，我也将路径改为小写，以保持一致性
    { path: '/tasks', component: Tasks },
    { path: '/activity', component: Activity }, // 这里将ActivityFeed替换为Activity
    { path: '/activity-feed', component: ActivityFeed }, // 这里将ActivityFeed替换为Activity
    { path: '/register', component: () => import('@/views/RegisterPage.vue') },
    { path: '/login', component: () => import('@/views/LoginPage.vue') },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
