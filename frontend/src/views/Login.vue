<template>
  <div class="container" style="max-width: 400px; text-align: center;">
    <h2>LOGIN</h2>
    <div v-if="errorMsg" style="color: red; margin-bottom: 10px;">{{ errorMsg }}</div>
    <form @submit.prevent="handleLogin">
      <div class="input-group">
        <input v-model="form.username" type="text" placeholder="Username" required />
      </div>
      <div class="input-group">
        <input v-model="form.password" type="password" placeholder="Password" required />
      </div>
      <button class="btn" type="submit" style="width: 100%;">Login</button>
    </form>
    <p style="margin-top: 15px;">Belum punya akun? <router-link to="/register">Registrasi</router-link></p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import api from '../services/api';
import { authState } from '../store/auth';

const router = useRouter();
const form = ref({ username: '', password: '' });
const errorMsg = ref('');

const handleLogin = async () => {
  try {
    const response = await api.post('/users/login', form.value);
    authState.setToken(response.data.token);
    router.push('/dashboard');
  } catch (error) {
    errorMsg.value = error.response?.data?.message || 'Username atau password salah';
  }
};
</script>