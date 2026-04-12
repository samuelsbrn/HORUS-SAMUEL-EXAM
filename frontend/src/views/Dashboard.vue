<template>
  <div class="container">
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <h2>DASHBOARD PENGGUNA</h2>
      <button class="btn btn-danger" @click="handleLogout">Logout</button>
    </div>
    
    <SearchBar @search="filterUsers" />
    <UserTable :users="filteredUsers" @edit="goToUpdate" @delete="deleteUser" />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import api from '../services/api';
import { authState } from '../store/auth';
import SearchBar from '../components/SearchBar.vue';
import UserTable from '../components/UserTable.vue';

const router = useRouter();
const users = ref([]);
const searchQuery = ref('');

const fetchUsers = async () => {
  try {
    const response = await api.get('/users');
    users.value = response.data;
  } catch (error) {
    console.error("Gagal mengambil data", error);
  }
};

onMounted(fetchUsers);

const filterUsers = (query) => {
  searchQuery.value = query;
};

const filteredUsers = computed(() => {
  if (!searchQuery.value) return users.value;
  const lowerCaseQuery = searchQuery.value.toLowerCase();
  return users.value.filter(u => 
    u.nama.toLowerCase().includes(lowerCaseQuery) || 
    u.username.toLowerCase().includes(lowerCaseQuery)
  );
});

const goToUpdate = (user) => {
  // Simpan data user ke localStorage sbg state sementara agar mudah diambil di halaman Update
  localStorage.setItem('editUser', JSON.stringify(user));
  router.push({ name: 'UpdateUser', params: { id: user.id } });
};

const deleteUser = async (id) => {
  if (confirm('Apakah Anda yakin ingin menghapus user ini?')) {
    try {
      await api.delete(`/users/${id}`);
      fetchUsers(); // Refresh tabel
    } catch (error) {
      alert('Gagal menghapus user');
    }
  }
};

const handleLogout = () => {
  authState.logout();
  router.push('/login');
};
</script>