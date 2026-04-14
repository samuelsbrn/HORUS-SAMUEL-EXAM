<template>
  <div class="container" style="max-width: 400px; text-align: center;">
    <h2>REGISTRASI AKUN</h2>
    <div v-if="errorMsg" style="color: red; margin-bottom: 10px;">{{ errorMsg }}</div>
    <form @submit.prevent="handleRegister">
      <div class="input-group">
        <input v-model="form.nama" type="text" placeholder="Nama Lengkap" required />
      </div>
      <div class="input-group">
        <input v-model="form.email" type="email" placeholder="Email" required />
      </div>
      <div class="input-group">
        <input v-model="form.username" type="text" placeholder="Username" required />
      </div>
      <div class="input-group">
        <input v-model="form.password" type="password" placeholder="Password" required />
      </div>
      <button class="btn" type="submit" style="width: 100%;">Registrasi</button>
    </form>
    <p style="margin-top: 15px;">Sudah punya akun? <router-link to="/login">Login</router-link></p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import api from '../services/api';

const router = useRouter();
const form = ref({ nama: '', email: '', username: '', password: '' });
const errorMsg = ref('');

const handleRegister = async () => {
  try {
    await api.post('/users/register', form.value);
    alert('Registrasi berhasil');
    router.push('/login');
  } catch (error) {
    errorMsg.value = error.response?.data?.message || 'Gagal mendaftar';
  }
};
</script>