import { createRouter, createWebHistory } from 'vue-router';
import { authState } from '../store/auth';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Dashboard from '../views/Dashboard.vue';
import UpdateUser from '../views/UpdateUser.vue';

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login, meta: { guestOnly: true } },
  { path: '/register', component: Register, meta: { guestOnly: true } },
  { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/update/:id', name: 'UpdateUser', component: UpdateUser, meta: { requiresAuth: true } }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// Penjaga Rute (Navigation Guard)
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !authState.isAuthenticated()) {
    next('/login');
  } else if (to.meta.guestOnly && authState.isAuthenticated()) {
    next('/dashboard');
  } else {
    next();
  }
});

export default router;