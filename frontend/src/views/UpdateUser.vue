<template>
  <div class="container" style="max-width: 400px;">
    <h2 style="text-align: center;">UPDATE USER</h2>
    <div v-if="errorMsg" style="color: red; margin-bottom: 10px; text-align: center;">{{ errorMsg }}</div>
    <form @submit.prevent="handleUpdate">
      <div class="input-group">
        <label>Nama Lengkap:</label>
        <input v-model="form.nama" type="text" required />
      </div>
      <div class="input-group">
        <label>Email:</label>
        <input v-model="form.email" type="email" required />
      </div>
      <div class="input-group">
        <label>Username:</label>
        <input v-model="form.username" type="text" required />
      </div>
      
      <div style="display: flex; justify-content: space-between; margin-top: 20px;">
        <button class="btn" type="submit" style="width: 48%;">Update</button>
        <button class="btn btn-danger" type="button" style="width: 48%;" @click="goBack">Kembali</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import api from '../services/api';

const router = useRouter();
const route = useRoute();
const form = ref({ nama: '', email: '', username: '' });
const errorMsg = ref('');

onMounted(() => {
  const userData = localStorage.getItem('editUser');
  if (userData) {
    const user = JSON.parse(userData);
    form.value.nama = user.nama;
    form.value.email = user.email;
    form.value.username = user.username;
  }
});

const handleUpdate = async () => {
  try {
    const userId = route.params.id;
    await api.put(`/users/${userId}`, form.value);
    alert('Data user berhasil diperbarui');
    localStorage.removeItem('editUser');
    router.push('/dashboard');
  } catch (error) {
    errorMsg.value = error.response?.data?.message || 'Gagal update data';
  }
};

const goBack = () => {
  localStorage.removeItem('editUser');
  router.push('/dashboard');
};
</script>